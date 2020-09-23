import json
import requests
headers = {"Authorization": "ya29.a0AfH6SMDgDHdvzqLU8-Q_D7xnvh3DaNZJRBoLnrhUWBvTkrkbrywj_srwbPzq6csku-h0qQ1lFxO4j4G3CSV7EYNsOeNnCbp9db1Xd8XYnwovOSsaTueYS-bwRPrgQdzNw_ygs32eeJ90cb9_bm7QstGuWi5XCHJCBQ0"}
para = {
    "name": "silka.xlsx",
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open("./silka.xlsx", "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)
