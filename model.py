import pandas as pd
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                             f1_score, classification_report, confusion_matrix,
                             roc_auc_score, roc_curve, matthews_corrcoef)
from sklearn.utils import resample
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split, cross_val_score

def separate_features(complete_data):
	""" Separates data into X (features) and y (label) datasets

    Args:
        complete_data: dataset combining like and disliked songs

    Returns:
        X: features dataset
        y: labels dataset
    """

	X = complete_data[['energy', 'liveness', 'tempo', 'speechiness', 'acousticness', 
								'instrumentalness', 'time_signature', 'danceability', 
								'key', 'duration_ms', 'loudness', 'valence', 'mode', 
								'length', 'popularity', 'explicit']]

	y = complete_data[['target']]

	return X, y

def split_data(features, target):
	""" Splits data into training and test datasets

    Args:
        features: consists of features used for prediction
        target: labeled data (either like or dislike)

    Returns:
        X_train, X_test, y_train, y_test
    """

	X_train, X_test, y_train, y_test = train_test_split(features, target, random_state=42)
	return X_train, X_test, y_train, y_test

def kNN_model(X_train, X_test, y_train, y_test):
	""" 
	Implements k-Nearest-Neighbor algorithm
    """

	knn = KNeighborsClassifier()
	knn.fit(X_train, y_train)
	y_pred_knn = knn.predict(X_test)
	y_pred_prob_knn = knn.predict_proba(X_test)[:,1]
	knn_roc = roc_auc_score(y_test, y_pred_prob_knn)

	print(knn_roc)

def logreg_model(X_train, X_test, y_train, y_test):
	""" 
	Implements Logistic Regression algorithm
    """
	logreg = LogisticRegression()
	logreg.fit(X_train, y_train)
	y_pred_logreg = logreg.predict(X_test)
	y_pred_prob_logreg = logreg.predict_proba(X_test)[:,1]
	logreg_roc = roc_auc_score(y_test, y_pred_prob_logreg)

	print(logreg_roc)

def rf_model(X_train, X_test, y_train, y_test):
	""" 
	Implements Random Forest algorithm
    """
	rf = RandomForestClassifier()
	rf.fit(X_train, y_train)
	y_pred_rf = rf.predict(X_test)
	y_pred_prob_rf = rf.predict_proba(X_test)[:,1]
	rf_roc = roc_auc_score(y_test, y_pred_prob_rf)

	print(rf_roc)

def mlp_model(X_train, X_test, y_train, y_test):
	""" 
	Implements Multilayer Perceptron (Neural Net) algorithm
    """
	mlp = MLPClassifier()
	mlp.fit(X_train, y_train)
	y_pred_mlp = mlp.predict(X_test)
	y_pred_prob_mlp = mlp.predict_proba(X_test)[:,1]
	mlp_roc = roc_auc_score(y_test, y_pred_prob_mlp)

	print(mlp_roc)

