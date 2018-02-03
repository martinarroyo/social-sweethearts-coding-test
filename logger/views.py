from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView, View
from django.urls import reverse
import base64
import json
import hmac
import hashlib
from allauth.socialaccount.models import SocialApp, SocialAccount

class IndexView(TemplateView):
    template_name = 'logger/index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('logger:profile'))
        return super().get(request, *args, **kwargs)


class ProfileView(TemplateView):
    template_name = 'logger/profile.html'


class DeauthorizeView(View):

    def post(self, request, *args, **kwargs):
        import pdb; pdb.set_trace()
        try:
            # TODO: KeyError
            signed_request = request.POST['signed_request']
            encoded_sig, payload = signed_request.split('.')
        except (ValueError, KeyError):
            return HttpResponse(status=400, content='Invalid request')
        
        try:
            # Reference for request decoding: https://developers.facebook.com/docs/games/gamesonfacebook/login#parsingsr
            # For some reason, the request needs to be padded in order to be decoded. See https://stackoverflow.com/a/6102526/2628463
            decoded_payload = base64.urlsafe_b64decode(payload+"==").decode('utf-8')
            decoded_payload = json.loads(decoded_payload)
            
            if type(decoded_payload) is not dict or not 'user_id' in decoded_payload.keys():
                return HttpResponse(status=400, content='Invalid payload data')

        except (ValueError, json.JSONDecodeError):
            return HttpResponse(status=400, content='Could not decode payload')

        try:
            secret = SocialApp.objects.get(id=1).secret

            sig = base64.urlsafe_b64decode(encoded_sig+"==")
            expected_sig = hmac.new(bytes(secret, 'utf-8'), bytes(payload, 'utf-8'), hashlib.sha256)
        except:
            return HttpResponse(status=400, content='Could not decode signature')

        if not hmac.compare_digest(expected_sig.digest(), sig):
            return HttpResponse(status=400, content='Invalid request')

        user_id = decoded_payload['user_id']

        try:
            social_account = SocialAccount.objects.get(uid=user_id)
        except SocialAccount.DoesNotExist:
            return HttpResponse(status=200)

        social_account.user.is_active = False
        social_account.user.save()
        social_account.delete()

        return HttpResponse(status=200)
