from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.forms import model_to_dict

from myapp import utils
from myapp.models import Author


def foo():
    pass


@receiver([post_save, post_delete], sender=Author)
def on_author_saved(sender, instance, **kwargs):
    if 'created' in kwargs:
        method = 'CREATE' if kwargs['created'] else 'UPDATE'
    else:
        method = 'DELETE'
    utils.ws_push('test_group', method, model_to_dict(instance))
