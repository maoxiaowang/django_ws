import json

import websockets
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


async def ws_connect(uri, func=None, **kwargs):
    """
    func为收到消息后执行的函数，第一个参数为ws接收到的result
    """
    async with websockets.connect(uri) as ws:
        # 循环接收消息
        while True:
            result = await ws.recv()
            if func:
                assert callable(func)
                await func(json.loads(result), **kwargs)


def ws_push(group_name, method: str, data, send_type='send.data'):
    """
    Push data through websocket

    group_name: channel group name
    method: create/update/delete
    send_type: e.g. send.data -> method name "send_data" in consumer class
    data: objects could be dumps by JSON (dict, list, ...)
    """
    assert method.upper() in ('CREATE', 'UPDATE', 'DELETE')
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        group_name, {'type': send_type, 'data': data, 'method': method.upper()})
