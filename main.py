from fastapi import FastAPI
from schemas.user import Iris_model , Petient_model
import pickle


pre_model = pickle.load(open('model.sav','rb'))
peti_model = pickle.load(open('model.svs','rb'))

app = FastAPI()

@app.post('/')
def predict(req:Iris_model):
    slength = req.SepalLengthCm
    swidth = req.SepalWidthCm
    plength = req.PetalLengthCm 
    pwidth = req.PetalWidthCm 


    pre_test_list = [slength,swidth,plength,pwidth]
    prediction = pre_model.predict([pre_test_list])
    print(prediction)

    if prediction[0] == '0':
        return 'this is Iris-setosa '
    elif prediction[0] == '1':
        return 'this is Iris-versicolor '
    else:
        return "this is Iris-virginica "

 # Iris-setosa':'0', 'Iris-versicolor':'1', 'Iris-virginica':'2'

@app.post('/petient')
def petient_predict(req:Petient_model):
        age = req.Age
        h = req.Height
        w = req.Weight 
      

        predi_list = [age,h,w]
        predicts = peti_model.predict([predi_list])

        # print(predicts[0][0])
        if predicts[0]== None:
             return "this is wrong value !"
        else:
             return f"this is your predict value {predicts[0][0]}"

        


 #["Age","Height","Weight"]



