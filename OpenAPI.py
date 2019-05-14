from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote

from tkinter import*

decode_key = unquote('xZ%2ByjfoWhIOr7s%2BJ0QG0HbPyNRNi46%2F4l8g7G5qTQp6IgeYNACJFFvSQe%2FEgAKR09JsMDhLWpLdyHpYibXU0bQ%3D%3D')

url = 'http://apis.data.go.kr/1320000/SearchMoblphonInfoInqireService/getMoblphonAcctoKindAreaPeriodInfo'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : decode_key, quote_plus('pageNo') : '1', quote_plus('numOfRows') : '2', quote_plus('title') : '1987', quote_plus('rtNo') : '2017-MF02149', quote_plus('aplcName') : '주식회사 우정필름' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'

#check error
#response_body = urlopen(request).read()
#print(response_body)

window = Tk()
window.geometry("800x600")  #window size

def SearchAreaBoc():
    global AreaEntry

    AreaText = Label(window, text="지역 : ")
    AreaText.place(x=400, y=60)

    AreaEntry = Entry(window, width=13)
    AreaEntry.place(x=430, y=60)

def InitSearchYMD():
    global SearchStartYearEntry, SearchStartMonthEntry, SearchStartDayEntry
    global SearchEndYearEntry, SearchEndMonthEntry, SearchEndDayEntry

    SearchStartEntryPos = (10, 10)

    SearchStartText = Label(window, text="예상 분실 시작날짜")
    SearchStartText.place(x=SearchStartEntryPos[0] + 10, y=SearchStartEntryPos[1])

    SearchStartYearEntry = Spinbox(window, from_=2000, to=2019, width=4)
    SearchStartYearEntry.pack()
    SearchStartYearEntry.place(x=SearchStartEntryPos[0], y=SearchStartEntryPos[1] + 20)

    SearchStartMonthEntry = Spinbox(window, from_=1, to=12, width=2)
    SearchStartMonthEntry.pack()
    SearchStartMonthEntry.place(x=SearchStartEntryPos[0] + 60, y=SearchStartEntryPos[1] + 20)

    SearchStartDayEntry = Spinbox(window, from_=1, to=31, width=2)
    SearchStartDayEntry.pack()
    SearchStartDayEntry.place(x=SearchStartEntryPos[0] + 100, y=SearchStartEntryPos[1] + 20)

    SearchEndEntryPos = (10, 60)

    SearchEndText = Label(window, text="예상 분실 끝날짜")
    SearchEndText.place(x=SearchEndEntryPos[0] + 10, y=SearchEndEntryPos[1])

    SearchEndYearEntry = Spinbox(window, from_=2000, to=2019, width=4)
    SearchEndYearEntry.pack()
    SearchEndYearEntry.place(x=SearchEndEntryPos[0], y=SearchEndEntryPos[1] + 20)

    SearchEndMonthEntry = Spinbox(window, from_=1, to=12, width=2)
    SearchEndMonthEntry.pack()
    SearchEndMonthEntry.place(x=SearchEndEntryPos[0] + 60, y=SearchEndEntryPos[1] + 20)

    SearchEndDayEntry = Spinbox(window, from_=1, to=31, width=2)
    SearchEndDayEntry.pack()
    SearchEndDayEntry.place(x=SearchEndEntryPos[0] + 100, y=SearchEndEntryPos[1] + 20)

def main():
    SearchAreaBoc()
    InitSearchYMD()
    window.mainloop()

main()
