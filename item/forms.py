from django import forms

from .models import Category, Item

Tailwind_CLASS = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'name', 'description', 'price', 'image']
        widgets = {
            'category': forms.Select(attrs={
                'class': Tailwind_CLASS}),
            'name': forms.TextInput(attrs={
                'class': Tailwind_CLASS}),
            'description': forms.Textarea(attrs={
                'class': Tailwind_CLASS}),
            'price': forms.NumberInput(attrs={
                'class': Tailwind_CLASS}),
            'image': forms.FileInput(attrs={
                'class': Tailwind_CLASS}),
        }