from trail_conditions.models import Conditions


class TrailConditions:
	def __init__(self):
		self.temp_limit = 60
		self.cloud_cover_limit = 50

	def check_conditions(self, dark_sky_response):
		good_to_go = True
		all_temps = []
		all_cloud_cover = []
		weighted_precip_intensity = 0

		for hour in dark_sky_response['hourly']['data']:
			all_temps.append(hour['temperature'])
			all_cloud_cover.append(hour['cloudCover'])
			if hour['precipProbability'] > .1 and hour['precipIntensity'] > .001:
				weighted_precip_intensity += hour['precipIntensity'] * hour['precipProbability']

		probably_rained = 1 if weighted_precip_intensity > 0.2 else 0
		low_temps = self.check_temperature(all_temps, self.temp_limit)
		high_cloud_cover = self.check_cloud_cover(all_cloud_cover, self.cloud_cover_limit)
		if probably_rained:
			if low_temps or high_cloud_cover:
				good_to_go = False

		condition = Conditions(condition_verdict=good_to_go)
		condition.save()
		return good_to_go

	@staticmethod
	def check_temperature(all_temps, limit):
		average_temp = 0

		for temp in all_temps:
			average_temp += temp

		average_temp = average_temp / len(all_temps)

		if average_temp < limit:
			return 1
		else:
			return 0

	@staticmethod
	def check_cloud_cover(all_cloud_cover, limit):
		average_cloud_cover = 0

		for cloud_cover in all_cloud_cover:
			average_cloud_cover += cloud_cover

		average_cloud_cover = average_cloud_cover / len(all_cloud_cover)

		if average_cloud_cover > limit:
			return 1
		else:
			return 0


# Unit Weighted Regression Factors

# 24 hour precipitation probability
# 24 hour precipitation intensity
# 12 hour post-precipitation average temp
# 12 hour post-precipitation cloud cover
# 12 hour post-precipitation humidity

# what other ambient factors impact evaporation rates?


