from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('homepage.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)