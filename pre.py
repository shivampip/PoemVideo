from PIL import Image, ImageFilter
import glob
import os
import ntpath

#user= "predemo"
#std_img= "0.jpg"



#=======Preprocessing====================================

#std_img= user+"/"+std_img


#=======Convert PNG to JPG===============================

def png_to_jpg(folder):
	png_imgs= glob.glob(folder+"/*.png", recursive= False)
	for img in png_imgs:
		fn, fext= os.path.splitext(ntpath.basename(img))
		img= Image.open(img)
		rgb_img = img.convert('RGB')
		rgb_img.save(folder+"/"+fn+".jpg")

"""
png_imgs= glob.glob(user+"/*.png", recursive= False)
for img in png_imgs:
	fn, fext= os.path.splitext(ntpath.basename(img))
	img= Image.open(img)
	rgb_img = img.convert('RGB')
	rgb_img.save(user+"/"+fn+".jpg")
	print(fn+".jpg saved")
"""
#========================================================

def getImgsFromFolder(folder):
	imgfs= glob.glob(folder+"/*.jpg", recursive= False)
	imgs= []
	for img in imgfs:
		imgs.append(Image.open(img))
	return imgs


#imgfs= glob.glob(user+"/*.jpg", recursive= False)
#imgs= []
#for img in imgfs:
#	imgs.append(Image.open(img))

#======Cropping==========================================

def crop(std_file, img):
	std_size= sw, sh= Image.open(std_file).size
	w, h= img.size
	sd= sw/sh
	pd= w/h
	if(sd>pd):
		x= w
		y= w*(1.0/sd)
	else:
		y= h
		x= h*sd
	x1,y1=0,0
	return img.crop((x1,y1,x,y))
	
"""
std_size= sw, sh= Image.open(std_img).size
print("Standard size:",std_size)

prefix= "crop_"
crp_imgs= []

for img in imgs:
	w, h= img.size
	sd= sw/sh
	pd= w/h
	if(sd>pd):
		x= w
		y= w*(1.0/sd)
	else:
		y= h
		x= h*sd
	x1,y1=0,0
	crp_img= img.crop((x1,y1,x,y))
	nm= ntpath.basename(img.filename)
	crp_img.save(user+"/"+prefix+nm)
	print(user+"/"+prefix+nm,'Saved')
"""
 
 #========Black n White==================================

def bw(img):
	return img.convert(mode="L")

"""
prefix= "bw_"
bw_imgs=[]

for img in imgs:
	nm= ntpath.basename(img.filename)
	img.convert(mode="L").save(user+"/"+prefix+nm)
	print(user+"/"+prefix+nm,'Saved')
"""

 #========Blur===========================================

def blur(img, radius=10):
	return img.filter(ImageFilter.GaussianBlur(radius))

"""
prefix= "blur_"
bw_imgs=[]

for img in imgs:
	nm= ntpath.basename(img.filename)
	img.filter(ImageFilter.GaussianBlur(10)).save(user+"/"+prefix+nm)
	print(user+"/"+prefix+nm,'Saved')
"""

#============================================

def Img(file):
	return Image.open(file)

def getName(img):
	return ntpath.basename(img.filename)

def save(folder, img, prefix, nm):
	img.save(folder+"/"+prefix+nm)

def main():
	user= 'predemo'
	imgs= getImgsFromFolder(user)

	std_imgfile= user+"/0.jpg"
	for img in imgs:
		nm= ntpath.basename(img.filename)
		save(user, crop(std_imgfile, img), "crop_", nm)
		save(user, bw(img), "bw_", nm)
		save(user, blur(img), "blur_", nm)
		print(nm, "Done")







if(__name__=="__main__"):
	#main()
	png_to_jpg("444")