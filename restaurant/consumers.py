import json
from channels.generic.websocket import AsyncWebsocketConsumer

class OrderNotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.user_channel_name = f"user_{self.user.id}"
        self.group_name = 'order_notifications'
        
        await self.channel_layer.group_add(
           self.user_channel_name,
            self.channel_name
        )
        
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.user_channel_name
        )
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'order_notification',
                'message': message
            }
        )
    
    async def order_notification(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
        