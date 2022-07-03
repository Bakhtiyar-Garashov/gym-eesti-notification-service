from typing import Final
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

API_URL: Final[str] = "https://goapi2.perfectgym.com/v1/Clubs/WhoIsInCount"
TOKEN: Final[str] = ""

TWILIO_SID: Final[str] = ""
TWILIO_AUTH_TOKEN: Final[str] = ""
TWILIO_PHONE_NR: Final[str] = "+"

MY_CLUB_ID: Final[int] = 752