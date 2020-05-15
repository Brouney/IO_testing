import unittest
import requests

class testGET(unittest.TestCase):
    def testStatusCodeApiTournamentName(self):
        r = requests.get('http://77.55.192.26:2137/api/tournament')
        self.assertEqual(r.status_code,200)

    def testApiTournamentName(self):
        r = requests.get('http://77.55.192.26:2137/api/tournament')
        text = "TRBO DEBATA"
        name = ""
        for t in r.json():
            if t["id"] == 1:
                name =  t["name"]
                break;
        self.assertEqual(text,name)

    def testStatusCodeGetPhaseApiFor1Tournament(self):
        r = requests.get('http://77.55.192.26:2137/api/tournament/1/phase')
        self.assertEqual(r.status_code,200)


    def testGetPhaseApiFor1Tournament(self):
        r = requests.get('http://77.55.192.26:2137/api/tournament/1/phase')
        text = "faza pierwsza"
        name = ""
        for t in r.json():
            if t["id"] == 1:
                name =  t["name"]
                break;
        self.assertEqual(text,name)   

    def testStatusCodeGetDebate(self):
        r = requests.get('http://77.55.192.26:2137/api/tournament/1/phase/1/debate')
        self.assertEqual(r.status_code,200)    

    def testGetDebate(self):
        r = requests.get('http://77.55.192.26:2137/api/tournament/1/phase/1/debate')
        text = "Sala3"
        
        sala = ""
        for t in r.json():
            if t["id"] == 2:
                sala =  t["location"]
                break;
        self.assertEqual(text,sala)



if __name__ == '__main__':
    
    unittest.main()