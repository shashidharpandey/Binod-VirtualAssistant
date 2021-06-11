import datefinder
import winsound
import datetime

def alarm(text):
    dTimeA = datefinder.find_dates(text)
    for match in dTimeA:
        print (match)
    stringA = str(match)
    timeA = stringA[11:]
    hourA = timeA[:-6]
    hourA = int(hourA)
    minA = timeA[3:-3]
    minA = int (minA)

    while True:
        # print("your alarm has been set")
        if hourA == datetime.datetime.now().hour:
            if minA == datetime.datetime.now().minute:
                print("alarm is running")
                winsound.PlaySound('D:\\benod\\alarm.wav',winsound.SND_LOOP)
            elif minA<datetime.datetime.now().minute:
                break
# alarm("set alarm at  5:39 pm")