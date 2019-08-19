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

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
class_names = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
feature_names = column_names[:-1]
label_name = column_names[-1]

labels = labels.map({"Iris-setosa":0, "Iris-virginica":2, "Iris-versicolor":1})
# Convert string list to float list
labels = list(map(float, labels))

# Split the data for training and testing
train_x, test_x, train_y, test_y = train_test_split(datas, labels, test_size=0.20)

NUM_EXAMPLES = len(train_y)

def make_input_fn(X, y, n_epochs=None, shuffle=True):
  def input_fn():
    dataset = tf.data.Dataset.from_tensor_slices((dict(X), y))
    if shuffle:
      dataset = dataset.shuffle(NUM_EXAMPLES)
    dataset = dataset.repeat(n_epochs)  
    dataset = dataset.batch(NUM_EXAMPLES)
    return dataset
  return input_fn

# Training and evaluation input functions.
train_input_fn = make_input_fn(train_x, train_y)
eval_input_fn = make_input_fn(test_x, test_y, shuffle=False, n_epochs=1)

fc = tf.feature_column
feature_columns = []
  
for feature_name in feature_names:
  feature_columns.append(fc.numeric_column(feature_name, dtype=tf.float32))

n_batches = 1
num_classes = len(class_names)
# Boosted Tree hien tai chi ho tro n_classes = 2 (0 va 1) nen ta se khai bao nhu vay, va do multi class nen khong tao cay duoc
est = tf.estimator.BoostedTreesClassifier(feature_columns, n_batches_per_layer=n_batches) 
# Do tensorflow chua ho tro multi-class, neu duoc ho tro thi ta se khai bao nhu nay`, khi do chuong trinh se chay dc
"""
est = tf.estimator.BoostedTreesClassifier(feature_columns, n_batches_per_layer=n_batches, n_classes = num_classes)
est.train(train_input_fn, max_steps=100)

# Test
results = est.evaluate(eval_input_fn)
print('Predicted:', results['prediction/mean'])
"""