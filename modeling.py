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
from sklearn.svm import LinearSVC
#from prepare import train, X_train, X_validate, X_test, y_train, y_validate, y_test



# Random forest function 
def RF_model(data1, data2, data3, data4):
    metrics_X = []

    for i in range(1,30):
        rf = RandomForestClassifier(max_depth=(i), 
                                    random_state=13)
    
        rf = rf.fit(data1, data2)
    
        in_sample_accuracy = rf.score(data1, data2)
    
        out_of_sample_accuracy = rf.score(data3, data4)
    
        output = {"max_depth": (i),
            "train_accuracy": in_sample_accuracy,
            "validate_accuracy": out_of_sample_accuracy}
        
        metrics_X.append(output)
    
    RFX_prediction = pd.DataFrame(metrics_X)
    RFX_prediction["difference"] = RFX_prediction.train_accuracy - RFX_prediction.validate_accuracy
    return RFX_prediction


    #decision tree function 
def DT_model(data1, data2, data3, data4):
    metric = []
        
    for i in range(1,30):
        tree1 = DecisionTreeClassifier(max_depth=(i), random_state=13)

        tree1 = tree1.fit(data1, data2)
        
        in_sample_accuracy = tree1.score(data1, data2)
        
        out_of_sample_accuracy = tree1.score(data3, data4)
        
        output = {"max_depth": (i),
            "train_accuracy": in_sample_accuracy,
            "validate_accuracy": out_of_sample_accuracy}
            
        metric.append(output)
        
    DT_prediction = pd.DataFrame(metric)
    DT_prediction["difference"] = DT_prediction.train_accuracy - DT_prediction.validate_accuracy
    return DT_prediction


    # KNN function 
def KNN_model(data1, data2, data3, data4):
    metric_knn = []

    for i in range(1,30):
        # weights = ['uniform', 'density']
        knn = KNeighborsClassifier(n_neighbors=(i), weights='uniform')
       
        knn = knn.fit(data1, data2)
        
        in_sample_accuracy = knn.score(data1, data2)
        
        out_of_sample_accuracy = knn.score(data3, data4)
        
        output = {"max_depth": (i),
            "train_accuracy": in_sample_accuracy,
            "validate_accuracy": out_of_sample_accuracy}
            
        metric_knn.append(output)
        
    KNN_prediction2 = pd.DataFrame(metric_knn)
    KNN_prediction2["difference"] = KNN_prediction2.train_accuracy - KNN_prediction2.validate_accuracy
    return KNN_prediction2



    #Logistic regression function
def LR_model(data1, data2, data3, data4):
    metrics_lr2 = []
    for i in range(1,3):
    # weights = ['uniform', 'density']
        logit = LogisticRegression(random_state=13)
    
        #fit model
        logit = logit.fit(data1, data2)
        in_sample_accuracy = logit.score(data1, data2)
    
        out_of_sample_accuracy = logit.score(data3, data4)
    
        output = {"max_depth": (i),
            "train_accuracy": in_sample_accuracy,
            "validate_accuracy": out_of_sample_accuracy}
        
        metrics_lr2.append(output)
    
    LR_prediction2 = pd.DataFrame(metrics_lr2)
    LR_prediction2["difference"] = LR_prediction2.train_accuracy - LR_prediction2.validate_accuracy
    return LR_prediction2



    # function for one vs rest on train
def ovr(data1, data2):
    ovr = OneVsRestClassifier(LinearSVC(random_state=13, multi_class='ovr')).fit(data1, data2)
    ovr.n_classes_
    #number of classes
    #3
    ovr.estimators_
    ovr.predict(data1) 
    ovr.score(data1, data2)
    return ovr.score(data1, data2)

# function for ovr on validate
def ovr_val(data3, data4):
    ovr = OneVsRestClassifier(LinearSVC(random_state=13, multi_class='ovr')).fit(data3, data4)

    ovr.n_classes_
#number of classes
#3
    ovr.estimators_
    ovr.predict(data3) 
    ovr.score(data3, data4)
    return ovr.score(data3, data4)



#model for test
def RF_T(data1, data2, data3):
    rf = RandomForestClassifier(max_depth=14, random_state=13)
    #fit model
    rf.fit(data1, data2)
    y_pred = rf.predict(data1)
    y_pred_proba = rf.predict_proba(data1)

    # df to hold predictions 
    pred_Test = pd.DataFrame({ # for test
    'actual': data2.rating_bin
    })
    pred_Test['baseline'] = data3[data3['rating_bin'] == 'alright'].shape[0] /data3.shape[0]

    pred_Test['RF'] = rf.score(data1, data2)
    return pred_Test


    # function for not rated df
def RF_pred(data1, data2, data3):
    rf = RandomForestClassifier(max_depth=21, random_state=123).fit(data1, data2)
    y_pred = rf.predict(data3)
    not_rated2['Predicted_Rating'] = rf.predict(not_rated)
    predictions = not_rated2[['name', 'id', 'Predicted_Rating']].copy()
    return predictions.tail()