# PLANNATE — Your Planning Mate

A command-line productivity app built for JEE aspirants to streamline their preparation.
PLANNATE tracks study hours, test scores, and question-solving speed across Physics, Chemistry,
and Maths — with visual analytics to help identify weaknesses.

---

## Features

- **Per-User Database** — Each user gets their own MySQL database.
- **Study Time Tracker** — Log daily hours per subject.
- **Speed Tracker** — Timer-based question speed calculator.
- **Test Analyzer** — Enter mock test scores and get instant feedback.
- **Weakness Detection** — Identifies your weakest subject automatically.
- **Visual Graphs:**
  - Bar Graph *(time spent per subject)*
  - Line Graph *(speed over the week)*
  - Pie Charts *(test question distribution)*
  - Progress Line Graph *(percentage trend over 5 tests)*

---

## Tech Stack

| Layer        | Technology              |
|--------------|-------------------------|
| Frontend     | Python 3.9+             |
| Backend      | MySQL 8.0               |
| Connectivity | mysql-connector-python  |
| Graphs       | matplotlib, numpy       |
| Timer        | oclock                  |

---

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/sifatkochar/Plannate.git
cd Plannate
```

**2. Install dependencies**

```bash
pip install mysql-connector-python numpy matplotlib oclock python-dotenv
```

**3. Set up environment variables**

Create a `.env` file in the project folder:

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
```

**4. Run the app**

```bash
python main.py
```

---

## Database Structure

PLANNATE automatically creates a personal MySQL database for each user on signup.
Three tables are created per user -

| Table       | Description                                      |
|-------------|--------------------------------------------------|
| `JEE_TIME`  | Stores daily study hours per subject.            |
| `JEE_SPEED` | Stores question-solving speed per subject per day.|
| `JEE_MARKS` | Stores mock test scores and performance data.    |

See `structure.sql` for the full database structure.

---

## Menu Options

| Option | Feature                                        |
|--------|------------------------------------------------|
| 1      | Enter time spent studying                      |
| 2      | View time chart *(bar graph)*                  |
| 3      | Start study timer                              |
| 4      | View speed graph                               |
| 5      | View weak points                               |
| 6      | Enter test details                             |
| 7      | View test detail graph *(line graph)*          |
| 8      | View pie chart *(analysis)*                    |
| 9      | Exit                                           |

---

## Author

**Sifat Kaur Kochar**