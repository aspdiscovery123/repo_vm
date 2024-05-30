

import joblib
from flask import Flask,request

model=joblib.load(r'ccpp_model (2).pkl')

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])

def application():
    data=request.get_json(force=True)
    print(data)
    data=data['info']
    out=model.predict([data])
    print(out)
    return str(out) 

app.run(host='0.0.0.0')
