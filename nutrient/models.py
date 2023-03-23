from typing import Any
from django.db import models
from .manager import ChatBotManager

# Create your models here.

class Element(models.Model) :
    name = models.CharField(max_length=10 , primary_key= True)
    alternative_name = models.CharField(blank=True , null= True , max_length=10)

    def __str__(self) -> str:
        return self.name

class Nutrient(models.Model):
    MEASUREMENT_CHOICE = (
        ("1","%"),
        ("2","ppm")
    )
    name = models.ForeignKey(Element,on_delete=models.CASCADE, null=True, blank=True, related_name='sub_elements_name' )
    lower = models.FloatField()
    upper = models.FloatField()
    measurment = models.CharField(choices= MEASUREMENT_CHOICE , max_length= 5)

    def __str__(self) -> str:
        return "Nutrient {}".format(self.name.name)

    
    def __repr__(self) -> str:

        return "Nutrient([{0},{1},{2}])".format(self.name, (self.lower , self.upper), self.measurment)
    

class Crop(models.Model):
    name = models.CharField(max_length=20 , primary_key= True) 
    parent_crop = models.ManyToManyField('self', blank=True, related_name='sub_cropies' ) #myindustry.sub_industries.all().
    nutrients = models.ManyToManyField(Nutrient, related_name='nutrienties' )
    chatbot_manager = ChatBotManager()

    class Meta:
        pass
        #default_manager_name = 'chatbot_manager'

    def __str__(self) -> str:
        return "Name: {0}".format(self.name)
    
    @property
    def get_nutreints(self):
        return self.nutrients.all()

    
    def __repr__(self) -> str:

        return "Crop([{0})".format(self.name)
    
   
 

