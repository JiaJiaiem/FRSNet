# A novel deep learning-based method for generating floor response spectra of building structures  
## This repository for FRSNet
The FRSNet can predict the FRS efficiently without requiring numerical simulation and model analysis.
This repository contains the following content:
1. The trained models are provided in 'trained model' folder.
2. Loss curves of the final model is provided in loss.xlsx.
3. Model architecture and its code is provided in FRSNet.png and FRSNet.ipynb.
4. The code of the compared models(DNN,CNN,LSTM).
5. The predict results of different models are provided in 'DMResults'folder.
6. The code of excitation interpolation method.
7. The predict results of different number of neurons in the feature extraction part are provided in 'DNResults' folder.
## Requirements
tensorflow 2.10.0  
python 3.9.13  
numpy 1.23.5  
pandas 2.0.3  
matplotlib 3.7.2  
sklearn 1.0.2  
