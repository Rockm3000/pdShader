import PIL
from PIL import Image
import os

#Functions for creating the spritesheets
def get_concat_h_blank(im1, im2, color=(32, 120, 56, 255)):
    dst = Image.new('RGBA', (im1.width + im2.width + 5, max(im1.height, im2.height)), color)
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width+5, 0))
    return dst

def get_concat_v_blank(im1, im2, color=(32, 120, 56, 255)):
    dst = Image.new('RGBA', (max(im1.width, im2.width), im1.height + im2.height + 10), color)
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height+10))
    return dst

def get_concat_h_multi_blank(im_list):
    _im = im_list.pop(0)
    for im in im_list:
        _im = get_concat_h_blank(_im, im)
    return _im

def get_concat_v_multi_blank(im_list):
    _im = im_list.pop(0)
    for im in im_list:
        _im = get_concat_v_blank(_im, im)
    return _im

def swapGreenAlpha(image):
    sPixels = image.load()
    width = image.size[0] 
    height = image.size[1]
    for i in range(0,width):#Loop through all pixels in a row
        for j in range(0,height): #Loop through all pixels in a column
            data = sPixels[i,j]
            if data==(0,0,0,0):
                sPixels[i,j] = (0,255,0,255)
            elif data==(0,255,0,255):
                sPixels[i,j] = (0,0,0,0)
    return image

#Selecting the background colour of the sprites
spriteBackground = input("Should the sprites have Green (1) or Clear (2) backgrounds? ")
while spriteBackground != "1" and spriteBackground != "2" and spriteBackground != (0,255,0,255) and spriteBackground != (0,0,0,0):
    spriteBackground = input("Will the sprites have Green (1) or Clear (2) backgrounds? ")
if spriteBackground == "1":
    spriteBackground = (0,255,0,255)
elif spriteBackground == "2":
    spriteBackground = (0,0,0,0)

#Selecting the save location of the spritesheets
sheetSaveLocation = input("Should the spritesheets be saved in their respective character folders (1) or in a SpriteSheets folder (2)? ")
while sheetSaveLocation != "1" and sheetSaveLocation != "2":
    sheetSaveLocation = input("Should the spritesheets be saved in the respective character folders (1) or in a SpriteSheets folder (2)? ")
if sheetSaveLocation == "2":
    os.mkdir("SpriteSheets")

#Selecting the save location of The Spriters Resource icons
iconSaveLocation = input("Should the icons be saved in their respective character folders (1) or in an Icons folder (2)? ")
while iconSaveLocation != "1" and iconSaveLocation != "2":
    iconSaveLocation = input("Should the icons be saved in the respective character folders (1) or in an Icons folder (2)? ")
if iconSaveLocation == "2":
    os.mkdir("Icons")

#Applying the palettes to their respective sprites
for f in os.listdir():
    if f == "sScrapKnightPalette__large_0.png":
        continue
    if "Palette" in f and f.endswith(".png"):
        os.mkdir(f[1:f.find("Palette")])
        print(f"{f[1:f.find('Palette')]} folder created!")
        palette = Image.open(f)
        palettePixels = palette.load()

        for paletteCounter in range(8):
            os.mkdir(f"{f[1:f.find('Palette')]}/Palette {paletteCounter+1}") #Create a folder for each palette of a character
            print(f"Folder {paletteCounter+1} created!")
            #(f == "sPortraitShovelKnightPalette_0.png" and not file.startswith("sShovelKnightPortraitB"))
            #Loop through every sprite in the current directory, checking that it's not a palette, and that (the filename starts the same as the current folder's name, or the special case for mona where the file isn't "MonaKnight", or the file is a hub sprite) and "Floot" is not in the file.
            for file in os.listdir():
                if "Palette" not in file and (file.startswith(f"{f[0:f.find('Palette')]}") or file.startswith(f"sHub{f[1:f.find('Palette')]}") or (f == "sPortraitMonaKnightPalette_0.png" and file.startswith("sPortraitMona"))) and "Floot" not in file and not file.startswith("sShovelKnightPortraitB") and not file.startswith("sPropellerKnightB_portrait") and not file.startswith("sTinkerKnightB_portrait"):
                    sprite = Image.open(file)
                    sPixels = sprite.load()
                    width = sprite.size[0] 
                    height = sprite.size[1]
                    for iteration in range(18):
                        for i in range(0,width):#Loop through all pixels in a row
                            for j in range(0,height): #Loop through all pixels in a column
                                data = sPixels[i,j]
                                if (data[0]==(iteration*3) and data[1]==(iteration*3) and data[2]==(iteration*3) and data[3]==255):
                                    sPixels[i,j] = palettePixels[paletteCounter,iteration]
                                if data[3]==0:
                                    sPixels[i,j] = spriteBackground
                    sprite.save(f"{f[1:f.find('Palette')]}/Palette {paletteCounter+1}/{sprite.filename}") #Save the coloured sprite in the correct folder
                    print(f"{sprite.filename} created!")
                    
                elif (f == "sPortraitShovelKnightPalette_0.png" and file.startswith("sShovelKnightPortraitB")):
                    sprite = Image.open(file)
                    sPixels = sprite.load()
                    width = sprite.size[0] 
                    height = sprite.size[1]
                    for iteration in range(18):
                        for i in range(0,width):#Loop through all pixels in a row
                            for j in range(0,height): #Loop through all pixels in a column
                                data = sPixels[i,j]
                                if (data[0]==(iteration*3) and data[1]==(iteration*3) and data[2]==(iteration*3) and data[3]==255):
                                    sPixels[i,j] = palettePixels[paletteCounter,iteration]
                                if data[3]==0:
                                    sPixels[i,j] = spriteBackground
                    sprite.save(f"PortraitShovelKnight/Palette {paletteCounter+1}/{sprite.filename}") #Save the coloured sprite in the correct folder
                    print(f"{sprite.filename} created!")

                elif (f == "sPortraitPropellerKnightPalette_0.png" and file.startswith("sPropellerKnightB_portrait")):
                    sprite = Image.open(file)
                    sPixels = sprite.load()
                    width = sprite.size[0] 
                    height = sprite.size[1]
                    for iteration in range(18):
                        for i in range(0,width):#Loop through all pixels in a row
                            for j in range(0,height): #Loop through all pixels in a column
                                data = sPixels[i,j]
                                if (data[0]==(iteration*3) and data[1]==(iteration*3) and data[2]==(iteration*3) and data[3]==255):
                                    sPixels[i,j] = palettePixels[paletteCounter,iteration]
                                if data[3]==0:
                                    sPixels[i,j] = spriteBackground
                    sprite.save(f"PortraitPropellerKnight/Palette {paletteCounter+1}/{sprite.filename}") #Save the coloured sprite in the correct folder
                    print(f"{sprite.filename} created!")

                elif (f == "sPortraitTinkerKnightPalette_0.png" and file.startswith("sTinkerKnightB_portrait")):
                    sprite = Image.open(file)
                    sPixels = sprite.load()
                    width = sprite.size[0] 
                    height = sprite.size[1]
                    for iteration in range(18):
                        for i in range(0,width):#Loop through all pixels in a row
                            for j in range(0,height): #Loop through all pixels in a column
                                data = sPixels[i,j]
                                if (data[0]==(iteration*3) and data[1]==(iteration*3) and data[2]==(iteration*3) and data[3]==255):
                                    sPixels[i,j] = palettePixels[paletteCounter,iteration]
                                if data[3]==0:
                                    sPixels[i,j] = spriteBackground
                    sprite.save(f"PortraitTinkerKnight/Palette {paletteCounter+1}/{sprite.filename}") #Save the coloured sprite in the correct folder
                    print(f"{sprite.filename} created!")

#Creating spritesheets and placing them in their respective folders
for folder in os.listdir():
    if folder.startswith("Portrait"):
        continue
    if folder.endswith("Knight"):
        if sheetSaveLocation == "2":
            os.mkdir(f"SpriteSheets/{folder}")
        for palette in os.listdir(f"./{folder}"):
            vertSprites = []
            horizSprites = []
            for sprite in os.listdir(f"./{folder}/{palette}"):
                if sprite.endswith("0.png") and len(horizSprites) != 0:
                    row = get_concat_h_multi_blank(horizSprites)
                    horizSprites = [Image.open(f"./{folder}/{palette}/{sprite}")]
                    vertSprites.append(row)
                elif sprite.endswith(".png"):
                    horizSprites.append(Image.open(f"./{folder}/{palette}/{sprite}"))
            row = get_concat_h_multi_blank(horizSprites)
            horizSprites = [Image.open(f"./{folder}/{palette}/{sprite}")]
            vertSprites.append(row)
            if sheetSaveLocation == "2":
                os.mkdir(f"SpriteSheets/{folder}/{palette}")
                get_concat_v_multi_blank(vertSprites).save(f"./SpriteSheets/{folder}/{palette}/{folder}SpriteSheet.png")
            else:
                get_concat_v_multi_blank(vertSprites).save(f"./{folder}/{palette}/{folder}SpriteSheet.png")

#Creating icons (148x125 px) that can be used for The Spriters Resouce page
#Top left of 64x64 must be pasted at position (42,30) on 148x125 to be centred
for folder in os.listdir():
    if folder.endswith("Knight") and "Portrait" not in folder:
        icon = Image.new('RGBA', (148, 125), (0,0,0,0))
        knight = Image.open(f"./{folder}/Palette 1/s{folder}_0.png")
        if spriteBackground == (0,255,0,255):
            sPixels = knight.load()
            width = knight.size[0] 
            height = knight.size[1]
            for i in range(0,width):#Loop through all pixels in a row
                for j in range(0,height): #Loop through all pixels in a column
                    data = sPixels[i,j]
                    if data ==(0,255,0,255):
                        sPixels[i,j] = (0,0,0,0)
        #resize the knight, but check for scrap and mona since they're weird
        if knight.filename == "./MonaKnight/Palette 1/sMonaKnight_0.png":
            knight = knight.crop((0,6,63,69))
            knight = knight.resize((125,125), resample=PIL.Image.Resampling.NEAREST)
            icon.paste(knight, (24, 0))
        elif knight.filename == "./ScrapKnight/Palette 1/sScrapKnight_0.png":
            knight = knight.crop((16,16,79,79))
            knight = knight.resize((125,125), resample=PIL.Image.Resampling.NEAREST)
            icon.paste(knight, (12, 0))
        else:
            knight = knight.resize((125,125), resample=PIL.Image.Resampling.NEAREST)
            icon.paste(knight, (12, 0))
        if iconSaveLocation == "1":
            icon.save(f"./{folder}/{folder}Icon.png")
        else:
            icon.save(f"./Icons/{folder}Icon.png")
        print(f"Created {folder}Icon.png!")

#Creating full portraits
for folder in os.listdir():
    if folder.startswith("Portrait"):
        for palette in os.listdir(f"./{folder}"):
            portrait = ""
            prev = ""
            for sprite in os.listdir(f"./{folder}/{palette}"):
                if sprite.endswith("0.png") and portrait == "":
                    portrait = Image.open(f"./{folder}/{palette}/{sprite}")
                    if spriteBackground == (0,255,0,255): portrait = swapGreenAlpha(portrait)
                elif sprite.endswith("0.png") and portrait != "":
                    if spriteBackground == (0,255,0,255): portrait = swapGreenAlpha(portrait)
                    portrait.save(f"./{folder}/{palette}/{prev[:-6]}.png")
                    print(f"Created {prev[:-6]}.png")
                    portrait = Image.open(f"./{folder}/{palette}/{sprite}")
                    if spriteBackground == (0,255,0,255): portrait = swapGreenAlpha(portrait)
                elif sprite.endswith(".png"):
                    newPiece = Image.open(f"./{folder}/{palette}/{sprite}")
                    if spriteBackground == (0,255,0,255): newPiece = swapGreenAlpha(newPiece)
                    portrait.paste(newPiece, (0,0), newPiece)
                prev = sprite
            if portrait != "":
                if spriteBackground == (0,255,0,255): portrait = swapGreenAlpha(portrait)
                portrait.save(f"./{folder}/{palette}/{prev[:-6]}.png")
                print(f"Created {prev[:-6]}.png")

#Creating all portraits
portrait = ""
prev = ""
os.mkdir("Portraits")
for sprite in os.listdir():
    #print(sprite)
    if "palette" in sprite.lower() or "knight" in sprite.lower() or "mona" in sprite.lower() or "portal" in sprite.lower() or "teleport" in sprite.lower() or "portbox" in sprite.lower():
        continue
    if sprite.endswith("0.png") and portrait == "" and ("port" in sprite.lower() or "idle" in sprite.lower() or "hurt" in sprite.lower()):
        portrait = Image.open(sprite)
        prev = sprite
    elif sprite.endswith("0.png") and portrait != "" and ("port" in sprite.lower() or "idle" in sprite.lower() or "hurt" in sprite.lower()):
        print(f"Prev is {prev}")
        portrait.save(f"./Portraits/{prev[:-6]}.png")
        print(f"Created {prev[:-6]}.png")
        portrait = Image.open(sprite)
        prev = sprite
    elif sprite.endswith(".png") and ("port" in sprite.lower() or "idle" in sprite.lower() or "hurt" in sprite.lower()):
        newPiece = Image.open(sprite)
        portrait.paste(newPiece, (0,0), newPiece)
        prev = sprite
print(f"Prev is {prev}")
portrait.save(f"./Portraits/{prev[:-6]}.png")
print(f"Created {prev[:-6]}.png")
