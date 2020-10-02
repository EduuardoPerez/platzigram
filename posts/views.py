""" Posts views """

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime


posts = [
	{
		'name': 'Mont Blac',
		'user': 'Yésica Cortés',
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'picture': 'https://picsum.photos/200/200/?image=1036',
	},
    {
        'name': 'Via Láctea',
        'user': 'C. Vander',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=903',
    },
    {
        'name': 'Nuevo auditorio',
        'user': 'Thespianartist',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1076',
    },
	{
        'name': 'My Dog.',
        'user': 'Yésica Cortes',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/237/200/200'
    },
    {
        'name': 'Khe.',
        'user': 'Pink Woman',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/84/200/200'
    },
    {
        'name': 'Nautural web.',
        'user': 'Pancho Villa',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/784/200/200'
    },
]


def list_posts(request):
	""" List existing posts """
	content = []
	for post in posts:
		content.append("""
			<p><strong>{name}</strong></p>
			<p><small>{user} - <i>{timestamp}</i></small></p>
			<figure><img src="{picture}"/></figure>
		""".format(**post))
	return HttpResponse('<br>'.join(content))
