from swimlane import Swimlane


class Records:
    def __init__(self, swimlaneUser, swimlanePass, swimlaneHost, verifySsl=False):
        self.swimlaneUser = swimlaneUser
        self.swimlanePass = swimlanePass
        self.swimlaneHost = swimlaneHost
        self.swimlane = swimlane = Swimlane(self.swimlaneHost, self.swimlaneUser, self.swimlanePass, verify_ssl=verifySsl)

    def test(self):
        print self.swimlane
