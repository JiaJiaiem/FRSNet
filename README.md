# A novel deep learning-based method for generating floor response spectra of building structures

## Requirements
tensorflow 2.10.0  
python 3.9.13  
numpy 1.23.5  
pandas 2.0.3  
matplotlib 3.7.2  
sklearn 1.0.2  
## Dataset
All data are downloaded from https://www.strongmotioncenter.org/  
The station names are in the data.  
Dataset Split: The dataset is split to create a test set in a 0.2 ratio.
## Model
Build model using TensorFlow framework.  
The dimension of the input features: input_size1=dimension(dimension=(60,1)),
input_size2=dimension(dimension=13)  
Batch_size:32  
Epoch:3000  
Optimize functions: Adam  
learning rate:0.0001  
Loss function:MAE  
## Some Results
