from flask import request,redirect,session

def islogin(fun):
    def newFun(*args,**kwargs):
        if session.get("username",None):
            return fun(*args,**kwargs)
        else:
            return redirect("/login")
    return newFun
