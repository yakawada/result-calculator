from calculator import grade, compute_results

def test_grade_boundaries():
    assert grade(70) == "A"
    assert grade(69.9) == "B"
    assert grade(39) == "F"

def test_positions_and_ties():
    rows = [{"name": "A", "x": "50"}, {"name": "B", "x": "80"}, {"name": "C", "x": "80"}]
    res = compute_results(rows, ["x"])
    assert [r["position"] for r in res] == [1, 1, 3]
