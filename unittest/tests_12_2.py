from runner_and_tournament import Runner
from runner_and_tournament import Tournament
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global all_results
        all_results = {}

    def setUp(self):
        self.Usein = Runner("Усэйн", 10)
        self.Andrei = Runner("Андрей", 9)
        self.Nik = Runner("Ник", 3)


    @classmethod
    def tearDownClass(cls):
        for key, value in all_results.items():
            print(value)


    def test_run_an(self):
        andrei_nik = Tournament(90, self.Andrei, self.Nik)
        results = andrei_nik.start()

        zabeg = ""
        for key, value in results.items():
            zabeg += str(key) + ": " + str(value) + " "
        all_results["1"] = zabeg

        self.assertTrue(results[2] == "Ник", "Неверное имя последнего бегуна в забеге 1")


    def test_run_un(self):
       usein_nik = Tournament(90, self.Usein, self.Nik)
       results = usein_nik.start()

       zabeg = ""
       for key, value in results.items():
           zabeg += str(key) + ": " + str(value) + " "
       all_results["2"] = zabeg

       self.assertTrue(results[2] == "Ник", "Неверное имя последнего бегуна в забеге 2")


    def test_run_uan(self):
        us_andrei_nik = Tournament(90, self.Usein, self.Andrei, self.Nik)
        results = us_andrei_nik.start()

        zabeg = ""
        for key, value in results.items():
            zabeg += str(key) + ": " + str(value) + " "
        all_results["3"] = zabeg

        self.assertTrue(results[3] == "Ник", "Неверное имя последнего бегуна в забеге 3")


if __name__ == "__main__":
    unittest.main()