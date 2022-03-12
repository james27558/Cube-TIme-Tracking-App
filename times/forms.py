from django.forms import ModelForm
from .models import Session, Attempt, Tag, SessionJSON

class SessionModelForm(ModelForm):
    class Meta:
        model = Session
        fields = "__all__"

class AttemptModelForm(ModelForm):
    class Meta:
        model = Attempt
        fields = "__all__"

class TagModelForm(ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"

class SessionJSONModelForm(ModelForm):
    class Meta:
        model = SessionJSON
        fields = "__all__"