import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "21288218"))
    API_HASH = os.environ.get("API_HASH", "dd47d5c4fbc31534aa764ef9918b3acd")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6021415198:AAGJ5z8r-bBK9iXzvymHHoKywAW-TDEPzCY")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "6065594762")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://FORWARD:FORWARD@cluster0.k1omlka.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQB4gF94WgYNtRb9GL2zOT-nE9dz8NrjEWxXGyquI5zgc7YB4tjBNIb-iAIRgCqTguMnFQ_t5-nvxlK4yj2er7GVPYD3dBMprG9egD5sMuHQHs8yMq1Uix3-B5zBjBKU2CMshx5dfv4yakpKRwEgUe3gFwo8hSMkFAVkc-PbzbpwkMIn38-ryrLSMLcP2v-GaVBRHZZzPVp94WqxbnMczfQVISwJuTODm7PkUPGo1T6UEBU1Akb2ljy5XcKGKccfv72vDGUZyke2XrEuv2ra3QavW6IyQVsL_BnupVa3swgU8ItsEHcHpy6uHn-O1NAFzD45GmEOTVJGJZUX2jy0yTzCAAAAAWmJoYoA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001946118544"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "VIP_FORWARD_ROBOT")

    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
