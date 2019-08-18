from __future__ import absolute_import, division, print_function

import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split

tf.enable_eager_execution()

tf.logging.set_verbosity(tf.logging.ERROR)
tf.set_random_seed(123)

# Load dataset.
datas = pd.read_csv('./dataset/iris.csv')
labels = datas.pop('species')
labels = labels.replace('Iris-setosa', '0')
labels = labels.replace('Iris-versicolor', '1')
labels = labels.replace('Iris-virginica', '2')
# Convert string list to float list
labels = list(map(float, labels))

# Split the data for training and testing
train_x, test_x, train_y, test_y = train_test_split(datas, labels, test_size=0.20)

# Use entire batch since this is such a small dataset.
NUM_EXAMPLES = len(train_y)

def make_input_fn(X, y, n_epochs=None, shuffle=True):
  def input_fn():
    dataset = tf.data.Dataset.from_tensor_slices((dict(X), y))
    if shuffle:
      dataset = dataset.shuffle(NUM_EXAMPLES)
    # For training, cycle thru dataset as many times as need (n_epochs=None).    
    dataset = dataset.repeat(n_epochs)  
    # In memory training doesn't use batching.
    dataset = dataset.batch(NUM_EXAMPLES)
    return dataset
  return input_fn

# Training and evaluation input functions.
train_input_fn = make_input_fn(train_x, train_y)
eval_input_fn = make_input_fn(test_x, test_y, shuffle=False, n_epochs=1)

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
feature_names = column_names[:-1]
label_name = column_names[-1]
class_names = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

fc = tf.feature_column
feature_columns = []
  
for feature_name in feature_names:
  feature_columns.append(fc.numeric_column(feature_name, dtype=tf.float32))

n_batches = 1
est = tf.estimator.BoostedTreesRegressor(feature_columns, n_batches_per_layer=n_batches)
est.train(train_input_fn, max_steps=100)

# Test
results = est.evaluate(eval_input_fn)
print('Predicted:', results['prediction/mean'])

