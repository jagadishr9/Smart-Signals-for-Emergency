import ibmiotf.application
import ibmiotf.device
from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
import time
print("since hardware is not available, enter the ambulance coordinates manually");
print();
while True:
     print("enter latitude Coordinate:", end = ' ');
     latitude=input();
     print("enter longitude Coordinate:", end = ' ');
     longitude=input();
     organization = "652j8u"
     deviceType = "GPS"
     deviceId = "Locations"
     authMethod = "token"
     authToken = "IoFLai8PWgy!ZN_kzs"
     try:
         deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod,"auth-token": authToken}
         deviceCli = ibmiotf.device.Client(deviceOptions)
 #..............................................

     except Exception as e:
         print("Caught exception connecting device: %s" % str(e))
     deviceCli.connect()

     client = Cloudant("a7f80401-360b-421a-85e0-071d83bddb8b-bluemix",
    "6d6fe40cc5c255020a94455a87a2ce22df362111b29f696b06d1faf072b8e766", url="https://a7f80401-360b-421a85e0-071d83bddb8bbluemix:6d6fe40cc5c255020a94455a87a2ce22df362111b29f696b06d1faf072b8e766@a7f80401-360b-421a-85e0-071d83bddb8b-bluemix.cloudantnosqldb.appdomain.cloud")
     client.connect()
     while True:
         data = {"d":{ 'lat' : latitude, 'lon':longitude}}
         def myOnPublishCallback():
             print ("Published data to IBM Watson")
         success = deviceCli.publishEvent("Data", "json", data, qos=0, on_publish=myOnPublishCallback)
         if not success:
             print("Not connected to IoTF")
             time.sleep(10)
             break;
         else:
             break;
     deviceCli.disconnect()
     if success:
         print("Data Sent");
         print("Switch to Node-red and Analyze the Data")
     print("Do you want to test another data (yes/no):",end="")
     res=input();
     if(res=="yes"):
         continue;
     else:
         break;
