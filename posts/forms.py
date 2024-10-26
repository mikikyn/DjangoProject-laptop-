from django import forms

from posts.models import Tag


class PostForm(forms.Form):
    image = forms.ImageField()
    title = forms.CharField()
    content = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if title and content and title.lower() == content.lower():
            raise forms.ValidationError('Заголовок и контент не должны совпадать!')

        return cleaned_data

    def clean_title(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')

        if title and title.lower() == 'python':
            raise forms.ValidationError('Заголовок не может равняться слову python')
        return title

    def save(self):
        pass


class SearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Введите текст для поиска',
                'class': 'form-control',
            }
        )
    )
    tag = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
    orderings = (
        ('title', 'По названию'),
        ('-title', 'По названию в обратном порядке'),
        ('rate', 'По рейтингу'),
        ('-rate', 'По рейтингу в обратном порядке'),
        ('created_at', "По дате создания"),
        ('-created_at', "По дате создания в обратном порядке"),
    )
    ordering = forms.ChoiceField(
        required=False,
        choices=orderings,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
