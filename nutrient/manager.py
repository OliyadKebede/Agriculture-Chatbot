from django.db import models

class ChatBotManager(models.Manager):

        
    def get_nutrients_query(self,list_of_crops=None,list_of_entities=None):
        records_for_crops = []
        if len(list_of_crops) == 1 and list_of_entities == None:
            pass

        for crop_name in list_of_crops:
            crop = super().get_queryset().filter(name= crop_name.capitalize())
            print("crop result :",crop)
            nutrients = crop[0].get_nutreints
            print("Nutrient :",nutrients)
            row_nurients = []
            for nutrient in nutrients:
                entity = nutrient.name.name
                value = (nutrient.lower , nutrient.upper)
                result = {"entity":entity, "value" : value}
                print("result :",result)

                print("list of entity :",list_of_entities)
                print("nutrient name :",entity in list_of_entities)
                crops_current = [n.get('crop') for n in records_for_crops]
                if entity in list_of_entities:
                    print("crops current : ",crops_current)

                    if crop_name in crops_current:
                        for c in records_for_crops:
                            if c.get('crop') == crop_name:
                                c.get("result").append({crop_name:result})
                    else:
                        records_for_crops.append({"crop":crop_name , "result":[{crop_name:result}]})
                else:
                    pass
                    #retrun all nurients info available in the db

                    #row_nurients.append({crop_name:result})
                    #records_for_crops.append({"crop":crop_name , "result":row_nurients})


        print("final result : ",records_for_crops)
        return records_for_crops
    