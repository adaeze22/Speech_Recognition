#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 15:59:50 2023

@author: ada-eze
"""

import streamlit as st 
import speech_recognition as sr
from app import transcribe_speech 


def main():
    st.title('Speech Recognition App')
    
    r = sr.Recognizer()
    
    st.title( "Voice to Text Application")
    st.write(" |")
    
    st.header("Welcome to my Voice Recognition webapp :smile:")
    st.write(" |")
    
    #with sr.AudioFile("audio_file.wav") as file:
       # audio_text = r.record(file)
    with sr.Microphone() as source:
        #print('Speak now...')
        st.info("Speak now...")
        # listen for speech and store in audio_text variable
        audio_text = r.listen(source)
        #print('Transcribing...')
        st.info("Transcribing...")
        #try:
            # Using google to recognize audio
            #MyText = r.recognize_google(audio_text)
            #MyText = MyText.lower()
            #if st.checkbox("Check your text here..."):
             #   st.write(MyText)
                
        try:
             # using Google Speech Recognition
             text = r.recognize_google(audio_text)
             st.write(text)
             #print(text)
    
        except:
            st.write("sorry run again...")
        transcribe_speech()
    
    
    
if __name__ == '__main__':
    main()