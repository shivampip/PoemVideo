import os
import sys
from gtts import gTTS

class Speaker:
    
    def __init__(self):
        self.lang= 'en'
        
    def setLang(self, lang):
        self.lang= lang
        
    def save(self, text, outname):
        print("Please wait")
        self.tts= gTTS(text= text, lang= self.lang)
        self.tts.save(outname+'.mp3')
        print("Done")
        self.outname= outname+'.mp3'
        return outname+'.mp3'

    def play(self):
        filename= self.outname.replace('/','\\')
        print("Playing ",filename)
        os.system(filename)
    

    
if __name__=='__main__':
    spk= Speaker()
    spk.save("Hello Shivam", "hello")
    spk.play()











#==============================================================
poem= """
Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveler, long I stood
And looked down one as far as I could
To where it bent in the undergrowth;

Then took the other, as just as fair,
And having perhaps the better claim,
Because it was grassy and wanted wear;
Though as for that the passing there
Had worn them really about the same,

And both that morning equally lay
In leaves no step had trodden black.
Oh, I kept the first for another day!
Yet knowing how way leads on to way,
I doubted if I should ever come back.

I shall be telling this with a sigh
Somewhere ages and ages hence:
Two roads diverged in a wood, and I—
I took the one less traveled by,
And that has made all the difference.
"""

if __name__=='__main__':
    play(convert(poem, "111/TheRoad"))