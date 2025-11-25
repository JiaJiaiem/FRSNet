# Prediction models of floor response spectra

## Requirements
tensorflow 2.10.0  
python 3.9.13  
numpy 1.23.5  
pandas 2.0.3  
matplotlib 3.7.2  
sklearn 1.0.2  
## Dataset
All data are downloaded from https://www.strongmotioncenter.org/  
In this study, data from CESMD consisting of 102 structures, including 48 concrete structures, 44 steel structures, and 10 masonry structures, was collected.
The FRS collected from all structural sensors was calculated using the excitation interpolation method with damping ratios of 0, 0.02, 0.05, 0.1, and 0.2, resulting in a total of 16570 pieces of data. 80% will be used as the training set and 20% will be used as the test set.
## Model
Build model using TensorFlow framework.  
The dimension of the input features: input_size1=dimension(dimension=(60,1)),
input_size2=dimension(dimension=9)  
Batch_size:32  
Epoch:3000  
Optimize functions: Adam  
learning rate:0.0001  
Loss function:MAE  
