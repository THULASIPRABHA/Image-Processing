from PIL import Image,ImageDraw, ImageFont                                 
img = Image.open("dog.jpg")                                                 #open it
img.show()                                                                  #show the image
img.save("original.jpeg")                                                   #name the image
Pixels = list(map(lambda x: int((x[0] + x[1] + x[2])/3), list(img.getdata()))) #average the Red,Green,Blue Value
GreyscaleImg1 = Image.new("L", (img.size[0], img.size[1]), 255)   #instantiate an image
GreyscaleImg1.putdata(Pixels)                                     #Copies pixel list to this image
GreyscaleImg1.show()
GreyscaleImg1.save("greyscale.jpeg")
print("width*height", img.width, "*", img.height)
w=img.width
h=img.height
if w>=800 and h>=500:
    new_wid = 500
    new_heig=300
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('arial.ttf', 60)
    draw.text((0, 0), "Thulasi PROJECT",(0,0,0), font=font)
    img1 = img.resize((new_wid,new_heig),Image.ANTIALIAS).show()

    
    
