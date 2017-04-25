from PIL import Image  

im1 = Image.open("Project1Images/1.png")  
im2 = Image.open("Project1Images/2.png")
im3 = Image.open("Project1Images/3.png")
im4 = Image.open("Project1Images/4.png")
im5 = Image.open("Project1Images/5.png")
im6 = Image.open("Project1Images/6.png")
im7 = Image.open("Project1Images/7.png")
im8 = Image.open("Project1Images/8.png")
im9 = Image.open("Project1Images/9.png")

images = [im1, im2, im3, im4, im5, im6, im8, im9];  

def medianOdd(myList):   
    listLength = len(myList)
    sortedValues = sorted(myList)
    middleIndex = ((listLength + 1)/2) - 1
    return sortedValues[middleIndex]

num =  len(images)

w,h = im2.size      

final = Image.new('RGBA',(w,h))  

for y in range(h):
    
    for x in range(w): 
        
        medianR = []
        medianG = []
        medianB = []
        
        for i in range(0,num):
            
            current = images[i]
            r,g,b = current.getpixel((x,y))
            
            medianR.append(r)
            medianG.append(g)
            medianB.append(b)
            
        r = medianOdd(medianR)
        g = medianOdd(medianG)
        b = medianOdd(medianB)
        
        final.putpixel((x,y), (r,g,b))  
        
        del medianR[:]
        del medianG[:]
        del medianB[:]

final.save('FinalImg.png')  

print "done"   