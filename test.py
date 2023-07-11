from bidder_service import BidderService

bidder_service = BidderService()

# Check the bid request
bid_request = bidder_service.get_bid_request()
print('----------Bid Request----------')
print(bid_request)
print()

# Check all the campaigns
available_campaigns = bidder_service.get_available_campaigns()
print('----------All the Available Campaigns----------')
for campaign in available_campaigns:
    print(campaign)
    print()
print()

# Check the filtered campaigns based on country and coordinates
filtered_campaigns = bidder_service.filtered_campaigns(bid_request, available_campaigns)
print('----------Filtered Campaigns----------')
for campaign in filtered_campaigns:
    print(campaign)
    print()
print()    

# Check the most profitable campaign
max_profit_campaign = bidder_service.find_max_profit_campaign(filtered_campaigns)
print('----------Max Profitable Camapign----------')
print(max_profit_campaign)
print()

# Check the final bid response
bid_response = bidder_service.submit_bid_response(bid_request["id"], max_profit_campaign)
print('----------Bid Respponse----------')
print(bid_response)