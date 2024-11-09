import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def __str__(self):
        return self.name

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
                    break
        return finishers

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print({place: runner.name for place, runner in result.items()})

    def test_race_runner1_and_runner3(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()

        self.all_results.append(results)
        self.assertTrue(results[1] == self.runner1)
        self.assertTrue(results[2] == self.runner3)

    def test_race_runner2_and_runner3(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()

        self.all_results.append(results)
        self.assertTrue(results[1] == self.runner2)
        self.assertTrue(results[2] == self.runner3)

    def test_race_runner1_runner2_and_runner3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()

        self.all_results.append(results)
        self.assertTrue(results[1] in [self.runner1, self.runner2])
        self.assertTrue(results[2] in [self.runner1, self.runner2])
        self.assertTrue(results[3] == self.runner3)

if __name__ == '__main__':
    unittest.main()