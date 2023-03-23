import django
django.setup()
import json
import requests
from nutrient.models import Crop
import random
from string import Template
from rasa.core.agent import Agent
import traceback
from path import getModelPath


class ChatBot(object):

    response_msg ={
        "greet": (
            "Hey! How are you?",
            "Fine, thanks.",
            "Great! How are you doing?",
            "Oh gosh, all kinds of stuff !",
            "Very well, thanks.",
        ),

        "goodbye": (
            "Bye bye!",
            "See you later",
            "Take it easy",
            "Have a nice day ",
            "It was nice to see you again",
        ),
        "crop_search": (
            "You are ",
            "Fine, thanks.",
            "Great! How are you doing?",
            "Oh gosh, all kinds of stuff !",
            "Very well, thanks.",
        ),

         "affirm": (
            "I really appreciat it.",
            "I really value hearing that.",
            "TI would appsolutly love it",
            
        ),

         "bot_challenge": (
            "I am a bot",
            "I cant answer this question",
            "Sorry I am not trained to do that yet...",
        
            
        ),
        
        }


    instance = None

    @classmethod
    def getBot(cls):
        if cls.instance is None:
            cls.instance = ChatBot()
        return cls.instance
    
    def extractEntityIntent(self , text):
        payload = {"text": text}
        headers = {
            'Content-Type': "application/json",
            }
        
        data = requests.post("http://localhost:5005/model/parse", data=json.dumps(payload), headers=headers )
        return data.json()

    def __init__(self):
        print("Init")
        if self.instance is not None:
            raise ValueError("Did you forgot to call getBot function ? ")
        
    def askDBbyName(self ,list_of_crops , list_of_entity): # [{"entity_name":value },{"entity_name":value }....]

        nutrient = Crop.chatbot_manager.get_nutrients_query(list_of_crops,list_of_entity)
        return nutrient

    def generate_template(self , intent , result):
        try:
            response = ""
            print("Intent :",intent)
            msgs = self.response_msg.get(intent) 
            choice_msg = random.choice(msgs)
            
            if result: 
                t = Template('Nutrient level for $crop_name is $nutrient from $lower to $upper ')
                list_of_entities_template = []
                for crop in result:
                    for r in crop['result']:
                        items = list(r.values())

                        print("items :",items)

                        nutrient = items[0]['entity']
                        lower , upper = items[0]['value']


                        new = t.substitute(crop_name =crop['crop'], nutrient=nutrient, lower=lower , upper = upper)
                        list_of_entities_template.append(new)

                    # Nitrogen Nutreint sufficent level for Corn is from to is recommended
                    # Nutrient level for corn is Nitrogen from 0 to 1 , .....
                    # N
            response = f'\n'.join(list_of_entities_template)

        except:
            print(traceback.format_exc())

        response = response + choice_msg

        return response
                    


    def response(self , sentence):
        responce = {'text' : " i dont know the answer"}

        data = self.extractEntityIntent(text= sentence)
        
        print("sentence :",data)
        intent = data.get("intent").get('name')
        entities = data.get("entities")
        ERROR_THRESHOLD = 0.25
        
        list_of_entity = { element['value'] for element in entities if element['entity'] == "element" }

        list_of_crop ={crop['value'] for crop in entities if crop['entity'] == "crop" }

        print("list_of_entity :",list_of_entity)
        print("list_of_crop :",list_of_crop)

        result = self.askDBbyName(list_of_crop,list_of_entity)

        respond  = self.generate_template(intent , result )

        return respond 
