from django.views.generic import UpdateView, DetailView

from user.decorators import class_login_required
from .utils import ProfileGetObjectMixin
from .models import Profile





@class_login_required
class ProfileDetail(
        ProfileGetObjectMixin, DetailView):
    model = Profile

class PublicProfileDetail(DetailView):
    model = Profile

@class_login_required
class ProfileUpdate(
        ProfileGetObjectMixin, UpdateView):
    fields = ('about',)
    model = Profile
    template_name = 'profiles/profile_form_update.html'







