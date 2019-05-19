from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote

from tkinter import*
from tkinter import font
from tkinter import ttk
from tkinter import messagebox

import xml.etree.ElementTree as etree

import smtplib
from email.mime.text import MIMEText

BRANDCODE = {'삼성': "PRJ100", '엘지': "PRJ200", '스카이': "PRJ300", '아이폰': "PRJ400", '기타': "PRJ500"}
COLORCODE = {'화이트': "CL1001", '검정': "CL1002", '빨강': "CL1003", '주황': "CL1004", '노랑': "CL1005", '초록': "CL1006",
             '파랑': "CL1007", '브라운': "CL1008", '보라': "CL1009", '기타': "CL1010"}
AREACODE = {'서울': "LCA000", '인천': "LCV000", '대구': "LCR000",
            '경기도': "LCI000", '경상북도': "LCK000", '경상남도': "LCJ000", '전라북도': "LCM000", '전라남도': "LCL000",
            '강원도': "LCH000", '울산': "LCU000", '부산': "LCT000", '광주': "LCQ000",
            '충청남도': "LCN000", '충청북도': "LCO000"}


decode_key = unquote('xZ%2ByjfoWhIOr7s%2BJ0QG0HbPyNRNi46%2F4l8g7G5qTQp6IgeYNACJFFvSQe%2FEgAKR09JsMDhLWpLdyHpYibXU0bQ%3D%3D')
ResultURL = 'http://apis.data.go.kr/1320000/SearchMoblphonInfoInqireService/getMoblphonAcctoKindAreaPeriodInfo'
DETAILURL = 'http://apis.data.go.kr/1320000/SearchMoblphonInfoInqireService/getMoblphonDetailInfo'

queryParams = '?' + urlencode({ quote_plus('ServiceKey'): decode_key, quote_plus('pageNo')
: '1', quote_plus('numOfRows') : '2', quote_plus('title') : '1987', quote_plus('rtNo')
: '2017-MF02149', quote_plus('aplcName') : '주식회사 우정필름' })

#queryParams = '?' + urlencode({ quote_plus('ServiceKey'): decode_key})

request =  Request(ResultURL+queryParams)
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
    ButtonText = Button(window,text='검색하기',font=boldFont, width= 120, height = 45,command=SearchButtonClick)
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


def SearchAreaButton():
    global AreaEntry

    AreaText = Label(window, text="지역  ",font= normalFont)
    AreaText.place(x=20, y=80)

    AreaEntry = Entry(window, width=10)
    AreaEntry.place(x=60, y=85)

def SearchBrandButton():
    global BrandEntry

    AreaText = Label(window, text="브랜드  ",font= normalFont)
    AreaText.place(x=150, y=80)

    BrandComBox = ttk.Combobox(window, width=12, height=15, textvariable=str)
    BrandComBox['values'] = ('애플', '삼성', 'LG', '샤오미', '소니', '베가', '펜택', '기타')
    BrandComBox.grid(column=0, row=0)
    BrandComBox.current(0)
    BrandComBox.place(x=210, y=84)
    BrandComBox.set("브랜드선택")


def SearchColorButton():
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


def SearchYMDButton():
    global SearchStartYearEntry, SearchStartMonthEntry, SearchStartDayEntry
    global SearchEndYearEntry, SearchEndMonthEntry, SearchEndDayEntry

    SearchStartEntryPos = (20, 20)

    SearchStartText = Label(window, text="예상 분실 시작날짜",font= normalFont)
    SearchStartText.place(x=SearchStartEntryPos[0]-10 , y=SearchStartEntryPos[1]-10)

    SearchStartYearEntry = Spinbox(window, from_=2019, to=2020, width=4)
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

    SearchEndYearEntry = Spinbox(window, from_=2019, to=2020, width=4)
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
    EmailButton = Button(window,text='메일전송',font=boldFont,command=SendMailTkinter)
    logo = PhotoImage(file='mail.gif')
    EmailButton.img = logo.subsample(12, 12)
    EmailButton.config(image=EmailButton.img, compound=LEFT)
    EmailButton.place(x=820, y=580)

def SendMailTkinter():
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

def PageButton():
    global leftButton
    global rightButton
    global PageText

    leftButton = Button(window, text = "◁", command = pageDOWN, width= 1, height = 1, font = normalFont)
    leftButton.place(x= 100, y = 600)
    rightButton = Button(window, text = "▷",command = pageUP, width= 1, height = 1, font = normalFont)
    rightButton.place(x= 240, y = 600)

    PageText =Label(window, font = normalFont , text = "0/0")
    PageText.place(x = 165, y = 600)

def pageUP():
    if queryp['page'] < totalpage:
        queryp['page'] = queryp['page'] + 1
        OpenURL(queryp)
        paget = str(queryp['page']) + "/" + str(totalpage)
        PageText.configure(text=paget)

def pageDOWN():
    if queryp['page'] > 1:
        queryp['page'] = queryp['page'] - 1
        OpenURL(queryp)
        paget = str(queryp['page']) + "/" + str(totalpage)
        PageText.configure(text=paget)


def SearchButtonClick():
    global pageNum
    global totalpage
    global queryp

    # 어떻게 가져오지
    #brand = BrandComBox.get()
    brand = BRANDCODE['삼성']

    starty = SearchStartYearEntry.get()
    startm = SearchStartMonthEntry.get()
    startd = SearchStartDayEntry.get()
    startperiod = starty + startm + startd

    endy = SearchEndYearEntry.get()
    endm = SearchEndMonthEntry.get()
    endd = SearchEndDayEntry.get()
    endperiod = endy + endm + endd


    area = AREACODE['서울']

    #어떻게 가져오지
    #color = SearchColorBox.get(ACTIVE)
    color = COLORCODE['검정']

    pageNum = 1

    queryp = {'keynum': decode_key, 'Color': color, 'Location': area,
              'start': startperiod, 'end': endperiod, 'Brand': brand,
              'page': pageNum, 'numOfRows': 20}

    totalnum = int(OpenURL(queryp))
    totalpage = int(totalnum / 20)
    paget = str(pageNum) +"/"+ str(totalpage)
    PageText.configure(text = paget)

def OpenDetailURL(qeueryp):
    DetailEntry.delete('1.0', END)
    query = '?' + urlencode({quote_plus('ServiceKey'): decode_key,
                             quote_plus('ATC_ID'): qeueryp['id'],
                             quote_plus('FD_SN'): qeueryp['num']
                             })

    tree = etree.parse(urlopen(DETAILURL + query))
    root = tree.getroot()
    body = root[1]
    item = body[0]
    global imageurl
    imageurl = item.findtext('fdFilePathImg')
    if imageurl == "https://www.lost112.go.kr/lostnfs/images/sub/img04_no_img.gif" :
        imageurl = "이미지가 없습니다."
    csteSteNm = "보관상태      :" + item.findtext('csteSteNm') + "\n"
    depPlace = "보관장소      : " +  item.findtext('depPlace') + "\n"
    fdPlace = "습득장소      : " +  item.findtext('fdPlace') + "\n"
    model = "모델          : " +  item.findtext('mdcd') + "\n"
    fdYmd = "습득일자      : " +  item.findtext('fdYmd') + "\n"
    tel = "전화번호      : " +  item.findtext('tel') + "\n"
    uniq = item.findtext('uniq')
    totaltext = imageurl +"\n\n"+ csteSteNm + depPlace + fdPlace + model + fdYmd + tel + \
                "\n"+uniq
    DetailEntry.insert(END, totaltext)

def OpenURL(queryp):

    global ResultForDetail
    query = '?' + urlencode({quote_plus('ServiceKey'): queryp['keynum'],
                             quote_plus('COL_CD'): queryp['Color'],
                             quote_plus('FD_LCT_CD'): queryp['Location'],
                             quote_plus('START_YMD'): queryp['start'],
                             quote_plus('END_YMD'): queryp['end'],
                             quote_plus('PRDT_CL_CD_02'):queryp['Brand'],
                             quote_plus('pageNo'): queryp['page'],
                             quote_plus('numOfRows'): queryp['numOfRows'],
                             })

    tree = etree.parse(urlopen(ResultURL + query))
    root = tree.getroot()
    body = root[1]
    items = body[0]

    i =0 ;
    ResultForDetail = {}
    ResultList.delete(0, END)
    for item in items:
        ResultForDetail[i] = {'id':item.findtext('atcId'),'num':item.findtext('fdSn')}#id, 순번
        ResultList.insert(i,item.findtext('fdSbjt'))
        i+=1
    return body.findtext('totalCount')


def InitResultList():
    global ResultList
    global querye
    ResultBoxScrollbar = Scrollbar(window)
    ResultBoxScrollbar.place(x = 365, y = 170,width = 20, height = 370)


    ListBoxHorizon = Scrollbar(window, orient = "horizontal")
    ListBoxHorizon.place(x = 20, y  =540, width = 350, height = 20)

    ResultList = Listbox(window, font = normalFont, width = 42, height = 19,
                         yscrollcommand=ResultBoxScrollbar.set,
                         xscrollcommand= ListBoxHorizon.set )
    ResultList.place(x= 20, y = 170)
    ResultList.bind('<<ListboxSelect>>',onselect)

    ResultBoxScrollbar.config(command=ResultList.yview)
    ListBoxHorizon.config(command= ResultList.xview)

def onselect(evt):
    w= evt.widget
    index = int(w.curselection()[0])
    OpenDetailURL( ResultForDetail[index])

def InitDetailWindow():
    global DetailEntry
    DFont = font.Font(window, size=10, family='Consolas')
    DetailEntry = Text(window, font = DFont, width = 48, height = 9)
    DetailEntry.place(x= 400 , y= 400)



def InitButtons():
    TotalSearchButton()     # 검색버튼
    CheckSortButton()       # 정렬 버튼
    SearchAreaButton()      # 지역 버튼
    SearchBrandButton()     # 브랜드 버튼
    SearchColorButton()     # 색 버튼
    SearchYMDButton()       # 기간 버튼
    EmailButton()           # 이메일 전송 버튼
    mapButton()             # 맵 출력 버튼
    ImageButton()           # 이미지 출력 버튼
    PageButton()            # 페이지 변경 버튼

def main():
    InitButtons()

    InitResultList()
    #DetailWindow()      #상세정보
    window.mainloop()

main()
