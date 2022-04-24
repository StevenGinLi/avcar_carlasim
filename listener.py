from flask import Flask, request,  jsonify, make_response
import tutorial, threading, sample
import subprocess
from multiprocessing import Process

app = Flask(__name__)

@app.route('/', methods=['POST'])
def result():
	print(request.data)  # raw data
	print(request.json)  # json (if content-type of application/json is sent with the request)
	print(request.data)  # raw data
	print(request.get_json(force=True))  # json (if content-type of application/json is not sent)
	
	car_type = request.json['car_type']
	print('car_type:', car_type)
	car_id = request.json['car_id']
	print('car_id', car_id)
	booking_id = request.json['booking_id']
	print('booking_id', booking_id)
	
	#Spawn New Thread for request
	#threading.Thread(target=sample.main(), args=[]).start()
	#multiprocessing.Process(target=sample.main(), args=[]).start()
	#subprocess.call(['python','sample.py'])
	#p = Process(target=sample.main, args=(,))
	#p.start()
	subprocess.Popen(["python","auto_pilot.py","-id",str(car_id),"-bid",str(booking_id),"--filter",car_type])
	#tutorial.main()
	
	data = {'message': 'message', 'code': 'SUCCESS'}
	return make_response(jsonify(data), 201)