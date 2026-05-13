import os
import sys

sys.path.append(os.path.abspath("src"))

from priority_scorer import calculate_priority


def test_high_priority_email():
    email = {
        "subject": "Urgent payment required",
        "snippet": "Please confirm immediately."
    }

    assert calculate_priority(email) == "High"


def test_medium_priority_email():
    email = {
        "subject": "Project meeting reminder",
        "snippet": "Please check the schedule."
    }

    assert calculate_priority(email) == "Medium"


def test_low_priority_email():
    email = {
        "subject": "Weekend discount",
        "snippet": "Sale on selected items."
    }

    assert calculate_priority(email) == "Low"