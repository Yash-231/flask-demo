from flask import Flask, redirect, render_template, request, flash, url_for
from forms import ContactForm
app = Flask(__name__)
app.secret_key = 'development key'



@app.route('/contact', methods = ['GET', 'POST'])  
def contact():
    form = ContactForm()
    return render_template('contact.html', form=form)
    
@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/error', methods = ['GET','POST'])  
def error():
   form = ContactForm()
   if form.validate()==False:
        flash('Please enter the correct details:')  
        return render_template('contact.html', form=form)
   else:
        return redirect(url_for('success'))

if __name__ == '__main__':
   app.run(debug = True)