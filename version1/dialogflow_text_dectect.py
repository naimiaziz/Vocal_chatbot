from fbchat import  Client, log
from fbchat.models import *
import apiai, codecs, json
import credentials
import pyasn1, certifi, asn1crypto, cryptography, OpenSSL, urllib3
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context





def apiaiCon(message):
    CLIENT_ACCESS_TOKEN = "848886a235e64039992ffd0d84829a92"
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
    request = ai.text_request()
    request.lang = 'de' #Default : English
    request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"
    request=ai.text_request()
    
    request.query=message

    res=request.getresponse()
    
    obj = json.load(res)
    print(obj)

    # Get reply from the list
    reply = obj['result']['fulfillment']['speech']
    return(reply)




