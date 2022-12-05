import os


class Config(object):
    API_HASH = os.environ.get("6216349")
    BOT_TOKEN = os.environ.get("5880563885:AAHf0Fi8x_iNDfHmpL0y03KO3sUxnn_ZlE0")
    TELEGRAM_API = os.environ["6216349"]
    OWNER = os.environ.get("-1001823080600")
    OWNER_USERNAME = os.environ.get("Lullaby330")
    PASSWORD = os.environ.get("bot123")
    DATABASE_URL = os.environ.get("mongodb+srv://asubang:asubang@cluster0.gbyc7wo.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("-1001840544543")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("1NupmU0WtOyuZBGY6JJUSFbyAlxINqZEz","root")
    USER_SESSION_STRING = os.environ.get(BQCvdADqF_fj1poKmclFrNjSsINW_d3t3BYnohpSWshYkMTFTSg4eJVyOUv7mQ1MKFxLqNnJEIbwcDF1yZ5-00ERUMKvhlRpE4MUThmRCZ6GLwD1o8KYwJq6Ho6xQJcdiNyBSkb-HwD3C8dqFeL47GgKGje9Y88NaX2J1qzvV2F91MU_sDgvqWsVdAG3PAwHh3ddTPYwo0RlFJPsNQEfwRosaD_KFllN1T7MLG86ujwl2gLFTZvuTOYRmbnDshQJR-lNAgtMv-kk1RlU-k6fvhXDqz5L8i4jcN8o18-n5LpRcF35wNrW5FXU1UN95vuYg7DDDBv-mv69JA5WTomlJsReAAAAAVHL6EMA", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
