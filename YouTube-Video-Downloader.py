from pytube import YouTube
import os


def line(): print("%"*33)


URL = "https://youtu.be/jNQXAC9IVRw"

video = YouTube(URL)

line()

print(video.title)

line()

print(video.thumbnail_url)

line()

video = video.streams.get_highest_resolution()

video.download()

print("Downloaded AT ->>>", os.getcwd())

line()
