import sklearn
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
 
# import the iris dataset
iris = sklearn.datasets.load_iris()
 
print("Printing some sample data from the dataset")
for training_sample in list(zip(iris.data,iris.target))[:5]:
    print(training_sample)
# the features and class
features = iris.data
classes = iris.target
 
# Split the dataset into training (70%) and testing (30%)
ratio_train, ratio_test = 0.7 , 0.3
x_train, x_test,y__train, y__test = train_test_split(features, classes, train_size=ratio_train, test_size=ratio_test, shuffle=True)
 
# Before training the network we must scale the feature data
scaler = StandardScaler()
scaler.fit(x_train)
x_train_scale = scaler.transform(x_train)
x_test_scale = scaler.transform(x_test)
 
iterations = 1000   # the iterations for training over the dataset
hidden_layers = [10,10,10]  # the layers/depth of the NN
print("Creating a neural network with " + str(len(hidden_layers)) + " layers and " + str(iterations) + " iterations")
 
# The MLPClassifier and MLPRegressor are sklearn implementations of NNs
mlp = MLPClassifier(hidden_layer_sizes=(hidden_layers), max_iter=iterations) 
mlp.fit(x_train_scale, y__train)  # fit features over NN
 
# Run the test data over the network to see the predicted outcomes.
predicted = mlp.predict(x_test_scale)  
 
# predict over test data
# evaluation metrics and analysing the accuracy/output.
print("Evaluation: ")
print(confusion_matrix(y__test,predicted))  
 
print("Evaluation report:")
print(classification_report(y__test,predicted)) #f1-score/accuracy
