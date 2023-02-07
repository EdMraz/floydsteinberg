from PIL import Image

img = Image.open("girl.jpg")
pixels = img.load()
for j in range(img.size[1]):
    for i in range(img.size[0]):
        sf = int(sum(pixels[i,j])/3)
        pixels[i,j]=(sf,sf,sf)

for j in range(img.size[1]):
    for i in range(img.size[0]):
        tien = pixels[i,j][0]
        if tien > 127:
            new_colour = 255
        else:
            new_colour = 0
        pixels[i,j] = (new_colour,new_colour,new_colour)

        error = tien - new_colour

        if i+1 < (img.size[0]):
            sfn_7_16 = round((error/16)*7)
            new_tien = pixels[i+1,j][0]+sfn_7_16
            pixels[i+1,j] = (new_tien,new_tien,new_tien)

        if i-1 >= 0 and j+1 < img.size[1]:
            sfn_3_16 = round((error/16)*3)
            new_tien = pixels[i-1,j+1][0]+sfn_3_16
            pixels[i-1,j+1] = (new_tien,new_tien,new_tien)

        if j+1 < (img.size[1]):
            sfn_5_16 = round((error/16)*5)
            new_tien = pixels[i,j+1][0]+sfn_5_16
            pixels[i,j+1] = (new_tien,new_tien,new_tien)

        if i+1 < (img.size[0]) and j+1 < (img.size[1]):
            sfn_1_16 = round((error/16)*1)
            new_tien = pixels[i+1,j+1][0]+sfn_1_16
            pixels[i+1,j+1] = (new_tien,new_tien,new_tien)

img.save("girlnew.png")
