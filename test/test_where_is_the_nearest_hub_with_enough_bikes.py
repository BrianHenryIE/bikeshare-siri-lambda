import unittest
import json
from where_is_the_nearest_bikeshare_bike.where_is_the_nearest_bikeshare_bike import where_is_the_nearest_hub_with_enough_bikes


class NearestHubTests(unittest.TestCase):

    def test_where_is_the_nearest_hub_with_enough_bikes_only_possible(self):

        with open('data/station_status.json', 'r') as f:
            station_status = json.load(f)['data']['stations']

        with open('data/station_information.json', 'r') as f:
            station_information = json.load(f)['data']['stations']

        city_park_gps = {
            "longitude": -121.49305556,
            "latitude": 38.58638889
        }

        number_of_bikes = 50

        expected = {"station_id": "hub_4487", "name": "Westacre Rd & Portsmouth Ct", "region_id": "region_450",
                    "lon": -121.53169512748718, "lat": 38.585789931124765,
                    "address": "9 Westacre Road, West Sacramento",
                    "rental_methods":["KEY", "APPLEPAY", "ANDROIDPAY", "TRANSITCARD", "ACCOUNTNUMBER", "PHONE"]}

        expected = "The nearest dock with 50 bikes is Westacre Rd & Portsmouth Ct, 3360 m west."

        actual = where_is_the_nearest_hub_with_enough_bikes(station_status, station_information, city_park_gps, number_of_bikes)

        self.assertEqual(expected, actual['message'])


    def test_where_is_the_nearest_hub_with_enough_bikes_nearest_anyway(self):

        with open('data/station_status.json', 'r') as f:
            station_status = json.load(f)['data']['stations']

        with open('data/station_information.json', 'r') as f:
            station_information = json.load(f)['data']['stations']

        city_park_gps = {
            "longitude": -121.49305556,
            "latitude": 38.58638889
        }

        number_of_bikes = 2

        expected = "The nearest dock with 2 bikes is E St & 9th St, 92 m east."

        actual = where_is_the_nearest_hub_with_enough_bikes(station_status, station_information, city_park_gps, number_of_bikes)

        self.assertEqual(expected, actual['message'])
