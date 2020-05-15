import unittest
import requests

class testGET(unittest.TestCase):
    def testStatusCodeApiTournamentName(self):
        r = requests.get('http://77.55.192.26:2137/api/tournament')
        self.assertEqual(r.status_code,200)

    def testApiTournamentName(self):
        r = requests.get('http://77.55.192.26:2137/api/tournament')
        temp = False
        for t in r.json():
            if t["id"] == 3:
                temp = True
                break;
        self.assertEqual(temp,True)

    def testStatusCodeGetPhaseApiFor1Tournament(self):
        r = requests.get('http://77.55.192.26:2137/api/tournament/3/phase')
        self.assertEqual(r.status_code,200)


    def testGetPhaseApiFor1Tournament(self):
        r = requests.get('http://77.55.192.26:2137/api/tournament/3/phase')
        tmp = False
        for t in r.json():
            if t["id"] == 7:
                tmp = True
                break;
        self.assertEqual(tmp,True)   

    def testStatusCodeGetDebate(self):
        r = requests.get('http://77.55.192.26:2137/api/tournament/3/phase/7/debate')
        self.assertEqual(r.status_code,200)    

    def testGetDebate(self):
        r = requests.get('http://77.55.192.26:2137/api/tournament/3/phase/7/debate')
        checkID = False
        for t in r.json():
            if t["tournament_id"] == 3:
                checkId = True
                break;
        self.assertEqual(checkId,True)



if __name__ == '__main__':
    
    unittest.main()