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
    data_train = []
    date_target = []
    # data
    data_train_temp = []
    read = csv.reader(open(f'datasets/{game_name}/All_{game_name}_retention.csv', 'r', encoding="utf-8"))
    for row in read:
        data_train_temp.append(row)

    for j in range(0, len(data_train_temp), 9):
        # pprint(j)
        data_train.append(float(data_train_temp[j][3].replace('%', '')) / 100)
        data_train.append(float(data_train_temp[j+1][3].replace('%', '')) / 100)
        data_train.append(float(data_train_temp[j+2][3].replace('%', '')) / 100)
        data_train.append(float(data_train_temp[j+3][3].replace('%', '')) / 100)
        data_train.append(float(data_train_temp[j+4][3].replace('%', '')) / 100)
        data_train.append(float(data_train_temp[j+5][3].replace('%', '')) / 100)
        data_train.append(float(data_train_temp[j+6][3].replace('%', '')) / 100)
    # target
    for i in range(0, len(data_train_temp), 9):
        date_target.append(float(data_train_temp[i+7][3].replace('%', '')) / 100)
    # data_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
    # counts_5_per = data_scaler.fit_transform(np.array(counts_5_per).reshape(-1, 1))
    # counts_4_per = data_scaler.fit_transform(np.array(counts_4_per).reshape(-1, 1))
    # counts_3_per = data_scaler.fit_transform(np.array(counts_3_per).reshape(-1, 1))
    # counts_2_per = data_scaler.fit_transform(np.array(counts_2_per).reshape(-1, 1))
    # counts_1_per = data_scaler.fit_transform(np.array(counts_1_per).reshape(-1, 1))
    # rating_average = data_scaler.fit_transform(np.array(rating_average).reshape(-1, 1))
    # positive_percent = data_scaler.fit_transform(np.array(positive_percent).reshape(-1, 1))

    dict_machine = {
        'data_train': data_train,
        'data_target': date_target
    }

    data = json.dumps(dict_machine, indent=1, ensure_ascii=False)
    with open(f'datasets/{game_name}/Machine_{game_name}_middle.json', 'w', encoding='utf-8') as f:
        f.write(data)
    print("data_train", len(dict_machine['data_train']))
    print("data_target", len(dict_machine['data_target']))
    return dict_machine


x = []
y = []


def get_machine_data(game_name):
    dict_machine = write_machine_data_target(game_name)
    x.extend(dict_machine['data_train'])
    y.extend(dict_machine['data_target'])


def machine_learning_ad_curve():
    x_train_temp = np.array(x).reshape(-1, 7)
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

    parameter_grid = np.array([25,50,75,100,125,150,175,200,213])
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
    x_train_temp = np.array(x).reshape(-1, 7)
    y_train_temp = np.array(y).reshape(-1, 1)
    # pprint(len(x_train))

    x_train_temp, y_train_temp = shuffle(x_train_temp, y_train_temp, random_state=7)

    num_training = int(0.98 * 200)
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
    x_train_temp = np.array(x).reshape(-1, 7)
    y_train_temp = np.array(y).reshape(-1, 1)
    # pprint(len(x_train))

    x_train_temp, y_train_temp = shuffle(x_train_temp, y_train_temp, random_state=7)

    num_training = int(0.98 * 200)
    x_train, y_train = x_train_temp[:num_training], y_train_temp[:num_training]
    x_test, y_test = x_train_temp[num_training:], y_train_temp[num_training:]
    pprint(num_training)
    dt_regressor = DecisionTreeRegressor(max_depth=17, criterion='mse', min_samples_leaf=1, splitter='random')
    dt_regressor.fit(x_train, y_train)

    ad_regressor = AdaBoostRegressor(
        DecisionTreeRegressor(max_depth=17, criterion='mse', min_samples_leaf=1, splitter='random'), n_estimators=800,
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

# def machine_learn_poly_svm():
#     x_train_temp = np.array(x).reshape(-1, 7)
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
def machine_learning_rd_curve():
    x_train_temp = np.array(x).reshape(-1, 7)
    y_train_temp = np.array(y).reshape(-1, 1)
    # pprint(len(x_train))

    x_train_temp, y_train_temp = shuffle(x_train_temp, y_train_temp, random_state=7)

    num_training = int(0.98 * len(x_train_temp))
    x_train, y_train = x_train_temp[:num_training], y_train_temp[:num_training]
    x_test, y_test = x_train_temp[num_training:], y_train_temp[num_training:]
    pprint(num_training)

    regr_rf = MultiOutputRegressor(RandomForestRegressor())
    regr_rf.fit(x_train, y_train)

    parameter_grid = np.array([50, 75, 100, 125, 150, 175, 200, 213])
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
        x_train_temp = np.array(x).reshape(-1, 7)
        y_train_temp = np.array(y).reshape(-1, 1)
        # pprint(len(x_train))

        x_train_temp, y_train_temp = shuffle(x_train_temp, y_train_temp, random_state=7)

        num_training = int(0.98 * 200)
        x_train, y_train = x_train_temp[:num_training], y_train_temp[:num_training]
        x_test, y_test = x_train_temp[num_training:], y_train_temp[num_training:]
        pprint(num_training)

        paras = {
            "n_estimators": [50, 80, 100, 120, 150],
            "max_depth": np.arange(1, 30),
        }
        DT = RandomForestRegressor()
        GS = GridSearchCV(DT, param_grid=paras, cv=8).fit(x_train, y_train)
        pprint(GS.best_params_)
        pprint(GS.best_score_)
def machine_learning_mul_randomforest():
    x_train_temp = np.array(x).reshape(-1, 7)
    y_train_temp = np.array(y).reshape(-1, 1)

    x_train_temp, y_train_temp = shuffle(x_train_temp, y_train_temp, random_state=7)
    num_training = int(0.98 * 200)
    x_train, y_train = x_train_temp[:num_training], y_train_temp[:num_training]
    x_test, y_test = x_train_temp[num_training:], y_train_temp[num_training:]
    pprint(num_training)

    # 定义模型
    regr_rf = MultiOutputRegressor(RandomForestRegressor(n_estimators=100, max_depth=29,
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



def save_model():
    model = machine_learn_ada_decisiontree()
    output_model_file = 'saved_model_middle.pkl'
    with open(output_model_file, 'wb') as f:
        pickle.dump(model, f)


def use_model():
    with open('saved_model_middle.pkl', 'rb') as f:
        model_linregr = pickle.load(f)

    x_train_temp = np.array(x).reshape(-1, 7)
    y_train_temp = np.array(y).reshape(-1, 1)
    # pprint(len(x_train))
    x_train_temp, y_train_temp = shuffle(x_train_temp, y_train_temp, random_state=7)
    num_training = int(0.98 * 200)
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
get_machine_data("Woodoku")
get_machine_data("Wordscapes")
get_machine_data("Project Makeover")
get_machine_data("Fishdom")
get_machine_data("Among us")
get_machine_data("Homescapes")


save_model()
use_model()
