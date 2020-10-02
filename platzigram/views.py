""" Platzigram views """

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json


def hello_world(request):
	""" Return a greeting """
	now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
	return HttpResponse(f'Hello! Current server time is {now}')


# get arguments like 10,5434,49,2
def sort_integers(request):
	""" Return a JSON response with sorted integers """
	numbers = [int(i) for i in request.GET['numbers'].split(',')] # split the string and create the list from the list comprehension
	sorted_ints = sorted(numbers)
	data = {
		'status': 'ok',
		'numbers': sorted_ints,
		'message': 'Integers sorted successfully',
	}
	return HttpResponse(
		json.dumps(data, indent=4),
		content_type='application/json'
	)


def say_hi(request, name, age):
	""" Return a greeting """
	if age < 12:
		message = f'Sorry {name} you are not allowed here'
	else:
		message = f'Hello, {name}! Welcome to platzigram'
	return HttpResponse(message)
