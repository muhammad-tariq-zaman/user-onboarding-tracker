import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import progress


def row(e, done):
    return {"employee": e, "task": "t", "done": done}


class TestOnboarding(unittest.TestCase):
    def test_percent_computed(self):
        self.assertEqual(progress([row("Ali", "yes"), row("Ali", "no")])[0][1], 0.5)

    def test_lowest_first(self):
        result = progress([row("A", "yes"), row("B", "no")])
        self.assertEqual(result[0][0], "B")

    def test_all_done_is_100(self):
        self.assertEqual(progress([row("A", "yes"), row("A", "yes")])[0][1], 1.0)

    def test_empty(self):
        self.assertEqual(progress([]), [])
