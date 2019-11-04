# MatHub - A Scratch Knockoff
Inspired by the Interactive Programming Platform - [Scratch](https://scratch.mit.edu/). The basic difference between the two being - Scratch represents a visually appealing programming interface, while MatHub is a visually appealing mathematics hub, for students from different stages of their schooling.

## Development
This project is currently under development with a goal of delivering workable at the end of every sprint.

**Development Team (Contributors):**
1. [Piyush Malhotra](https://github.com/piyush2896/)
2. [Anusha Singh](https://github.com/anushasingh30/)
3. [Sandya Manoharan](https://github.com/san1197/)
4. [Amudhan Manisekaran](https://github.com/AmudhanManisekaran)

## Basic System Requirements
- Programming Language: Python 3.5
- OS: Windows 10/Linux

## How to run?
- **Step 1: ** `git clone https://github.com/piyush2896/Scratch_knockoff.git`
- **Step 2: ** `pip install -r requirements.txt`
- **Step 3: ** Start two terminals
- **Step 4: ** In first terminal:
  - `cd Scratch_knockoff\backend`
  - `python app.py`
  - This will start your arithmetic RESTFul API
- **Step 5: ** In second terminal:
  - `cd Scratch_knockoff\src`
  - `python app.py`
  - This will start your basic dynamic frontend based on flask.
- **Step 6: ** Go to `localhost:3000`:
  - This will initialize the firebase based Database
  - Default admin username - `admin@mathub.com`
  - Default admin password - `admin` (SHA256 encrypted on firebase)
