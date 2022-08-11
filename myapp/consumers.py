from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.db.models import Model
from django.forms import model_to_dict


class AuthorBookWebsocketConsumer(AsyncJsonWebsocketConsumer):
    groups = ['test_group']

    async def send_data(self, text):
        if isinstance(text, Model):
            data = await self.get_data(text)
        else:
            data = text
        await self.send_json(data)

    def get_data(self, instance):
        return model_to_dict(instance)
