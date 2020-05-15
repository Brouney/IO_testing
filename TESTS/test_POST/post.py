import unittest
import requests

class testPUT(unittest.TestCase):
    def testPostTournament(self):
        load = {'start_date':'01-01-2020', 'name': 'tournament1', 'city': 'krakow', 'location': 'ulica Pokątna'}
        r = requests.post('http://77.55.192.26:2137/api/tournament', data = load)
        self.assertEqual(r.status_code,200)


    def testPostAPhaseToATournament(self):
        load = {'name': 'nazwa', 'structure': {}}
        r = requests.post('http://77.55.192.26:2137/api/tournament/3/phase', data = load)
        self.assertEqual(r.status_code,200)

    def testPostDebateToPhase(self):
        load = {'d_time': 'time', 'd_date': 'date', 'location': 'varchar', 'team_1': 1, 'team_2': 2}
        r = requests.post('http://77.55.192.26:2137/api/tournament/3/phase/7/debate',data = load)
        self.assertEqual(r.status_code,200)
if __name__ == '__main__':
    
    unittest.main()