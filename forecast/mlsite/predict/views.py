from flask import render_template, request,Blueprint
from mlsite.predict.forms import PredictForm
from mlsite.predict.model_prediction import get_predict


predict = Blueprint('predict',__name__)

@predict.route('/predict',methods=['GET','POST'])
def prediction_page():
    form = PredictForm()
    if form.validate_on_submit():

        # field1=form.field1.data
        # field2=form.field2.data
        result=get_predict(form)
        
        return  render_template('prediction.html',form=form, result=result)

    return render_template('prediction.html',form=form, result=None)