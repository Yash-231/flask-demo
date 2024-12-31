from flask import Flask, request, flash, url_for, redirect, render_template, Response
from flask_sqlalchemy import SQLAlchemy  
from werkzeug.utils import secure_filename

app = Flask(__name__)  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'  
app.config['SECRET_KEY'] = "secret key"  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  
  
class Image(db.Model):
   __tablename__ = 'images'
   id = db.Column(db.Integer, primary_key = True)  
   img = db.Column(db.String, unique=True, nullable=False)  
   img_name = db.Column(db.String, nullable=False)  
   mimetype = db.Column(db.String, nullable=False)
  
   def __init__(self, img, img_name, mimetype):  
      self.img = img  
      self.img_name = img_name  
      self.mimetype = mimetype

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/success', methods = ['GET', 'POST'])
def success():
   if request.method=='POST':
        f = request.files['file']
        if not f:
         return "No file uploaded", 400
        img_name = secure_filename(f.filename)
        mimetype = f.mimetype
        img = Image(img=f.read(), img_name=img_name, mimetype=mimetype)
        db.session.add(img)
        db.session.commit()
        return render_template("success.html", name=img_name)

@app.route('/view-images/<int:id>')
def get_images(id):
   img = Image.query.filter_by(id=id).first()
   if not img:
      return "Image not found", 404
   return Response(img.img, mimetype=img.mimetype)
		
if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)