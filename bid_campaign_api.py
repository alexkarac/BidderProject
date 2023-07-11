from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Campaign(db.Model):           # Campaign class. It is built only for the db creation to work with some examples
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    ad_creative = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"{self.name} - {self.price} - {self.ad_creative}"

class TargetedCountries(db.Model):  # TargetedCountries class. It is built only for the db creation, to work with some examples. There is not an appropriate connection with the Campaign(like foreign key)
    id = db.Column(db.Integer, primary_key=True)
    isoCode = db.Column(db.String(3), nullable=False)
    campaign_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"{self.isoCode} - {self.campaign_id}"
    
class TargetedLocations(db.Model):  # TargetedLocations class. It is built only for the db creation, to work with some examples. There is not an appropriate connection (like foreign key)
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longtitude = db.Column(db.Float, nullable=False)
    campaign_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"{self.latitude} - {self.longtitude} - {self.campaign_id}"

class Bid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mAppID = db.Column(db.Integer, nullable=False)
    mAppName = db.Column(db.String(15), nullable=False)
    mDevID = db.Column(db.Integer, nullable=False)
    mDevLat = db.Column(db.Float, nullable=True)
    mDevLong = db.Column(db.Float, nullable=True)
    mDevCountry = db.Column(db.String(3), nullable=False)
    mDevSoft = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"{self.id} - {self.mAppID} - {self.mAppName} - {self.mDevID} - {self.mDevLat} - {self.mDevLong} - {self.mDevCountry} - {self.mDevSoft}"


@app.route('/campaigns')            # Retrieve all campaigns
def get_campaigns():
    campaigns = Campaign.query.all()
    output = []
    for campaign in campaigns:
        campaign_data = {'name': campaign.name, 
                        'price': campaign.price, 
                        'ad_creative': campaign.ad_creative,
                        'countries': get_countries(campaign.id),
                        'locations': get_locations(campaign.id)
                         }
        output.append(campaign_data)

    return output

@app.route('/campaigns/<id>')       # Search Campaign by id
def get_campaign(id):
    campaign = Campaign.query.get_or_404(id)
    return jsonify({"name":campaign.name,
                    "price":campaign.price,
                    "ad_creative": campaign.ad_creative,
                    "countries": get_countries(campaign.id),
                    "locations": get_locations(campaign.id)})

# @app.route('/countries/<id>')     # Search Country by ths campaign id NOT the country id
def get_countries(id):
    countries = TargetedCountries.query.all()
    output = []
    for country in countries:
        if(country.campaign_id == int(id)):
            country_data = {"isoCode":country.isoCode,
                    "campaign_id":country.campaign_id}
            output.append(country_data)
    return output

# @app.route('/locations/<id>')     # Search Locations by ths campaign id NOT the locations id
def get_locations(id):
    locations = TargetedLocations.query.all()
    output = []
    for location in locations:
        if(location.campaign_id == int(id)):
            location_data = {"latitude":location.latitude,
                         "longtitude":location.longtitude,
                        "campaign_id":location.campaign_id}
            output.append(location_data)
    return output

#@app.route('/bid')
def get_bid():
    bid = Bid.query.get_or_404(1)
    return jsonify({"id":bid.id,
                    "mAppID":bid.mAppID,
                    "mAppName": bid.mAppName,
                    "mDevID": bid.mDevID,
                    "mDevLat": bid.mDevLat,
                    "mDevLong": bid.mDevLong,
                    "mDevCountry": bid.mDevCountry,
                    "mDevSoft": bid.mDevSoft})

@app.route('/bid_resp', methods=['POST'])
def post_bid():
    bid_response = {
        'bid_id': 1,
        'campaign_id': 5,
        'price': 20,
        'ad_creative': '<script>..3..</script>'
    }

    return jsonify(bid_response)




if __name__ == '__main__':
    app.run()