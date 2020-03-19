from django import forms

class SearchableChoiceWidget(forms.widgets.Select):
    template_name = 'admin/PropertyProject_api/widgets/SearchableChoice.html'

    def __init__(self, attrs=None, choices=(),widget_title=''):
        super().__init__(attrs,choices)
        self.widget_title = widget_title

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['title'] = self.widget_title

        return context
