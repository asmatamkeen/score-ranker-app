# Score Ranker App

A simple, lightweight Streamlit application that allows users to log names and scores into a local SQLite database and view a live leaderboard.

# Features
* **Score Submission:** Input a name and a numeric score. Pressing **Save** and instantly clears the input fields for the next entry.
* **Live Leaderboard:** Displays a clean, sorted table of all entries, dynamically highlighting the current top-scorer as the winner.
* **Data Management:** Includes a dedicated option to wipe the database and start fresh.

## Tech Stack
* [Python](https://www.python.org/)
* [Streamlit](https://streamlit.io/)
* [SQLite3](https://docs.python.org/3/library/sqlite3.html)
* [Pandas](https://pandas.pydata.org/)

## How to Run

1. **Clone the repository:**
   ```bash
   git clone <https://github.com/asmatamkeen/score-ranker-app>
   cd score-ranker-app