import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6547572521:AAFd-O5QFHs9SevJd3QOEkx1--MR2DjHSCE)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOIEBu47Uc2rH8qjgmjdiP-x1VGw9GnKYNRV1WiECAYPXBP4ab5nfz3C8To5lxv8kqJJXLP3yG4K22f4GodGb5NLIQEyRXSS5PISabfbi3zLKL0zscSDmtSmfzSPtzd0aOysILzTyMuwvZ6-gFtYumFcZ89Zovpt3b1Im4D_VWKYfgNi00YgMbJHKqlaCLWWprTZDzIHCpc-zrbjZWqS9DLdRI6e0_AWtDXc0dHG11SmxDkF1MoAbsCn00kWKofP7oQ4jovi_kzZ815-ZyIzjCJF69jgyjPwBysQaAxP1dT8AgxmLjiIwY3O4pgww3Ww3rBGMjHdvhFU1WVVnJqyaoQbu09c=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
