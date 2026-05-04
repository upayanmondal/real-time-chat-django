import json
from channels.generic.websocket import AsyncWebsocketConsumer

'''
What is a "Consumer" in Django Channels?
Think of it like this:

    In normal Django, a View handles HTTP requests.
    In Django Channels, a Consumer handles WebSocket connections.'''

'''
Why is it called a "Consumer"?
---> Because it consumes (receives and processes) messages/events that come through the connection. 
     It sits there, listens, and reacts.
'''

# class ChatConsumer(AsyncWebsocketConsumer) ----> creating a custom WebSocket handler using Channels

class ChatConsumer(AsyncWebsocketConsumer):

    # async: This function runs asynchronously (non-blocking)
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f"chat_{self.room_id}"

        # scope : a dictionary containing connection details
        # Example of a scope dictionary
        """
        {
            'type': 'websocket',
            'path': '/ws/chat/1/',
            'user': <User object>,
            'url_route': {
                'kwargs': {
                    'room_id': 1
                }
            }
        }
        """
        # so, self.scope['url_route']['kwargs']['room_id'] returns 'room_id' inside kwargs which is 1 here

        # await : Wait for this async operation to finish, but don’t block other tasks
        # channel_layer : Redis connection system
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name # It is a unique ID for this specific connection (this tab/device) , example: specific.websocket.ABCD1234
            # Each browser tab = one connection
            # Each connection = one channel_name
        )

        await self.accept()

        # connect() summary: User connects → added to room → connection accepted
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        # disconnect() summary : User leaves → removed from room 

    async def receive(self, text_data):
        data = json.loads(text_data) # Convert JSON string → Python dict
        message = data['message']  # Extract actual message

        # await self.channel_layer.group_send() : send the message to the entire group via Redis
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message", # Call a function named chat_message next. Basically it calls async def chat_message(self, event)
                "message": message
            }
        )
    
    async def chat_message(self, event):
        # seft.send() : Sends data back to frontend (browser)
        await self.send(text_data = json.dumps({
            "message": event["message"]
        }))
