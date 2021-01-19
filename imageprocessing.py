from PIL import Image,ImageDraw, ImageFont,ImageEnhance                               
img = Image.open("pic.jpg")                                                 #open it
img.show()                                                                  #show the image
img.save("original.jpeg")

#greyscale
Pixels = list(map(lambda x: int((x[0] + x[1] + x[2])/3), list(img.getdata()))) #average the Red,Green,Blue Value
GreyscaleImg1 = Image.new("L", (img.size) )                               #change the image
GreyscaleImg1.putdata(Pixels)                                     #Copies pixel list to this image
GreyscaleImg1.show()
GreyscaleImg1.save("greyscale.jpeg")

#color contrast
img2=ImageEnhance.Contrast(img)
img2.enhance(1.5).show()
img.save("contrast.jpeg")

#resize the image
print("width*height", img.width, "*", img.height)
w=img.width
h=img.height
if w>=800 and h>=500:
    new_wid = 500
    new_heig=300
    print("The new width*height is",new_wid,"*",new_heig)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('arial.ttf', 60)
    draw.text((0, 0), "Thulasi PROJECT",(0,0,0), font=font)
    img1 = img.resize((new_wid,new_heig),Image.ANTIALIAS).show()
img.save("resize.jpg")
#decrease color  image contrast
img2=ImageEnhance.Color(img)
img2.enhance(0.5).show()
img.save("color.jpeg")
    
   
