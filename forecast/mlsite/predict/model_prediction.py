import pickle


MODEL_FILE = "shared_vol/DTC.p"

with open(MODEL_FILE, "rb") as f:
    RFC = pickle.load(f)

def predict(data):
    # return RFC.predict_proba([[2,0,3,1,5]])[0][1]
    prob = RFC.predict_proba([data])[0][1]
    return prob


def get_predict(predictRow):  
    return predict(predictRow)