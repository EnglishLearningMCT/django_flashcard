#�J�[�h�`�F�b�N(�P��m�F)�y�[�W�̃t�H�[��

from django import forms


class CardCheckForm(forms.Form):
    card_id = forms.IntegerField(required=True) #�`�F�b�N����J�[�h�̎�L�[
    solved = forms.BooleanField(required=False) #�����킩�遨True, �����łȂ��Ȃ�False
