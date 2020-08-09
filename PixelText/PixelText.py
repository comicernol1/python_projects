import numpy, math
from PIL import Image

f = open("demo_text.txt", "r")
lines = f.readlines()
FLm = (len(max(lines, key=len)) - 1)
cnt = len(lines)
L_Rx = []
for line in lines:
    L_Ry = []
    line = line.replace("\n","")
    for c in range(FLm):
        try:
            Cx = ord(line[c])
            if Cx <= 255 and Cx >= 0:
                L_Ry.append([Cx])
            else:
                raise ValueError
        except IndexError:
            L_Ry.append([0])
    L_Rx.append(L_Ry)
a = numpy.dstack((L_Rx,L_Rx,L_Rx))
f.close()
fb = open("demo_text.temp", "w")
fb.write(str(L_Rx))
im_out = Image.fromarray(a.astype('uint8')).convert('RGB')
im_out.save('demo.jpg')
fb.close()
