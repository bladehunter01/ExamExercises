from datetime import datetime
import urllib.request
import json
from time import sleep


def mydecode():
    global html
    html = urllib.request.urlopen(html)
    html = html.read()
    html = html.decode()
    html = json.loads(html)


year = str(datetime.now().year)
month = datetime.now().month
day = datetime.now().day

# Δημιουργία του str για το λινκ
if len(str(month)) == 1:
    month = "0" + str(month)
else:
    month = str(month)

for index in range(1, day+1):

    # Αρχικοποίηση της κάθε μέρας
    if len(str(index)) == 1:
        DayCount = "0" + str(index)
    else:
        DayCount = str(index)

    # Έυρεση πρώτου draw της ημέρας
    html = "https://api.opap.gr/draws/v3.0/1100/draw-date" \
           "/"+year+"-"+month+"-"+DayCount+"/"+year+"-"+month+"-"+DayCount+"/draw-id"

    mydecode()
    FirstDraw = str(html[0])

    # Έυρεση κληρώσεων
    html = "https://api.opap.gr/draws/v3.0/1100/"+FirstDraw
    mydecode()
    print(DayCount+"/"+month+"/"+year+"\n")
    print("Winning Numbers were:\n", html["winningNumbers"]["list"], "\n")
    sleep(3)
