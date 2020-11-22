from rest_framework import fields

class ChoiceFieldCustomDisplay(fields.ChoiceField):
    def to_representation(self,value):
        if value in ('', None):
            return value
        return super(ChoiceFieldCustomDisplay,self).choices[value]
        # super(ChoiceFieldInterface,self).str(value), value)


class MultipleChoiceFieldCustomDisplay(fields.MultipleChoiceField):
    def to_representation(self,value):
        return {
        super(MultipleChoiceFieldCustomDisplay,self).choices[item] for item in value
        }
