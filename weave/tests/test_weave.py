import json
import tempfile
import unittest
import werkzeug.test
import weave


class WeaveTestUserAPI(unittest.TestCase):
    """
    API https://docs.services.mozilla.com/reg/apis.html
    """

    def setUp(self):
        tempdir = tempfile.mkdtemp()
        self.tempdir = tempdir
        # XXX activated registration
        self.app = weave.make_app(tempdir, register=True)
        self.c = werkzeug.test.Client(self.app)

    def test_not_implemented(self):
        app_iter, status, headers = self.c.get('/')
        self.assertEqual(status, '501 NOT IMPLEMENTED')

    def test_get_username(self):
        #GET https://server/pathname/version/username
        app_iter, status, headers = self.c.get('/user/1.0/peter')
        self.assertEqual(''.join(app_iter), '0')

    def test_get_weave(self):
        #GET https://server/pathname/version/username/node/weave
        app_iter, status, headers = self.c.get('/user/1.0/peter/node/weave')
        self.assertEqual(''.join(app_iter), 'http://localhost/')

    def test_register_user_no_body(self):
        #PUT https://server/pathname/version/username
        app_iter, status, headers = self.c.put('/user/1.0/peter')
        self.assertEqual(''.join(app_iter), '6')

    def test_register_user(self):
        #PUT https://server/pathname/version/username
        data = json.dumps({'password': 'secure', 'e-mail': 'peter@peter.de'})
        app_iter, status, headers = self.c.put('/user/1.0/peter', data=data)
        self.assertEqual(''.join(app_iter), 'peter')

    def test_ccaptcha(self):
        #GET https://server/misc/1.0/captcha_html
        app_iter, status, headers = self.c.get('/misc/1.0/captcha_html')
        self.assertEqual(len(''.join(app_iter)), 109)

    def test_not_implemented(self):
        #GET https://server/pathname/version/username/password_reset
        app_iter, status, headers = self.c.get('/')

    def test_not_implemented(self):
        #POST https://server/pathname/version/username/password
        app_iter, status, headers = self.c.get('/')

    def test_not_implemented(self):
        #POST https://server/pathname/version/username/email
        app_iter, status, headers = self.c.get('/')

    def test_not_implemented(self):
        #DELETE https://server/pathname/version/username
        app_iter, status, headers = self.c.get('/')

    def test_not_implemented(self):
        #GET https://server/pathname/version/username/node/weave
        app_iter, status, headers = self.c.get('/')
