from flask import Flask, Response, request
from flask_restful import Api, Resource
from flask import request
from flask_cors import CORS
from dotenv import load_dotenv
import json
import requests
import os

from helpers.twilio_func import makeCall, makeSMS


load_dotenv()
app = Flask(__name__)
CORS(app)

GOV_URL = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"


@app.route("/call-sms", methods=["GET", "POST"])
def call_sms():
    try:
        # phone_number = request.json['phone_number']
        phone_number = '+919987483893'
        message = """किसान मित्रों,
        
        कृपया ध्यान दें, कुछ ही घंटों में मौसम बदलने की संभावना है। कृपया अपनी फसलों की सुरक्षा के लिए आवश्यक कदम उठाएं।

        धन्यवाद,
        आपका कृषि बंधु ऐप
        """
        makeCall(phone_number, message)
        makeSMS(phone_number, message)
        return {"data": "success"}, 200
    except Exception as ex:
        print(f"--error: {str(ex)}")
        return {"error": str(ex)}, 500

@app.route("/getCropPrice", methods=["GET", "POST"])
def getCropPrice():
    try:
        print("request Payload - ", json.loads(request.data))
        data = json.loads(request.data)

        params = {
           "api-key":  os.environ.get('CROP_PREDICTOR_API_KEY'),
           "format": 'json',
           "offset":0,
           "limit":10,
        }

        if "state" in data:
            params["filters[state.keyword]"] = data["state"]

        if "district" in data:
            params["filters[district]"] =  data["district"]
        
        
        if "commodity" in data:
            params["filters[commodity]"] = data["commodity"]
        

        print("Params - ", params)
            
        res = requests.get(GOV_URL, params)

        response_bytes = res.content
        responseData = json.loads(response_bytes.decode('utf-8'))  # Assuming UTF-8 encoding
        print("responseData : ", responseData)
        print("response - ", responseData["records"])

        return Response(
           response=json.dumps({
            "message":"Success",
            "metaData": data,
            "result": responseData["records"]
            }),
           status = 200,
           mimetype="application/json"

        )
        
    except Exception as ex:
       print("Exception -- ", str(ex))
       return {"error": str(ex)}, 500

api = Api(app)

if __name__ == '__main__':
  print("Server running succesfully")
  app.run(debug="True",port=5000)