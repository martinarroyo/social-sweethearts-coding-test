from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView, View
from django.urls import reverse


class IndexView(TemplateView):
    template_name = 'logger/index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('logger:profile'))
        return super().get(request, *args, **kwargs)


class ProfileView(TemplateView):
    template_name = 'logger/profile.html'


class DeactivateView(View):

    def post(self, request, *args, **kwargs):

        return HttpResponse(status=200)
