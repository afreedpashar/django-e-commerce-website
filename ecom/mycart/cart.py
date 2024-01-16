
class Cart():
    def __init__(self,request):
        self.session = request.session

        #get the session key if it exists
        cart = self.session.get('session_key')

        #if the user is new, no session key, create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        #make sure cart is availableon all pages of site
        self.cart = cart


"""
use thes commands to find the session 
>>> from django.contrib.sessions.models import Session
>>> session_k = Session.objects.get(pk='ygzh4gxlunbrj7xhkps7f06gh7xmgv4v')
>>> session_k.get_decoded()
{'_auth_user_id': '1', '_auth_user_backend': 'django.contrib.auth.backends.ModelBackend', '_auth_user_hash': '8490ee2a97ee8f52eef9149765453a22fdb948fdd85c00b78622c31f1a04ef4f', 'session_key': {}}
"""