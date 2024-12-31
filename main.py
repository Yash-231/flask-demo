from flask import *

# Initialize the Flask application
app = Flask(__name__)

# Flask Routing

@app.route('/hello')
def hello_world():
   return 'Hello World'

   # Alternate for above 3 lines is below 3 lines

# def hello_world():
#    return 'hello world'
# app.add_url_rule('/hello', 'hello', hello_world)

# Flask Variable Rules

@app.route('/hello/<name>/')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/blog/<int:postID>/')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>/')
def revision(revNo):
   return 'Revision Number %f' % revNo

# Flask URL Building

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest', guest=name))

# Flask HTTP Methods (GET & POST)

@app.route('/success/<name>')
def success(name):
   return 'Welcome %s' % name

@app.route('/login', methods=['POST','GET'])
def login():
   if request.method=='POST':
      user=request.form['nm']
      return redirect(url_for('success', name=user))
   else:
      user=request.args.get('nm')
      return redirect(url_for('success', name=user))

# Flask Templates

@app.route('/marks/<int:score>')
def marks(score):
   return render_template('score.html', marks=score)

@app.route('/result')
def result():
   dict = {'Physics': 50, 'Chemistry': 60, 'Maths': 70}
   return render_template('result.html', result=dict)

# Flask static files

@app.route('/message')  
def message():  
      return render_template('message.html')

# Sending form data to template

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/new_result', methods=['POST', 'GET'])
def new_result():
   if request.method=='POST':
      result = request.form
      return render_template("result.html", result=result)

# Flask cookies

@app.route('/error')  
def error():  
    return "<p><strong>Enter correct password</strong></p>"  
 
@app.route('/index')  
def index():  
    return render_template("index.html")  
 
@app.route('/success', methods=['POST'])  
def success_cookie():  
    if request.method == "POST":  
        email = request.form['email']  
        password = request.form['pass']
    if password=="jtp":
        resp = make_response(render_template('success.html'))  
        resp.set_cookie('email', email)  
        return resp
    else:  
        return redirect(url_for('error'))  
 
@app.route('/profile')  
def profile():  
    email = request.cookies.get('email')  
    resp = make_response(render_template('profile.html', name=email))  
    return resp  



if __name__ == '__main__':
    app.run(debug=True)