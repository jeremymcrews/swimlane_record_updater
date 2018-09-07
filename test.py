from swimlane import Swimlane
from swimlane_records_updater.SruRecords import Records
import os

os.environ['HTTPS_PROXY'] = 'http://10.111.64.98:3128'
recordUpdater = Records('internalapiuser', '900576f8b34557d7193170a2835b28a9ac5d397c3bdaf6e389f4d59830e90826', 'https://phx0-psspsl01.pss.phoenixnap-internal.com')
appData = recordUpdater.getApp('SEV2', 'aP0pSxO_qFQhNWteI')
print recordUpdater.apps['SEV2']

