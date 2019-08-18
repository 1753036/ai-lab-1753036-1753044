from sklearn.datasets import load_iris          
from sklearn import tree 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.tree.export import export_text
from sklearn.model_selection import train_test_split
import graphviz 

iris = load_iris()                                                  # Load thư viện data
x = iris['data']
y = iris['target']
# Split the data for training and testing
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.20)

decision_tree = DecisionTreeClassifier(random_state=0, max_depth=3) # Tạo cây
decision_tree = decision_tree.fit(x, y)
predicted = decision_tree.predict(test_x)

predicted = sum(predicted == test_y) / float(len(test_y))
print(predicted)

# Draw graph
tree.plot_tree(decision_tree.fit(iris.data, iris.target)) 
r = export_text(decision_tree, feature_names=iris['feature_names'])
print(r)

# Export to file (convert to image if needed)
dot_data = tree.export_graphviz(decision_tree, out_file="tree.dot", filled=True, rounded=True) 