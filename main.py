import requests
from functions.online_ops import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message
from functions.os_ops import open_calculator, open_camera, open_cmd, open_notepad, open_edge, open_clean_manager, open_control_panel, open_game_panel
from pprint import pprint
from AURA import wish_user, user_input, speak
import datetime


if __name__ == '__main__':
    wish_user()
    while True:
        query = user_input().lower()

        if 'open notepad' in query:
            open_notepad()

        elif 'open edge' in query:
            open_edge()

        elif 'open command prompt' in query or 'open cmd' in query:
            open_cmd()

        elif 'open camera' in query:
            open_camera()

        elif 'open calculator' in query:
            open_calculator()

        elif 'open clean Manager' in query:
            open_clean_manager()

        elif 'open control panel' in query:
            open_control_panel()

        elif 'open game panel' in query:
            open_game_panel()

        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen Buddy.')
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, Buddy?')
            search_query = user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen Buddy.")
            print(results)

        elif 'youtube' in query:
            speak('What do you want to play on Youtube, Buddy?')
            video = user_input().lower()
            play_on_youtube(video)

        elif 'search on google' in query:
            speak('What do you want to search on Google, Buddy?')
            query = user_input().lower()
            search_on_google(query)

        elif "send whatsapp message" in query:
            speak('On what number should I send the message Buddy? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message Buddy?")
            message = user_input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message Buddy.")

        elif "send an email" in query:
            speak("On what email address do I send Buddy? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject Buddy?")
            subject = user_input().capitalize()
            speak("What is the message Buddy?")
            message = user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email Buddy.")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs Buddy.")

        elif 'joke' in query:
            speak(f"Hope you like this one Buddy")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen Buddy.")
            pprint(joke)

        elif "advice" in query:
            speak(f"Here's an advice for you, Buddy")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen Buddy.")
            pprint(advice)


        elif 'news' in query:
            speak(f"I'm reading out the latest news headlines, Buddy")
            speak(get_latest_news())
            speak("For your convenience, I am printing it on the screen Buddy.")
            print(*get_latest_news(), sep='\n')

        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen Buddy.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

        if 'time' in query:
            strTime = datetime.now().strftime("%H:%M:%S")
            speak(f"Dude, the time is {strTime}")
            print(strTime)