from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone

from .dark_sky_service import DarkSkyApiService
from .weather import TrailConditions
from .utilities import DateUtility

from trail_conditions.models import Conditions


class HomeView(TemplateView):
	def __init__(self):
		self.message = ''

	def get(self, request):
		dark_sky = DarkSkyApiService()
		trail_conditions = TrailConditions()
		date_utility = DateUtility()
		yesterday_request_time = date_utility.get_time_request_string(date_utility.get_past_date(1))
		today_request_time = date_utility.get_time_request_string(date_utility.current_date)

		try:
			most_recent_conditions = Conditions.objects.latest('timestamp')
		except Conditions.DoesNotExist:
			yesterday_response_json = dark_sky.get_time_machine(yesterday_request_time)
			today_response_json = dark_sky.get_time_machine(today_request_time)
			full_response = dark_sky.concatenate_responses(today_response_json, yesterday_response_json)
			TrailConditions.check_conditions(trail_conditions, full_response)
			most_recent_conditions = Conditions.objects.latest('timestamp')

		diff = timezone.now() - most_recent_conditions.timestamp
		if diff.days > 0:
			yesterday_response_json = dark_sky.get_time_machine(yesterday_request_time)
			today_response_json = dark_sky.get_time_machine(today_request_time)
			full_response = dark_sky.concatenate_responses(today_response_json, yesterday_response_json)
			TrailConditions.check_conditions(trail_conditions, full_response)
			most_recent_conditions = Conditions.objects.latest('timestamp')

		print(request.session.get('has_voted'))
		if request.session.get('has_voted') is True:
			self.message = 'You have already voted!'
		elif request.GET.get('yes-vote'):
			most_recent_conditions.yes_votes += 1
			most_recent_conditions.save()
			request.session['has_voted'] = True
		elif request.GET.get('no-vote'):
			most_recent_conditions.no_votes += 1
			most_recent_conditions.save()
			request.session['has_voted'] = True

		good_to_go = most_recent_conditions.condition_verdict

		context = {
			'message': self.message,
			'good_to_go': good_to_go,
			'yes_votes': most_recent_conditions.yes_votes,
			'no_votes': most_recent_conditions.no_votes,
		}

		return render(request, 'trail_conditions/index.html', context)
