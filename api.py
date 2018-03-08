from flask import Flask,request
from utils import *

app = Flask(__name__)

@app.route('/train',methods=['GET','POST'])
def train():
	dtstring = request.values['datastring'].decode('utf-8')
	cid = request.values['cid'].decode('utf-8')
	df = create_dataframe(datastring)
	df = get_sorted_dataset(df)
	df = create_learn_df(df)
	md = train_model()




