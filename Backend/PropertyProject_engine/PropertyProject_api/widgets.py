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


class MultipleChoiceWidget(forms.CheckboxSelectMultiple):
    template_name = 'admin/PropertyProject_api/widgets/multiple_choice.html'

    def __init__(self, attrs=None, choices=(), default_choice=tuple()):
        super().__init__(attrs,choices)
        self.default_choice = default_choice

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        if self.default_choice:
            context['widget']['default_choice_value'] = self.default_choice
        return context

    class Media:
        js = ('admin/js/PropertyProject_api/parking-switch-control.js',)
