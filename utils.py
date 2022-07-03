from config import logger, TWILIO_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NR
from twilio.rest import Client

def send_sms(phone: str, message: str)->bool:
    """
    Send an SMS message to a phone number
    """

    try:
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
                              from_=TWILIO_PHONE_NR,
                              body =message,
                              to =phone
                          )
        logger.info(f"SMS sent to {phone}")
        logger.info(f"SMS ID: {message.sid}")
        return True
    except Exception as e:
        logger.error(e)
        return False