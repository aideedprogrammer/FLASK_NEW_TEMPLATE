import unittest
from .. import intial_app
from proj.models.model import *


class UserTestCase(unittest.TestCase):

    def setUp(self):
        self.app = intial_app('testing')
        self.appctx = self.app.app_context()
        self.appctx.push()
        self.client = self.app.test_client()

    def tearDown(self):

        # db.drop_all()

        self.appctx.pop()
        self.app = None
        self.client = None

    def test_call_user(self):
        response = self.client.get('/user/list')

        user = User.query.filter_by(age="ff").first()
        
        assert user.age == "ff"

        assert response.status_code == 200
