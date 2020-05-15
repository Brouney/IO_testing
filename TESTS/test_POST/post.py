import unittest
import requests

class testPUT(unittest.TestCase):
    def testPostTournament(self):
        load = {'start_date':'01-01-2020', 'name': 'tournament1', 'city': 'krakow', 'location': 'ulica Pokątna'}
        r = requests.post('http://77.55.192.26:2137/api/tournament', json = load)
        self.assertEqual(r.status_code,200)


    def testPostAPhaseToATournament(self):
        load = {'name': 'nazwa', 'structure': {}}
        r = requests.post('http://77.55.192.26:2137/api/tournament/3/phase', json = load)
        self.assertEqual(r.status_code,200)

    def testPostDebateToPhase(self):
        load = {'d_time': '23:00:00.000', 'd_date': '2022-03-03', 'location': 'pod cerkwia'}
        r = requests.post('http://77.55.192.26:2137/api/tournament/3/phase/8/debate',json = load)
        self.assertEqual(r.status_code,200)
if __name__ == '__main__':
    
    unittest.main()