from PIL import Image
import os,random
import numpy as np
path = os.path.join( "N:", "Project", "turtle.jpg" )
destPath = os.path.join( "N:", "Project", "newerturtle.jpg" )

im = Image.open(path)
pix = im.load()
width,height = im.size
num = 0
st = input('Enter your message: ')

msg = bin(int.from_bytes(st.encode(), 'big'))[2:]
print(len(msg))
print(msg)
for x in range(width):
    for y in range(height):
        if num < len(msg):
            tup = pix[x,y]
            if bin(tup[0] & 0b1) == msg[num]:
                pass
            binary = list(bin(tup[0]))
            
            binary[-1] = msg[num]
            binary = ''.join(binary)
            newPix = int(binary,2)
            newPix1 = tup[1]
            newPix2 = tup[2]
            pix[x,y] = (newPix,newPix1,newPix2,0)
            num+=1
        else:
            break
print(im.size)

im.save(destPath)

img = Image.open(destPath)
pix = im.load()
width,height = img.size
newMsg = []
no = 0
for x in range(width):
    for y in range(height):
        no+=1
        if no <= len(msg):
            tup = pix[x,y]
            newMsg.append(str(list(bin(tup[0]))[-1]))
        else:
            break
msgBin = '0b'+''.join(newMsg)
n = int(msgBin, 2)
print(len(msgBin[2:]))
print(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())