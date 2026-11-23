# Result Calculator

A small Python tool that turns a CSV of student scores into totals, averages, grades and class positions.

I built it as a simple version of the result-processing module in the school portal I developed for Al-Yaqeen Academy, Kaduna.

## What it does
- Reads student scores from a CSV file
- Calculates each student's total and average
- Gives a grade (A to F) based on the average
- Ranks students by total; students with the same total share a position

## How to run
python calculator.py

## Example output
1. Fatima: 233.0 (77.7, A)
1. Aisha: 233.0 (77.7, A)
3. Musa: 163.0 (54.3, C)
4. Ibrahim: 130.0 (43.3, D)

## Run the tests
pip install pytest
pytest

## Grading scale
| Average | Grade |
|---------|-------|
| 70+     | A     |
| 60–69   | B     |
| 50–59   | C     |
| 45–49   | D     |
| 40–44   | E     |
| Below 40 | F    |
