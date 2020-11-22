from django import forms


class SearchableChoiceWidget(forms.widgets.Select):
    template_name = 'admin/api/widgets/SearchableChoice.html'

    def __init__(self, attrs=None, choices=(), widget_title=''):
        super().__init__(attrs, choices)
        self.widget_title = widget_title

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['title'] = self.widget_title
        return context


class MultipleChoiceWidget(forms.CheckboxSelectMultiple):
    template_name = 'admin/api/widgets/multiple_choice.html'

    def __init__(self, attrs=None, choices=(), not_comleted_choice=""):
        super().__init__(attrs, choices)
        self.not_comleted_choice = not_comleted_choice

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['not_comleted_choice_value'] = self.not_comleted_choice
        return context

    def _media(self):
        if self.not_comleted_choice:
            return forms.Media(
                js=('admin/js/api/parking-switch-control.js',)
            )
        return forms.Media()

    media = property(_media)
    # class Media:
    #     js = ('admin/js/api/parking-switch-control.js',)
