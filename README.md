# python bootcamp projects
#### Interactive Command-line Application (Quiz & Guess the Number Game),November 2026
#### By **Ruth**
## Description
This repository contains my weekly python programming assignment project 
The main application feautured in this version is the **Guess the number game**('guess_the_number.py'), along with **CLI quiz game** ('week_one.py/cli_quiz.py)

### Key Features of Guess the Numnber Game:
**Difficulty selection:**Allows players to select between Easy (10 attempts),Medium (7 attempts),and hard (5 attempts).Automatically defaults to Hardif unrecognized optionis typed
**Robust Input Validation:** Uses 'try/except' blocks to catch invalid non-numeric inputs without deducting player attempts 
**Range Bounds Enforcement:**Rejects guesses outside the 1-100 range 
**Attempts Tracking & game loop:** Tracks attempts used, gives instant "Too high" /" Too low" feedback, and exits cleanly using 'break' upon a correct guess

## setup/Installation Requirements
*Ensure you have python 3 installed on your machine
* clone this repository to your local computer:
'''bash
git clone [https://github.com/ruth-ops/week-one-project.git](https://github.com/ruth-ops/week-two-project.git)
*Navigate into the repository root folder:
cd week-one-project
*Run the Guess the Number Game:
python week_two.py/guess_the_number.py
*Run the CLI Quiz Game:
python week_one.py/cli_quiz.py
## Known Bugs
There are currently no known unresolved bugs. Input errors (letters instead of numbers) and out-of-range numbers (below 1 or above 100) are gracefully caught and handled by defensive try/except logic.
## Technologies Used
**Python 3 (utilizing modules like random for secret number generation)
**Git & GitHub for version control and project organization
### Support and Contact Details
If you run into any issues or have questions regarding this repository, please feel free to reach out via GitHub or create an issue directly on this repository.
###License
*Licensed under the MIT License.
Copyright (c) 2026 Ruth