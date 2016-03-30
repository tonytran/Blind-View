from havenondemand.hodclient import *
import http


def getTextFromImage(logofile):
    client = HODClient("your haven ondemand key here")
    #check = ["STOP", "EPIC Ave", "stop"]
    thisDict = {'file' : logofile}

    jsonDict = client.post_request(thisDict, HODApps.RECOGNIZE_IMAGES, False)
    if jsonDict != None:
        if jsonDict['object'] != None:
            if jsonDict['object'][0] != None:
                if jsonDict['object'][0]['name'] != None:
                    texty = jsonDict['object'][0]['name']
                else:
                        texty = "invalid image"
            else:
                    texty = "invalid image"
        else:
                texty = "invalid image"
    else :
            texty ="invalid image"
    
        

    return texty

