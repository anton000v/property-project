from rest_framework import fields

class ParkingChoiceField(fields.MultipleChoiceField):
    def to_representation(self,value):
        return {
        super(ParkingChoiceField, self).choices[item] for item in value
        }
