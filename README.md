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
- **Step 1:** `git clone https://github.com/piyush2896/Scratch_knockoff.git`
- **Step 2:** `pip install -r requirements.txt`
- **Step 3:** Start a terminal
- **Step 4:** In the terminal:
  - `cd Scratch_knockoff\src`
  - `python app.py`
- **Step 5:** Go to `localhost:3000`:
  - This will initialize the firebase based Database
  - Default admin username - `admin@mathub.com`
  - Default admin password - `admin` (SHA256 encrypted on firebase)
  - Example Student1:
    - Username: `vaishali@mathub.com`
    - Password: `s103_vaishali@mathub-com`to be updated
  - Example Student2:
    - Username: `piyush@mathub.com`
    - Password: `s105_piyush@mathub-com`
  - When admin creates a new student, make sure to remember the ID displayed on creation, as that will be a part of the default password for that user. 
    - Default password format: `<lowercase ID>_<username, with -com replacing .com>`. See Example students for clarification.


