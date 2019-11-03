import urllib.request as urllib2
import speech_recognition as sr
import subprocess
import os
import requests
import pyasn1, certifi, asn1crypto, cryptography, OpenSSL, urllib3
import ssl
import random


try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

def voice_recongnition(url):
    nom='test'+str(random.random())
    nommp4=nom+'.mp4'
    nomwav=nom+'.wav'
    r = requests.get(url)

    mp4file = urllib2.urlopen(url)

    with open(nommp4, "wb") as handle:
        handle.write(mp4file.read())

    cmdline = ['/usr/local/bin/avconv','-i',nommp4,'-vn','-f','wav',nomwav]
    subprocess.call(cmdline)
    r = sr.Recognizer()
    with sr.AudioFile(nomwav) as source:
        audio = r.record(source)
    try:
        command = r.recognize_google(audio)
    except sr.UnknownValueError:
        command="fsfsfs"
    except sr.RequestError as e:
       command="fsfsfs"

    os.remove(nommp4)
    os.remove(nomwav)
    return(command)




