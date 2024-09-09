import unittest
from runner import Runner


class TestRunner(unittest.TestCase):
    def test_walk(self):
        runner = Runner("Бегун №1")
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("Бегун №2")
        for j in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner("Бегун №3")
        runner2 = Runner("Бегун №4")
        for q in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()