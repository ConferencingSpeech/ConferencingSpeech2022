
import numpy as np
import pandas as pd; pd.options.mode.chained_assignment = None
import matplotlib.pyplot as plt
from tqdm import tqdm
from scipy.stats import pearsonr
from scipy.stats import spearmanr
from scipy.optimize import minimize
from scipy.optimize import least_squares

def is_const(x):
    if np.linalg.norm(x - np.mean(x)) < 1e-13 * np.abs(np.mean(x)):
        return True
    elif np.all( x==x[0]):
        return True
    else:
        return False

def calc_eval_metrics(y, y_hat, y_hat_map=None, d=None, ci=None):
    '''
    Calculate RMSE, Pearson's correlation.
    '''
    r = {
        'r_p': np.nan,
        'r_p_map': np.nan,
        'rmse': np.nan,
        'rmse_map': np.nan,
        'rmse_star_map': np.nan,
    }
    if is_const(y_hat):
        r['r_p'] = np.nan
    else:
        r['r_p'] = pearsonr(y, y_hat)[0]
    r['rmse'] = calc_rmse(y, y_hat)
    if y_hat_map is not None:
        r['rmse_map'] = calc_rmse(y, y_hat_map, d=d)
        r['r_p_map'] = pearsonr(y, y_hat_map)[0]
        if ci is not None:
            r['rmse_star_map'] = calc_rmse_star(y, y_hat_map, ci, d)[0]
    return r

def calc_rmse(y_true, y_pred, d=0):
    if d== 0:
        rmse = np.sqrt(np.mean(np.square(y_true - y_pred)))
    else:
        N = y_true.shape[0]
        if (N - d) < 1:
            rmse = np.nan
        else:
            rmse = np.sqrt(1 / (N - d) * np.sum(np.square(y_true - y_pred)))  # Eq (7-29) P.1401
    return rmse


def calc_rmse_star(mos_sub, mos_obj, ci, d):
    N = mos_sub.shape[0]
    error = mos_sub - mos_obj

    if ci[0] == -1:
        p_error = np.nan
        rmse_star = np.nan
    else:
        p_error = (abs(error) - ci).clip(min=0)  # Eq (7-27) P.1401
        if (N - d) < 1:
            rmse_star = np.nan
        else:
            rmse_star = np.sqrt(1 / (N - d) * sum(p_error) ** 2)  # Eq (7-29) P.1401

    return rmse_star, p_error, error


def calc_mapped(x, b):
    N = x.shape[0]
    order = b.shape[0] - 1
    A = np.zeros([N, order + 1])
    for i in range(order + 1):
        A[:, i] = x ** (i)
    return A @ b


def fit_first_order(y_con, y_con_hat):
    A = np.vstack([np.ones(len(y_con_hat)), y_con_hat]).T
    b = np.linalg.lstsq(A, y_con, rcond=None)[0]
    return b


def fit_second_order(y_con, y_con_hat):
    A = np.vstack([np.ones(len(y_con_hat)), y_con_hat, y_con_hat ** 2]).T
    b = np.linalg.lstsq(A, y_con, rcond=None)[0]
    return b


def fit_third_order(y_con, y_con_hat):
    A = np.vstack([np.ones(len(y_con_hat)), y_con_hat, y_con_hat ** 2, y_con_hat ** 3]).T
    b = np.linalg.lstsq(A, y_con, rcond=None)[0]

    p = np.poly1d(np.flipud(b))
    p2 = np.polyder(p)
    rr = np.roots(p2)
    r = rr[np.imag(rr) == 0]
    monotonic = all(np.logical_or(r > max(y_con_hat), r < min(y_con_hat)))
    if monotonic == False:
        print('Not monotonic!!!')
    return b


def fit_monotonic_third_order(
        dfile_db,
        dcon_db=None,
        pred=None,
        target_mos=None,
        target_ci=None,
        mapping=None):
    y = dfile_db[target_mos].to_numpy()

    y_hat = dfile_db[pred].to_numpy()

    if dcon_db is None:
        if target_ci in dfile_db:
            ci = dfile_db[target_ci].to_numpy()
        else:
            ci = 0
    else:
        y_con = dcon_db[target_mos].to_numpy()

        if target_ci in dcon_db:
            ci = dcon_db[target_ci].to_numpy()
        else:
            ci = 0

    x = y_hat
    y_hat_min = min(y_hat) - 0.01
    y_hat_max = max(y_hat) + 0.01

    def polynomial(p, x):
        return p[0] + p[1] * x + p[2] * x ** 2 + p[3] * x ** 3

    def constraint_2nd_der(p):
        return 2 * p[2] + 6 * p[3] * x

    def constraint_1st_der(p):
        x = np.arange(y_hat_min, y_hat_max, 0.1)
        return p[1] + 2 * p[2] * x + 3 * p[3] * x ** 2

    def objective_con(p):
        x_map = polynomial(p, x)
        dfile_db['x_map'] = x_map
        x_map_con = dfile_db.groupby('con').mean().x_map.to_numpy()
        err = x_map_con - y_con
        if mapping == 'pError':
            p_err = (abs(err) - ci).clip(min=0)
            return (p_err ** 2).sum()
        elif mapping == 'error':
            return (err ** 2).sum()
        else:
            raise NotImplementedError

    def objective_file(p):
        x_map = polynomial(p, x)
        err = x_map - y
        if mapping == 'pError':
            p_err = (abs(err) - ci).clip(min=0)
            return (p_err ** 2).sum()
        elif mapping == 'error':
            return (err ** 2).sum()
        else:
            raise NotImplementedError

    cons = dict(type='ineq', fun=constraint_1st_der)

    if dcon_db is None:
        res = minimize(
            objective_file,
            x0=np.array([0., 1., 0., 0.]),
            method='SLSQP',
            constraints=cons,
        )
    else:
        res = minimize(
            objective_con,
            x0=np.array([0., 1., 0., 0.]),
            method='SLSQP',
            constraints=cons,
        )
    b = res.x
    return b


def calc_mapping(
        dfile_db,
        mapping=None,
        dcon_db=None,
        target_mos=None,
        target_ci=None,
        pred=None,
):
    if dcon_db is not None:
        y = dcon_db[target_mos].to_numpy()
        y_hat = dfile_db.groupby('con').mean().get(pred).to_numpy()
    else:
        y = dfile_db[target_mos].to_numpy()
        y_hat = dfile_db[pred].to_numpy()

    if mapping == None:
        b = np.array([0, 1, 0, 0])
        d_map = 0
    elif mapping == 'first_order':
        b = fit_first_order(y, y_hat)
        d_map = 1
    elif mapping == 'second_order':
        b = fit_second_order(y, y_hat)
        d_map = 3
    elif mapping == 'third_order':
        b = fit_third_order(y, y_hat)
        d_map = 4
    elif mapping == 'monotonic_third_order':
        b = fit_monotonic_third_order(
            dfile_db,
            dcon_db=dcon_db,
            pred=pred,
            target_mos=target_mos,
            target_ci=target_ci,
            mapping='error',
        )
        d_map = 4
    else:
        raise NotImplementedError

    return b, d_map


def eval_results(
        df,
        target_mos='mos',
        target_ci='mos_ci',
        pred='mos_pred',
        mapping=None,
        do_print=False
):
    '''
    Evaluates a trained model on given dataset.
    '''
    # Loop through databases
    db_results_df = []
    df['y_hat_map'] = np.nan

    for db_name in df.db.astype("category").cat.categories:

        df_db = df.loc[df.db == db_name]

        # per file -----------------------------------------------------------
        y = df_db[target_mos].to_numpy()
        if np.isnan(y).any():
            r = {'r_p': np.nan, 'r_s': np.nan, 'rmse': np.nan, 'r_p_map': np.nan,
                 'r_s_map': np.nan, 'rmse_map': np.nan}
        else:
            y_hat = df_db[pred].to_numpy()

            b, d = calc_mapping(
                df_db,
                mapping=mapping,
                target_mos=target_mos,
                target_ci=target_ci,
                pred=pred
            )
            y_hat_map = calc_mapped(y_hat, b)

            r = calc_eval_metrics(y, y_hat, y_hat_map=y_hat_map, d=d)
            r.pop('rmse_star_map')
        r = {f'{k}_file': v for k, v in r.items()}

        if do_print and (not np.isnan(y).any()):
            print('%-30s r_p_file: %0.2f, rmse_file: %0.2f, rmse_map_file: %0.2f'
                      % (db_name + ':', r['r_p_file'],r['rmse_file'], r['rmse_map_file']))
        db_results_df.append({'db': db_name, **r})

    # Save individual database results in DataFrame
    db_results_df = pd.DataFrame(db_results_df)

    r_average = {}
    r_average['r_p_mean_file'] = db_results_df.r_p_file.mean()
    r_average['rmse_mean_file'] = db_results_df.rmse_file.mean()
    r_average['rmse_map_mean_file'] = db_results_df.rmse_map_file.mean()


    y = df[target_mos].to_numpy()
    y_hat = df[pred].to_numpy()

    r_total_file = calc_eval_metrics(y, y_hat)
    r_total_file = {'r_p_all': r_total_file['r_p'], 'rmse_all': r_total_file['rmse']}

    overall_results = {
        **r_total_file,
        **r_average
    }

    return db_results_df, overall_results



def evaluate_mos(csv_mos,csv_mos_pre):
    df = pd.read_csv(csv_mos)
    df2 = pd.read_csv(csv_mos_pre)
    df['mos_pred'] = df2['mos_pred']
    db_results_df, overall_results = eval_results(
            df,
            target_mos='mos',
            target_ci= 'mos_ci',
            pred='mos_pred',
            mapping = 'monotonic_third_order',
            do_print=True)
    print('r_p_mean_file {:0.4f} rmse_mean_file {:0.4f} rmse_map_mean_file {:0.4f} '
            .format(overall_results['r_p_mean_file'], overall_results['rmse_mean_file'], overall_results['rmse_map_mean_file'])
            )

if __name__=='__main__':
    evaluate_mos('csv_mos.csv','csv_mos_pred.csv')
'''
 This script is used to verify the accuracy of the submitted team results. It needs to input two csv files, "csv_mos.csv" and 'csv_mos_pred.csv'
'csv_mos.csv'  has three columns: 'db', 'deg_wav', 'mos'. 
'db'  represents the name of the dataset to which the speech clips belongs; 
'deg_wav' represents the name of speech to be tested;
'mos' represents the mos tag of speech to be tested.

'csv_mos_pred.csv'  has three columns: 'db', 'deg_wav', 'mos_pred'. 
'db'  represents the name of the dataset to which the speech clips belongs; 
'deg_wav' represents the name of the speech clip;
'mos_pred' represents the predicted mos of the  speech clip.
'''

