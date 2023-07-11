class CampaignsAPI:
    def __init__(self):             # Instance of campaigns 
        self.campaigns = [
            {
                "id": 1,
                "name": "Campaign 1",
                "price": 10,
                "ad_creative": "<script>...1...</script>",
                "targetedCountries": ["GR", "FR"],
                "targetedLocations": [
                    {"latitude": 39.170048, "longitude": 21.70132},
                    {"latitude": 38.161123, "longitude": 22.728346}
                ]
            },
            {
                "id": 2,
                "name": "Campaign 2",
                "price": 20,
                "ad_creative": "<script>...2...</script>",
                "targetedCountries": ["GR", "IT"],
                "targetedLocations": [
                    {"latitude": 38.161123, "longitude": 21.728346}
                ]
            },
            {
                "id": 3,
                "name": "Campaign 3",
                "price": 20,
                "ad_creative": "<script>...3...</script>",
                "targetedCountries": ["GR"],
                "targetedLocations": [
                    {"latitude": 38.174079, "longitude": 21.746211},
                    {"latitude": 38.154789, "longitude": 21.325689}
                ]
            }
        ]

    def get_campaigns(self):            # Retrieve all available campaigns
        return self.campaigns