# A centralized control panel for all security APIs (eventually)

import requests
import time

APIS = {
	api:{
		parameters:[],
		actions:[],
		rate_limit:0,
		base_url:''
	}
}

all_apis = list(APIS.keys())

class Request:
	def __init__(self, api, **kwargs):
		self.api = api
		self.base_url = APIS[api]['base_url']
		self.rate_limit = APIS[api]['rate_limit']
		if 'parameters' in kwargs.keys():
			self.parameters = kwargs['parameters']
		if 'actions' in kwarg.keys():
			self.actions = kwargs['actions']

	def make_requests(self):
		'''Form a request url from the API name, parameters, and actions.'''
		return request_urls = []

	def send_requests(self, request_urls):
		'''Send the HTTP request.'''
		responses = []
		for request_url in requests_urls:
			response = requests.get(request_url)
			responses.append(response)
			time.wait(self.rate_limit)



# A user will select an API and various actions and parameters through a GUI.
# Those inputs will be fed into a Request instance constructor that will be 
# used to make and send the HTTP request.
request = Request(api, parameters=[], actions=[])
request_urls = request.make_request()
response = request.send_request(request_urls)

# The system will inform the user that their response is ready.