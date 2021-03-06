import requests
from trail_conditions.config import DarkSkyConfig


class DarkSkyApiService:
	def __init__(self):
		self.key = DarkSkyConfig.dark_sky_key
		self.lat = '40.494312'
		self.lng = '-111.830759'
		self.exclude = 'currently, flags'

	def get_time_machine(self, time):
		response = requests.get(self.construct_url(time))
		return response.json()

	def construct_url(self, time):
		base_url = 'https://api.darksky.net/forecast/'
		request_url = base_url \
			+ self.key + '/' \
			+ self.lat + ',' \
			+ self.lng + ',' \
			+ time + '?exclude=' \
			+ self.exclude
		return request_url

	@staticmethod
	def concatenate_responses(response_one, response_two):
		for hour in response_one['hourly']['data']:
			response_two['hourly']['data'].append(hour)
		return response_one
