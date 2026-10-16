"""
A tiny gradebook for a class.

Each student has a list of exam scores (numbers from 0 to 100).
This file has 4 bugs. The tests in test_gradebook.py will help you find them.
"""


def average(scores):
    """Return the average of a list of scores.

    An empty list has an average of 0.0.
    """
    total = 0
    for s in scores:
        total += s
    return total / (len(scores) - 1)


def letter_grade(avg):
    """Turn an average into a letter grade.

    90 and above -> "A"
    80 to 89.99  -> "B"
    70 to 79.99  -> "C"
    60 to 69.99  -> "D"
    below 60     -> "F"
    """
    if avg > 90:
        return "A"
    elif avg > 80:
        return "B"
    elif avg > 70:
        return "C"
    elif avg > 60:
        return "D"
    else:
        return "F"


def drop_lowest(scores):
    """Return a NEW list with the single lowest score removed.

    The original list must not change.
    A list with 0 or 1 scores is returned as an empty list.
    """
    if len(scores) <= 1:
        return []
    scores.remove(min(scores))
    return scores


def class_report(gradebook):
    """Build a report for the whole class.

    gradebook is a dict like {"Ana": [90, 85], "Ben": [70, 65, 80]}.
    Each student's lowest score is dropped before averaging.

    Returns a dict like {"Ana": ("A", 90.0), ...} mapping each student to
    (letter grade, average after dropping the lowest score).
    """
    report = {}
    for name, scores in gradebook.items():
        kept = drop_lowest(scores)
        avg = average(kept)
        report[name] = (letter_grade(avg), avg)
    return report


if __name__ == "__main__":
    my_class = {
        "Ana": [88, 92, 95],
        "Ben": [70, 65, 80, 75],
        "Cleo": [100],
    }
    for student, (grade, avg) in class_report(my_class).items():
        print(f"{student:6} {grade}  ({avg:.1f})")
