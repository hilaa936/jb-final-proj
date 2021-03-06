import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
import pickle

# Need to crawl data periodically from: https://data.gov.il/dataset/train_station and retrain the model

def prep(file_name):
    # Import the data
    df = pd.read_csv(file_name, encoding="utf-8")

    # Rename columns
    df['ple'] = df['parental level of education']
    df['prep_course'] = df['test preparation course']
    df["kind"] = df["race/ethnicity"]
    df['math'] = df['math score']
    df['reading'] = df['reading score']
    df['writing'] = df['writing score']
    df.drop(columns=[
        'parental level of education', 'test preparation course', \
        'race/ethnicity', 'math score', 'reading score', 'writing score'], inplace=True)

    # Feature Engineering
    df['avg'] = (df.math + df.reading + df.writing) / 3
    df['passed'] = df.avg >= 60

    # Translate into numeric values
    df.gender.replace({'female': 1, 'male': 2}, inplace=True)
    df.lunch.replace({'standard': 1, 'free/reduced': 0}, inplace=True)
    df.prep_course.replace({'completed': 1, 'none': 0}, inplace=True)
    df.kind = df.kind.apply(lambda x: x.split(' ')[1])
    df.kind.replace({"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}, inplace=True)
    df.ple.replace({"some high school": 1, "high school": 1, \
        "some college": 2, "associate's degree": 2, \
        "bachelor's degree": 3, "master's degree": 4 }, inplace=True)

    # Removing Extra Features
    df.drop(columns=['math', 'reading', 'writing', 'avg'], inplace=True)

    print(df.columns)
    # ['gender', 'lunch', 'ple', 'prep_course', 'kind', 'passed']
    return df.drop("passed", axis=1), df["passed"]


def train(x_train, y_train):
    dtc = DecisionTreeClassifier(random_state=40, min_samples_leaf=2)
    dtc.fit(x_train, y_train)
    return dtc


def save_model(model, output_file):
    with open(output_file, "wb") as f:
        pickle.dump(model, f)


if __name__ == '__main__':
    print("Data preparation process has started...")
    x_train, y_train = prep("shared_vol/StudentsPerformance.csv")
    print("Create DTC model and started training sequence...")
    DTC = train(x_train, y_train)
    print(DTC.predict_proba([[2,0,3,1,5]])[0][1])
    print("Save DTC model...")
    save_model(DTC, "shared_vol/DTC.p")
    print("Done")