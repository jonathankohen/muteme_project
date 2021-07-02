from django.shortcuts import render, redirect
import pyttsx3

# form => send data that indicates increase, decrease, mute
# in views => create function(s)
# might have to do POST reqs instead

engine = pyttsx3.init()


def index(req):
    return render(req, "index.html")


def increase(req):
    volume = engine.getProperty("volume")
    engine.setProperty("volume", 1.0)
    engine.runAndWait()
    print(volume)
    return render(req, "index.html")


def decrease(req):
    volume = engine.getProperty("volume")
    engine.setProperty("volume", 0.3)
    engine.runAndWait()
    print(volume)
    return render(req, "index.html")


def mute(req):
    volume = engine.getProperty("volume")
    engine.setProperty("volume", 0.0)
    engine.runAndWait()
    print(volume)
    return render(req, "index.html")
