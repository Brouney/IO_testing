import unittest
import requests

class testDEBUG(unittest.TestCase):
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
        tmp = True
        for t in r.json():
            if t["id"] == 2:
                tmp = False
                break;
        self.assertEqual(tmp,True)

    def testStatusCodeGetPhase(self):
        r = requests.get('http://77.55.192.26:2137/debug/phase')
        self.assertEqual(r.status_code,200)


    def testGetPhase(self):
        r = requests.get('http://77.55.192.26:2137/debug/phase')
        tmp = True
        for t in r.json():
            if t["id"] == 1:
                tmp = False
                break;
        self.assertEqual(tmp,True)

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

if __name__ == '__main__':
    
    unittest.main()