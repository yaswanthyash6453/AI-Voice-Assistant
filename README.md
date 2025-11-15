🚀 Chinnu – AI Personal Voice Assistant (Python)

Chinnu is a smart, voice-controlled personal assistant developed using Python.
It performs tasks like searching the web, fetching weather updates, answering questions, opening websites, taking photos, reading news, and much more — simply through voice commands.

⭐ Features

✔️ Voice Recognition (Speech-to-Text)
✔️ Natural Voice Responses (Text-to-Speech)
✔️ Wikipedia Search
✔️ Google / YouTube / Gmail Auto Open
✔️ Weather Report (via OpenWeather API)
✔️ Answers Questions (via WolframAlpha API)
✔️ Real-time News Headlines
✔️ Takes Photos using Webcam
✔️ Time & System Info
✔️ Custom Wake Word – "Hey Chinnu"
✔️ Professional code with .env support for API key protection
✔️ GitHub-safe (no visible API keys)

🛠️ Technologies Used

Python

SpeechRecognition

Pyttsx3

Wikipedia API

OpenWeather API

WolframAlpha API

Webbrowser

Subprocess

ecapture

dotenv (for hiding API keys)


📁 Project Structure
AI-Voice-Assistant/
│
├── main.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt

🔐 Environment Variables (.env file)

Create a .env file in the root folder and add:

OPENWEATHER_KEY=your_openweather_api_key
WOLFRAM_APP_ID=your_wolframalpha_app_id


⚠️ These keys are hidden from GitHub using .gitignore.


📦 Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/yourusername/AI-Voice-Assistant.git
cd AI-Voice-Assistant

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Create .env file
OPENWEATHER_KEY=your_api_key
WOLFRAM_APP_ID=your_app_id

4️⃣ Run the assistant
python main.py

🎤 How to Use

Just say:

Wake Word:
Hey Chinnu

Example Commands:
open youtube  
open google  
weather  
time  
who are you  
take a photo  
search computer vision  
ask what is artificial intelligence  
good bye  

📝 Requirements File (requirements.txt)

Add this to your requirements.txt:

SpeechRecognition
pyttsx3
wikipedia
ecapture
wolframalpha
python-dotenv
requests

👨‍💻 Developer

Karibugatha Yaswanth
AI | ML | Python Developer

⭐ Support this Project

If you like this project, kindly star the repository ⭐ on GitHub.

