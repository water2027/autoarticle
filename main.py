import AI
import time
dagh = AI.AI("dagh")
writer= AI.AI("writer")
score1= AI.AI("score")
score2= AI.AI("score")
score3= AI.AI("score")
reader1= AI.AI("reader")
reader2= AI.AI("reader")
reader3= AI.AI("reader")
zsjx = AI.AI("zsjx")
readers = [reader1, reader2, reader3]
scores = [score1, score2, score3]
article=""
ghyk=""

def get_score(uuru):
    score=0
    while(True): 
        for item in scores:
            score +=int(item.get_response(uuru))
        if(score>240):
            return "good"
        else:
            text=""
            for item in readers:
                text +=item.get_response("请你给出你的意见")
            yijm=zsjx.get_response(text)
            return yijm

def get_article():
    global article
    global ghyk
    print(ghyk)
    article +=writer.get_response('这是大纲，请你写一篇文章，500字左右，可以更多。\n'+ghyk)
    while(True):
        time.sleep(3)
        wow=writer.get_response("如果你已经完成文章，请输出0；如果没有请继续完成文章。不要生成与文章无关的东西，你只能生成文章")
        if(wow=="0"):
            break;
        else:
            article +=wow

def get_ghyk():
    global ghyk
    while(True):
        wow=dagh.get_response("如果你没有完成大纲，请继续完成大纲，你必须确保大纲完成！如果你已经完成了，请你只输出'0',不要输出其它的，只能输出'0'!。你只能在大纲已经完成的时候输出0！如果大纲没有完成，但是你输出了0，一个老奶奶可能会因此离开")
        if(wow=="0"):
            break;
        else:
            ghyk +=wow

def loop_get():
    global article
    global ghyk
    while(True):
        time.sleep(3)
        get_article()
        yijm=get_score(article)
        if(yijm=="good"):
            break;
        else:
            article=""

title="标题:女人想你了，会发出这四个“信号”，别看不懂"
ghyk +=dagh.get_response(title)
get_ghyk()
time.sleep(10)
loop_get()
with open('article.txt','w',encoding='UTF-8')as f:
    f.write(article)




