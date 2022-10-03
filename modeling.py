import env
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.multiclass import OneVsRestClassifier




# Random forest function 
def RF_model():
    metrics_X = []

    for i in range(1,30):
        rf = RandomForestClassifier(max_depth=(i), 
                                    random_state=123)
    
        rf = rf.fit(X_train, y_train)
    
        in_sample_accuracy = rf.score(X_train, y_train)
    
        out_of_sample_accuracy = rf.score(X_validate, y_validate)
    
        output = {"max_depth": (i),
            "train_accuracy": in_sample_accuracy,
            "validate_accuracy": out_of_sample_accuracy}
        
        metrics_X.append(output)
    
    RFX_prediction = pd.DataFrame(metrics_X)
    RFX_prediction["difference"] = RFX_prediction.train_accuracy - RFX_prediction.validate_accuracy
    return RFX_prediction


    #decision tree function 
    def DT_model():
    metric = []

    for i in range(1,30):
        tree1 = DecisionTreeClassifier(max_depth=(i), random_state=123)

    
        tree1 = tree1.fit(X_train, y_train)
    
        in_sample_accuracy = tree1.score(X_train, y_train)
    
        out_of_sample_accuracy = tree1.score(X_validate, y_validate)
    
        output = {"max_depth": (i),
            "train_accuracy": in_sample_accuracy,
            "validate_accuracy": out_of_sample_accuracy}
        
        metric.append(output)
    
    DT_prediction = pd.DataFrame(metric)
    DT_prediction["difference"] = DT_prediction.train_accuracy - DT_prediction.validate_accuracy
    return DT_prediction


    # KNN function 
    def KNN_model():
    metric_knn = []

    for i in range(1,30):
    # weights = ['uniform', 'density']
        knn = KNeighborsClassifier(n_neighbors=(i), weights='uniform')


    
        knn = knn.fit(X_train, y_train)
    
        in_sample_accuracy = knn.score(X_train, y_train)
    
        out_of_sample_accuracy = knn.score(X_validate, y_validate)
    
        output = {"max_depth": (i),
            "train_accuracy": in_sample_accuracy,
            "validate_accuracy": out_of_sample_accuracy}
        
        metric_knn.append(output)
    
    KNN_prediction2 = pd.DataFrame(metric_knn)
    KNN_prediction2["difference"] = KNN_prediction2.train_accuracy - KNN_prediction2.validate_accuracy
    return KNN_prediction2



    #Logistic regression function
    def LR_model():
    metrics_lr2 = []

    for i in range(1,3):
    # weights = ['uniform', 'density']
        logit = LogisticRegression(random_state=123)


    
        #fit model
        logit = logit.fit(X_train, y_train)
    
        in_sample_accuracy = logit.score(X_train, y_train)
    
        out_of_sample_accuracy = logit.score(X_validate, y_validate)
    
        output = {"max_depth": (i),
            "train_accuracy": in_sample_accuracy,
            "validate_accuracy": out_of_sample_accuracy}
        
        metrics_lr2.append(output)
    
    LR_prediction2 = pd.DataFrame(metrics_lr2)
    LR_prediction2["difference"] = LR_prediction2.train_accuracy - LR_prediction2.validate_accuracy
    return LR_prediction2