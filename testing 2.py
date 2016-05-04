import wave, os, sys, pygame
from pygame import mixer
from pygame.locals import *

folder = os.path.dirname(os.path.realpath('__file__'))
fileName = os.path.join(folder, '..Platformer/Sounds/')
fileName = os.path.abspath(os.path.realpath(fileName))
namesList = ["chicken", "duck", "cat", "sheep"] #name of the song files
songList = [] #puts the song paths into a list
for names in namesList:
    songPath = fileName + "\\" + names + ".wav"
    songList.append(songPath)
print songList

finalSongList = []

pygame.init()
sound = pygame.mixer.Sound(songList[1])

while True:

        for event in pygame.event.get():

            #Changes the moving variables only when the key is being pressed
            if event.type == KEYDOWN:
                pygame.mixer.music.play()
                if event.key == K_LEFT:
                    sound.play()
                if event.key == K_RIGHT:
                    sound.play()
                if event.key == K_DOWN:
                    sound.play()
                if event.key == K_UP:
                    sound.play()


            #Stops moving the image once the key isn't being pressed
            elif event.type == KEYUP:
                pygame.mixer.music.stop()
                

"""
for num in range(0,4):
    sound = pygame.mixer.Sound(songList[num])
    sound.play()
"""

"""

newSong = 'C:\\Users\\Jennifer Nguyen\\Documents\\GitHub\\Platformer\\Sounds\\newSong.wav'
output = wave.open(newSong, 'wb')
output.setparams(data[0][0])
output.writeframes(data[0][1])
output.writeframes(data[1][1])

mixer.init()

mixer.music.load(newSong)
mixer.music.play()
output.close()
"""
