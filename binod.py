import pyttsx3   #pip install pyttsx3 
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import pyjokes  
import webbrowser 
import os
import imdb  #pip install IMDbpy
import requests 
import json
import smtplib 
import pywhatkit #pip install pywhatkit
import winshell #pip install winshell
import ctypes
import PyPDF2   #pip install PyPDF2
import alarmf    #alarmf.py file in folder
import subprocess 
import time
import random
import pygame       #pip install pygame
import wolframalpha     #pip install wolframalpha
from tkinter import *  

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak ("good morning")          
    elif hour>=12 and hour<17:
        speak ("good afternoon")
    else :
        speak ("good evening")
    speak ("nmastey! this is benod")
    speak("What should i call you")
    uname = takeCommand()
    speak("Welcome ")
    speak(uname)
    speak("How can i Help you,")
    return uname

def CurrencyConvertor(url):
    pass

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)    
        print("Say that again please...")
        speak ("say that again please")  
        return "None"
    return query

def getWeather():
    speak("for which city you want to check the weather")
    city = takeCommand()
    api = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=63898b952bbac072d8bb20cd84fc1b2c"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    finalData = "weather conditions at " + city + "are" + condition +"current temperature is" + str(temp) + "celcius"
    speak(finalData)

def tellDay(): 
      
    # This function is for telling the 
    # day of the week 
    day = datetime.datetime.today().weekday() + 1
      
    #this line tells us about the number  
    # that will help us in telling the day 
    Day_dict = {1: 'Monday', 2: 'Tuesday',  
                3: 'Wednesday', 4: 'Thursday',  
                5: 'Friday', 6: 'Saturday', 
                7: 'Sunday'} 
    if day in Day_dict.keys(): 
        day_of_the_week = Day_dict[day] 
        print(day_of_the_week) 
        speak("The day is " + day_of_the_week)

def tellTime(): 
      
    # This method will give the time 
    time = str(datetime.datetime.now()) 
      
    # the time will be displayed like  
    # this "2020-06-05 17:50:14.582630" 
    #nd then after slicing we can get time 
    print(time) 
    hour = time[11:13] 
    min = time[14:16] 
    speak("The time is sir" + hour + "Hours and" + min + "Minutes")

def sendEmail(to, content):
    server = smtplib.SMTP ('smtp.gmail.com', 587)
    server.ehlo ()
    server.starttls ()

    # Enable low security in gmail
    server.login ('iv16182@gmail.com', 'Isha@2002')  #(apni maiil, or uska password, low security settings as well)
    server.sendmail ('iv16182@gmail.com', to, content)  #(Apnii mail)
    server.close ()

def news():
    r = requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=e78d6b80b9cc46f1ba26a0a25e69aab5")
    data = json.loads(r.content)
    speak ("top 5 news of the day on your way")
    for i in range(5):
        news = data['articles'][i]['title']
        print (news)
        speak(news)

if __name__ == "__main__":
    nameu = wishme()

    while True:
        query = takeCommand().lower()
        #wikipedia
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak ("According to wikipedia,")
            print(results)
            speak (results)

        elif 'powerpoint' in query:
            powerPath = "C:\\Program Files\\Microsoft Office\\root\Office16\\POWERPNT.EXE"
            os.startfile(powerPath)

        elif 'open code' in query or 'v s code' in query:
            codePath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'microsoft word' in query or 'word' in query:
            wordPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(wordPath)

        elif 'chrome' in query :
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)
            
        #youtube
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        #google
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music from folder' in query or 'play music from system' in query:
            speak ("Please select the song")
            window = Tk ()
            pygame.mixer.init ()
            n = 0

            def start_stop():
                global n
                n = n + 1
                if n == 1:
                    song_name = songs_listbox.get ()
                    pygame.mixer.music.load (song_name)
                    pygame.mixer.music.play (0)

                elif (n % 2) == 0:
                    pygame.mixer.music.pause ()

                elif (n % 2) != 0:
                    pygame.mixer.music.unpause ()


            l1 = Label (window, text="MUSIC PLAYER", font="times 20")
            l1.grid (row=1, column=1)

            b2 = Button (window, text='o', command=start_stop)
            b2.grid (row=4, column=1)

            songs_list = os.listdir ()
            songs_listbox = StringVar (window)
            songs_listbox.set ("select songs")
            menu = OptionMenu (window, songs_listbox, *songs_list)
            menu.grid (row=4, column=4)
            window.mainloop ()

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'stack over flow' in query or 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
            speak("opening flipkart")   

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")
            speak("opening google mail") 
            
        elif 'open snapdeal' in query:
            webbrowser.open("https://www.snapdeal.com") 
            speak("opening snapdeal")  
             
        elif 'open amazon' in query or 'shop online' in query:
            webbrowser.open("https://www.amazon.com")
            speak("opening amazon")

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("opening facebook")

        elif 'open ebay' in query:
            webbrowser.open("https://www.ebay.com")
            speak("opening ebay")

        elif 'e mail' in query or 'mail' in query:
            try:
                speak ("What should I say?")
                content = takeCommand ()
                speak ("whome should i send, please enter below")
                to = input ()
                sendEmail (to, content)
                speak ("Email has been sent !")
            except Exception as e:
                print (e)
                speak ("I am not able to send this email")
                
        elif 'play' in query:
            song = query.replace('play', '')
            so = "playing" + song
            print ("playing")
            speak(so)
            pywhatkit.playonyt(song)

        elif 'news' in query :
            news()

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("you asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" +location+ "")

        elif 'weather' in query or 'temperature' in query:
            getWeather()

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'covid active cases' in query or 'active cases' in query:
            url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"
            headers = {
                'x-rapidapi-key': "2b2e2cef91msh1e84d53f985a28ep1b132bjsn14494b5b1d6b",
                'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers).json()

            def search_by_city(city_name):
                for each in response ['state_wise']:
                    if int(response['state_wise'][each]['active'])!=0:
                        for city in response ['state_wise'][each]['district']: 
                            if city.lower() == city_name.lower():
                                return response ['state_wise'][each]['district'][city]['active']
            
            speak("for which city you want to know the number of active cases:")
            city_name = takeCommand().lower()
            cases = search_by_city(city_name)
            data = "Number of active cases in "+city_name+"are "+ str(cases)
            print (data)
            speak(data)

        elif "day" in query: 
            tellDay() 

        elif 'the time' in query:
            tellTime()

        elif "calculate" in query: 
             
            app_id = "524VE5-XHL3GEY99T"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate') 
            query = query.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text
            print("The answer is " + answer) 
            speak("The answer is " + answer) 

        elif "write a note" in query or "make note" in query or "create note" in query:
            speak("What should i write")
            note = takeCommand()
            file = open('benod.txt', 'w')
            speak("Should i include time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        elif "show note" in query or "open note" in query:
            speak("Showing Notes")
            file = open("benod.txt", "r") 
            print(file.read())
            speak(file.read(6))

        elif 'lock window' in query:
            speak ("locking the device")
            ctypes.windll.user32.LockWorkStation ()

        elif 'shutdown' in query:
            speak ("Hold On a Sec ! Your system is on its way to shut down")
            os.system("shutdown /s /t 1") 

        elif "don't listen" in query or "stop listening" in query:
            speak ("for how much time you want to stop jarvis from listening commands, in seconds")
            a = int(takeCommand())
            time.sleep (a)
            print (a)

        elif 'empty recycle bin' in query:
            winshell.recycle_bin ().empty (confirm=False, show_progress=False, sound=True)
            speak ("Recycle Bin Recycled")

        elif "alarm" in query or "reminder" in query:
            alarmf.alarm(query)

        elif 'snake game' in query or 'game' in query:
            pygame.init ()

            white = (255, 255, 255)
            yellow = (255, 255, 102)
            black = (0, 0, 0)
            red = (213, 50, 80)
            green = (0, 255, 0)
            blue = (50, 153, 213)

            dis_width = 600
            dis_height = 400

            dis = pygame.display.set_mode ((dis_width, dis_height))
            pygame.display.set_caption ('Snake Game by GROP -3')

            clock = pygame.time.Clock ()

            snake_block = 10
            snake_speed = 15

            font_style = pygame.font.SysFont ("bahnschrift", 25)
            score_font = pygame.font.SysFont ("comicsansms", 35)


            def Your_score(score):
                value = score_font.render ("Your Score: " + str (score), True, yellow)
                dis.blit (value, [0, 0])


            def our_snake(snake_block, snake_list):
                for x in snake_list:
                    pygame.draw.rect (dis, black, [x[0], x[1], snake_block, snake_block])


            def message(msg, color):
                mesg = font_style.render (msg, True, color)
                dis.blit (mesg, [dis_width / 6, dis_height / 3])


            def gameLoop():
                game_over = False
                game_close = False

                x1 = dis_width / 2
                y1 = dis_height / 2

                x1_change = 0
                y1_change = 0

                snake_List = []
                Length_of_snake = 1

                foodx = round (random.randrange (0, dis_width - snake_block) / 10.0) * 10.0
                foody = round (random.randrange (0, dis_height - snake_block) / 10.0) * 10.0

                while not game_over:

                    while game_close == True:
                        dis.fill (blue)
                        message ("You Lost! Press C-Play Again or Q-Quit", red)
                        Your_score (Length_of_snake - 1)
                        pygame.display.update ()

                        for event in pygame.event.get ():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_q:
                                    game_over = True
                                    game_close = False
                                if event.key == pygame.K_c:
                                    gameLoop ()

                    for event in pygame.event.get ():
                        if event.type == pygame.QUIT:
                            game_over = True
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT:
                                x1_change = -snake_block
                                y1_change = 0
                            elif event.key == pygame.K_RIGHT:
                                x1_change = snake_block
                                y1_change = 0
                            elif event.key == pygame.K_UP:
                                y1_change = -snake_block
                                x1_change = 0
                            elif event.key == pygame.K_DOWN:
                                y1_change = snake_block
                                x1_change = 0

                    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                        game_close = True
                    x1 += x1_change
                    y1 += y1_change
                    dis.fill (blue)
                    pygame.draw.rect (dis, green, [foodx, foody, snake_block, snake_block])
                    snake_Head = []
                    snake_Head.append (x1)
                    snake_Head.append (y1)
                    snake_List.append (snake_Head)
                    if len (snake_List) > Length_of_snake:
                        del snake_List[0]

                    for x in snake_List[:-1]:
                        if x == snake_Head:
                            game_close = True

                    our_snake (snake_block, snake_List)
                    Your_score (Length_of_snake - 1)

                    pygame.display.update ()

                    if x1 == foodx and y1 == foody:
                        foodx = round (random.randrange (0, dis_width - snake_block) / 10.0) * 10.0
                        foody = round (random.randrange (0, dis_height - snake_block) / 10.0) * 10.0
                        Length_of_snake += 1

                    clock.tick (snake_speed)

                pygame.quit ()
                quit ()

            gameLoop ()

        elif 'movie info' in query or 'about movie' in query:
            try:
                hr = imdb.IMDb ()
                speak ("what is name of movie")
                movie_name = takeCommand ()
                movies = hr.search_movie (str (movie_name))
                index = movies[0].getID ()
                movie = hr.get_movie (index)
                title = movie['title']
                year = movie['year']
                rating = movie['rating']
                cast = movie['cast']
                director = movie['directors']
                direcStr = ','.join (map (str, director))
                list_of_cast = ','.join (map (str, cast))
                speak ("title of movie is ")
                speak (title)
                speak ("year of release is  ")
                speak (year)
                speak("drector of movie is ")
                speak(direcStr)
                speak("rating of movie is ")
                speak(rating)
                speak ("cast are ")
                speak (list_of_cast)
            except Exception as e:
                print (e)
                speak ("Sorry my friend. I am not able to find")

        elif 'read pdf' in query:  #pdf reader
            speak ("what is name of pdf, enter below")
            to = input ()
            book = open (to, 'rb')
            pdfreader = PyPDF2.PdfFileReader (book)
            pages = pdfreader.numPages
            # print(pages)
            speaker = pyttsx3.init ()
            page = pdfreader.getPage (0)
            text = page.extractText ()
            speaker.say (text)
            speaker.runAndWait ()

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif 'remember my name' in query:
            speak("how could I forget your name, ")
            speak (nameu)

        elif "what's your name" in query or "your name" in query:
            speak("My friends call me")
            speak("benod")
            print("My friends call me, benod")

        elif "who made you" in query or "who created you" in query: 
            speak("I have been created by group 3 of C S E 2 A.")

        elif 'how are you' in query:
            speak("I am good, how are you?")

        elif 'you like to eat' in query or 'you love to eat' in query:
            speak("I can always go for some food for thought. Like facts, jokes, or interesting searches, we could look something up now")

        elif "will you be my g f" in query or "will you be my b f" in query or "will you be my girlfriend" in query or "will you be my boyfriend" in query:   
            print ("I'm not sure about, may be you should give me some time")
            speak("I'm not sure about, may be you should give me some time")
 
        elif "how are you" in query:
            print("I'm fine, glad you me that")
            speak("I'm fine, glad you me that")

        elif "favourite colour" in query:
            print("I love rainbows, it makes me happy to see so many colours together")
            speak("I love rainbows, it makes me happy to see so many colours together")

        elif "favourite drink" in query:
            print ("just a cup of chai emoji")
            speak("just a cup of chai emoji")
 
        elif "favourite animal" in query or "pet" in query:
            print ("I always wanted a puppy and I love them")
            speak("I always wanted a puppy and I love them")
 
        elif "i love you" in query:
            print("It's hard to understand")
            speak("It's hard to understand")
        
        elif "benod" in query:  
            wishme()
            speak("benod in your service")
        
        elif 'exit' in query or "bye" in query or 'close' in query or "quit" in query or "thank" in query or "thanks" in query:
            speak("Thanks for giving me your time")
            exit()

        elif 'covid' in query or 'corona virus' in query:
            speak("redirecting to messenger chats")
            webbrowser.open ("https://m.me/105859688133956")

        elif 'none' in query:
            continue

        else:
        
            try:
                app_id = "524VE5-XHL3GEY99T"
                client = wolframalpha.Client (app_id)
                res = client.query (query)
                answer = next (res.results).text
                print (answer)
                speak(answer)
                continue
                    
            except:
                 # print ("wolframalpha does not have answer")
                 temp = query.replace(' ','+')
                 g_url="https://www.google.com/search?q="    
                 res_g = 'okay, result window your way' #*
                 print(res_g)
                 speak(res_g)
                 webbrowser.open(g_url+temp)
                 continue
            