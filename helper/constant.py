PATH = 'data/autos.csv'

CHANGE_COLUMN = {"dateCreated": "ad_created",
                 "dateCrawled": "date_crawled",
                 "fuelType": "fuel_type",
                 "lastSeen": "last_seen",
                 "monthOfRegistration": "registration_month",
                 "notRepairedDamage": "unrepaired_damage",
                 "nrOfPictures": "num_of_pictures",
                 "offerType": "offer_type",
                 "postalCode": "postal_code",
                 "powerPS": "power_ps",
                 "vehicleType": "vehicle_type",
                 "yearOfRegistration": "registration_year"}

DATETIME = ["ad_created", "date_crawled", "last_seen"]

DROP_COLUMNS = ["seller", "offer_type", "num_of_pictures", "name", "postal_code"]