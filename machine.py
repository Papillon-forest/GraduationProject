import csv
import datetime
import json
import pickle
from pprint import pprint

import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing
from sklearn.ensemble import AdaBoostRegressor, RandomForestRegressor
from sklearn.model_selection import cross_val_score, learning_curve, GridSearchCV
from sklearn.multioutput import MultiOutputRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from hmmlearn.hmm import GaussianHMM
import sklearn.metrics as sm
from sklearn.utils import shuffle


def write_machine_data_target(game_name):
    keywords = []
    key_days = []
    counts_5 = []
    counts_4 = []
    counts_3 = []
    counts_2 = []
    counts_1 = []
    counts_5_per = []
    counts_4_per = []
    counts_3_per = []
    counts_2_per = []
    counts_1_per = []
    rating_average = []
    positive_percent = []
    user_retention = []

    data_keys = []
    dela = datetime.timedelta(days=1)
    read = csv.reader(open(f'datasets/{game_name}/All_{game_name}_retention.csv', 'r', encoding="utf-8"))
    # data
    read_1 = json.load(open(f'datasets/{game_name}/Reviews_{game_name}_all_rating_percent_average.json', 'r', encoding="utf-8"))
    for row in read:
        data_keys.append(row)
    for i in range(len(read_1)):
        for j in range(len(data_keys)):
            if data_keys[j][3] == '100.00%':
                continue
            if read_1[i]['keywords'] == data_keys[j][0]:
                date_key = datetime.datetime.strptime(data_keys[j][0], "%Y-%m-%d")
                if 14 < date_key.day < 30:
                    key_days.append(30)
                else:
                    key_days.append(date_key.day)
                keywords.append(read_1[i]['keywords'])
                # counts_5.append(read_1[i]['counts_5'])
                # counts_4.append(read_1[i]['counts_4'])
                # counts_3.append(read_1[i]['counts_3'])
                # counts_2.append(read_1[i]['counts_2'])
                # counts_1.append(read_1[i]['counts_1'])
                counts_5_per.append(read_1[i]['rating_5_percent'])
                counts_4_per.append(read_1[i]['rating_4_percent'])
                counts_3_per.append(read_1[i]['rating_3_percent'])
                counts_2_per.append(read_1[i]['rating_2_percent'])
                counts_1_per.append(read_1[i]['rating_1_percent'])
                rating_average.append(read_1[i]['rating_average'])

    read_2 = json.load(open(f'datasets/{game_name}/Reviews_{game_name}_all_sentiment_percent.json', 'r', encoding="utf-8"))
    for i in range(len(read_2)):
        for j in range(len(data_keys)):
            if read_2[i]['keywords'] == data_keys[j][0]:
                positive_percent.append(read_2[i]['positive_percent'])

    # target
    for i in range(len(data_keys)):
        y_temp = float(data_keys[i][3].replace('%', '')) / 100
        if y_temp == float(1):
            continue
        for j in range(len(keywords)):
            if keywords[j] == data_keys[i][0]:
                user_retention.append(y_temp)
    # data_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
    # counts_5_per = data_scaler.fit_transform(np.array(counts_5_per).reshape(-1, 1))
    # counts_4_per = data_scaler.fit_transform(np.array(counts_4_per).reshape(-1, 1))
    # counts_3_per = data_scaler.fit_transform(np.array(counts_3_per).reshape(-1, 1))
    # counts_2_per = data_scaler.fit_transform(np.array(counts_2_per).reshape(-1, 1))
    # counts_1_per = data_scaler.fit_transform(np.array(counts_1_per).reshape(-1, 1))
    # rating_average = data_scaler.fit_transform(np.array(rating_average).reshape(-1, 1))
    # positive_percent = data_scaler.fit_transform(np.array(positive_percent).reshape(-1, 1))

    dict_machine = {
        'keywords': keywords,
        # 'counts_5': counts_5,
        # 'counts_4': counts_4,
        # 'counts_3': counts_3,
        # 'counts_2': counts_2,
        # 'counts_1': counts_1,
        'key_days': key_days,
        'rating_5_percent': counts_5_per,
        'rating_4_percent': counts_4_per,
        'rating_3_percent': counts_3_per,
        'rating_2_percent': counts_2_per,
        'rating_1_percent': counts_1_per,
        'rating_average': rating_average,
        'positive_percent': positive_percent,
        'user_retention': user_retention
    }

    data = json.dumps(dict_machine, indent=1, ensure_ascii=False)
    with open(f'datasets/{game_name}/Machine_{game_name}.json', 'w', encoding='utf-8') as f:
        f.write(data)
    print(len(dict_machine['keywords']))
    print('key_days', len(dict_machine['key_days']))
    print("rating_5_percent", len(dict_machine['rating_5_percent']))
    print("rating_4_percent", len(dict_machine['rating_4_percent']))
    print("rating_3_percent", len(dict_machine['rating_3_percent']))
    print("rating_2_percent", len(dict_machine['rating_2_percent']))
    print("rating_1_percent", len(dict_machine['rating_1_percent']))
    print("rating_average", len(dict_machine['rating_average']))
    print("positive_percent", len(dict_machine['positive_percent']))
    print("user_retention", len(dict_machine['user_retention']))
    return dict_machine


x = []
y = []


def get_machine_data(game_name):
    dict_machine = write_machine_data_target(game_name)
    # data_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
    # dict_machine['rating_5_percent'] = data_scaler.fit_transform(
    #     np.array(dict_machine['rating_5_percent']).reshape(-1, 1))
    # dict_machine['rating_4_percent'] = data_scaler.fit_transform(
    #     np.array(dict_machine['rating_4_percent']).reshape(-1, 1))
    # dict_machine['rating_3_percent'] = data_scaler.fit_transform(
    #     np.array(dict_machine['rating_3_percent']).reshape(-1, 1))
    # dict_machine['rating_2_percent'] = data_scaler.fit_transform(
    #     np.array(dict_machine['rating_2_percent']).reshape(-1, 1))
    # dict_machine['rating_1_percent'] = data_scaler.fit_transform(
    #     np.array(dict_machine['rating_1_percent']).reshape(-1, 1))
    # dict_machine['rating_average'] = data_scaler.fit_transform(
    #     np.array(dict_machine['rating_average']).reshape(-1, 1))
    # dict_machine['positive_percent'] = data_scaler.fit_transform(
    #     np.array(dict_machine['positive_percent']).reshape(-1, 1))
    for i in range(len(dict_machine['keywords'])):
        temp = []
        # temp.append(counts_5[i])
        # temp.append(counts_4[i])
        # temp.append(counts_3[i])
        # temp.append(counts_2[i])
        # temp.append(counts_1[i])
        temp.append(dict_machine['key_days'][i])
        temp.append(dict_machine['rating_5_percent'][i])
        temp.append(dict_machine['rating_4_percent'][i])
        temp.append(dict_machine['rating_3_percent'][i])
        temp.append(dict_machine['rating_2_percent'][i])
        temp.append(dict_machine['rating_1_percent'][i])
        temp.append(dict_machine['rating_average'][i])
        temp.append(dict_machine['positive_percent'][i])
        x.extend(temp)
    for i in range(len(dict_machine['keywords'])):
        temp = []
        temp.append(dict_machine['user_retention'][i])
        y.extend(temp)


def machine_learning_ad_curve():
    x_train_temp = np.array(x).reshape(-1, 8)
    y_train_temp = np.array(y).reshape(-1, 1)
    # pprint(len(x_train))

    x_train_temp, y_train_temp = shuffle(x_train_temp, y_train_temp, random_state=7)

    num_training = int(0.98 * len(x_train_temp))
    x_train, y_train = x_train_temp[:num_training], y_train_temp[:num_training]
    x_test, y_test = x_train_temp[num_training:], y_train_temp[num_training:]
    pprint(num_training)

    dt_regressor = DecisionTreeRegressor()
    dt_regressor.fit(x_train, y_train)
    ad_regressor = AdaBoostRegressor(DecisionTreeRegressor(), n_estimators=800, random_state=7)

    parameter_grid = np.array([200,300,400,500,600,700,800,900,1000])
    train_sizes, train_scores, validation_scores = learning_curve(ad_regressor, x_train, y_train,
                                                                  train_sizes=parameter_grid, cv=5)
    pprint(train_scores)
    pprint(validation_scores)
    plt.figure()
    plt.plot(parameter_grid, 100 * np.average(train_scores, axis=1), color='black')
    plt.title('Learning curve')
    plt.xlabel('Number of training samples')
    plt.ylabel('Accuracy')
    plt.show()


def machine_learning_ad_gs():
    x_train_temp = np.array(x).reshape(-1, 8)
    y_train_temp = np.array(y).reshape(-1, 1)
    # pprint(len(x_train))

    x_train_temp, y_train_temp = shuffle(x_train_temp, y_train_temp, random_state=7)

    num_training = int(0.98 * 800)
    x_train, y_train = x_train_temp[:num_training], y_train_temp[:num_training]
    x_test, y_test = x_train_temp[num_training:], y_train_temp[num_training:]
    pprint(num_training)

    paras = {
        "splitter": ['best', 'random'],
        "max_depth": np.arange(1, 20),
        "min_samples_leaf": np.arange(1, 20),
        "criterion": ['mse', 'mae']
    }
    DT = DecisionTreeRegressor()
    GS = GridSearchCV(DT, param_grid=paras, cv=8).fit(x_train, y_train)
    pprint(GS.best_params_)
    pprint(GS.best_score_)


def machine_learn_ada_decisiontree():
    x_train_temp = np.array(x).reshape(-1, 8)
    y_train_temp = np.array(y).reshape(-1, 1)
    # pprint(len(x_train))

    x_train_temp, y_train_temp = shuffle(x_train_temp, y_train_temp, random_state=7)

    num_training = int(0.98 * 800)
    x_train, y_train = x_train_temp[:num_training], y_train_temp[:num_training]
    x_test, y_test = x_train_temp[num_training:], y_train_temp[num_training:]
    pprint(num_training)
    dt_regressor = DecisionTreeRegressor(max_depth=18, criterion='mse', min_samples_leaf=17, splitter='random')
    dt_regressor.fit(x_train, y_train)

    ad_regressor = AdaBoostRegressor(
        DecisionTreeRegressor(max_depth=18, criterion='mse', min_samples_leaf=17, splitter='random'), n_estimators=800,
        random_state=7)
    ad_regressor.fit(x_train, y_train)
    y_pred_ab = ad_regressor.predict(x_test)

    a = cross_val_score(ad_regressor, x_train, y_train, scoring='explained_variance', cv=5)
    b = cross_val_score(ad_regressor, x_train, y_train, scoring='neg_mean_squared_error', cv=5)
    c = cross_val_score(ad_regressor, x_train, y_train, scoring='r2', cv=5)
    pprint(f"Explained variance:{a}")
    pprint(f"Mean squared error:{b}")
    pprint(f"R2 score:{c}")
    pprint(y_test)
    pprint(y_pred_ab)
    print("ada decisiontree:")
    print("Mean absolute error =", round(sm.mean_absolute_error(y_test, y_pred_ab), 2))
    print("Mean squared error =", round(sm.mean_squared_error(y_test, y_pred_ab), 2))
    print("Median absolute error =", round(sm.median_absolute_error(y_test, y_pred_ab), 2))
    print("Explained variance score =", round(sm.explained_variance_score(y_test, y_pred_ab), 2))
    print("R2 score =", round(sm.r2_score(y_test, y_pred_ab), 2))
    return ad_regressor


# def machine_learn_rbf_svm():
#     x_train_temp = np.array(x).reshape(-1, 8)
#     y_train_temp = np.array(y).reshape(-1, 1)
#     x_train_temp, y_train_temp = shuffle(x_train_temp, y_train_temp, random_state=7)
#     num_training = int(0.98 * len(x_train_temp))
#     x_train, y_train = x_train_temp[:num_training], y_train_temp[:num_training]
#     x_test, y_test = x_train_temp[num_training:], y_train_temp[num_training:]
#     pprint(num_training)
#
#     params = {'kernel': 'rbf', 'C': 1e3, 'epsilon': 0.2}
#     regressor = SVR(**params)
#     regressor.fit(x_train, y_train)
#
#     y_pred_svm = regressor.predict(x_test)
#     pprint(y_test)
#     pprint(y_pred_svm)
#     print("rbf_svm:")
#     print("Mean absolute error =", round(sm.mean_absolute_error(y_test, y_pred_svm), 2))
#     print("Mean squared error =", round(sm.mean_squared_error(y_test, y_pred_svm), 2))
#     print("Median absolute error =", round(sm.median_absolute_error(y_test, y_pred_svm), 2))
#     print("Explained variance score =", round(sm.explained_variance_score(y_test, y_pred_svm), 2))
#     print("R2 score =", round(sm.r2_score(y_test, y_pred_svm), 2))
#
#
# def machine_learn_linear_svm():
#     x_train_temp = np.array(x).reshape(-1, 8)
#     y_train_temp = np.array(y).reshape(-1, 1)
#     x_train_temp, y_train_temp = shuffle(x_train_temp, y_train_temp, random_state=7)
#     num_training = int(0.98 * len(x_train_temp))
#     x_train, y_train = x_train_temp[:num_training], y_train_temp[:num_training]
#     x_test, y_test = x_train_temp[num_training:], y_train_temp[num_training:]
#     pprint(num_training)
#
#     params = {'kernel': 'linear', 'C': 1e3}
#     regressor = SVR(**params)
#     regressor.fit(x_train, y_train)
#
#     y_pred_svm = regressor.predict(x_test)
#     pprint(y_test)
#     pprint(y_pred_svm)
#     print("linear svm:")
#     print("Mean absolute error =", round(sm.mean_absolute_error(y_test, y_pred_svm), 2))
#     print("Mean squared error =", round(sm.mean_squared_error(y_test, y_pred_svm), 2))
#     print("Median absolute error =", round(sm.median_absolute_error(y_test, y_pred_svm), 2))
#     print("Explained variance score =", round(sm.explained_variance_score(y_test, y_pred_svm), 2))
#     print("R2 score =", round(sm.r2_score(y_test, y_pred_svm), 2))
#
#
# def machine_learn_poly_svm():
#     x_train_temp = np.array(x).reshape(-1, 8)
#     y_train_temp = np.array(y).reshape(-1, 1)
#     x_train_temp, y_train_temp = shuffle(x_train_temp, y_train_temp, random_state=7)
#     num_training = int(0.98 * len(x_train_temp))
#     x_train, y_train = x_train_temp[:num_training], y_train_temp[:num_training]
#     x_test, y_test = x_train_temp[num_training:], y_train_temp[num_training:]
#     pprint(num_training)
#
#     params = {'kernel': 'poly', 'C': 1e3, 'degree': 2}
#     regressor = SVR(**params)
#     regressor.fit(x_train, y_train)
#
#     y_pred_svm = regressor.predict(x_test)
#     pprint(y_test)
#     pprint(y_pred_svm)
#     print("poly svm:")
#     print("Mean absolute error =", round(sm.mean_absolute_error(y_test, y_pred_svm), 2))
#     print("Mean squared error =", round(sm.mean_squared_error(y_test, y_pred_svm), 2))
#     print("Median absolute error =", round(sm.median_absolute_error(y_test, y_pred_svm), 2))
#     print("Explained variance score =", round(sm.explained_variance_score(y_test, y_pred_svm), 2))
#     print("R2 score =", round(sm.r2_score(y_test, y_pred_svm), 2))
#
#


def machine_learning_rd_curve():
    x_train_temp = np.array(x).reshape(-1, 8)
    y_train_temp = np.array(y).reshape(-1, 1)
    # pprint(len(x_train))

    x_train_temp, y_train_temp = shuffle(x_train_temp, y_train_temp, random_state=7)

    num_training = int(0.98 * len(x_train_temp))
    x_train, y_train = x_train_temp[:num_training], y_train_temp[:num_training]
    x_test, y_test = x_train_temp[num_training:], y_train_temp[num_training:]
    pprint(num_training)

    regr_rf = MultiOutputRegressor(RandomForestRegressor())
    regr_rf.fit(x_train, y_train)

    parameter_grid = np.array([200,300,400,500,600,700,800,900,1000])
    train_sizes, train_scores, validation_scores = learning_curve(regr_rf, x_train, y_train,
                                                                  train_sizes=parameter_grid, cv=5)
    pprint(train_scores)
    pprint(validation_scores)
    plt.figure()
    plt.plot(parameter_grid, 100 * np.average(train_scores, axis=1), color='black')
    plt.title('Learning curve')
    plt.xlabel('Number of training samples')
    plt.ylabel('Accuracy')
    plt.show()


def machine_learning_rd_gs():
    x_train_temp = np.array(x).reshape(-1, 8)
    y_train_temp = np.array(y).reshape(-1, 1)
    # pprint(len(x_train))

    x_train_temp, y_train_temp = shuffle(x_train_temp, y_train_temp, random_state=7)

    num_training = int(0.98 * 800)
    x_train, y_train = x_train_temp[:num_training], y_train_temp[:num_training]
    x_test, y_test = x_train_temp[num_training:], y_train_temp[num_training:]
    pprint(num_training)

    paras = {
        "n_estimators": [50,80,100,120,150],
        "max_depth": np.arange(1, 30),
    }
    DT = RandomForestRegressor()
    GS = GridSearchCV(DT, param_grid=paras, cv=8).fit(x_train, y_train)
    pprint(GS.best_params_)
    pprint(GS.best_score_)

def machine_learning_mul_randomforest():
    x_train_temp = np.array(x).reshape(-1, 8)
    y_train_temp = np.array(y).reshape(-1, 1)

    x_train_temp, y_train_temp = shuffle(x_train_temp, y_train_temp, random_state=7)
    num_training = int(0.98 * 800)
    x_train, y_train = x_train_temp[:num_training], y_train_temp[:num_training]
    x_test, y_test = x_train_temp[num_training:], y_train_temp[num_training:]
    pprint(num_training)

    # 定义模型
    regr_rf = MultiOutputRegressor(RandomForestRegressor(n_estimators=150, max_depth=4,
                                                         random_state=2))
    # 集合模型
    regr_rf.fit(x_train, y_train)
    # 利用预测
    y_pred_rf = regr_rf.predict(x_test)
    a = cross_val_score(regr_rf, x_train, y_train, scoring='explained_variance', cv=5)
    b = cross_val_score(regr_rf, x_train, y_train, scoring='neg_mean_squared_error', cv=5)
    c = cross_val_score(regr_rf, x_train, y_train, scoring='r2', cv=5)
    pprint(f"Explained variance:{a}")
    pprint(f"Mean squared error:{b}")
    pprint(f"R2 score:{c}")
    pprint(y_test)
    pprint(y_pred_rf)
    print("mul randomforest:")
    print("Mean absolute error =", round(sm.mean_absolute_error(y_test, y_pred_rf), 2))
    print("Mean squared error =", round(sm.mean_squared_error(y_test, y_pred_rf), 2))
    print("Median absolute error =", round(sm.median_absolute_error(y_test, y_pred_rf), 2))
    print("Explained variance score =", round(sm.explained_variance_score(y_test, y_pred_rf), 2))
    print("R2 score =", round(sm.r2_score(y_test, y_pred_rf), 2))
#
#
# def machine_learning_hmm():
#     x_train_temp = np.array(x).reshape(-1, 8)
#     y_train_temp = np.array(y).reshape(-1, 1)
#     x_train_temp, y_train_temp = shuffle(x_train_temp, y_train_temp, random_state=7)
#     num_training = int(0.98 * len(x_train_temp))
#     x_train, y_train = x_train_temp[:num_training], y_train_temp[:num_training]
#     x_test, y_test = x_train_temp[num_training:], y_train_temp[num_training:]
#     pprint(num_training)
#
#     # 定义模型
#     model = GaussianHMM(n_components=2, covariance_type="diag", n_iter=10000)
#     # 集合模型
#     model.fit(x_train)
#     # 利用预测
#     y_pred_hmm = model.predict(x_test)
#     pprint(y_test)
#     pprint(y_pred_hmm)
#     print("hmm randomforest:")
#     print("Mean absolute error =", round(sm.mean_absolute_error(y_test, y_pred_hmm), 2))
#     print("Mean squared error =", round(sm.mean_squared_error(y_test, y_pred_hmm), 2))
#     print("Median absolute error =", round(sm.median_absolute_error(y_test, y_pred_hmm), 2))
#     print("Explained variance score =", round(sm.explained_variance_score(y_test, y_pred_hmm), 2))
#     print("R2 score =", round(sm.r2_score(y_test, y_pred_hmm), 2))


def save_model():
    model = machine_learn_ada_decisiontree()
    output_model_file = 'saved_model.pkl'
    with open(output_model_file, 'wb') as f:
        pickle.dump(model, f)


def use_model():
    with open('saved_model.pkl', 'rb') as f:
        model_linregr = pickle.load(f)

    x_train_temp = np.array(x).reshape(-1, 8)
    y_train_temp = np.array(y).reshape(-1, 1)
    # pprint(len(x_train))
    x_train_temp, y_train_temp = shuffle(x_train_temp, y_train_temp, random_state=7)
    num_training = int(0.98 * 800)
    x_train, y_train = x_train_temp[:num_training], y_train_temp[:num_training]
    x_test, y_test = x_train_temp[num_training:], y_train_temp[num_training:]

    y_test_pred_new = model_linregr.predict(x_test)
    pprint(y_test)
    pprint(y_test_pred_new)
    print("ada decisiontree:")
    print("Mean absolute error =", round(sm.mean_absolute_error(y_test, y_test_pred_new), 2))
    print("Mean squared error =", round(sm.mean_squared_error(y_test, y_test_pred_new), 2))
    print("Median absolute error =", round(sm.median_absolute_error(y_test, y_test_pred_new), 2))
    print("Explained variance score =", round(sm.explained_variance_score(y_test, y_test_pred_new), 2))
    print("R2 score =", round(sm.r2_score(y_test, y_test_pred_new), 2))


get_machine_data('Angry Birds')
get_machine_data('Candy Crush Saga')
get_machine_data('Plants vs. Zombies')
get_machine_data('Subway Surfers')
get_machine_data("Lily's Garden")
get_machine_data("Tetris")


# machine_learning_rd_curve()
# machine_learning_rd_gs()
# machine_learning_mul_randomforest()


# machine_learning_curve()
# machine_learning_gs()
a = machine_learn_ada_decisiontree()

# feature_importances = 100.0 * (a.feature_importances_ / max(a.feature_importances_))
# pprint(a.feature_importances_)

save_model()
use_model()
