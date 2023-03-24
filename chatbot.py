import django
django.setup()


import json
import requests
from nutrient.models import Crop
import random
from string import Template


class ChatBot(object):

    response_msg ={
        "greet": (
            "Hey! How are you?",
            "Fine, thanks.",
            "Great! How are you doing?",
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
         "Suggestion": (
            "I suggest that,",
            "I recommend that",
            "Let's try this",       
            
        ),
        
        }

    template_for_nutrient =Template('$nutrient from $lower to $upper ')
    NO_INFORMATION = "I have't see any information related with crops in your query"
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
        
        response = self.NO_INFORMATION
        msgs = self.response_msg.get(intent) 
        choice_msg = random.choice(msgs)
            

        if intent == "greet" :
                return choice_msg 
            
        if intent == "goodbye" :
                return choice_msg
            
        if intent == "bot_challenge" :
                return choice_msg
            

        if result[0].get("invalid"):
            crop_name = result[0].get("crop_name")
            return f"Sorry , There is no avalable {crop_name} information "

        elif result:
            list_of_entities_template = []
            for crop in result:
                 for r in crop['result']:
                     items = list(r.values())
                     nutrient = items[0]['entity']
                     lower , upper = items[0]['value']
                     new = self.template_for_nutrient.substitute( nutrient=nutrient, lower=lower , upper = upper)
                     list_of_entities_template.append(new)

            suggest =  random.choice(self.response_msg.get("Suggestion") )

            name = result[0]["crop"]

            response =suggest+ f",The nutrient level for {name} \n"+ f',\n'.join(list_of_entities_template)

        return response
                    


    def response(self , sentence):
        data = self.extractEntityIntent(text= sentence)
        intent = data.get("intent").get('name')
        entities = data.get("entities")
        ERROR_THRESHOLD = 0.25
        
        list_of_entity = { element['value'].capitalize() for element in entities if element['entity'] == "element" }
        list_of_crop ={crop['value'] for crop in entities if crop['entity'] == "crop" }
        result = self.askDBbyName(list_of_crop,list_of_entity)
        respond  = self.generate_template(intent , result )
    
        return respond 
