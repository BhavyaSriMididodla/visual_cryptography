from PIL import ImageDraw
from tkinter import *
import os
import sys
from random import SystemRandom
import PIL.Image
random = SystemRandom()

infile = str(sys.argv[0])
img = PIL.Image.open(r"C:\crypto\red.jpg")
pixels = list(img.getdata())
#pixels = np.array(im.getdata()).reshape(im.size)
print(pixels)
f, e = os.path.splitext(infile)
out_filename_A = "Z_1.png"
out_filename_B = "Z_2.png"

img = img.convert('1')  # convert image to 1 bit

# Prepare two empty slider images for drawing
width = img.size[0]*2
height = img.size[1]*2
out_image_A = PIL.Image.new('1', (width, height))
out_image_B = PIL.Image.new('1', (width, height))
draw_A = ImageDraw.Draw(out_image_A)
draw_B = ImageDraw.Draw(out_image_B)

# There are 6(4 choose 2) possible patterns
patterns = ((1,0,1,0),(0,1,0,1),(1,0,0,1),(0,1,1,0),(0,0,1,1),(1,1,0,0))
# Cycle through pixels
for x in range(0, int(width/2)):
    for y in range(0, int(height/2)):
        pixel = img.getpixel((x, y))
        pat = random.choice(patterns)
        # A will always get the pattern
        draw_A.point((x*2, y*2), pat[0])
        draw_A.point((x*2+1, y*2), pat[1])
        draw_A.point((x*2, y*2+1), pat[2])
        draw_A.point((x*2+1, y*2+1), pat[3])
        if pixel == 0:
            draw_B.point((x*2, y*2), 1-pat[0])
            draw_B.point((x*2+1, y*2), 1-pat[1])
            draw_B.point((x*2, y*2+1), 1-pat[2])
            draw_B.point((x*2+1, y*2+1), 1-pat[3])
        else:
            draw_B.point((x*2, y*2), pat[0])
            draw_B.point((x*2+1, y*2), pat[1])
            draw_B.point((x*2, y*2+1), pat[2])
            draw_B.point((x*2+1, y*2+1), pat[3])

out_image_A.save(out_filename_A, 'PNG')
out_image_B.save(out_filename_B, 'PNG')
print("Done.")

#patterns = ((1,1,1,0,0,0),(1,0,1,1,0,0),(1,1,0,1,0,0),(1,0,0,1,0,1),(1,0,1,0,1,0), (1,1,0,0,0,1), (1,0,0,0,1,1), 
#            (1,0,0,1,1,0),(0,1,0,0,1,1),(0,1,0,1,1,0),(0,0,0,1,1,1),(0,1,0,0,1,1),(0,1,1,0,0,1),(0,1,1,0,1,0),
#            (0,1,0,1,0,1),(0,0,1,1,1,0),(0,1,1,1,0,0),(0,0,1,0,1,1),(1,0,1,1,0,0),(1,0,1,0,0,1))