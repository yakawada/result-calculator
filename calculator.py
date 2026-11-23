import csv

def grade(score):
    if score >= 70: return "A"
    if score >= 60: return "B"
    if score >= 50: return "C"
    if score >= 45: return "D"
    if score >= 40: return "E"
    return "F"

def load_scores(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))

def compute_results(rows, subjects):
    results = []
    for row in rows:
        scores = [float(row[s]) for s in subjects]
        total = sum(scores)
        results.append({"name": row["name"], "total": total,
                        "average": round(total / len(scores), 1),
                        "grade": grade(total / len(scores))})
    results.sort(key=lambda r: r["total"], reverse=True)
    for i, r in enumerate(results):
        # students with the same total share a position
        if i > 0 and r["total"] == results[i - 1]["total"]:
            r["position"] = results[i - 1]["position"]
        else:
            r["position"] = i + 1
    return results

if __name__ == "__main__":
    rows = load_scores("sample_scores.csv")
    for r in compute_results(rows, ["maths", "english", "ict"]):
        print(f'{r["position"]}. {r["name"]}: {r["total"]} ({r["average"]}, {r["grade"]})')
