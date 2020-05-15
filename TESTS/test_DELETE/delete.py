import unittest
import requests


class testDELETE(unittest.TestCase):
    def testDeleteTournament(self):
        load = {'start_date': '01-01-2020', 'name': 'tournament1',
                'city': 'krakow', 'location': 'ulica Pokątna'}
        l = requests.post('http://77.55.192.26:2137/api/tournament', data=load)
        id_tournament = l.json()["id"]
        tmp = 'http://77.55.192.26:2137/api/tournament/'+str(id_tournament)
        r = requests.delete(tmp)
        self.assertEqual(r.status_code, 200)

    def testDeletePhase(self):
        load = {'start_date': '01-01-2020', 'name': 'tournament1',
                'city': 'krakow', 'location': 'ulica Pokątna'}
        l = requests.post('http://77.55.192.26:2137/api/tournament', data=load)
        id_tournament = l.json()["id"]

        load2 = {'name': 'nazwa', 'structure': {}}
        string = 'http://77.55.192.26:2137/api/tournament/' + str(id_tournament) +'/phase'
        ll = requests.post(string, data = load2)
        id_phase = ll.json()["id"]

        strToDelete = 'http://77.55.192.26:2137/api/tournament/'+ str(id_tournament) +'/phase/+'+str(id_phase)
        r = requests.delete(strToDelete)
        self.assertEqual(r.status_code, 200)

    def testDeleteDebate(self):
        load = {'start_date': '01-01-2020', 'name': 'tournament1',
                'city': 'krakow', 'location': 'ulica Pokątna'}
        l = requests.post('http://77.55.192.26:2137/api/tournament', data=load)
        id_tournament = l.json()["id"]

        load2 = {'name': 'nazwa', 'structure': {}}
        string = 'http://77.55.192.26:2137/api/tournament/' + str(id_tournament) +'/phase'
        ll = requests.post(string, data = load2)
        id_phase = ll.json()["id"]

        load = {'d_time': 'time', 'd_date': 'date', 'location': 'varchar', 'team_1': 1, 'team_2': 2}
        string2 = 'http://77.55.192.26:2137/api/tournament/'+ str(id_tournament) +'/phase/+'+str(id_phase)+'/debate'
        lll = requests.post(string2,data = load)
        id_debate = lll.json()["id"]

        strToDelete = 'http://77.55.192.26:2137/api/tournament/'+ str(id_tournament) +'/phase/+'+str(id_phase)+'/debate/'+str(id_debate)
        r = requests.delete(strToDelete)

        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':

    unittest.main()
