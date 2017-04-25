#GIT HUB LINK: https://github.com/vfuchscsumb/205proj1section2.git
#
from PIL import Image
def medianOdd(imagelist):
    listlenght=len(imagelist)
    sortedValues=sorted(imagelist)
    middleIndex=((listlenght+1)/2)-1
    return sortedValues [middleIndex]
    
picture list=[]    
folder=("image/")

#add all images to an array.img
img=Image.open ("image/1.png")
picturesList.append(image)
img=Image.open("image/2.png")
picturesList.append (image)
img=Image.open ("image/3.png")
picturesList.append (image)
img=Image.open ("image/4.png")
picturesList.append (image)
img=Image.open ("image/5.png")
picturesList.append (image)
img=Image.open ("image/6.png")
picturesList.append(image)
img=Image.open("image/7.png")
picturesList.append (image)
img=Image.open ("image/8.png")
picturesList.append (image)
img=Image.open ("image/9.png")
picturesList.append (image)

#size of the images
picW, picH=picturesList[0].size

#create list for pixel values
redlist=[]
greenlist=[]
bluelist=[]

#create blank image
newImg=image.new ("RGB", size)

#loop
for i in range (0, picW)
    for j in range (0, picH)
        for k in range (0,9)
        
            temp =picturesList [k].getpixel ((i,j))
            reslist.append(temp[0])
            greenlist.append(temp[1])
            bluelist.append(temp[2])
        newr=medianOdd(redList)
        newg=medianOdd(greenList)
        newb=medianOdd(blueList)
        
        newImg.putpixel ((i,j),(newr,newg,newb))
        
