import pickle


# MODEL_FILE = "shared_vol/rfc.p"

# with open(MODEL_FILE, "rb") as f:
#     RFC = pickle.load(f)

# def predict(data):
#     return RFC.predict([data])[0]


def get_predict(predictRow):
    
    return f'the prediction is bla bla bla {" ,".join(predictRow)}'