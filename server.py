from flask import Flask, flash, render_template, request, url_for, redirect, session
from logzero import logger
import crud
import urllib
from db import items

app = Flask(__name__)

app.secret_key = 'rohit'



@app.route('/', methods=['GET'] )
def main():
    return render_template('main.html')

@app.route('/home', methods=['GET', 'POST'])
def home():

    result = crud.getTaskdetails(uid = session.get("UID"))

    if result:
        data = result
    else:
        data = None

    return render_template('home.html', data = data)


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template('login.html')
    else:
        usn = str(request.form.get('email'))
        psw = str(request.form.get('password'))

        logger.info("Username: {} Password: {}".format(usn, psw))

        error = None

        result = crud.checkUser(usn, psw)

        logger.warning("-----> Result: {}".format(result))

        if not result:
            error = 'Invalid credentials'

        else:

            flash('You were successfully logged in')
            return redirect(url_for('home'))

        return render_template('login.html', error=error)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')

    else:
        fname = str(request.form.get('fname'))
        lname = str(request.form.get('lname'))
        uname = str(request.form.get('uname'))
        email = str(request.form.get('email'))
        password = str(request.form.get('password'))


        logger.info("Fname: {} LName: {} UNamee: {} Email: {} password: {}".format(fname, lname, uname, email, password))

        crud.createUser(fname, lname, uname, email, password)

        return render_template('login.html') 


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    else:
        item = str(request.form.get('item'))



    logger.info("item: {}".format(item))
    
    crud.additem(item)
    

    return redirect('/home')



@app.route('/delete/<todo>/', methods = ['POST', 'GET'])
def delete(todo):
    try:

        if request.method == 'GET':

            result = crud.gettaskbyid(uid = session.get('UID'), todo = todo)
            
            return render_template('delete.html', task = result.item, id = todo)
        else :
            ID = todo
            # item = str(request.form.get('task'))
            
            logger.info("ID : {}".format(ID))
            

            result = crud.delitem(ID)
            logger.warning("-----> Result: {}".format(result))


        
    except Exception as e:
        print(e)
        
    return redirect(url_for("home"))


@app.route('/update/<todo>', methods = ['GET','POST'])
def update(todo):
    try:
        if request.method == 'GET':

            result = crud.gettaskbyid(uid = session.get('UID'), todo = todo)

            return render_template("update.html", task = result.item, id = todo)
        else:

            ID = todo

            item = str(request.form.get('task'))

        logger.info("ID : {}".format(ID))
        logger.info("item : {}".format(item))

        result = crud.updateitem(ID, item)
        logger.warning("-----> Result: {}".format(result))
        

    except Exception as e:
        print(e)
        
    return redirect(url_for("home"))


@app.route('/view', methods = ['GET, POST'])
def view():
    
    try:
        
        if request.method == 'POST':
            
            return render_template('view.html')

            result = crud.readUser()
        
            logger.info("result : {}".format(result))

    except Exception as e:
        print(e)


if __name__ == '__main__':
    app.run(debug=True)