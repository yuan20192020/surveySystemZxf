from django.dispatch import receiver
from django.db.models.signals import post_save

from django.utils.crypto import get_random_string

from .. import models


def create_unique_code(sender, **kwargs):
	'''
	print(kwargs)
	{'signal': <django.db.models.signals.ModelSignal object at 0x7f3d2bd33c10>,
	'instance': <Survey: Survey object (7)>, 
	'created': True, 
	'update_fields': None, 
	'raw': False, 
	'using': 'default'}
	'''
	created=kwargs.get("created",False)
	if not created:
		return 

	instance = kwargs.get("instance")
	count = instance.count
	codes=[]
	while count:
		_code = get_random_string(8)
		if models.SurveyCode.objects.filter(unique_code=_code).exists():
			continue
		codes.append(models.SurveyCode(unique_code=get_random_string(8),
			survey=instance))
		count -= 1

	models.SurveyCode.objects.bulk_create(codes)

post_save.connect(create_unique_code, sender = models.Survey)

