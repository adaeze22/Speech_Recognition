#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 12:20:03 2023

@author: ada-eze
"""

import speech_recognition as sr

def transcribe_speech():
    # Initialize recognizer class
    r = sr.Recognizer()
    # Reading Microphone as source
    with sr.Microphone() as source:
        print('Speak now...')
        #st.info("Speak now...")
        # listen for speech and store in audio_text variable
        audio_text = r.listen(source)
        print('Transcribing...')
        #st.info("Transcribing...")

        try:
            # using Google Speech Recognition
            text = r.recognize_google(audio_text)
            print(text)
        except:
            return "Sorry, I did not get that."

transcribe_speech()