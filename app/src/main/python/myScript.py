from PIL import Image
import re
from io import BytesIO
import cv2
import matplotlib.pyplot as plt
import easyocr
import base64
from os.path import dirname, join
from com.chaquo.python import Python

def main(bName,im):
	files_dir=str(Python.getPlatform().getApplication().getFilesDir())
	fileimg1=join(dirname(files_dir),"input.jpg")
	fileimg2=join(dirname(files_dir),"output.jpg")
	print("**********Reached Python**************")
	text = bName
	pattern = list(text.split(" "))
	print(pattern)
	imgb = bytes(im, 'ascii')
	img_bytes = base64.decodebytes(imgb)
	with open(fileimg1, 'wb') as ip:
		ip.write(img_bytes)
	#reader = easyocr.Reader(['en'])
	image = cv2.imread(fileimg1)
	#res = reader.readtext(fileimg1)
	#for (bbox, text, prob) in res:
	# unpack the bounding box
	#    (tl, tr, br, bl) = bbox
	#    tl = (int(tl[0]), int(tl[1]))
	#    tr = (int(tr[0]), int(tr[1]))
	#    br = (int(br[0]), int(br[1]))
	#    bl = (int(bl[0]), int(bl[1]))
	#    cv2.rectangle(image, tl, br, (0, 255, 0), 2)
	#    cv2.putText(image, text, (tl[0], tl[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
	#plt.rcParams['figure.figsize'] = (16, 16)
	cv2.imwrite(fileimg2, image)
	encoded_string = ' '
	with open(fileimg2, "rb") as op:
		encoded_string = base64.b64encode(op.read())
	return ""+str(encoded_string,'utf-8')

