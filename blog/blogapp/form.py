from django import forms
from .models import Blog

class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog #어떤 모델을 기반으로 만들거냐
        fields = ['title', 'body'] # 그 중에서 타이틀과 바디를 입력받을 공간을 만들겠다