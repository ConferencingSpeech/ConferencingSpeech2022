# ConferencingSpeech2022 Datasets
This folder gives the conferencingSpeech2022 datasets download link and a brief introduction. Participants can divide the training set and development verification set according to their own needs. More detail can be found this [paper](https://github.com/ConferencingSpeech/ConferencingSpeech2022/blob/main/Training/Dev%20datasets/ConferencingSpeech_2022_Challenge_Evaluation_Plan_version2.pdf).

# Datasets Brief Introduction
## Tencent Corpus
This dataset  includes with reverberation and without reverberation  situations. In the without reverberation  situation, there are about 10k Chinese corpus and  all speech clips experience the simulated impairment which will often be suffered in online conference. While, in the with reverberation situation, simulated impairment and live recorded speech clips are considered and totally count about 4k. The above dataset can be found in [here](https://www.dropbox.com/s/ocmn78uh2lu5iwg/TencentCorups.zip?dl=0)(Google chrome is recommended). For participants in China, the above dataset can also be found in [here](https://share.weiyun.com/B4IS0l3z).
##  NISQA Corpus
The NISQA Corpus includes more than 14,000 speech samples with simulated (e.g. codecs, packet-loss, background noise) and live (e.g. mobile phone, Zoom, Skype, WhatsApp) conditions. 
Subjective ratings are collected through an extension of P.808 Toolkit in which participants rated the overall quality and the perceptual quality dimensions Noisiness, Coloration, Discontinuity, and Loudness. 
Each clip has on average 5 valid votes.

For detail description about NISQA Corpus visit [https://github.com/gabrielmittag/NISQA/wiki/NISQA-Corpus](https://github.com/gabrielmittag/NISQA/wiki/NISQA-Corpus).
The corpus can be also downloaded from [here](https://depositonce.tu-berlin.de/bitstream/11303/13012.5/9/NISQA_Corpus.zip). 
The MOS values can be found in the zip file, and also in [NISQACorpus/NISQA_corpus_mos.csv](NISQACorpus/NISQA_corpus_mos.csv).

If you use the NISQA Corpus in a publication, please cite the following paper:

    @article{mittag2021nisqa,
      title={NISQA: A Deep CNN-Self-Attention Model for Multidimensional Speech Quality Prediction with Crowdsourced Datasets},
      author={Mittag, Gabriel and Naderi, Babak and Chehadi, Assmaa and M{\"o}ller, Sebastian},
      journal={INTERSPEECH},
      pages={2127-2131},
      year={2021}
    }


## IU Bloomington Corpus
There are 36,000 speech signals (16-bit single-channel audios sampled at 16 kHz) extracted from COSINE and VOiCES datasets, each truncated between 3 to 6 seconds long, with a total length of around 45 hours. The dataset (e.g. speech signals, MOS ratings, and an example data loader) can be found [here](https://drive.google.com/drive/folders/1wIgOqnKA1U-wZQrU8eb67yQyRVOK3SnZ).

If you use the IU Bloomington Corpus in a publication, please cite the following paper:

    @article{dong2020pyramid,
      title={{A pyramid recurrent network for predicting crowdsourced speech-quality ratings of real-world signals}},
      author={Dong, Xuan and Williamson, Donald S},
      booktitle={Interspeech}，
      pages={4631--4635},
      year={2020}
    }

## PSTN Corpus
In the PSTN Training dataset, 58,709 degraded speech clips with a duration of 10 seconds were collected, 40,739 files based on noisy reference files, and 17,970 files based on clean reference files. Parts of the PSTN training dataset can be downloaded [here](https://challenge.blob.core.windows.net/pstn/train.zip).

If you use the PSTN Corpus in a publication, please cite the following paper:

    @inproceedings{mittag20b_interspeech,
      author={Gabriel Mittag and Ross Cutler and Yasaman Hosseinkashi and Michael Revow and Sriram Srinivasan and Naglakshmi Chande and Robert Aichner},
      title={{DNN No-Reference PSTN Speech Quality Prediction}},
      year=2020,
      booktitle={Proc. Interspeech 2020},
    }

## Dataset Division
The training, development, and evaluation test sets in this challenge are all originated from the above-mentioned datasets. It is worth noting that the IU Bloomington corpus differs from the Tencent, NISQA and PSTN corpora that used ITU-T P.808 for subjective testing, where the IU Bloomington corpus adopted ITU-R BS.1534 for subjective testing, which resulted in a rating range of 0~100 instead of 1~5. Thus, the IU Bloomington corpus will only be provided to participants as additional materials, speech clips from IU Bloomington corpus will not appear in the evaluation test set of the challenge. Participants can decide whether to use it according to their needs. 

Due to the imbalanced size of the datasets, 80% of Tencent Corpus and 95% of PSTN Corpus are used for training and development. The rest 20% of Tencent Corpus, 5% of PSTN Corpus, and newly created TUB corpus are used for evaluation test in this challenge. We aim to make the impairment situation and score distribution in the divided dataset as even as possible.

In summary, there are about 86000 speech clips for training and development, and 4372 clips for the evaluation test in this challenge. 
They are composed of Chinese, English, and German, and consider background noise, speech enhancement system, reverberation, codecs, packet-loss and other possible online conference voice impairment scenarios.
