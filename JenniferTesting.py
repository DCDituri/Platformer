import wave
from pygame import mixer
import os


folder = os.path.dirname(os.path.realpath('__file__'))
fileName = os.path.join(folder, '..Platformer/Sounds/')
fileName = os.path.abspath(os.path.realpath(fileName))
namesList = ["chicken", "duck", "cat", "sheep"] #name of the song files
songList = [] #puts the song paths into a list
for names in namesList:
    songPath = fileName + "\\" + names + ".wav"
    songList.append(songPath)
print songList


"""
import sys, pygame
from pygame.locals import *

import pygame.mixer

folder = os.path.dirname(os.path.realpath('__file__'))
fileName = os.path.join(folder, '..Platformer/Sounds/')
fileName = os.path.abspath(os.path.realpath(fileName))

pygame.mixer.init()
sound = pygame.mixer.Sound("C:\\Users\\Jennifer Nguyen\\Documents\\GitHub\\Platformer\\Sounds\\chicken.wav")
sound.play()
"""


"""import shutil
from pygame import mixer
import sys

chicken = 'C://Users//Jennifer Nguyen//Desktop//Testing//chicken.wav'
duck = 'C://Users//Jennifer Nguyen//Desktop//Testing//duck.wav'


mixer.init()

mixer.music.load(duck)
mixer.music.play()

destination = open('newSong.wav', 'wb')
newSong = 'C://Users//Jennifer Nguyen//Desktop//Testing//newSong.wav'
shutil.copyfileobj(open(chicken,'rb'), destination)
shutil.copyfileobj(open(duck,'rb'), destination)


mixer.music.load(newSong)
mixer.music.play()

duck.close()
newSong.close()
"""



"""
import pyaudio
from pydub import AudioSegment
from pydub.playback import play
import sys

empty = AudioSegment.from_mp3('C://Users//Jennifer//Desktop//Testing//Empty.mp3')
song1 = 'C://Users//Jennifer//Desktop//Testing//OnlyOneRingtone.mp3'
song2 = 'C://Users//Jennifer//Desktop//Testing//StillAliveRingtone.mp3'

combined = song1+song2
combined.sounds.export("C://Users//Jennifer//Desktop//Testing//.mp3", format="mp3")

combined= empty
infiles = [song1, song2]
outfiles = (len(infiles)-1)
while (outfiles >=0):
    outfiles -=1
    Sequence = AudioSegment.from_mp3(infiles[outfiles])
    play(Sequence)
    combined = combined + song"""
    
    


