from moviepy.editor import *
import pre
import glob
import speaker


#=================================================
#=======Title=====================================

user= '111' 
title= "THE ROAD NOT TAKEN"
writter_name= "ROBERT FROST"

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


title_duration= 6
font_title= "Ubuntu-Bold"
fontsize_title= 140
img_title= "0.jpg"
blur_title= True

#=================================================
#=======Poem======================================

font_poem= "Ubuntu"
fontsize_poem= 75
reading_speed= 8.0

img_poem="1.jpg"
blur_poem= True

#=================================================
#=======Images====================================

imageName=[2,3,2,2,92,2,7,2,2,9,2,0,1,2,2,2]
imageName=[]

#=================================================
#=======Audio=====================================

audio_file= "song.mp3"
audio_offset= 0

#=================================================
#=======Output====================================

out_res_height= 1280
output_file= "TheTiger.mp4"

#=================================================
#=======Credits===================================

written_duration= 6
editor_duration= 4
editor_name= "Shivam Agrawal"

img_end= "2.jpg"
blur_credit= False

#=================================================
#=======Effects===================================

darken_effect= 0.4

#=================================================
#===========Start Processing======================
#=================================================
img_title= user+ "/"+ img_title
img_poem= user+ "/"+ img_poem
img_end= user+ "/"+ img_end
audio_file= user+ "/"+ audio_file
output_file= user+ "/"+ output_file


pre.save(user, pre.crop(img_title, pre.Img(img_poem)), "", pre.getName(pre.Img(img_poem)))
pre.save(user, pre.crop(img_title, pre.Img(img_end)), "", pre.getName(pre.Img(img_end)))


if(blur_title):
	pre.save(user, pre.blur(pre.Img(img_title)), "", pre.getName(pre.Img(img_title)))
if(blur_poem):
	pre.save(user, pre.blur(pre.Img(img_poem)), "", pre.getName(pre.Img(img_poem)))
if(blur_credit):
	pre.save(user, pre.blur(pre.Img(img_end)), "", pre.getName(pre.Img(img_end)))


#=================================================
#=================================================
images=[]
for img in imageName:
	images.append("Files/vinita/"+str(img)+".jpg")


times= []
text_clips= []
total_time= 0

poem= poem.split("\n")
poem.remove("")

spk= speaker.Speaker()
spk.setLang('en')
os.mkdir(user+"/temp")
#for i in range(len(poem)):
#    if(len(poem[i])>2):
#        file= spk.save(poem[i], user+"/temp/"+str(i))
#        print(file)
#
#print("Conversion done")
#quit()

#====================================================

def processLine(line):
	if(len(line)>50):
		index= line.find(" ",40)
		line= line[:index]+ "\n" +line[index+1:]
		if(len(line)>100):
			index= line.find(" ",78)
			line= line[:index]+ "\n" +line[index+1:]
	return line

def getClip(text, duration):
	return TextClip(text, font= font_poem, fontsize= fontsize_poem, color='white').set_position('center').set_duration(duration)

def getTitle(text, duration):
	return TextClip(text, font= font_title, fontsize= fontsize_title, color='white').set_position('center').set_duration(duration)
	


text_clips.insert(0, getTitle(title, title_duration))

i=0
for line in poem:
	if(len(line)<5):
		continue
	t= len(line)/reading_speed
	times.append(t)
	line= processLine(line)
	text_clips.append(getClip(line, t))
	total_time+=t
    
    spk.save(line, user+"/temp/"+str(i))
    i+=1





text_final= concatenate_videoclips(text_clips)
text_final= text_final.set_position('center')

#======================================================
total_time+=title_duration

times.insert(0, title_duration)
images.insert(0, img_title)


def getImgClip(name, duration):
	return ImageClip(name).resize(height=out_res_height).set_duration(duration).set_position('center').fx( vfx.colorx, darken_effect)

img_final= None
if(len(images)>2):
	#print("Image list is given")
	img_clips=[]
	for i in range(len(times)):
		img_clip= ImageClip(images[i]).resize(height=out_res_height).set_duration(times[i]).set_position('center').fx( vfx.colorx, darken_effect)
		img_clips.append(img_clip)
	imgclips.append(getImgClip(img_end, written_duration+ editor_duration))
	img_final= concatenate_videoclips(img_clips)
else:
	#print("Single Img is given")
	title_clip= ImageClip(images[0]).resize(height=out_res_height).set_duration(title_duration).set_position('center').fx(vfx.colorx, darken_effect)
	img_poem= ImageClip(img_poem).resize(height=out_res_height).set_duration(total_time- title_duration).set_position('center').fx(vfx.colorx, darken_effect)
	img_final= concatenate_videoclips([title_clip, img_poem, getImgClip(img_end, written_duration+ editor_duration)])



img_final= img_final.set_position('center')

#=======================================================
def getCredit(text, fs, duration):
	return TextClip(text, font= font_poem, fontsize= fs, color='white').set_position('center').set_duration(duration)


#end_clip_img= getImgClip(img_end, 9)
writtenby_text= getCredit("written by- ", 40, written_duration)
effectsby_text= getCredit("Effects by-", 30, editor_duration)
writer_text= getCredit(writter_name, 80, written_duration)
editor_text= getCredit(editor_name, 50, editor_duration)

by_text= concatenate_videoclips([writtenby_text, effectsby_text])
by_text= by_text.set_position((0.25, 0.38), relative= True)
name_text= concatenate_videoclips([writer_text, editor_text])
name_text= name_text.set_position((0.25, 0.45), relative= True)


#=======================================================
result= CompositeVideoClip([img_final, text_final, name_text.set_start(total_time), by_text.set_start(total_time)]) 
#=======================================================



total_time+=written_duration+ editor_duration


#=======================================================
audioclip = AudioFileClip(audio_file).subclip(audio_offset,total_time+audio_offset)
#=======================================================

result= result.set_audio(audioclip)
result.write_videofile(output_file, fps= 24)

print("-"*25)
print("Successfully Completed")
print("-"*25)