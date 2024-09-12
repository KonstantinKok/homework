import runner_and_tournament
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Запускаем тест")
    def test_walk(self):
        ocr = runner_and_tournament.Runner("Олег")
        for _ in range(10):
            ocr.walk()
        self.assertEqual(ocr.distance, 50)

    @unittest.skipIf(is_frozen, "Запускаем тест")
    def test_run(self):
        ocr = runner_and_tournament.Runner("Олег")
        for _ in range(10):
            ocr.run()
        self.assertEqual(ocr.distance, 100)

    @unittest.skipIf(is_frozen, "Запускаем тест")
    def test_challenge(self):
        Elena = runner_and_tournament.Runner("Елена")
        Tat = runner_and_tournament.Runner("Татьяна")
        for _ in range(10):
            Elena.walk()
            Tat.run()
        self.assertNotEqual(Elena.distance, Tat.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        all_results = {}

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self):
        self.Us = runner_and_tournament.Runner("Усэйн", 10)
        self.Andr = runner_and_tournament.Runner("Андрей", 9)
        self.Nik = runner_and_tournament.Runner("Ник", 3)


    @classmethod
    def tearDownClass(cls):
        print("Да")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        us_andr_nik = runner_and_tournament.Tournament(90, self.Us, self.Andr, self.Nik)
        us_andr_nik.start()
        if self.assertTrue(True):
            print("Андрей")
        else:
            print("Ник")

if __name__ == "__main":
    unittest.main()