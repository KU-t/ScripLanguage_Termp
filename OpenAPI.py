
from urllib.request import  urlopen

from urllib.parse import quote_plus, urlencode, unquote
from tkinter import*
from tkinter import font
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO

#Map
import folium
import webbrowser
import os
import xml.etree.ElementTree as etree

import urllib
import urllib.request

# Email
import smtplib
from email.mime.text import MIMEText

urlArea = 'http://apis.data.go.kr/1320000/SearchMoblphonInfoInqireService/getMoblphonAcctoKindAreaPeriodInfo'
urlDetail = 'http://apis.data.go.kr/1320000/SearchMoblphonInfoInqireService/getMoblphonDetailInfo'
key = unquote("xZ%2ByjfoWhIOr7s%2BJ0QG0HbPyNRNi46%2F4l8g7G5qTQp6IgeYNACJFFvSQe%2FEgAKR09JsMDhLWpLdyHpYibXU0bQ%3D%3D")

BrandCode = {'삼성': "PRJ100", '엘지': "PRJ200", '스카이': "PRJ300", '아이폰': "PRJ400", '기타': "PRJ500"}

ColorCode = {'화이트': "CL1001", '검정': "CL1002", '빨강': "CL1003", '주황': "CL1004", '노랑': "CL1005",
             '초록': "CL1006",'파랑': "CL1007", '브라운': "CL1008", '보라': "CL1009", '기타': "CL1010"}

AreaCode = {'서울': "LCA000", '인천': "LCV000", '대구': "LCR000", '경기도': "LCI000", '경상북도': "LCK000",
            '경상남도': "LCJ000", '전라북도': "LCM000", '전라남도': "LCL000", '강원도': "LCH000", '울산': "LCU000",
            '부산': "LCT000", '광주': "LCQ000", '충청남도': "LCN000", '충청북도': "LCO000"}

POSITIONCode = [
    ['﻿가평경찰서', 37.8253995, 127.514911],
    ['경기남부지방경찰청', 37.2941531, 127.0334451],
    ['경기북부지방경찰청', 37.7560662, 127.0698444],
    ['일산경찰서', 37.6647674, 126.7695768],
    ['고양경찰서', 37.6283005, 126.8295943],
    ['과천경찰서', 37.4291373, 126.9898326],
    ['광명경찰서', 37.4739848, 126.8679017],
    ['광주경찰서', 37.4082228, 127.2396699],
    ['구리경찰서', 37.5871136, 127.1290086],
    ['군포경찰서', 37.3603903, 126.9362838],
    ['김포경찰서', 37.6369103, 126.6817472],
    ['남양주경찰서', 37.6116123, 127.1714532],
    ['동두천경찰서', 37.9103817, 127.0459792],
    ['부천원미경찰서', 37.5024622, 126.7773319],
    ['부천소사경찰서', 37.4803963, 126.7723898],
    ['부천오정경찰서', 37.514514, 126.8002796],
    ['분당경찰서', 37.3650589, 127.1053817],
    ['성남수정경찰서', 37.4419936, 127.1266515],
    ['성남중원경찰서', 37.442382, 127.1698186],
    ['수원남부경찰서', 37.2720438, 127.0540236],
    ['수원서부경찰서', 37.2585174, 126.9723444],
    ['수원중부경찰서', 37.297788, 126.9965885],
    ['시흥경찰서', 37.3762247, 126.7879168],
    ['안산상록경찰서', 37.2993135, 126.8448789],
    ['안산단원경찰서', 37.3216184, 126.8288569],
    ['안성경찰서', 37.0001607, 127.2488803],
    ['안양만안경찰서', 37.3870272, 126.9263686],
    ['안양동안경찰서', 37.3911121, 126.9486444],
    ['양주경찰서', 37.840583, 127.0540159],
    ['양평경찰서', 37.4881114, 127.4904838],
    ['여주경찰서', 37.2934968, 127.63491],
    ['연천경찰서', 38.0981369, 127.0738946],
    ['화성동부경찰서', 37.1536951, 127.0821651],
    ['용인서부경찰서', 37.3092308, 127.1065466],
    ['용인동부경찰서', 37.2412407, 127.1810948],
    ['의왕경찰서', 37.3505919, 126.9681764],
    ['의정부경찰서', 37.7441764, 127.0442602],
    ['이천경찰서', 37.2734108, 127.4349884],
    ['파주경찰서', 37.7534211, 126.7785467],
    ['평택경찰서', 36.9946071, 127.0909191],
    ['포천경찰서', 37.8936394, 127.2047452 ],
    ['하남경찰서', 37.5227417, 127.2246128],
    ['화성서부경찰서', 37.1762931, 126.8125367]
]

window = Tk()
window.geometry("1000x650")  #window size
window.title("☏ 폰파인더 ☏")
normalFont = font.Font(window,size= 12, weight='bold', family='맑은 고딕')
boldFont = font.Font(window,size= 15, weight='bold', family='맑은 고딕')

imageurl = "이미지가 없습니다."
NoImageText = "이미지가 없습니다."
file = 'map.html'

def ComboboxSearch_ABCInit():
    global AreaEntry
    global BrandEntry
    global ColorEntry

    AreaText = Label(window, text="지역  ", font=normalFont)
    AreaText.place(x=20, y=80)

    AreaEntry = Entry(window, width=10)

    AreaEntry = ttk.Combobox(window, width=8, height=15, textvariable=str)
    AreaEntry['values'] = ('서울', '경기도', '인천', '대구', '경상북도', '경상남도', '전라북도',
                           '전라남도', '강원도', '울산', '부산', '광주', '충청남도', '충청북도')
    AreaEntry.grid(column=0, row=0)
    AreaEntry.current(0)
    AreaEntry.place(x=60, y=85)
    AreaEntry.set("지역선택")


    BrandText = Label(window, text="브랜드  ", font=normalFont)
    BrandText.place(x=150, y=80)
    BrandEntry = ttk.Combobox(window, width=12, height=15, textvariable=str)
    BrandEntry['values'] = ('삼성', '엘지', '스카이', '아이폰', '기타')
    BrandEntry.grid(column=0, row=0)
    BrandEntry.current(0)
    BrandEntry.place(x=210, y=84)
    BrandEntry.set("브랜드선택")


    ColorText = Label(window, text="색상  ", font=normalFont)
    ColorText.place(x=330, y=80)
    ColorEntry = ttk.Combobox(window, width=12, height=15, textvariable=str)
    ColorEntry['values'] = ('화이트', '검정', '빨강', '주황', '노랑', '초록', '파랑', '브라운', '보라', '기타')
    ColorEntry.grid(column=0, row=0)
    ColorEntry.current(0)
    ColorEntry.place(x=370, y=84)
    ColorEntry.set("색상선택")


def SpindoxSearch_YMDInit():
    global SearchStartYearEntry, SearchStartMonthEntry, SearchStartDayEntry
    global SearchEndYearEntry, SearchEndMonthEntry, SearchEndDayEntry

    SearchStartEntryPos = (20, 20)

    SearchStartText = Label(window, text="예상 분실 시작날짜", font=normalFont)
    SearchStartText.place(x=SearchStartEntryPos[0] - 10, y=SearchStartEntryPos[1] - 10)

    SearchStartYearEntry = Spinbox(window, from_=2018, to=2020, width=4)
    SearchStartYearEntry.pack()
    SearchStartYearEntry.place(x=SearchStartEntryPos[0], y=SearchStartEntryPos[1] + 20)

    SearchStartMonthEntry = Spinbox(window, from_=1, to=12, width=2)
    SearchStartMonthEntry.pack()
    SearchStartMonthEntry.place(x=SearchStartEntryPos[0] + 60, y=SearchStartEntryPos[1] + 20)

    SearchStartDayEntry = Spinbox(window, from_=1, to=31, width=2)

    SearchStartDayEntry.pack()
    SearchStartDayEntry.place(x=SearchStartEntryPos[0] + 100, y=SearchStartEntryPos[1] + 20)

    SearchEndEntryPos = (180, 20)

    SearchEndText = Label(window, text="예상 분실 끝날짜", font=normalFont)
    SearchEndText.place(x=SearchEndEntryPos[0] - 5, y=SearchEndEntryPos[1] - 10)

    SearchEndYearEntry = Spinbox(window, from_=2018, to=2020, width=4)
    SearchEndYearEntry.pack()
    SearchEndYearEntry.place(x=SearchEndEntryPos[0], y=SearchEndEntryPos[1] + 20)

    SearchEndMonthEntry = Spinbox(window, from_=1, to=12, width=2)
    SearchEndMonthEntry.pack()
    SearchEndMonthEntry.place(x=SearchEndEntryPos[0] + 60, y=SearchEndEntryPos[1] + 20)

    SearchEndDayEntry = Spinbox(window, from_=1, to=31, width=2)
    SearchEndDayEntry.pack()
    SearchEndDayEntry.place(x=SearchEndEntryPos[0] + 100, y=SearchEndEntryPos[1] + 20)


def WindowScreen():
    global ResultList
    global querye
    global DetailEntry

    DFont = font.Font(window, size=10, family='Consolas')
    DetailEntry = Text(window, font = DFont, width = 60, height = 9)
    DetailEntry.place(x= 500 , y= 400)

    ResultBoxScrollbar = Scrollbar(window)
    ResultBoxScrollbar.place(x = 420, y = 170,width = 20, height = 400)

    ListBoxHorizon = Scrollbar(window, orient = "horizontal")
    ListBoxHorizon.place(x = 20, y  =550, width = 390, height = 20)

    ResultList = Listbox(window, font = normalFont, width = 44, height = 17,
                         yscrollcommand=ResultBoxScrollbar.set,
                         xscrollcommand= ListBoxHorizon.set )

    ResultList.place(x= 20, y = 170)
    ResultList.bind('<<ListboxSelect>>',onselect)

    ResultBoxScrollbar.config(command=ResultList.yview)
    ListBoxHorizon.config(command= ResultList.xview)

    ResultListText = Label(window, text="[검색 결과를 확인하세요]", font=normalFont)
    ResultListText.place(y=135,x=20)

    ImageText = Label(window, text="[핸드폰 이미지]", font=normalFont)
    ImageText.place(x=500, y =135)

    ImageText = Label(window, text="[디데일 정보]", font=normalFont)
    ImageText.place(x=500, y=372)

    ResultImage = Listbox(window, font=normalFont, width=47, height=9,
                         yscrollcommand=ResultBoxScrollbar.set,
                         xscrollcommand=ListBoxHorizon.set)

    ResultImage.place(x=500, y=170)

    ImagePhone = PhotoImage (file="./image./phone1.png")
    label = Label(window, image =ImagePhone, height= 140, width=110)
    label.place(x=800,y=10)

    label.img = ImagePhone.subsample(1, 2)
    label.config(image=label.img)
    print(type(label.img))


class WindowButtons:
    def __init__(self):
        self.SearchButtonFunction()
        self.MapButtonFunction()
        self.ListPageButton()
        self.ImageButtonFunction()
        self.EmailButtonFunction()

    def SearchButtonFunction(self):
        global ModelEntry
        global SearchButton

        SearchButton = Button(window,text='검색하기',font=boldFont, width= 120, height = 45, command = SearchCommandFunction)
        logo = PhotoImage(file='./image./search.gif')
        SearchButton.img = logo.subsample(5, 5)
        SearchButton.config(image=SearchButton.img, compound=LEFT)
        SearchButton.place(x=500, y=50)

    def ImageButtonFunction(self):
        ShowImageButton = Button(window,text='사진보기',font=boldFont,command=ShowImageCommandFunction)
        logo = PhotoImage(file='./image./image.gif')
        ShowImageButton.img = logo.subsample(12, 12)
        ShowImageButton.config(image=ShowImageButton.img, compound=LEFT)
        ShowImageButton.place(x=480, y=580)

    def EmailButtonFunction(self):
        global EmailButton
        EmailButton = Button(window,text='메일전송',font=boldFont, command = self.EMailButtonMiniWindow)
        logo = PhotoImage(file='./image./mail.gif')
        EmailButton.img = logo.subsample(12, 12)
        EmailButton.config(image=EmailButton.img, compound=LEFT)
        EmailButton.place(x=820, y=580)

    def MapButtonFunction(self):
        global MapButton
        MapButton = Button(window,text='지도보기',font=boldFont,command=ShowMapCommandFunction)
        logo = PhotoImage(file='./image./map.gif')
        MapButton.img = logo.subsample(12, 12)
        MapButton.config(image=MapButton.img, compound=LEFT)
        MapButton.place(x=650, y=580)

    def ListPageButton(self):
        global leftButton
        global rightButton
        global PageText

        leftButton = Button(window, text = "◁", command = self.PageDOWN, width= 1, height = 1, font = normalFont)
        leftButton.place(x=100, y=600)
        rightButton = Button(window, text = "▷",command = self.PageUP, width= 1, height = 1, font = normalFont)
        rightButton.place(x=240, y=600)
        PageText =Label(window, font = normalFont , text = "0/0")
        PageText.place(x=165, y=600)

#ListPageButton command
    def PageUP(self):
        if queryp['page'] < totalpage:
           queryp['page']  = queryp['page'] +1
           OpenURL(queryp)
           paget = str(queryp['page']) + "/" + str(totalpage)
           PageText.configure(text=paget)

    def PageDOWN(self):
        if queryp['page'] > 1:
           queryp['page']  = queryp['page'] -1
           OpenURL(queryp)
           paget = str(queryp['page']) + "/" + str(totalpage)
           PageText.configure(text=paget)


    def EMailButtonMiniWindow(self):
        global popip
        global emailaddress
        global emailsendbutton


        popip = Toplevel(window)
        popip.geometry("320x160")
        popip.title("메일 입력창")
        popip.configure(background='pink')

        label = Label(popip, text="메일을 입력해주세요♡", font=normalFont)
        label.place(x=75, y=30)

        emailaddress= Entry(popip, width=14)
        emailaddress.place(x=50, y=85)

        emailsendbutton = ttk.Combobox(popip, width=12, height=15, textvariable=str)
        emailsendbutton['values'] = ('naver.com', 'daum.net', 'gmail.com', 'nate.com', 'hanmail.net', 'kpu.ac,kr')
        emailsendbutton.grid(column=0, row=0)
        emailsendbutton.current(0)
        emailsendbutton.place(x=160, y=85)
        emailsendbutton.set("메일선택")

        EmailSend = Button(popip, text='메일전송', command=SendEmailCommandFunction)
        EmailSend.place(x=230, y=120)




def OpenDetailURL(qeueryp):
    global position
    global imageurl

    DetailEntry.delete('1.0', END)
    query = '?' + urlencode({quote_plus('ServiceKey'): key, quote_plus('ATC_ID'): qeueryp['id'], quote_plus('FD_SN'): qeueryp['num']})

    tree = etree.parse(urlopen(urlDetail + query))
    root = tree.getroot()
    body = root[1]
    item = body[0]

    global NoImageText
    NoImageText = item.findtext('fdFilePathImg')
    if NoImageText == "https://www.lost112.go.kr/lostnfs/images/sub/img04_no_img.gif" :
        NoImageText = "이미지가 없습니다."

    state = "보관상태\t:" + item.findtext('csteSteNm') + "\n"
    place = "보관장소\t: " +  item.findtext('depPlace') + "\n"
    getplace = "습득장소\t: " +  item.findtext('fdPlace') + "\n"
    model = "모델\t: " +  item.findtext('mdcd') + "\n"
    getday = "습득일자\t: " +  item.findtext('fdYmd') + "\n"
    tel = "전화번호\t: " +  item.findtext('tel') + "\n"
    uniq = item.findtext('uniq')
    position = uniq[7:]

    totaltext = state + place + getplace + model + getday + tel + "\n" + uniq

    DetailEntry.insert(END, totaltext)

    if NoImageText == "이미지가 없습니다.":
        imagelabel = Label(window, height=220, width=420)
        phoneimage = PhotoImage(file='./image./image.gif')
        imagelabel.img = phoneimage.subsample(1, 2)
        imagelabel.config(image=imagelabel.img, compound=LEFT)

    else:
        with urllib.request.urlopen(NoImageText) as u:
            raw_data = u.read()
        im = Image.open(BytesIO(raw_data))
        phoneimage = ImageTk.PhotoImage(im)

        imagelabel = Label(window, image=phoneimage, height=220, width=420)
        imagelabel.place(x=500, y=170)
        print(type(imagelabel.img))

    imagelabel.place(x=500, y=170)


def OpenURL(queryp):

    global ResultForDetail
    query = '?' + urlencode({quote_plus('ServiceKey'): queryp['keynum'], quote_plus('COL_CD'): queryp['Color'],
                             quote_plus('FD_LCT_CD'): queryp['Location'], quote_plus('START_YMD'): queryp['start'],
                             quote_plus('END_YMD'): queryp['end'], quote_plus('PRDT_CL_CD_02'):queryp['Brand'],
                             quote_plus('pageNo'): queryp['page'], quote_plus('numOfRows'): queryp['numOfRows'], })

    tree = etree.parse(urlopen(urlArea + query))
    root = tree.getroot()
    body = root[1]
    items = body[0]

    i =0
    ResultForDetail = {}
    ResultList.delete(0, END)

    for item in items:
        ResultForDetail[i] = {'id':item.findtext('atcId'),'num':item.findtext('fdSn')}#id, 순번
        ResultList.insert(i, item.findtext('fdSbjt'))
        i+=1
    return body.findtext('totalCount')


def InitResultList():
    global ResultList
    global querye
    ResultBoxScrollbar = Scrollbar(window)
    ResultBoxScrollbar.place(x = 420, y = 170,width = 20, height = 400)


    ListBoxHorizon = Scrollbar(window, orient = "horizontal")
    ListBoxHorizon.place(x = 20, y  =550, width = 390, height = 20)


    ResultList = Listbox(window, font = normalFont, width = 44, height = 17,
                         yscrollcommand=ResultBoxScrollbar.set,
                         xscrollcommand= ListBoxHorizon.set )

    ResultList.place(x= 20, y = 170)
    ResultList.bind('<<ListboxSelect>>',onselect)

    ResultBoxScrollbar.config(command=ResultList.yview)
    ListBoxHorizon.config(command= ResultList.xview)

    ResultListText = Label(window, text="[검색 결과를 확인하세요]", font=normalFont)
    ResultListText.place(y=135,x=20)

    ImageText = Label(window, text="[핸드폰 이미지]", font=normalFont)
    ImageText.place(x=500, y =135)

    ImageText = Label(window, text="[디데일 정보]", font=normalFont)
    ImageText.place(x=500, y=372)


    ResultImage = Listbox(window, font=normalFont, width=47, height=9,
                         yscrollcommand=ResultBoxScrollbar.set,
                         xscrollcommand=ListBoxHorizon.set)

    ResultImage.place(x=500, y=170)

    ImagePhone = PhotoImage (file="phone1.png")
    label = Label(window, image =ImagePhone, height= 140, width=110)
    label.place(x=800,y=10)

    label.img = ImagePhone.subsample(1, 2)
    label.config(image=label.img)


def onselect(evt):
    w= evt.widget
    index = int(w.curselection()[0])
    OpenDetailURL( ResultForDetail[index])

#commandfunctions

def ShowImageCommandFunction():
    with urllib.request.urlopen(NoImageText) as u:
         raw_data = u.read()
    im = Image.open(BytesIO(raw_data))
    image = ImageTk.PhotoImage(im)

    width = image.width()
    height = image.height()
    popimage = Toplevel(window)
    popimage.geometry(str(width)+"x"+str(height)+"+150+50")
    imagelabel = Label(popimage, image=image, height=height, width=width)
    imagelabel.pack()
    imagelabel.place(x=0, y=0)
    popimage.mainloop()

def InitOtherButton():
    global EmailButton
    global MapButton

    ShowImageButton = Button(window,text='사진보기',font=boldFont,command=ShowImage)
    logo = PhotoImage(file='image.gif')
    ShowImageButton.img = logo.subsample(12, 12)
    ShowImageButton.config(image=ShowImageButton.img, compound=LEFT)
    ShowImageButton.place(x=480, y=580)

    EmailButton = Button(window,text='메일전송',font=boldFont, command = EMailButton)
    logo = PhotoImage(file='mail.gif')
    EmailButton.img = logo.subsample(12, 12)
    EmailButton.config(image=EmailButton.img, compound=LEFT)
    EmailButton.place(x=820, y=580)


    MapButton = Button(window,text='지도보기',font=boldFont,command=MapButton)
    logo = PhotoImage(file='map.gif')
    MapButton.img = logo.subsample(12, 12)
    MapButton.config(image=MapButton.img, compound=LEFT)
    MapButton.place(x=650, y=580)


def SendEmailCommandFunction():

    import smtplib
    from email.mime.text import MIMEText

    smtpHost ="smtp.gmail.com"
    port = "587"
    text = DetailEntry.get("1.0",'end-1c')
    msg = MIMEText(text)
    sender = "tjdtjsal96@naver.com"
    recipient = emailaddress.get() + "@" + emailsendbutton.get()
    msg['Subject'] = "당신의 분실된 핸드폰 정보입니다."
    msg['From'] = sender
    msg['To'] = recipient
    s = smtplib.SMTP(smtpHost, port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("tjdtjsal960723@gmail.com", "Sun_mee9113")
    s.sendmail(sender, [recipient], msg.as_string())
    s.close()
    popip.destroy()


def ShowMapCommandFunction():
    global position
    global file

    for i in range(20):
       if position[i] == '에':
          position = position[0:i]
          break

    posx, posy = -1, -1
    for pos in POSITIONCode:
       if pos[0] == position:
          posx, posy = pos[1], pos[2]
          break
    if posx != -1 and posy != -1:

       map = folium.Map(location=[posx, posy], zoom_start=13)
       folium.Marker([posx, posy], popup=position).add_to(map)
       file = 'map.html'
       map.save(file)
       print(type(map))
       webbrowser.open_new(file)


def SearchCommandFunction():
    global pageNum
    global totalpage
    global queryp

    SY = SearchStartYearEntry.get()
    SM = SearchStartMonthEntry.get()

    if(int(SM) < 10): SM = "0" + SM
    SD = SearchStartDayEntry.get()

    if (int(SD) < 10): SD = "0" + SD
    EY = SearchEndYearEntry.get()
    EM = SearchEndMonthEntry.get()

    if (int(EM) < 10): EM = "0" + EM
    ED = SearchEndDayEntry.get()

    if (int(ED) < 10): ED = "0" + ED
    startyear = SY + SM + SD
    endyear = EY + EM + ED
    brand = BrandEntry.get()
    area = AreaEntry.get()
    color = ColorEntry.get()
    pageNum= 1

    queryp = {'keynum': key, 'Color': ColorCode[color], 'Location': AreaCode[area],'start': startyear, 'end': endyear,
              'Brand': BrandCode[brand], 'page': pageNum, 'numOfRows': 20}
    totalnum = int(OpenURL(queryp))
    totalpage = int(totalnum / 20) + 1

    paget = str(pageNum) +"/"+ str(totalpage)
    PageText.configure(text = paget)

#######################################################
def ShowWindow():
    windowbuttons = WindowButtons()
    windowbuttons.__init__()
    WindowScreen()
    ComboboxSearch_ABCInit()  # 지역 버튼
    SpindoxSearch_YMDInit()  # 기간 버튼


def main():
    ShowWindow()
    WindowScreen()        #결과창
    window.mainloop()

main()
os.remove(file)
