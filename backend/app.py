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


api = Api(app)

if __name__ == '__main__':
  print("Server running succesfully")
  app.run(debug="True",port=5000)