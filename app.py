from apps import app
from apps import db
from flask import render_template
from flask import request
from apps import model
import csv
import pandas as pd
import numpy as np

# 初始页面
@app.route('/')
def welcomeindex():
    return render_template('mysql.html') #初始页面html


@app.route('/toTask1')
def toTask1():
    return render_template('task1.html')

@app.route('/toTask2')
def toTask2():
    return render_template('task2.html')

@app.route('/toTask3')
def toTask3():
    return render_template('task3.html')

# mission A
@app.route('/Task1',methods=['GET','POST'])
def missionA():
    if request.method == 'GET':
        return render_template('task1.html')  # missionA index
    else:
        resultA = []
        userid = request.form.get('userid')  # 前端的关键字
        print(userid)
        bf=pd.read_csv(open(r'/home/flyfly/final.csv', 'r'),error_bad_lines=False)

        # print(bf.loc[bf['userId'].isin([userid])])
        # print(type(bf.loc[bf['userId'].isin([userid]),['userId','title','rating','tag']]))
        # print(bf.loc[bf['userId'].isin([userid]),['userId','title','rating','tag']])
        df = bf.loc[bf['userId'].isin([userid]),['userId','title','rating','tag']]
        # print(df)

        dataSet = np.array(df)  # datafram转numpy.array
        resultA = dataSet.tolist()  # numpy.array转list

        print(resultA)
        #for i in resultA:
        #    print(i[2])
        return render_template('task1.html', a=resultA)  # 重定向到页面


# mission B
@app.route('/Task2',methods=['GET','POST'])
def missionB():
     if request.method == 'GET':
         return render_template('task2.html') # missionB index
     else:
         resultB = []
         key = request.form.get('key') #前端的关键字
         print(key)
         resultB_temp = model.Movies.query.filter(model.Movies.title.like("%"+key+"%")).all()
         for i in resultB_temp:
             resultB.append(i.title)
         print(resultB)
         # print(type(resultB))
         return render_template('task2.html',b=resultB) # 重定向到页面



#
#mission C
@app.route('/Task3',methods=['GET','POST'])
def missionC():
    if request.method == 'GET':
        return render_template('')  #missonC index 需要展示所有的风格名字
    else:
        genre = request.form.get('genre')    #前端需要展示所有的风格 用户传风格名字Action Adventure Animation
        print(genre)
        if(genre == "Action"):
            print('ok')
            resultC_temp = model.MissionC.query.with_entities(model.MissionC.Action).all()
        elif(genre == "Adventure"):
            resultC_temp = model.MissionC.query.with_entities(model.MissionC.Adventure).all()
        elif (genre == "Animation"):
            resultC_temp = model.MissionC.query.with_entities(model.MissionC.Animation).all()
        elif (genre == "Children"):
            resultC_temp = model.MissionC.query.with_entities(model.MissionC.Children).all()
        elif (genre == "Comedy"):
            resultC_temp = model.MissionC.query.with_entities(model.MissionC.Comedy).all()
        elif (genre == "Crime"):
            resultC_temp = model.MissionC.query.with_entities(model.MissionC.Crime).all()
        elif (genre == "Documentary"):
            resultC_temp = model.MissionC.query.with_entities(model.MissionC.Documentary).all()
        elif (genre == "Drama"):
            resultC_temp = model.MissionC.query.with_entities(model.MissionC.Drama).all()
        elif (genre == "Fantasy"):
            resultC_temp = model.MissionC.query.with_entities(model.MissionC.Fantasy).all()
        elif (genre == "FilmNoir"):
            resultC_temp = model.MissionC.query.with_entities(model.MissionC.FilmNoir).all()
        elif (genre == "Horror"):
            resultC_temp = model.MissionC.query.with_entities(model.MissionC.Horror).all()
        elif (genre == "IMAX"):
            resultC_temp = model.MissionC.query.with_entities(model.MissionC.IMAX).all()
        elif (genre == "Musical"):
            resultC_temp = model.MissionC.query.with_entities(model.MissionC.Musical).all()
        elif (genre == "Mystery"):
            resultC_temp = model.MissionC.query.with_entities(model.MissionC.Mystery).all()
        elif (genre == "Romance"):
            resultC_temp = model.MissionC.query.with_entities(model.MissionC.Romance).all()
        elif (genre == "SciFi"):
            resultC_temp = model.MissionC.query.with_entities(model.MissionC.SciFi).all()
        elif (genre == "Thriller"):
            resultC_temp = model.MissionC.query.with_entities(model.MissionC.Thriller).all()
        elif (genre == "War"):
            resultC_temp = model.MissionC.query.with_entities(model.MissionC.War).all()
        elif (genre == "Western"):
            resultC_temp = model.MissionC.query.with_entities(model.MissionC.Western).all()

        print(resultC_temp)
        return render_template('task3.html',c=resultC_temp)  # 重定向到页面


if __name__ == '__main__':
    # db.drop_all()
    db.create_all()
    app.run(host="0.0.0.0", debug=True)