from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import mysql.connector


mydb = mysql.connector.connect(
  host="chiri-pc",
  user="testuser",
  passwd="zxcvfdsa",
  database="intern"
)

mycursor = mydb.cursor()



app = Flask(__name__)


def answer(n):
	if(n==1):
		return 'fruit'
	else:
		return 'computer-company'


@app.route('/')
def home():
	return render_template('home.html') ## home.html file will be called and initially it will be
	## displayed




@app.route('/predict',methods=['POST'])
def predict():

	model_loaded = open("data/NB_model_final.pkl","rb")
	model_loaded_ = pickle.load(model_loaded)
	tf = open("data/cv_final.pkl","rb")
	tf = pickle.load(tf)
	

	if request.method == 'POST':
		comment = request.form['comment']

		data = [comment]
		vect = tf.transform(data)
		my_prediction = model_loaded_.predict(vect)

		ans = answer(my_prediction)			
		
		sql = "INSERT INTO apple (TEXT, CLASS) VALUES (%s, %s)"
		val = (comment, ans)
		mycursor.execute(sql, val)
		mydb.commit()

	return render_template('result.html',prediction = my_prediction) ## render_template will
## call the file result.html and pass the prediction argument as my_prediction

@app.route('/database')
def showdata():

	mycursor.execute("SELECT * FROM apple")
	myresult = mycursor.fetchall()
	df = pd.DataFrame(myresult, columns=['ID', 'TEXT', 'CLASS'])
	df = df.set_index('ID')
	return df.to_html(header="true", table_id="table")

	



if __name__ == '__main__':
	app.run(debug=True)