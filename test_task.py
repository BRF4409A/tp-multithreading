import unittest

from numpy.testing import assert_allclose

from task import Task


class TestTask(unittest.TestCase):
    def test_ax_equals_b(self):
        t = Task()
        assert_allclose(t.a @ t.x, t.b)
