import wave
from pygame import mixer
import os

""""
folder = os.path.dirname(os.path.realpath('__file__'))
fileName = os.path.join(folder, '../Testing/Sounds/')
fileName = os.path.abspath(os.path.realpath(fileName))
songPath = fileName + "\\" + ____ + ".wav"
"""
 
chicken = 'C://Users//Jennifer Nguyen//Desktop//Testing//Sounds//chicken.wav'
duck = 'C://Users//Jennifer Nguyen//Desktop//Testing//Sounds//duck.wav'
destination = open('newSong.wav', 'wb')
infiles = [chicken, duck]
outfile = destination

data= []
for infile in infiles:
    w = wave.open(infile, 'rb')
    data.append( [w.getparams(), w.readframes(w.getnframes())] )
    w.close()

output = wave.open((fileName + "\\" + ____ + ".wav"), 'wb')
output.setparams(data[0][0])
output.writeframes(data[0][1])
output.writeframes(data[1][1])

mixer.init()

mixer.music.load(output)
mixer.music.play()
output.close()
