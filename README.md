💬 Real-Time Chat Application (Django + Channels)
A real-time chat application built using Django, Django Channels, and WebSockets. This project demonstrates how to implement live communication between users using asynchronous handling.

🚀 Features
🔌 Real-time messaging using WebSockets
👥 Multiple chat rooms (based on room ID)
⚡ Instant message delivery across multiple tabs/users
🧠 Asynchronous handling with Django Channels
🔄 Group-based communication (channel layers)
🛠️ Tech Stack
Backend: Django
Real-time Layer: Django Channels
Protocol: WebSockets
ASGI Server: Daphne
Message Broker: Redis
Frontend: HTML, JavaScript
📂 Project Structure
Real_Time_Chat_App/
│
├── Real_Time_Chat_App/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│
├── chat/
│   ├── consumers.py
│   ├── routing.py
│   ├── views.py
│   ├── templates/
│   │   └── chat/
│   │       └── room.html
│
└── manage.py
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone <your-repo-link>
cd Real_Time_Chat_App
2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
3️⃣ Install dependencies
pip install django channels daphne redis
4️⃣ Configure settings.py
INSTALLED_APPS = [
    'daphne',
    'channels',
    'chat',
]

ASGI_APPLICATION = "Real_Time_Chat_App.asgi.application"

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    }
}
5️⃣ Run Redis (optional but recommended)
redis-server
6️⃣ Run the server
python manage.py runserver
🌐 Usage
Open in browser:

http://127.0.0.1:8000/chat/1/
Open the same URL in multiple tabs
Send messages → see real-time updates
🧠 How It Works
User opens a chat room (/chat/<room_id>/)

JavaScript creates a WebSocket connection

Django Channels routes it via ASGI

ChatConsumer:

Connects user to a group
Receives messages
Broadcasts to all users in the room
Messages instantly appear for all connected users

🔑 Key Concepts
ASGI → Handles async communication
Channels → Adds WebSocket support to Django
Consumers → Handle WebSocket events
Channel Layers → Enable group messaging
Redis → Backend for channel layers (production use)
⚠️ Notes
Current setup uses InMemoryChannelLayer (for development only)
Use Redis for production
Room IDs are dynamic (created via URL)
📌 Future Improvements
🔐 User authentication
💬 Private messaging (user-to-user)
🗄️ Store messages in database
🔔 Notifications
🎨 Improved UI
🙌 Acknowledgment
This project is built for learning real-time systems using Django and understanding async architecture.

📜 License
This project is open-source and free to use.