from flask import Flask, render_template, request, redirect
import random
app = Flask(__name__)

@app.route("/")
def hello():
    # return "WoW!"
    return render_template("index.html")
    
#variable routing
@app.route("/greeting/<string:name>")
def greeting(name):
    return f"ㅎㅇ {name}쓰"
    

@app.route("/google")
def gogle():
    return render_template("google.html")

# 범한 실수 -> template"s", render_template, action오타    
# 사용자에게 정보받기 1. 입력창을 보여준다

@app.route("/lunch")
def lunch():
    return render_template("lunch.html")
    
@app.route("/menupick")
def menupick():
    name = request.args.get("person")
    # name = args.
    if name == "씅마이":
        return f"{name} 푸라닭 무라"
    else:
        return f"{name} 이 닭발 무러 가라"
        
@app.route("/menu/add")
def menuadd():
    return render_template("menu_add.html")
    
@app.route("/menu/create")
def menu_create():
    menu = request.args.get("menu")
    with open("menu.txt", "a") as file: #append
        file.write(menu+"\n")
    # return render_template("menu_create.html", menu=menu)
    return redirect("/menu")

@app.route("/menu")
def menu():
    addList = []
    f = open("menu.txt", "r")
    #1. 파일들 불러와서 리스트에 담는다.
    # addList = f.readlines()
    # addList = addList.split("\n")\
    with open('menu.txt') as f:
        addList = [line.rstrip() for line in f]
    #2. 리스트 하나 뽑아서 변수에 저장
    # for line in addList:
    recmdd = random.sample(addList,1)
    recmd = recmdd[0]
    # -> 아니면 
    #3. html에 추천한 것을 보여준다.
    return render_template("menu_recommend.html", recmd=recmd)