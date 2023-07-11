from bidder_api import BidAPI
from campaigns_api import CampaignsAPI

class BidderService:
    def __init__(self):
        self.bid_api = BidAPI()
        self.campaigns_api = CampaignsAPI()

    def get_bid_request(self):
        bid_request = self.bid_api.get_bid()
        return bid_request
    
    def get_available_campaigns(self):
        available_campaigns = self.campaigns_api.get_campaigns()
        return available_campaigns
    
    def filtered_campaigns(self, bid_request, available_campaigns):
        campaigns = []
        for campaign in available_campaigns:
            if bid_request["mDevCountry"] in campaign["targetedCountries"]:
                for location in campaign["targetedLocations"]:
                    if (location["latitude"] - 0.1 <= bid_request["mDevLat"] <= location["latitude"] + 0.1 and
                            location["longitude"] -0.1 <= bid_request["mDevLong"] <= location["longitude"] + 0.1):
                        campaigns.append(campaign)
                        break
        return campaigns
    
    def find_max_profit_campaign(self, filtered_campaigns):
        if not filtered_campaigns:
            return None
        
        max_profit_campaign = None
        max_profit = 0
        for campaign in filtered_campaigns:
            if campaign["price"] > max_profit:
                max_profit_campaign = campaign
                max_profit = campaign["price"]
        return max_profit_campaign
    
    def submit_bid_response(self, bid_id, campaign):
        if not campaign:
            bid_response = {
            "bid_id": bid_id,
            "campaign_id": None,
            "price": None,
            "ad_creative": None
            }
        else:
            bid_response = {
            "bid_id": bid_id,
            "campaign_id": campaign["id"],
            "price": campaign["price"],
            "ad_creative": campaign["ad_creative"]
            }
            
        return bid_response
    
    