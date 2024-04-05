from machine import Pin, SoftSPI
import st7789
import time
import random
import os
import vga2_bold_16x32 as font1
import vga1_8x8 as font2
import json

with open("data.json", "r") as f:
    try:
        data = json.load(f)
        f.close()
    except:
        data = {}
        
if("Reaction_Count" not in data):
    data["Reaction_Count"] = 0

with open("data.json", "w") as f:
    json.dump(data, f)
    f.close()
    
sck  = Pin(29)
mosi = Pin(28)
reset = Pin(27, Pin.OUT)
dc = Pin(26, Pin.OUT)
backlight = Pin(15, Pin.OUT)

miso = Pin(13)

spi = SoftSPI(mosi = mosi, sck = sck, baudrate=40000000, polarity=1, miso=miso)
tft = st7789.ST7789(spi, 240, 240, reset = reset, dc = dc, backlight = backlight)

tft.init()
tft.on()

yOffset = 120 - (4*32)//2
tft.text(font1, "MY", 120 - 9*8, yOffset)
time.sleep(0.1)
tft.text(font1, "MY HONEST", 120 - 9*8, yOffset)
time.sleep(0.2)
tft.text(font1, "REACTION", 120 - 8*8, 32 + yOffset)
time.sleep(0.4)
tft.text(font1, "TO", 120 - 7*8, 64 + yOffset)
time.sleep(0.1)
tft.text(font1, "TO THAT", 120 - 7*8, 64 + yOffset)
time.sleep(0.2)
tft.text(font1, "INFORMATION", 120 - 11*8, 96 + yOffset)
time.sleep(1)

with open("data.json", "r") as f:
    data = json.load(f)
    f.close()
        
data["Reaction_Count"] += 1
Reaction_Count = data["Reaction_Count"]

with open("data.json", "w") as f:
    json.dump(data, f)
    f.close()
    
selectedFile = "images/" + random.choice(os.listdir("images/"))
tft.png(selectedFile, 0, 0)
tft.text(font2, str(Reaction_Count), 120 - len(str(Reaction_Count))*4, 232)


