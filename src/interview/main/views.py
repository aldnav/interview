import json

from django.core.cache import cache
from django.http import HttpResponse
from django.views.generic import View, TemplateView

from core import tokbox


class HomeView(TemplateView):
    template_name = 'main/home.html'


class GetSessionInfoView(View):

    def get(self, *args, **kwargs):
        session = cache.get('session')
        token = cache.get('token')

        if not session:
            tokhang = tokbox.Tokbox()
            session = tokhang.create_session()  # save session somewhere else
            token = tokhang.get_token(session)
        context_data = json.dumps({
            'apiKey': tokbox.OPENTOK_API_KEY,
            'sessionId': session.session_id,
            'token': token
        })
        return HttpResponse(context_data, content_type='json')
