import json
import requests
from config import API_URL, TOKEN, MY_CLUB_ID, logger
from utils import send_sms

def notify(event, context):
    logger.info("Starting...")
    response = requests.get(API_URL, headers={"Authorization": "Bearer " + TOKEN})
    logger.info("Response: %s", response.text)
    parsed_response = json.loads(response.text)
    nr_of_people = list(filter(lambda x: x["clubId"] == MY_CLUB_ID, parsed_response["data"]))[0]["count"]
    logger.info("Nr of people: %s", nr_of_people)

    if nr_of_people >= 0 and nr_of_people <= 20:
        logger.info("Sending SMS...")
        send_sms("+37257839690", "There are %s people in the gym. Let's go!!!" % nr_of_people)
        logger.info("SMS sent")
    else:
        logger.info("Not a time for gym. No SMS sent")


