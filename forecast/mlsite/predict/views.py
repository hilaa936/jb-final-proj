from flask import render_template, request,Blueprint
from mlsite.predict.forms import PredictForm
from mlsite.predict.model_prediction import get_predict


predict = Blueprint('predict',__name__)

@predict.route('/predict',methods=['GET','POST'])
def prediction_page():
    form = PredictForm()
    if form.validate_on_submit():
        predictRow = form.getValues()
        result=get_predict(predictRow)
        resultDisplay=f'{result} the prediction for {" ,".join(predictRow)} '
        return  render_template('prediction.html',form=form, result=resultDisplay)

    return render_template('prediction.html',form=form, result=None)