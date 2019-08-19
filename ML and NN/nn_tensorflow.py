# Dependencies
import tensorflow as tf
import pandas as pd
import numpy as np

# Make results reproducible
seed = 1234
np.random.seed(seed)
tf.set_random_seed(seed)

# Loading the dataset
dataset = pd.read_csv('./dataset/iris.csv')
dataset = pd.get_dummies(dataset, columns=['species']) # One Hot Encoding
values = list(dataset.columns.values)

y = dataset[values[-3:]]
y = np.array(y, dtype='float32')
x = dataset[values[0:-3]]
x = np.array(x, dtype='float32')

# Shuffle Data
indices = np.random.choice(len(x), len(x), replace=False)
x_values = x[indices]
y_values = y[indices]

# Creating a Train and a Test Dataset
test_size = 10
x_test = x_values[-test_size:]
x_train = x_values[:-test_size]
y_test = y_values[-test_size:]
y_train = y_values[:-test_size]

sess = tf.Session() # Session

interval = 50
epoch = 500

# Initialize placeholders
x_data = tf.placeholder(shape=[None, 4], dtype=tf.float32)
y_target = tf.placeholder(shape=[None, 3], dtype=tf.float32)

# Input neurons : 4, Hidden neurons : 8, Output neurons : 3
hidden_layer_nodes = 8

# Create variables for Neural Network layers
w1 = tf.Variable(tf.random_normal(shape=[4, hidden_layer_nodes])) # Inputs -> Hidden Layer
w2 = tf.Variable(tf.random_normal(shape=[hidden_layer_nodes, 3])) # Hidden layer -> Outputs
b1 = tf.Variable(tf.random_normal(shape=[hidden_layer_nodes]))   # First Bias
b2 = tf.Variable(tf.random_normal(shape=[3]))   # Second Bias

# Operations
hidden_output = tf.nn.relu(tf.add(tf.matmul(x_data, w1), b1))
final_output = tf.nn.softmax(tf.add(tf.matmul(hidden_output, w2), b2))

# Cost Function
loss = tf.reduce_mean(-tf.reduce_sum(y_target * tf.log(final_output), axis=0))

# Optimizer
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(loss)

# Initialize variables
init = tf.global_variables_initializer()
sess.run(init)

# Training
print('Training the model...')
for i in range(1, (epoch + 1)):
    sess.run(optimizer, feed_dict={x_data: x_train, y_target: y_train})
    if i % interval == 0:
        print('Epoch', i, '|', 'Loss:', sess.run(loss, feed_dict={x_data: x_train, y_target: y_train}))

# Prediction
print('\n')
for i in range(len(x_test)):
    print('Actual:', y_test[i], 'Predicted:', np.rint(sess.run(final_output, feed_dict={x_data: [x_test[i]]})))