import cv2
from PIL import Image,ImageFont
import string
from math import ceil


import cv2
from PIL import Image,ImageDraw
import string

def black_pixel_count(c):
    image = Image.new('1', (30,30), color=255)
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), c)
    data = list(image.getdata())
    return data.count(0)

characters = sorted(string.letters+string.digits+string.punctuation+' ',key=black_pixel_count)[::-1]

def get_grayscale_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    h,w = Image.open(image_path).size
    return img,float(w)/h,w
    
def map_ascii_characters(image,ar,w):
    z = 255/len(characters)+1
    cw = len(image[0])
    ch = len(image)
    singleCharacterWidth = 5
    singleCharacterHeight = 6
    arr = "\n".join([ "".join([characters[y/z] for y in x]) for x in image ])
    img = Image.new("1",(cw*singleCharacterWidth/2,ch*singleCharacterHeight/2),color=255)
    for i in range(0,len(image),2):
        for j in range(0,len(image[0]),2):
            ImageDraw.Draw(img).text((j/2*singleCharacterWidth,i/2*singleCharacterHeight),characters[image[i][j]/z])
    #ImageDraw.Draw(img).text((0,0),arr)
    img.save("ascii_art.jpeg","jpeg")

map_ascii_characters(*get_grayscale_image('dog.png'))