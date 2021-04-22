from db import items
from db import Sessionlocal
from db import metadata
from db import usersData
from sqlalchemy import insert,delete,update, and_
from utils import passwordhashing
from sqlalchemy import select
from flask import session
from sqlalchemy.sql import text
from logzero import logger

# from sqlalchemy.sql.expression import update


#CREATE OR ADD

def additem(item):
    try:

        db = Sessionlocal


        insertitem = insert(items).values(userId = session.get('UID'), item = item)

        db.execute(insertitem)
        db.commit()
        db.close()

    except:

        db.rollback()
        db.close()
        raise Exception


def delitem(ID):
    try:
        db = Sessionlocal
        
        deleteitem = delete(items).where(and_(items.c.ID == ID , items.c.userId == session.get('UID')))
        

        db.execute(deleteitem)
        db.commit()
        db.cloes()
       
    except:

        db.rollback()
        db.close()
        raise Exception


def updateitem(ID, item):

    try:
        db = Sessionlocal

    
        updateitem = update(items).where(items.c.ID == ID).values(item = item)

        db.execute(updateitem)
        db.commit()
        db.close()
       
    except:

        db.rollback()
        db.close()
        raise Exception 


def view():

    try:

        db = Sessionlocal

        result = db.execute('SELECT * FROM items')
        data = cur.fetchall()
        

    except:
        db.rollback()
        db.close()
        raise Exception 


def createUser(fname, lname, uname, email, password):

    try:
        
        db = Sessionlocal

        convertedpassword = passwordhashing(password)

        insertuser = insert(usersData).values(FName = fname, LName= lname, UName = uname, Email = email, Password = convertedpassword)

        db.execute(insertuser)
        db.commit()
        db.close()

    except:

        db.rollback()
        db.close()
        raise Exception


def checkUser(usn, psw):


    try:

        db = Sessionlocal

        psw = passwordhashing(psw)

        result = db.query(usersData).filter(and_(usersData.c.Email == usn, usersData.c.Password == psw)).first()

        session ['UID'] = result.Id

        if result:
            return True
        else:
            return False

    except:

        db.rollback()



def getTaskdetails(uid):

    try:

        db = Sessionlocal

        result = db.query(items).filter(items.c.userId == uid).all()

        return result

    except Exception as e:
        
        logger.error(e)


def gettaskbyid(uid, todo):

    try:

        db = Sessionlocal

        result = db.query(items).filter(and_(items.c.userId == uid, items.c.ID == todo)).first()

        return result

    except Exception as e:
        
        logger.error(e)


        