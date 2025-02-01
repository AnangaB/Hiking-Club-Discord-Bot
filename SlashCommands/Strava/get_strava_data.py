from dotenv import load_dotenv
import requests
import os
from datetime import datetime

#get the refresh_tokem to use Strava's api, but this is just a onetime thing, so isn't invoked elsewhere and its result is already stored 
def get_refresh_token(code):
  # Load environment variables
    load_dotenv()
    
    url = "https://www.strava.com/api/v3/oauth/token"
    data = {
        "client_id": os.getenv('STRAVA_CLIENT_ID'),
        "client_secret": os.getenv('STRAVA_CLIENT_SECRET'),
        "grant_type": "authorization_code",
        "code": code,
        "scope":"activity:read"
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print("get_refresh_token(): Error")
        return None

def get_authorization_code():
    # Load environment variables
    load_dotenv()
    
    url = "https://www.strava.com/api/v3/oauth/token"
    data = {
        "client_id": os.getenv('STRAVA_CLIENT_ID'),
        "client_secret": os.getenv('STRAVA_CLIENT_SECRET'),
        "grant_type": "refresh_token",
        "refresh_token": os.getenv('STRAVA_REFRESH_TOKEN'),
        "scope":"activity:read"
    }
    current_time = datetime.now().timestamp()
    #use already stored access_token, if access_token does not need to be refreshed
    if current_time < int(os.getenv("STRAVA_ACCESS_EXPIRY_TIME")):
        return os.getenv("STRAVA_ACCESS_TOKEN")
    #get fresh access_token and new expiry code
    else:
        try:
            response = requests.post(url, data=data)

            if response.status_code == 200:
                response_json = response.json()
                access_token = response_json.get("access_token")
                expires_at = response_json.get("expires_at")
                os.environ["STRAVA_ACCESS_TOKEN"]= str(access_token)
                os.environ["STRAVA_ACCESS_EXPIRY_TIME"] = str(expires_at)
                return access_token
            else:
                print(f"get_authorization_code():  Error getting access_token from Strava_API.Response.status_code:{response.status_code}")
                return None 
        except:
            print("get_authorization_code(): Error getting access_token from Strava_API.")
            return None    

        
# returns a str about the most recent strava activity
# SFU Hikers strava only has hikes, so no need to filter thru activities further
def get_most_recent_activity():
    code = get_authorization_code()
    if  code != None:
        url = "https://www.strava.com/api/v3/athlete/activities"

        headers = {
            "Authorization": f"Bearer {code}"
        }
        try:
            hike = requests.get(url,headers=headers).json()[0]
            if hike:
                date = datetime.strptime(hike["start_date_local"], '%Y-%m-%dT%H:%M:%SZ').date()
                hike_info = f"**{hike['name']}**\nHike Distance: {int(hike['distance'])/1000} km\nElevation: {hike['total_elevation_gain']} m\nDate: {date}"
                return hike_info
            
        except:
            return None
    
    return None
    
# returns a str about the last 10 most recent strava activity
# SFU Hikers strava only has hikes, so no need to filter thru activities further
def get_last_10_hikes():
    code = get_authorization_code()
    if  code != None:
        url = "https://www.strava.com/api/v3/athlete/activities"

        headers = {
            "Authorization": f"Bearer {code}"
        }
        data = {"perPage":9} 
        try:
            hikes = requests.get(url,params=data,headers=headers)

            if hikes.status_code == 200:
                hike_list = hikes.json()
                if hike_list:
                    result_list = []
                    for hike in hike_list:
                        date = datetime.strptime(hike["start_date_local"], '%Y-%m-%dT%H:%M:%SZ').date()
                        hike_info = f"**{hike['name']}**\nHike Distance: {int(hike['distance'])/1000} km\nElevation: {hike['total_elevation_gain']} m\nDate: {date}"

                        result_list.append(hike_info + "\n \n")
                    return result_list
            
        except:
            print("get_last_10_hikes(): Error getting data of last 10 hikes from strava.")
            return None
    return None


