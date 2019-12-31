import picamera
import pyimgur
from twilio.rest import Client

# put your Twilio credentials here
ACCOUNT_SID = ""
AUTH_TOKEN = ""

# make sure to use format with +1 for USA #s. E.G +12463338910
TO_PHONE = "+12897956884"
FROM_PHONE = "+13343266983"

# text message to send with photo
TXT_MSG = "Motion Detected!"

# hostname or IP address of Raspberry Pi + port number
HOSTNAME = "50.16.14.95:80"

IMAGE_DIR = "/home/pi/"
CLIENT_ID = ""

# name and dimentsions of snapshot image
IMG = "snap.jpg"
IMG_WIDTH = 800
IMG_HEIGHT = 600

# initalize the Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)
im = pyimgur.Imgur(CLIENT_ID)


with picamera.PiCamera() as camera:
    camera.resolution = (IMG_WIDTH, IMG_HEIGHT)
    camera.capture(IMAGE_DIR + IMG)

uploaded_image = im.upload_image(IMAGE_DIR + IMG, title=TXT_MSG)
client.messages.create(
    to=TO_PHONE,
    from_=FROM_PHONE,
    body=TXT_MSG,
    media_url=uploaded_image.link,
)
