import soundfile as sf
import re
import os
from tinytag import TinyTag
directory_path = ('./album/')

with open('list.txt','w') as doc:
    for files in os.listdir(directory_path):
        #calculate file time
        f = sf.SoundFile('./album/' + files)
        time = float('{}'.format(f.frames / f.samplerate))
        minutes = time / 60
        intminutes = int(minutes)
        strminutes = str(intminutes)
        seconds = int(time) % 60
        strseconds = str(seconds)

        #get album tags
        tag = TinyTag.get('./album/' + files)

        if tag.disc != 'None':
            doc.write(tag.disc + '.')
            
        doc.write(tag.track + '|')

        if tag.albumartist == 'Various Artists':
            doc.write(tag.artist + ' - ')


        doc.write(tag.title + '|')
        doc.write(strminutes + ':' + strseconds.zfill(2) + '\n')
