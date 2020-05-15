import unittest
import requests

class testPUT(unittest.TestCase):
    def testPutTournament(self):
        load = {'start_date': '01-01-2020', 'name': 'tournament1', 'city': 'krakow', 'location': 'ulica Pokątna'}
        r = requests.put('http://77.55.192.26:2137/api/tournament', data = load)
        r = requests.get('http://77.55.192.26:2137/api/tournament')
        self.assertEqual(r.status_code,200)



if __name__ == '__main__':
    
    unittest.main()