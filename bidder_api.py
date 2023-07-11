class BidAPI:
    def __init__(self):
        self.bid={  "id": 1,
                    "mAppID": 159,
                    "mAppName": "someApp",
                    "mDevID": 35,
                    "mDevLat": 38.170048,
                    "mDevLong": 21.70132,
                    "mDevCountry": "GR",
                    "mDevSoft": "android"}

    def get_bid(self):
        return self.bid
