# CloseContacts Group 17 — Lab 2

## Overview
Android app that displays a list of contacts with phone numbers. Contacts are stored in a SQLite database managed by a Flask backend. Tapping a contact opens the phone dialer.

---

## Project Structure
```
server/
  app.py                  ← Flask API + Peewee ORM + SQLite database
android_project/
  CloseContactsGroup17/   ← Android app (Kotlin + Jetpack Compose)
```

---

## Requirements
**Server:** Python 3.9+, Flask, Peewee
```bash
pip install flask peewee
```
**Android:** Android Studio, min SDK 24 (Android 7.0)

---

## Running the Server
```bash
cd server
python app.py
```
Server starts at `http://127.0.0.1:5000`. On first run it auto-seeds 7 default contacts. Test it by opening `http://127.0.0.1:5000/contacts` in your browser or use a DB Browser for SQLite.

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/contacts` | Returns all contacts as JSON |
| POST | `/contacts` | Adds a new contact |

---

## Running the Android App

1. Open `android_project/CloseContactsGroup17` in Android Studio
2. In `MainActivity.kt`, set the server URL:
```kotlin
const val SERVER_URL = "http://10.0.2.2:5000/contacts"
```
- Use `10.0.2.2` for the Android emulator
- Use your PC's local IP (e.g. `192.168.1.X`) for a real device — both must be on the same network
3. Make sure the Flask server is running, then press ▶ Run

---

#Authors
Group17
