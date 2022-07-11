import webuntis
import datetime


s = webuntis.Session(
    server='https://cissa.webuntis.com',
    username=input('Username: '),
    password= input('Password: '),
    school='SZ+II+Utbremen',
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.75"
)
s.login()
today = datetime.date.today()
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
klasse = s.klassen().filter(id=970)[0]
choose = input("Do you want to see the table for this day? (y/n): ")
if choose == "y":
    tt = s.timetable(klasse=klasse, start=today, end=today)
    tt = sorted(tt, key=lambda k: k.start)
    for i in range(len(tt)):
        print(tt[i].start, "-", tt[i].end, " Room: ", tt[i].rooms[0].name, " Subject: ", tt[i].subjects[0].name)

choose = input("Do you want to see the table for tomorrow? (y/n): ")
if choose == "y":
    tt = s.timetable(klasse=klasse, start=tomorrow, end=tomorrow)
    tt = sorted(tt, key=lambda k: k.start)
    for i in range(len(tt)):
        print(tt[i].start, "-", tt[i].end, " Room: ", tt[i].rooms[0].name, " Subject: ", tt[i].subjects[0].name)