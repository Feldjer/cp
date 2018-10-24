DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_paycopg2',
		'NAME': 'db1',
		'USER': 'djangocp',
		'PASSWORD': 'wasdrety2200dja',
		'HOST': 'localhost',
		'PORT': '',
		
	}
}