import sklearn
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
 
## import the iris dataset for classification
iris=sklearn.datasets.load_iris()
 
## print some data, to see the imported dataset
print("Printing some sample data from the iris dataset")
for training_sample in list(zip(iris.data,iris.target))[:5]:
    print(training_sample)
 
## save the features and class
features=iris.data   	# split iris dataset into features and iris_class
iris_class=iris.target  # class[X] is output corresponding to features[X]
 
## Split the dataset into training (70%) and testing (30%)
## Note that the shuffle parameter has been used in splitting.
 
print("Splitting the data into testing and training samples")
ratio_train, ratio_test = 0.7 , 0.3
features_train, features_test,iris_class_train, iris_class_test = train_test_split(features,iris_class, train_size = ratio_train,test_size=ratio_test, shuffle=True)
 
## data preprocessing: Before training the network we must scale the feature data
print("Data preprocessing")
scaler = StandardScaler()
scaler.fit(features_train)
features_train_scale = scaler.transform(features_train)
features_test_scale = scaler.transform(features_test)
 
## The MLPClassifier and MLPRegressor are sklearn implementations of NNs
 
iterations=1000   # define the iterations for training over the dataset
hidden_layers=[10,10,10]  # define the layers/depth of the NN
print("Creating a neural network with "+str(len(hidden_layers))+" layers and "+str(iterations)+" iterations")
 
mlp = MLPClassifier(hidden_layer_sizes=(hidden_layers), max_iter=iterations) 
 
# an object which represents the neural network
# Remember to use the pre-processed data and not original values for fit()
 
mlp.fit(features_train_scale, iris_class_train)  # fit features over NN
 
## Run the test data over the network to see the predicted outcomes.
 
predicted = mlp.predict(features_test_scale)  
 
# predict over test data
## evaluation metrics and analysing the accuracy/output.
print("Evaluation: considering the confusion matrix")
print(confusion_matrix(iris_class_test,predicted))  
# all non-diagonal elements are 0 if you get 100% accuracy
 
print("Evaluation report:")
print(classification_report(iris_class_test,predicted)) 
#f1-score/accuracy