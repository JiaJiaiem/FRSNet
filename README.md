# A novel deep learning-based method for generating floor response spectra of building structures  
## This repository for FRSNet
The FRSNet can predict the FRS efficiently without requiring numerical simulation and model analysis.
This repository contains the following content:
1. The dataset are provided in 'dataset' folder. The dataset is in .csv format, with the first nine parameters representing the total number of stories, lateral length, longitudinal length, total height, story height, z/h, number of basement stories, damping ratio, and direction. This is followed by the ground spectrum and floor acceleration spectrum, velocity spectrum, and displacement spectrum.
2. Loss of the final model is provided in loss.zip.
3. Model architecture and its code is provided in FRSNet.png and FRSNet.ipynb.
4. The code of the compared models(DNN,CNN,LSTM).
5. The code of excitation interpolation method is provided in excitation.py.
6. The best trained model are provided in trained_models.zip.
## Requirements
tensorflow 2.10.0  
python 3.9.13  
numpy 1.23.5  
pandas 2.0.3  
matplotlib 3.7.2  
sklearn 1.0.2  
## Acknowledgments
The authors would like to acknowledge the Center for Engineering Strong Motion Data (CESMD) for providing the structural seismic response data.
