import unittest

import boatd

class MockDriver(object):
    def __init__(self):
        self.handlers = {
            'heading': lambda: 2.43,
            'pony': lambda: 'magic'
        }

class TestBoat(unittest.TestCase):
    def setUp(self):
        self.boat = boatd.Boat(MockDriver())

    def test_get_heading(self):
        assert self.boat.heading() == 2.43

    def test_get_pony(self):
        assert self.boat.pony() == 'magic'

    def test_active(self):
        assert not self.boat.active
