from django import forms

class SearchableChoiceWidget(forms.widgets.Select):
    template_name = 'admin/PropertyProject_api/widgets/SearchableChoice.html'

    class Media:
        css = {
            'all': ( "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css",
                      "https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.12.4/css/bootstrap-select.min.css",
                      )
        }

    def __init__(self, attrs=None, choices=(),widget_title=''):
        super().__init__(attrs,choices)
        self.widget_title = widget_title

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['title'] = self.widget_title

        return context

# class AddressChoiceWidget(SearchableChoiceWidget):
#     template_name = 'admin/PropertyProject_api/widgets/AddressChoice.html'
