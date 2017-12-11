from django.test import TestCase
from .weather import TrailConditions


class TrailConditionsTestCase(TestCase):
	def setUp(self):
		self.dark_sky_negative_response = {
			"hourly": {
				"data": [
					{
						"temperature": 59,
						"cloudCover": 10,
						"precipProbability": .75,
						"precipIntensity": 2
					},
					{
						"temperature": 57,
						"cloudCover": 15,
						"precipProbability": .75,
						"precipIntensity": 2
					},
					{
						"temperature": 58,
						"cloudCover": 10,
						"precipProbability": .75,
						"precipIntensity": 2
					},
					{
						"temperature": 40,
						"cloudCover": 12,
						"precipProbability": .75,
						"precipIntensity": 2
					}
				]
			}
		}
		self.dark_sky_positive_response = {
			"hourly": {
				"data": [
					{
						"temperature": 59,
						"cloudCover": 10,
						"precipProbability": .75,
						"precipIntensity": .02
					},
					{
						"temperature": 57,
						"cloudCover": 15,
						"precipProbability": .75,
						"precipIntensity": .02
					},
					{
						"temperature": 58,
						"cloudCover": 10,
						"precipProbability": .75,
						"precipIntensity": .02
					},
					{
						"temperature": 40,
						"cloudCover": 12,
						"precipProbability": .75,
						"precipIntensity": .02
					}
				]
			}
		}

		self.all_temps = [40, 40, 60, 40, 50, 50]
		self.cloud_cover = [40, 50, 50, 60, 60, 65]

	def test_check_conditions_with_negative_response(self):
		trail_conditions = TrailConditions()
		check = trail_conditions.check_conditions(self.dark_sky_negative_response)
		self.assertEquals(check, False)

	def test_check_conditions_with_positive_response(self):
		trail_conditions = TrailConditions()
		check = trail_conditions.check_conditions(self.dark_sky_positive_response)
		self.assertEquals(check, True)

	def test_check_temperature(self):
		trail_conditions = TrailConditions()
		positive_check = trail_conditions.check_temperature(self.all_temps, 60)
		negative_check = trail_conditions.check_temperature(self.all_temps, 30)
		self.assertEquals(positive_check, 1)
		self.assertEquals(negative_check, 0)

	def test_check_cloud_cover(self):
		trail_conditions = TrailConditions()
		negative_check = trail_conditions.check_cloud_cover(self.cloud_cover, 70)
		positive_check = trail_conditions.check_cloud_cover(self.cloud_cover, 30)
		self.assertEquals(positive_check, 1)
		self.assertEquals(negative_check, 0)



