import json

import requests

from myapp.api import APP_API
from myapp.datadeal.dataDeal import DataInit

contents = DataInit.SportInit().team_col.find_one()['result']['2']
print(contents)

