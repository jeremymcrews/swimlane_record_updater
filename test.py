from swimlane import Swimlane
from swimlane.core.search import EQ, NOT_EQ, CONTAINS, EXCLUDES, GT, GTE, LT, LTE
import os


class Setup:
    def __init__(self, sw_config, sw_inputs):
        for k, v in sw_inputs.iteritems():
            setattr(self, k, v)
        for k, v in sw_config.iteritems():
            setattr(self, k, v)


class Records(Setup):
    def __init__(self, sw_config, sw_inputs):
        Setup.__init__(self, sw_config, sw_inputs)
        self.swimlane = Swimlane(self.host, self.apiUser, self.apiKey, verify_ssl=False)
        self.app = None
        self.appRaw = None
        self.records = None
        self.report = None

    def getApp(self, appId):
        self.app = self.swimlane.apps.get(id=appId)

    def getAppRaw(self, appId):
        self.app = self.swimlane.apps.get(id=appId)
        self.appRaw = self.app._raw

    def getRecord(self, appId, recordId):
        self.getApp(appId)
        self.records = self.app.records.get(id=recordId)

    def getReport(self, appId, reportName, filters=None, limit=50):
        self.getApp(appId)
        self.report = self.app.reports.build(reportName, limit=limit)
        if filters is not None:
            for f in filters:
                self.report.filter(f[0], f[1], f[2])

    def pullFieldsFromRecords(self, appId, recordId, fields=None):
        self.getRecord(appId, recordId)
        if fields is not None:
            oldRecords = self.records
            newRecords = {}
            for r in oldRecords:
                for f in fields:
                    if f in r:
                        newRecords[f] = oldRecords[f]
            return newRecords
        else:
            return self.records


'''
swimlane = Swimlane(self.swimlaneHost, self.swimlaneUser, self.swimlanePass, verify_ssl=verifySsl)
app = swimlane.apps.get(id=id)
report = app.reports.build('test')
report.filter(+)
recordUpdater.getAppRaw('aP0pSxO_qFQhNWteI')
recordUpdater.getRecord('aP0pSxO_qFQhNWteI', 'aD5sJ1KDR50xNAOak')
filters = [('CS: Client Name', EQ, 'Avolve Software'), ('CS: Case Status', NOT_EQ, 'Closed')]
recordUpdater.getReport('aP0pSxO_qFQhNWteI', 'Test Report', filters, limit=0)
'''
os.environ['HTTPS_PROXY'] = 'http://10.111.64.98:3128'
config = {u'RecordId': u'aJxK5KVcnOfjiJPyI', u'ApplicationId': u'aP0pSxO_qFQhNWteI', u'SwimlaneUrl': u'https://swimlane.pss.phoenixnap-internal.com/'}
inputs = {u'host': u'https://phx0-psspsl01.pss.phoenixnap-internal.com/', u'apiKey': u'900576f8b34557d7193170a2835b28a9ac5d397c3bdaf6e389f4d59830e90826', u'apiUser': u'internalapiuser'}
recordUpdater = Records(config, inputs)
fields = ['Tracking Id', 'CS: Client Name']
recordUpdater.pullFieldsFromRecords(recordUpdater.ApplicationId, recordUpdater.RecordId, fields=fields)
sw_outputs = {'ApplicationId': recordUpdater.ApplicationId, 'RecordId': recordUpdater.RecordId, 'TrackingId': recordUpdater.records['Tracking Id']}
print sw_outputs

