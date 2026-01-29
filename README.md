# 🎮 Guessing League of Legends Character

**Guessing League of Legends Character** is a Python-based GUI game built using **Tkinter**.  
The game challenges players to identify a **League of Legends champion and their ability** based on an image clue.

This project was created as a **personal, non-commercial project** to practice Python programming, GUI development, and event-driven application design.

---

## 🧩 Game Overview
- An image of a League of Legends ability is displayed
- Players must guess:
  - The **ability key** (Q / W / E / R)
  - The **champion name**
- Correct answers increase the score
- Incorrect answers prompt the player to try again
- A new challenge is generated after each correct guess

---

## ✨ Features
- Graphical user interface built with **Tkinter**
- Image loading and resizing using **Pillow (PIL)**
- Randomized champion and ability selection
- Auto-complete champion name suggestion using a Listbox
- Keyboard-based input handling
- Real-time score tracking
- Simple and clean UI design

---

## 🛠️ Technologies Used
- **Python 3**
- **Tkinter** – GUI framework
- **Pillow (PIL)** – image processing
- **NumPy** – data handling
- **OS & Random** – file and game logic utilities

---

## 📁 Project Structure
.
├── main.py

├── Champion_Gallery/

│ ├── AhriQ.png

│ ├── GarenE.png

│ └── ...

├── Champion_Names/

│ └── champNames.txt


- `main.py` — Main application and game logic
- `Champion_Gallery/` — Ability images (not included in repo if ignored)
- `Champion_Names/champNames.txt` — List of champion names

---

## ▶️ How to Run

### 1️⃣ Install Python dependencies
    pip install pillow numpy

### 2️⃣ **Prepare assets**

Place champion ability images inside Champion_Gallery/

Ensure champNames.txt exists inside Champion_Names/

Image filenames should follow this format:

ChampionNameX.png
where X is the ability key (Q, W, E, or R)

### 3️⃣ **Run the game**

python main.py

---

## 🎯 How to Play

1. An ability image will appear on the screen

2. Enter the ability key (Q / W / E / R)

3. Enter the champion name

4. Use auto-complete suggestions to help

5. Press Enter or click CONFIRM

6. Score increases for correct answers

7. A new image appears after each correct guess

---

## 🧠 Learning Outcomes

Through this project, I practiced:

Object-oriented programming in Python

Tkinter GUI layout and widgets

Event handling (keyboard and button events)

Image processing with Pillow

Randomized game logic

User input validation and UI feedback

---

## 🚀 Future Improvements

Add difficulty levels or time limits

Add sound effects

Add high-score tracking

Add multiple game modes

Improve UI layout and animations

---

## ⚠️ Disclaimer

League of Legends and all related assets are trademarks and copyrights of Riot Games, Inc.
This project is a non-commercial, educational fan project and is not affiliated with or endorsed by Riot Games.

---
