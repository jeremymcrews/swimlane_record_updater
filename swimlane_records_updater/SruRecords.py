from swimlane import Swimlane


class Records:
    def __init__(self, swimlaneUser, swimlanePass, swimlaneHost, verifySsl=False):
        self.swimlaneUser = swimlaneUser
        self.swimlanePass = swimlanePass
        self.swimlaneHost = swimlaneHost
        self.swimlane = Swimlane(self.swimlaneHost, self.swimlaneUser, self.swimlanePass, verify_ssl=verifySsl)
        self.apps = {}
        self.records = {}

    def test(self):
        print self.swimlane

    def getApp(self, appName, appId):
        self.apps = self.swimlane.apps.get(id=appId)
        return self.apps


    def getRecord(self, appName, appId, recordId):
        self.getApp(self, appName, appId)
        self.records = self.apps[appName].records.get(id=recordId)
        print self.apps