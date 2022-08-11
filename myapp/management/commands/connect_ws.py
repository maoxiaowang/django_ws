import asyncio

from asgiref.sync import sync_to_async
from django.core.management import BaseCommand
from django.forms import model_to_dict

from myapp.models import Book
from myapp.utils import ws_connect


async def _handle_data(result, **kwargs):
    """
    ws连接的回调函数
    """
    payload = result['data']
    author_id = payload.get('id')
    author_name = payload.get('name')
    books = list()
    if author_id:
        books = await sync_to_async(Book.objects.filter)(author__id=author_id)

    books = await sync_to_async(books.values_list)('name', flat=True)
    books = await sync_to_async(list)(books)
    await sync_to_async(print)(f'作者{author_name}已被修改，所有著作：{books}')


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'ws_url', type=str
        )

    def handle(self, *args, **options):
        url = options['ws_url']
        asyncio.run(ws_connect(url, func=_handle_data))
