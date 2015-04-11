import subprocess, requests, simplejson
from utils import get_stream_info
from constants import API_ROOT, API_ACCESS_PUBLIC

class PeriscopeUser(object):
    def __init__(self, data):
        for k, v in data.items():
            setattr(self, k, v)
        self._data = data

    def __repr__(self):
        template = "PeriscopeUser(@{name})"
        return template.format(name = self.twitter_screen_name)

class PeriscopeBroadcast(object):
    def __init__(self, data, web_url = None, token_id = None):
        self.user = PeriscopeUser(data['user'])

        if web_url:
            data['broadcast']['web_url'] = web_url

        if token_id:
            data['broadcast']['token_id'] = token_id

        for k, v in data['broadcast'].items():
            setattr(self, k, v)

        self._data = data

    def refresh(self):
        data = get_stream_info(self.web_url)
        self.data = data

    def is_running(self, refresh = True):
        if refresh: self.refresh()
        return self.state == 'RUNNING'

    def _get_public_access(self):
        params = {"token": self.token_id}
        resp = requests.get(API_ROOT + API_ACCESS_PUBLIC, params = params)
        return simplejson.loads(resp.content)

    def get_hls_url(self, https = False):
        if not self.is_running():
            raise PeriscopeBroadcastEndedError("Cannot get raw stream because stream has already ended.")

        access_info = self._get_public_access()

        if access_info:
            if https:
                return access_info['https_hls_url']
            else:
                return access_info['hls_url']

    def coordinates(self):
        if self.has_location:
            return [self.ip_lat, self.ip_lng]

    def __repr__(self):
        template = "PeriscopeBroadcast(id = {id}, user = @{user})"
        return template.format(id = self.id, user = self.user.twitter_screen_name)

    def __eq__(self, other):
        return self.id == other.id
