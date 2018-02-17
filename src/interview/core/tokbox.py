import time

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from opentok import OpenTok, Roles

try:
    OPENTOK_API_KEY = settings.OPENTOK_API_KEY
except ImportError:
    raise ImproperlyConfigured('OPENTOK_API_KEY must be set')
try:
    OPENTOK_API_SECRET = settings.OPENTOK_API_SECRET
except Exception as e:
    raise ImproperlyConfigured('OPENTOK_API_SECRET must be set')


class Tokbox(object):
    opentok = OpenTok(OPENTOK_API_KEY, OPENTOK_API_SECRET)

    def create_session(self, *args, **kwargs):
        return self.opentok.create_session()

    def get_token(self, session):
        return session.generate_token(
            role=Roles.moderator,
            expire_time=int(time.time()) + 10,
            data=u'name=Johnny',
            initial_layout_class_list=[u'focus'])
