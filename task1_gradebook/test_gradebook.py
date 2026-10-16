"""
Tests for gradebook.py. Run from the workshop folder:

    python task1_gradebook/test_gradebook.py

You do not need to change this file. When every test says PASS, you are done.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gradebook import average, letter_grade, drop_lowest, class_report


def test_average_simple():
    assert average([80, 90, 100]) == 90.0, "average of 80, 90, 100 should be 90.0"


def test_average_one_score():
    assert average([75]) == 75.0, "average of [75] should be 75.0"


def test_average_empty():
    assert average([]) == 0.0, "average of an empty list should be 0.0"


def test_letter_grade_middle():
    assert letter_grade(95) == "A"
    assert letter_grade(85) == "B"
    assert letter_grade(50) == "F"


def test_letter_grade_exact_boundaries():
    assert letter_grade(90) == "A", "exactly 90 should be an A"
    assert letter_grade(80) == "B", "exactly 80 should be a B"
    assert letter_grade(70) == "C", "exactly 70 should be a C"
    assert letter_grade(60) == "D", "exactly 60 should be a D"


def test_drop_lowest_result():
    assert drop_lowest([70, 90, 80]) == [90, 80]


def test_drop_lowest_does_not_change_original():
    original = [70, 90, 80]
    drop_lowest(original)
    assert original == [70, 90, 80], "drop_lowest changed the list it was given"


def test_class_report():
    book = {"Ana": [88, 92, 95], "Cleo": [100]}
    report = class_report(book)
    assert report["Ana"] == ("A", 93.5), f"Ana got {report['Ana']}"
    assert report["Cleo"] == ("F", 0.0), f"Cleo got {report['Cleo']}"


def test_class_report_keeps_data():
    book = {"Ana": [88, 92, 95]}
    class_report(book)
    assert book["Ana"] == [88, 92, 95], "class_report changed the gradebook"


# ---------------------------------------------------------------------------
# Simple test runner (no extra packages needed)
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    tests = [(n, f) for n, f in list(globals().items()) if n.startswith("test_")]
    passed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"PASS  {name}")
            passed += 1
        except AssertionError as e:
            print(f"FAIL  {name}: {e}")
        except Exception as e:
            print(f"ERROR {name}: {type(e).__name__}: {e}")
    print(f"\n{passed}/{len(tests)} tests passed")
    if passed == len(tests):
        print("All tests pass. Nice work!")
