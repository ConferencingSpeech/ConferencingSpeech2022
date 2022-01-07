# ConferencingSpeech2022 Datasets
This folder gives the conferencingSpeech2022 datasets download link and a brief introduction. Participants can divide the training set and development verification set according to their own needs. More detail can be found in the above "ConferencingSpeech 2022 Challenge Evaluation Plan_version1.pdf".

# Datasets Brief Introduction
## Tencent Corpus
This dataset  includes reverberation and reverberation free situations. In the reverberation free situation, there are about 10k Chinese corpus and  all speech clips experience the simulated damage which will often be suffered in online conference. While, in the reverberation situation, simulated damage and live recorded speech clips are considered and totally count about 4k. The above dataset can be found in [website](https://share.weiyun.com/6Mn4bvOC).

##  NISQA Corpus
The NISQA Corpus includes more than 14,000 speech samples with simulated (e.g. codecs, packet-loss, background noise) and live (e.g. mobile phone, Zoom, Skype, WhatsApp) conditions. The corpus is already publicly available so it can only be used as part of the training and development test sets in the competition.
Subjective ratings are collected through an extension of P.808 Toolkit in which participants rated the overall quality and the quality dimensions Noisiness, Coloration, Discontinuity, and Loudness. Each clip has on average 5 valid votes.

## IU Bloomington Corpus
There are 36,000 speech signals (16-bit single-channel audios sampled at 16 kHz) extracted from COSINE  and VOiCESdatasets, each truncated between 3 to 6 seconds long, with a total length of around 45 hours.
About 10,000 corpus are offered in this competition.

## PSTN Corpus
The PSTN  Corpus contain 79,980 degraded speech clips with a duration
of 10 seconds were collected, 49,984 files based on noisy reference files, and 29,996 files based on clean reference files. The
files were then split into a training and validation set. 

## Dataset Division
The training, development test, and evaluation test sets in this challenge are all obtained from the above-mentioned datasets. It is worth noticing that 
different from Tencent , NISQA and PSTN corpus using ITU-T P.808 for subjective testing, the IU Bloomington corpus adopt ITU-R BS.153 to  subjective test each voice, which results in a score of 0-100 instead of 1-5. Thus, the IU Bloomington corpus will only  be provided to participants as additional materials, and will not appear in this challenge as a training, development test, or evaluation test set. Participants can decide whether to use it according to their needs. 

Due to  the imbalance in the size of the datasets, 80% of Tencent Corpus, 95% of PSTN Corpus  are used for training and development test. Then the rest 20% of Tencent Corpus and 5% of Microsoft Corpus are used for evaluation test in this challenge. We will try to make the damage situation  and score distribution in the divided dataset as even as possible.Meanwhile, due to the NISQA corpus are already publicly available so they can only be used as part of the training  and development test sets in the competition.
In addition, we will create two evaluation test datasets each with 200 clips one in German and one in English and subjective tests will be conducted using P.808 Toolkit. 

 Finally, there are about 101,000 corpus for training and  development test, 7,200 Corpus for evaluation test in this challenge. 
 They are composed of Chinese, English, and German, and consider background noise, speech enhancement system, reverberation, codecs, packet-loss and other possible online conference voice impairment scenarios.
