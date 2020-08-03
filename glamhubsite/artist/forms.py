from ckeditor.widgets import CKEditorWidget

from django import forms

from artist.models import ArtistPortfolio, ArtistryCategory
# from personal.models import ContactUs


# create artistportfolio form
class CreateArtistPortfolioForm(forms.ModelForm):
    artistry_category = forms.ModelChoiceField(
        queryset=ArtistryCategory.objects.filter(active=True),
        required=False
    )

    class Meta:
        model = ArtistPortfolio
        fields = '__all__'
        exclude = ('slug',)


class UpdateArtistPortfolioForm(forms.ModelForm):
    artistry_category = forms.ModelChoiceField(
        queryset=ArtistryCategory.objects.filter(active=True),
        required=False
    )

    class Meta:
        model = ArtistPortfolio
        fields = '__all__'
        exclude = ('slug',)

    # custom edit and save method of existing profile
    def save(self, commit=True):
        artistportfolio = self.instance
        artistportfolio.artistry_category = self.cleaned_data['artistry_category']  # noqa
        artistportfolio.business_name = self.cleaned_data['business_name']
        artistportfolio.business_owner = self.cleaned_data['business_owner']
        artistportfolio.email_address = self.cleaned_data['email_address']
        artistportfolio.phone_number = self.cleaned_data['phone_number']
        artistportfolio.description = self.cleaned_data['description']

        # if there is a new image set it
        if self.cleaned_data['profile_image']:
            artistportfolio.profile_image = self.cleaned_data['profile_image']

        if commit:
            artistportfolio.save()
        return artistportfolio















