 
import json
import time
from predictfunc import predict
import datetime
import os
from evaluate import predict_mask
import base64
from PIL import Image
from base64 import decodestring
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import io
items	=[]

def base64encode(image):
	directory="image"
	for files in os.listdir(directory):
		if files==image:
			with open("image/"+image,"rb") as f:
				response=base64.b64encode(f.read())

	return response.decode('utf8')

def base64encodemask(image):
	directory="maskedimage"
	for files in os.listdir(directory):
		if files==image:
			with open("maskedimage/"+image,"rb") as f:
				response=base64.b64encode(f.read())

	return response.decode('utf8')




class verfiyhandler(RequestHandler):
	def post(self):
  		data=self.request.body	
  		
  		#print(data)
  		json_string=data.decode('utf8')
  		json_d=json.loads(json_string)
  		bodypart=json_d["part"]
  		imgdata = base64.b64decode(json_d['image'])
  		filename = 'upload.jpg'
  		with open(filename, 'wb') as f:
  			f.write(imgdata)
  		
    	
  		ans=predict(filename,bodypart)
  		print("bodypart in tornado is "+bodypart)
  		print("prediction is ans"+ans)
  		self.write(ans)

class submitHandler(RequestHandler):
	def post(self):
		print("post recieved ")
		ctime=time.time()
		print(ctime)
		st = datetime.datetime.fromtimestamp(ctime).strftime('%Y-%m-%d %H:%M:%S')
		
		data=self.request.body
		json_string=data.decode('utf8')
		json_d=json.loads(json_string)
		imgdata = base64.b64decode(json_d['image'])


		#print(type(imgdata))
		filename = 'image/'+st+".jpg"
		print(filename)
		with open(filename, 'wb') as f:
		    f.write(imgdata)
		print("normal image saved successfully")
		predict_mask(filename)
		savefinalimg="work.jpg"
		with open(savefinalimg, "rb") as image:
  			f = image.read()
  			b = bytearray(f)

		destfile='maskedimage/'+st+".jpg"
		with open(destfile,"wb") as f:
			f.write(b)

		print(' masked image done successfully')
		#returndata=base64.b64encode(byte_img)	
		#print(returndata)	
		response=""	
		with open(savefinalimg,"rb") as f:
			
			response=base64.b64encode(f.read())
		#print(response)
		print(type(response))
		json_response={}
		json_response["image"]=response.decode('utf8')
		json_response=json.dumps(json_response)
		self.write(json_response)
  		
  		
class previousrecord(RequestHandler):
	def post(self):
		directory="image"
		imagelist=[]
		finallist=[]
		maskedlist=[]	
		maskedirectory="maskedimage"
		for filename in os.listdir(directory):
			#print(filename)
			imagelist.append(filename)	
		for filename in os.listdir(maskedirectory):
			maskedlist.append(filename)
		finallist=[image for image in imagelist if image in maskedlist]
		zprint(finallist)
		#json_response=[]
		
		#for img in finallist:
		#	img1=base64encode(img)
		#	img2=base64encodemask(img)
		#	perimagejson={"img1":img1,"img2":img2}
		#	json_response.append(perimagejson)
			#print(img1)
			#print(img2)
		#responsedict={}
		#responsedict["answer"]=json_response
		#rint("previous record ")
		
		#rint(responsedict)
		finalurl=[]
		finaljson={}
		response=[]
		for final in finallist:
			finalimage="http://192.168.43.116:8888/image/"+final
			finalmasked="http://192.168.43.116:8888/maskedimage/"+final
			perimagejson={"img1":finalimage,"img2":finalmasked}
			response.append(perimagejson)
		finaljson["answer"]=response
		print(finaljson)

		self.write(finaljson)

class submitHandler2(RequestHandler):
	def post(self):
	#print("post recieved ")
		ctime=time.time()
		print(ctime)
		st = datetime.datetime.fromtimestamp(ctime).strftime('%Y-%m-%d %H:%M:%S')
		data=self.request.body
		json_string=data.decode('utf8')
		json_d=json.loads(json_string)
		imgdata = base64.b64decode(json_d['image'])



		
		
		

		#print(type(imgdata))
		filename = 'image/'+st+".jpg"
		print(filename)
		with open(filename, 'wb') as f:
		    f.write(imgdata)
		print("normal image saved successfully")
		predict_mask(filename)
		savefinalimg="work.jpg"
		with open(savefinalimg, "rb") as image:
				f = image.read()
				b = bytearray(f)

		destfile='maskedimage/'+st+".jpg"
		with open(destfile,"wb") as f:
			f.write(b)

		print(' masked image done successfully')
		#returndata=base64.b64encode(byte_img)	
		#print(returndata)	
		response=""	
		with open(savefinalimg,"rb") as f:
			
			response=base64.b64encode(f.read())
		#print(response)
		print(type(response))
		json_response={}
		json_response["image"]=response.decode('utf8')
		json_response=json.dumps(json_response)
		self.write(json_response)
#liveimage=[]			




class submitHandler3(RequestHandler):
	def post(self):
		print("posted def")
		print(self.body.data)

		self.write("yes")
  		
def make_app():
 	urls = [("/", verfiyhandler),("/abc", submitHandler),("/prev",previousrecord),("/abc1",submitHandler2),("/def",submitHandler3)]
 	return Application(urls,debug=True)
 	 	  	
 	 	  
if __name__ == '__main__':
 	app = make_app()
 	app.listen(3000)
 	IOLoop.instance().start()

    