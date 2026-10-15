# StudySync (AI110 Tinker Starter)

Starter code for the AI110 **Tinker 1B / 2B / 3B** in-class activities. All three tinkers
build on this one project, each working in a different module.

| Tinker | Focus | Files you'll work in |
|---|---|---|
| 1B, Split the Logic | Writing your first `pytest` test, then a cross-file refactor | `scoring.py`, `scoring_helpers.py`, `test_scoring.py` |
| 2B, Wire It Up | Streamlit `session_state`, input validation, dataclasses, recurring dates | `sessions.py`, `app.py` |
| 3B, Rank & Explain | CSV loading, weighted scoring that returns reasons, ranking, a data-flow diagram | `ranking.py`, `data/study_spots.csv`, `diagram.mmd` |

## Setup

Fork this repo, then clone **your fork**:

```bash
git clone https://github.com/<YOUR-GITHUB-USERNAME>/ai110-tinker-studysync-starter.git
cd ai110-tinker-studysync-starter
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
```

macOS, Linux, Git Bash or WSL:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies and run:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m streamlit run app.py
```

Run the tests:

```bash
pytest
```

## Files

- `app.py` — Streamlit entry point, wires the three tabs together
- `scoring.py` — `session_rating()` and the Session Scorer tab
- `scoring_helpers.py` — helpers extracted during Tinker 1B
- `sessions.py` — session log, the Tinker 2B surface
- `ranking.py` — study-spot ranking, the Tinker 3B surface
- `data/study_spots.csv` — sample data for ranking
- `diagram.mmd` — Mermaid data-flow diagram, completed in Tinker 3B
- `test_scoring.py` — starting point for your own tests

Your instructor will tell you which tinker you're on. Follow the activity on the course portal.

## Week 2 Reflection

I moved apply_streak_bonus from scoring.py to scoring_helpers.py and added the import so scoring.py could still use it. The demo output stayed the same, and both tests passed.

One AI suggestion I accepted was testing a score of 80 to make sure it returned “Good.” I ran the test and confirmed it passed. Testing before moving the function helped me check that I hadn’t changed the behavior. I didn’t have an AI suggestion that I needed to fix or reject.

My breaker inputs were -10, 110, and 87.5. They returned “Skip,” “Great,” and “Good.” The 110 result stood out because the rating function accepts scores above 100. I left it unchanged because apply_streak_bonus caps scores at 100 in the normal app flow. I flagged negative scores as out of scope and kept the decimal behavior because it worked with the existing rating ranges.