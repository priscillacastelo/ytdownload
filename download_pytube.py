from pytube import YouTube
from moviepy.editor import *
import streamlit as st

st.title(':heart: Youtube to Mp3')
URL = st.text_input('YouTube URL:')

if st.button('Generate Audio File'):
    yt = YouTube(URL)
    with st.spinner("Please wait..."):
        stream = yt.streams.get_by_itag(22)
        video_file = stream.default_filename
        stream.download()
        video = VideoFileClip(video_file)
        title = video_file.strip('.mp4')
        video.audio.write_audiofile(title + '.mp3')
        audio_file = title + '.mp3'
        st.success(audio_file)

        with open(audio_file, "rb") as file:
            btn = st.download_button(
                label="Download",
                data=file,
                file_name=audio_file,
                mime="mp3"
            )


