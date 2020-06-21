from flask import request, jsonify
from datetime import datetime
import os
from image_process.service import Service

def main(resource_path):
	data = {}
	patch_data_path = os.path.join(resource_path, 'patch_data.json')
	if request.method == 'POST':
		data['name'] = request.args.get('name')
		data['age'] = request.args.get('age')
		data['contact_no'] = request.args.get('contact_no')
		data['sex'] = request.args.get('sex')
		if 'image' in request.files:
			img = request.files['image']
			img_name = '_'.join([datetime.now().strftime('%Y%m%d%H%M%S'), data['age'], data['sex']]) + "." + img.filename.split('.')[1]
			img_path = os.path.join(resource_path, 'uploaded_image', img_name)
			img.save(img_path)
			service = Service(img_path, patch_data_path)
			data['report'] = service.main()
			del service
		return jsonify(data)
	return jsonify(data)
