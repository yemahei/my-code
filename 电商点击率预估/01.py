import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from sklearn.preprocessing import Binarizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.model_selection import GridSearchCV





#文件读取
def read_csv_file(f,logging=False):
    print ("============================读取数据========================",f)
    print ("======================我是萌萌哒分界线========================")
    data = pd.read_csv(f)
    if logging:
        print(data.head(5))
        print(f,"  包含以下列....")
        print(data.columns.values)
        print(data.describe())
        print(data.info())
    return data

#第一类编码
def categories_process_first_class(cate):
    cate = str(cate)
    if len(cate)==1:
        if int(cate)==0:
            return 0
    else:
        return int(cate[0])

#第2类编码
def categories_process_second_class(cate):
    cate = str(cate)
    if len(cate)<3:
        return 0
    else:
        return int(cate[1:])

#年龄处理，切段
def age_process(age):
    age = int(age)
    if age==0:
        return 0
    elif age<15:
        return 1
    elif age<25:
        return 2
    elif age<40:
        return 3
    elif age<60:
        return 4
    else:
        return 5

#省份处理
def process_province(hometown):
    hometown = str(hometown)
    province = int(hometown[0:2])
    return province

#城市处理
def process_city(hometown):
    hometown = str(hometown)
    if len(hometown)>1:
        province = int(hometown[2:])
    else:
        province = 0
    return province

#几点钟
def get_time_day(t):
    t = str(t)
    t=int(t[0:2])
    return t

#一天切成4段
def get_time_hour(t):
    t = str(t)
    t=int(t[2:4])
    if t<6:
        return 0
    elif t<12:
        return 1
    elif t<18:
        return 2
    else:
        return 3

#评估与计算logloss
def logloss(act, pred):
  epsilon = 1e-15
  pred = sp.maximum(epsilon, pred)
  pred = sp.minimum(1-epsilon, pred)
  ll = sum(act*sp.log(pred) + sp.subtract(1,act)*sp.log(sp.subtract(1,pred)))
  ll = ll * -1.0/len(act)
  return ll
if __name__ == '__main__':
    train_data = read_csv_file('G:/360Downloads/pre/train.csv', logging=True)

    # ['creativeID' 'adID' 'camgaignID' 'advertiserID' 'appID' 'appPlatform']
    ad = read_csv_file('G:/360Downloads/pre/ad.csv', logging=True)
    app_categories = read_csv_file('G:/360Downloads/pre/app_categories.csv', logging=True)
    app_categories["app_categories_first_class"] = app_categories['appCategory'].apply(categories_process_first_class)
    app_categories["app_categories_second_class"] = app_categories['appCategory'].apply(categories_process_second_class)
    print(app_categories.head())
    user = read_csv_file('G:/360Downloads/pre/user.csv', logging=False)
    print(user.columns)
    print(user[user.age != 0].describe())
    print(user.age.value_counts())
    user = read_csv_file('G:/360Downloads/pre/user.csv', logging=True)
    user['age_process'] = user['age'].apply(age_process)
    user["hometown_province"] = user['hometown'].apply(process_province)
    user["hometown_city"] = user['hometown'].apply(process_city)
    user["residence_province"] = user['residence'].apply(process_province)
    user["residence_city"] = user['residence'].apply(process_city)
    print(user.head())
    print(train_data.head())
    train_data['clickTime_day'] = train_data['clickTime'].apply(get_time_day)
    train_data['clickTime_hour'] = train_data['clickTime'].apply(get_time_hour)
    # train data
    train_data['clickTime_day'] = train_data['clickTime'].apply(get_time_day)
    train_data['clickTime_hour'] = train_data['clickTime'].apply(get_time_hour)
    # train_data['conversionTime_day'] = train_data['conversionTime'].apply(get_time_day)
    # train_data['conversionTime_hour'] = train_data['conversionTime'].apply(get_time_hour)

    # test_data
    test_data = read_csv_file('G:/360Downloads/pre/test.csv', True)
    test_data['clickTime_day'] = test_data['clickTime'].apply(get_time_day)
    test_data['clickTime_hour'] = test_data['clickTime'].apply(get_time_hour)
    # test_data['conversionTime_day'] = test_data['conversionTime'].apply(get_time_day)
    # test_data['conversionTime_hour'] = test_data['conversionTime'].apply(get_time_hour)

    train_user = pd.merge(train_data, user, on='userID')
    train_user_ad = pd.merge(train_user, ad, on='creativeID')
    train_user_ad_app = pd.merge(train_user_ad, app_categories, on='appID')
    print(train_user_ad_app.head())
    print(train_user_ad_app.columns)
    x_user_ad_app = train_user_ad_app.loc[:, ['creativeID', 'userID', 'positionID',
                                              'connectionType', 'telecomsOperator', 'clickTime_day', 'clickTime_hour',
                                              'age', 'gender', 'education',
                                              'marriageStatus', 'haveBaby', 'residence', 'age_process',
                                              'hometown_province', 'hometown_city', 'residence_province',
                                              'residence_city',
                                              'adID', 'camgaignID', 'advertiserID', 'appID', 'appPlatform',
                                              'app_categories_first_class', 'app_categories_second_class']]

    x_user_ad_app = x_user_ad_app.values
    x_user_ad_app = np.array(x_user_ad_app, dtype='int32')

    # 标签部分
    y_user_ad_app = train_user_ad_app.loc[:, ['label']].values
    feat_labels = np.array(['creativeID', 'userID', 'positionID',
                            'connectionType', 'telecomsOperator', 'clickTime_day', 'clickTime_hour', 'age', 'gender',
                            'education',
                            'marriageStatus', 'haveBaby', 'residence', 'age_process',
                            'hometown_province', 'hometown_city', 'residence_province', 'residence_city',
                            'adID', 'camgaignID', 'advertiserID', 'appID', 'appPlatform',
                            'app_categories_first_class', 'app_categories_second_class'])

    forest = RandomForestClassifier(n_estimators=100,
                                    random_state=0,
                                    n_jobs=-1,oob_score=True)

    forest.fit(x_user_ad_app, y_user_ad_app.reshape(y_user_ad_app.shape[0], ))
    importances = forest.feature_importances_

    indices = np.argsort(importances)[::-1]
    print(train_user_ad_app.shape)
    print(importances)
    print(forest.oob_score_)
    test_data = pd.merge(test_data, user, on='userID')
    test_user_ad = pd.merge(test_data, ad, on='creativeID')
    test_user_ad_app = pd.merge(test_user_ad, app_categories, on='appID')

    x_test_clean = test_user_ad_app.loc[:, ['creativeID', 'userID', 'positionID',
                                            'connectionType', 'telecomsOperator', 'clickTime_day', 'clickTime_hour',
                                            'age', 'gender', 'education',
                                            'marriageStatus', 'haveBaby', 'residence', 'age_process',
                                            'hometown_province', 'hometown_city', 'residence_province',
                                            'residence_city',
                                            'adID', 'camgaignID', 'advertiserID', 'appID', 'appPlatform',
                                            'app_categories_first_class', 'app_categories_second_class']].values

    x_test_clean = np.array(x_test_clean, dtype='int32')
    print(forest.predict_proba(x_test_clean))
    print(forest.predict(x_test_clean))

    for f in range(x_user_ad_app.shape[1]):
        print("%2d) %-*s %f" % (f + 1, 30,
                                feat_labels[indices[f]],
                                importances[indices[f]]))

    plt.title('Feature Importances')
    plt.bar(range(x_user_ad_app.shape[1]),
            importances[indices],
            color='lightblue',
            align='center')

    plt.xticks(range(x_user_ad_app.shape[1]),
               feat_labels[indices], rotation=90)
    plt.xlim([-1, x_user_ad_app.shape[1]])
    print(plt.tight_layout())
    # plt.savefig('./random_forest.png', dpi=300)
    print(plt.show())


