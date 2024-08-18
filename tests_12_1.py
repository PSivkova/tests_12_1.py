import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner_1 = Runner('Den')
        for i in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    def test_run(self):
        runner_1 = Runner('Den')
        for i in range(10):
            runner_1.run()
        self.assertEqual(runner_1.distance, 100)

    def test_challenge(self):
        runner_1 = Runner('Den')
        runner_2 = Runner('Max')
        for i in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


if __name__ == "__main__":
    unittest.main()

