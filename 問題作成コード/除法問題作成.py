#input
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.units import mm
import random
sab_name = input("題名:")
question_number = int(input("問題列の数:"))
pege_number = int(input("ページ数:"))
max_number = int(input("最大値:"))
min_number = int(input("最小値:"))
question_data = []
# A4の新規PDFファイルを作成
p = canvas.Canvas(sab_name+"_"+str(question_number)+"_"+str(pege_number)+".pdf", pagesize=portrait(A4))
for a in range(pege_number):
    # フォント登録
    pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))

    # フォント指定
    p.setFont('HeiseiMin-W3', 5*mm)

    # テキスト挿入
    p.drawString(210/16*10*mm, 270*mm, "名前")
    p.drawString(210/16*9*mm, 270*mm, "番")
    p.drawString(210/32*15*mm, 270*mm, "組")
    p.drawString(mm, 290*mm, sab_name+"　"+str(question_number*10)+"問")

    #線を挿入
    p.line(200*mm, 270*mm-mm,210/32*13*mm,270*mm-mm)

    #問題生成
    for j in range(1,question_number+1):
        for i in range(10):
            x = random.randint(min_number,max_number)
            y = random.randint(min_number,max_number)
            if y<=-1:
                p.drawString(210/question_number*(question_number-j)*mm+mm, 20+i*28*mm, str(x)+" ÷ ("+str(y)+") =")
            elif y >=1:
                p.drawString(210/question_number*(question_number-j)*mm+mm, 20+i*28*mm, str(x)+" ÷ "+str(y)+" =")
            else:
                y = random.randint(1,max_number)
                p.drawString(210/question_number*(question_number-j)*mm+mm, 20+i*28*mm, str(x)+" ÷ "+str(y)+" =")
            question_data.insert(len(question_data),x)
            question_data.insert(len(question_data),y)
    # 保存
    p.showPage()
#ここからは答え---------------------------------------------------------------------------------------------------
for a in range(pege_number):
    #色を赤に変更
    p.setFillColor("red")
    p.setStrokeColor("red")
    
    # フォント登録
    pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))

    # フォント指定
    p.setFont('HeiseiMin-W3', 5*mm)

    # テキスト挿入
    p.drawString(210/16*10*mm, 270*mm, "名前")
    p.drawString(210/16*9*mm, 270*mm, "番")
    p.drawString(210/32*15*mm, 270*mm, "組")
    p.drawString(mm, 290*mm, sab_name+"　"+str(question_number*10)+"問")

    #線を挿入
    p.line(200*mm, 270*mm-mm,210/32*13*mm,270*mm-mm)

    #問題生成
    for j in range(1,question_number+1):
        for i in range(10):
            x = question_data[i*2+(j-1)*20]
            y = question_data[i*2+(j-1)*20+1]
            if y<0:
                p.drawString(210/question_number*(question_number-j)*mm+mm, 20+i*28*mm, str(x)+" ÷ ("+str(y)+") = "+str(x/y))
            else:
                p.drawString(210/question_number*(question_number-j)*mm+mm, 20+i*28*mm, str(x)+" ÷ "+str(y)+" = "+str(x/y))
    # 保存
    p.showPage()
p.save()