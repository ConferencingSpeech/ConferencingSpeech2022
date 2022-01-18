# ConferencingSpeech 2022 challenge
This repository contains the datasets list and scripts required for the ConferencingSpeech 2022 challenge. For more details about the challenge, please see our [website](https://tea-lab.qq.com/conferencingspeech-2022).
# Details
* `baseline`, this folder contains baseline system include inference model exported by inference scripts;
* `eval`, this folder contains evaluation scripts to calculate PLCC, RMSE and SRCC;
* ` Traing\Dev datasets`, this folder contains training and development test datasets provied to the participant; 
  * `Tencent Corpus`, this dataset  includes about 14,000 speech chinese speech clips with simulated (e.g. codecs, packet-loss, background noise) and live  conditions.
  * `NISQA Corpus`, the NISQA Corpus includes more than 14,000 speech samples with simulated (e.g. codecs, packet-loss, background noise) and live (e.g. mobile phone, Zoom, Skype, WhatsApp) conditions. 
  * `IU Bloomington Corpus`, there are 36,000 speech signals (18,000 each) extracted from COSINE and VOiCES datasets, each truncated between 3 to 6 seconds long. Note that the IU Bloomington corpus adopts ITU-R BS.1534 (MUSHRA) for subjective rating collection, which results in a score of 0-100 instead of 1-5. Thus, the IU Bloomington corpus will only be provided to participants as additional materials, and will NOT appear in this challenge as a evaluation test set. Participants can decide whether to use it according to their needs.
  * `PSTN Corpus`, there are about 80,000 speech clips through classic public switched telephone networks, each truncated 10 seconds long. 
  
# Requirements
To install requirements install Anaconda and then use:   

>conda env create -f envs.yml


This will create a new environment with the name "conferencingSpeech". Activate this environment to go on:

>conda activate conferencingSpeech

# Code license
[Apache 2.0](https://github.com/ConferencingSpeech/ConferencingSpeech2022/blob/main/LICENSE)
