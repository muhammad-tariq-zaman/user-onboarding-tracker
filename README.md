# user-onboarding-tracker

Show onboarding progress per new hire as a completion percentage, lowest first, so nobody slips through the first-week checklist.

## How to run

```sh
python3 main.py checklist.csv
```

## Example output

```
New Hire B: 25% complete (8 tasks)
New Hire A: 100% complete (8 tasks)
```

Standard library only. Run the tests with `python3 -m unittest discover`.
