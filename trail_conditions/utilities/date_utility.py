import datetime
import time


class DateUtility:
	def __init__(self):
		self.current_date = datetime.datetime.fromtimestamp(time.time())

	def get_past_date(self, days_back):
		return self.current_date - datetime.timedelta(days=days_back)

	@staticmethod
	def get_time_request_string(date):
		return str(int(date.timestamp()))
