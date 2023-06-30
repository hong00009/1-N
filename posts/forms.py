from django import forms
from .models import Post, Comment

# 사용자한테 보여줄 내 폼 양식
class PostForm(forms.ModelForm):
    # title = forms.CharField(
    #     label='제목',
    #     widget = forms.TextInput(
    #         attrs = {'class': 'form-control'}
    #     ),
    # )
    class Meta:
        model = Post
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        fields = ('content', )
        # fileds => 추가할 필드 이름 목록 (내가 보여주고 싶은 항목), __all__ = 모두
        exclude = ('post', )
        # exclude => 제외할 필드 이름 목록 (모든것중 일부 제외)