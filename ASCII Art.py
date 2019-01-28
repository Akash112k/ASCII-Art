
# coding: utf-8

# In[1]:


import cv2
from PIL import Image
import string
from math import ceil


# In[2]:


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
    arr = "\n".join([ "".join([characters[y/z] for y in x]) for x in image ])
    img = Image.new("1",(w*5,int(w*10*ar)),color=255)
    ImageDraw.Draw(img).text((0,0),arr)
    img.save("ascii_art.jpeg","jpeg")

#map_ascii_characters(*get_grayscale_image('/home/akash/Downloads/img.jpg'))


# In[ ]:


map_ascii_characters(*get_grayscale_image('/home/akash/Akash.png'))

