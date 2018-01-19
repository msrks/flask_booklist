import unittest
from flask_testing import TestCase
from app import app, db
from app.models import Book

class TestApp(TestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_main_route(self):
        response = self.client.get('/')
        self.assert_200(response)

    def test_not_found(self):
        response = self.client.get('/api/not/found')
        self.assert_404(response)

    def test_add_book(self):
        from datetime import datetime
        post_response = self.client.post(
            '/',
            data={'title': 'hogebook',
                  'price': 3980,
                  # 'when_added': datetime.strptime('2018/01/01 00:00:00', '%Y/%m/%d %H:%M:%S'),
                  'who_added': 'shinzo_abe'}
        )
        self.assert_status(post_response, 200)

        books = Book.query.all()
        self.assertEqual('hogebook', books[0].title)
        self.assertEqual(3980, books[0].price)
        # self.assertEqual(datetime.strptime('2018/01/01 00:00:00', '%Y/%m/%d %H:%M:%S'), books[0].when_added)
        self.assertEqual('shinzo_abe', books[0].who_added)

        response = self.client.get('/')
        self.assert_200(response)
        self.assertIn('hogebook', response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()