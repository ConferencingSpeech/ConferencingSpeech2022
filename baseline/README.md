# Baseline

The baseline model is adapted (simplified) from the [NISQA model](https://github.com/gabrielmittag/NISQA/) and is made 
of a deep feed forward network followed by LSTM and average pooling. Here we publish the weights of the model trained for 50 epochs.
We also user NISQA's toolset to run the prediction.


## Get started

The following steps should be performed to get predictions from the baseline model.


1. Install `python` and `pip` / `anaconda`, if they are not already installed. Follow the platform specific installation instructions.

1. Clone or download the NISQA repository from Github: https://github.com/gabrielmittag/NISQA , e.g.

    ```bash
    git clone https://github.com/gabrielmittag/NISQA.git
    cd NISQA
    ```

1. Install the python module dependencies using `anaconda` or `pip`

    ```bash    
    conda env create -f env.yml
    conda activate nisqa
    ```

1. Download the weights of the baseline model `training_base_model_dff_vanilla_ep_050.tar` from [`/weights`](https://github.com/ConferencingSpeech/ConferencingSpeech2022/tree/main/baseline/weights)
and add that to your working directory.

1. Add all wave files which you want to evaluate into `input` directory.

1. Run the prediction script from NISQA given the baseline model, the input directory and an output directory

    ```bash    
    python run_predict.py --mode predict_dir --pretrained_model training_base_model_dff_vanilla_ep_050.tar --data_dir input --num_workers 0 --bs 10 --output_dir YOUR_OUTPUT_DIR
    ```
 
1. The prediction is stored in the `YOUR_OUTPUT_DIR/NISQA_results.csv`  


For further details about NISQA and command line parameters of `run_predict` see its [Github project](https://github.com/gabrielmittag/NISQA).  


