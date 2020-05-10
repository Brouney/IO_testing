
import unittest
import requests

class TestDebater(unittest.TestCase):
    def testStatusCode(self):
        r = requests.get('http://77.55.192.26:2137/debug/database')
        self.assertEqual(r.status_code,200)

    def testMessage(self):
        r = requests.get('http://77.55.192.26:2137/debug/database')
        text = [{"message":"Database connection correct!"}]
        self.assertEqual(r.json(),text)


    def testMessageNode(self):
        r = requests.get('http://77.55.192.26:2137/debug/node')
        text = "Node server is working!"
        self.assertEqual(r.text,text)

    def testStatusCodeGetDebate(self):
        r = requests.get('http://77.55.192.26:2137/debug/debate')
        self.assertEqual(r.status_code,200)


    def testGetdebate(self):
        r = requests.get('http://77.55.192.26:2137/debug/debate')
        text = "Sala3"
        
        sala = ""
        for t in r.json():
            if t["id"] == 2:
                sala =  t["location"]
                break;
        self.assertEqual(text,sala)

    def testStatusCodeGetPhase(self):
        r = requests.get('http://77.55.192.26:2137/debug/phase')
        self.assertEqual(r.status_code,200)


    def testGetPhase(self):
        r = requests.get('http://77.55.192.26:2137/debug/phase')
        text = "faza pierwsza"
        name = ""
        for t in r.json():
            if t["id"] == 1:
                name =  t["name"]
                break;
        self.assertEqual(text,name)

    def testStatusCodeGetTable(self):
        r = requests.get('http://77.55.192.26:2137/debug/tables')
        self.assertEqual(r.status_code,200)

    def testGetTable(self):
        r = requests.get('http://77.55.192.26:2137/debug/tables')
        text = "pg_catalog"
        name = ""
        for t in r.json():
            if t["table"] == "pg_authid":
                name =  t["schema"]
                break;
        self.assertEqual(text,name)

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