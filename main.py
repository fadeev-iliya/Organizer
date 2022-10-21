import time

import speech_recognition as sr
import keyboard
from Settings import *

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

while True:
    if keyboard.is_pressed("1"):
        with sr.Microphone() as source:
            print("Слушаю")
            # r.adjust_for_ambient_noise(source)
            audio_data = r.listen(source)
            print("Закончил запись")

            text = " | | " + r.recognize_google(audio_data, language="ru-RU") + " | | "
            print(text)
            find_event(text)

    elif keyboard.is_pressed("2"):
        text = " | | Привет Как давай сходим в магазин в 21:00 и потом с собакой погуляем в 22 | | "
        find_event(text)
        time.sleep(0.1)
