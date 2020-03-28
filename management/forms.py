from django import forms
from django.core.validators import RegexValidator
from .models import Dosen, Matkul


class DosenChangeForm(forms.ModelForm):
    nip = forms.CharField(widget=forms.PasswordInput, required=False,
                               validators=[
                                   RegexValidator(r'^.{3,}$', 'NIP must has at least 12 characters.')])

    def __init__(self, *args, **kwargs):
        super(CountryChangeForm, self).__init__(*args, **kwargs)
        self.fields['nip'].required = True
        self.fields['name'].required = True

    def save(self, commit=True):
        dosen = super(DosenChangeForm, self).save(commit=False)
        if commit:
            dosen.save()
        return dosen

    class Meta:
        model = Dosen
        fields = ('nip', 'name')

class MatkulChangeForm(forms.ModelForm):
    kode_matkul = forms.CharField(widget=forms.PasswordInput, required=False,
                                validators=[
                                    RegexValidator(r'^.{3,}$', 'Kode Matakuliah must has at least 3 characters.')])

    def __init__(self, *args, **kwargs):
        super(GithubChangeForm, self).__init__(*args, **kwargs)
        self.fields['kode_matkul'].required = True
        self.fields['nama_matkul'].required = True
        self.fields['sks'].required = True

    def save(self, commit=True):
        matkul = super(MatkulChangeForm, self).save(commit=False)

        if commit:
            matkul.save()
        return matkul
    

    class Meta:
        model = Matkul
        fields = ('kode_matkul', 'nama_matkul', 'nip')
