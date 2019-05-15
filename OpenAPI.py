from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote

from tkinter import*
from tkinter import font
from tkinter import ttk
from tkinter import messagebox

import smtplib
from email.mime.text import MIMEText


decode_key = unquote('xZ%2ByjfoWhIOr7s%2BJ0QG0HbPyNRNi46%2F4l8g7G5qTQp6IgeYNACJFFvSQe%2FEgAKR09JsMDhLWpLdyHpYibXU0bQ%3D%3D')
url = 'http://apis.data.go.kr/1320000/SearchMoblphonInfoInqireService/getMoblphonAcctoKindAreaPeriodInfo'
queryParams = '?' + urlencode({ quote_plus('ServiceKey'): decode_key, quote_plus('pageNo')
: '1', quote_plus('numOfRows') : '2', quote_plus('title') : '1987', quote_plus('rtNo')
: '2017-MF02149', quote_plus('aplcName') : '주식회사 우정필름' })

#queryParams = '?' + urlencode({ quote_plus('ServiceKey'): decode_key})

request =  Request(url+queryParams)
call = urlopen (request) #API call
rescode = call.getcode()

if(rescode==200):
    response_body = call.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)


#request.get_method = lambda: 'GET'

#check error
#response_body = urlopen(request).read()
#print(response_body)

window = Tk()
window.geometry("1000x650")  #window size
window.title("☏ 폰파인더 ☏")
normalFont = font.Font(window,size= 12, weight='bold', family='맑은 고딕')
boldFont = font.Font(window,size= 15, weight='bold', family='맑은 고딕')


def TotalSearchButton():
    ButtonText = Button(window,text='검색하기',font=boldFont, width= 120, height = 45,command=NewEmailWindow)
    logo = PhotoImage(file='search.gif')
    ButtonText.img = logo.subsample(5, 5)
    ButtonText.config(image=ButtonText.img, compound=LEFT)
    ButtonText.place(x=330, y=20) #place사용시 pack제외


def CheckSortButton():
    ButtonText = Button(window,text='정렬하기',font=boldFont, width= 120, height = 45,command=NewEmailWindow)
    logo = PhotoImage(file='graph.gif')
    ButtonText.img = logo.subsample(7, 5)
    ButtonText.config(image=ButtonText.img, compound=LEFT)
    ButtonText.place(x=470, y=20) #place사용시 pack제외

    Variety01=IntVar()
    Variety02=IntVar()

    checkbutton1=Checkbutton(window, text="제조사 정렬", variable=Variety01, activebackground="yellow")
    checkbutton2=Checkbutton(window, text="습득일자 정렬", variable=Variety02, activebackground="pink")

    checkbutton1.place(x=620, y=20)
    checkbutton2.place(x=620, y=45)


def SearchAreaBoc():
    global AreaEntry

    AreaText = Label(window, text="지역  ",font= normalFont)
    AreaText.place(x=20, y=80)

    AreaEntry = Entry(window, width=10)
    AreaEntry.place(x=60, y=85)

def SearchBrandBoc():
    global BrandEntry

    AreaText = Label(window, text="브랜드  ",font= normalFont)
    AreaText.place(x=150, y=80)

    BrandComBox = ttk.Combobox(window, width=12, height=15, textvariable=str)
    BrandComBox['values'] = ('애플', '삼성', 'LG', '샤오미', '소니', '베가', '펜택', '기타')
    BrandComBox.grid(column=0, row=0)
    BrandComBox.current(0)
    BrandComBox.place(x=210, y=84)
    BrandComBox.set("브랜드선택")


def SearchColorBoc():
    global ColorEntry

    ColorText = Label(window, text="색상  ",font= normalFont)
    ColorText.place(x=330, y=80)

    ColorComBox = ttk.Combobox(window, width=12, height=15, textvariable=str)
    ColorComBox['values'] = ('블랙', '화이트', '그레이', '골드', '실버', '레드'
                             , '옐로우', '블루', '핑크', '기타')
    ColorComBox.grid(column=0, row=0)
    ColorComBox.current(0)
    ColorComBox.place(x=370, y=84)
    ColorComBox.set("색상선택")


def InitSearchYMD():
    global SearchStartYearEntry, SearchStartMonthEntry, SearchStartDayEntry
    global SearchEndYearEntry, SearchEndMonthEntry, SearchEndDayEntry

    SearchStartEntryPos = (20, 20)

    SearchStartText = Label(window, text="예상 분실 시작날짜",font= normalFont)
    SearchStartText.place(x=SearchStartEntryPos[0]-10 , y=SearchStartEntryPos[1]-10)

    SearchStartYearEntry = Spinbox(window, from_=2000, to=2019, width=4)
    SearchStartYearEntry.pack()
    SearchStartYearEntry.place(x=SearchStartEntryPos[0], y=SearchStartEntryPos[1] + 20)

    SearchStartMonthEntry = Spinbox(window, from_=1, to=12, width=2)
    SearchStartMonthEntry.pack()
    SearchStartMonthEntry.place(x=SearchStartEntryPos[0] + 60, y=SearchStartEntryPos[1] + 20)

    SearchStartDayEntry = Spinbox(window, from_=1, to=31, width=2)
    SearchStartDayEntry.pack()
    SearchStartDayEntry.place(x=SearchStartEntryPos[0] + 100, y=SearchStartEntryPos[1] + 20)

    SearchEndEntryPos = (180, 20)

    SearchEndText = Label(window, text="예상 분실 끝날짜",font= normalFont)
    SearchEndText.place(x=SearchEndEntryPos[0] -5, y=SearchEndEntryPos[1]-10)

    SearchEndYearEntry = Spinbox(window, from_=2000, to=2019, width=4)
    SearchEndYearEntry.pack()
    SearchEndYearEntry.place(x=SearchEndEntryPos[0], y=SearchEndEntryPos[1] + 20)

    SearchEndMonthEntry = Spinbox(window, from_=1, to=12, width=2)
    SearchEndMonthEntry.pack()
    SearchEndMonthEntry.place(x=SearchEndEntryPos[0] + 60, y=SearchEndEntryPos[1] + 20)

    SearchEndDayEntry = Spinbox(window, from_=1, to=31, width=2)
    SearchEndDayEntry.pack()
    SearchEndDayEntry.place(x=SearchEndEntryPos[0] + 100, y=SearchEndEntryPos[1] + 20)



# Email Preparing
def EmailButton():
    global EmailButton
    EmailButton = Button(window,text='메일전송',font=boldFont,command=NewCheckTkinter)
    logo = PhotoImage(file='mail.gif')
    EmailButton.img = logo.subsample(12, 12)
    EmailButton.config(image=EmailButton.img, compound=LEFT)
    EmailButton.place(x=820, y=580)

def NewCheckTkinter():
    miniWindow=Toplevel(window)
    miniWindow.geometry("320x160")
    miniWindow.title("메일 입력창")
    miniWindow.configure(background='pink')

    label= Label(miniWindow, text = "메일을 입력해주세요♡",font = normalFont)
    label.place(x=75,y=30)

    EmailEntry = Entry(miniWindow, width=14)
    EmailEntry.place(x=50,y=85)

    EmailComBox = ttk.Combobox(miniWindow, width=12, height=15, textvariable=str)
    EmailComBox['values'] = ('naver.com', 'daum.net', 'gmail.com', 'nate.com', 'hanmail.net', 'kpu.ac,kr'
                             ,'기타')

    EmailComBox.grid(column=0, row=0)
    EmailComBox.current(0)
    EmailComBox.place(x=160, y=85)
    EmailComBox.set("메일선택")

    EmailSend = Button(miniWindow, text='메일전송', command=NewEmailWindow)
    EmailSend.place(x=230, y= 120)

# map Preparing
def mapButton():
    global MapButton
    MapButton = Button(window,text='지도보기',font=boldFont,command=NewEmailWindow)
    logo = PhotoImage(file='map.gif')
    MapButton.img = logo.subsample(12, 12)
    MapButton.config(image=MapButton.img, compound=LEFT)
    MapButton.place(x=650, y=580)

# Image Preparing
def ImageButton():
    global ImageButton
    ImageButton = Button(window,text='사진보기',font=boldFont,command=NewEmailWindow)
    logo = PhotoImage(file='image.gif')
    ImageButton.img = logo.subsample(12, 12)
    ImageButton.config(image=ImageButton.img, compound=LEFT)
    ImageButton.place(x=480, y=580)

#함수 잘 불리는지 테스트 창
def NewEmailWindow():
    messagebox.showinfo("알림창,테스트창~", message="준비 중입니다^_^")

def main():
    CheckSortButton()
    ImageButton()
    mapButton()
    EmailButton()
    TotalSearchButton()
    SearchAreaBoc()
    InitSearchYMD()
    SearchBrandBoc()
    SearchColorBoc()
    window.mainloop()

main()
