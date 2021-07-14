from django import forms


class StackSearchForm(forms.Form):
    RESULT_ORDER = [
        ('desc', 'desc'),
        ('asc', 'asc')
    ]
    SORT_ORDER = [
        ('activity', 'activity'),
        ('creation', 'creation'),
        ('votes', 'votes'),
        ('relevance', 'relevance')
    ]
    BOOLEAN_ORDER = [
        ('True', 'True'),
        ('False', 'False'),
    ]
    q = forms.CharField(label='Question', widget=forms.TextInput(attrs={'placeholder': 'Search Question'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Title'}),required=False)
    fromdate = forms.CharField(widget=forms.TextInput(attrs={'type': 'date'}),required=False)
    todate = forms.CharField(widget=forms.TextInput(attrs={'type': 'date'}),required=False)
    min = forms.CharField(widget=forms.TextInput(attrs={'type': 'date'}), required=False)
    max = forms.CharField(widget=forms.TextInput(attrs={'type': 'date'}), required=False)
    pages = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Page no.', "type": 'number', 'value': 1}), required=False)
    pagesize = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Page Size.', "type": 'number', 'value': 10}),required=False)
    user = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter user id...', "type": 'number'}),required=False)
    views = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search by number of views...', "type": 'number'}),required=False)
    order = forms.CharField(label='Select result order', widget=forms.Select(choices=RESULT_ORDER))
    sort = forms.CharField(label='Select result sort type', widget=forms.Select(choices=SORT_ORDER))
    answered = forms.CharField(label='Answered or not', widget=forms.Select(choices=BOOLEAN_ORDER))


