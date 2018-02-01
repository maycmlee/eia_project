import ConfigParser
import requests
import dateutil.parser as dp

config = ConfigParser.RawConfigParser()
config.read('config.cfg')

api_key=str(config.get('EIA', 'api_key'))
url = 'http://api.eia.gov/series/?api_key=%s&series_id=EBA.NYIS-ALL.D.H' % api_key
r = requests.get(url=url, )
print(r)
ny_hourly_demand_data = r.json()
print(ny_hourly_demand_data['series'][0]['data'][0])


# t = '1984-06-02T19:05:00.000Z'
t='20180127T00Z'
parsed_t = dp.parse(t)
t_in_seconds = parsed_t.strftime('%s')
print(t_in_seconds)
# '455047500'
