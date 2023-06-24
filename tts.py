import uvicorn
from fastapi import FastAPI
import speech_recognition as sr
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this with the appropriate origins
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/record/audio")
async def record_audio():
    print("Recording audio...")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.record(source, duration=3)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)
        return {"query": "None"}  # Return a JSON response

    return {"query": query}  # Return a JSON response

if __name__ == "__main__":
    uvicorn.run(app, port=5500)