from django.test import TestCase, Client
from django.urls import reverse

from task_manager.users.models import User


class CRUDTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_user_create(self):
        username = 'Test'
        first_name = 'testname'
        last_name = 'surname'
        password = 'test1234Q'

        response = self.client.post(
            reverse('user_create'),
            data={'username': username,
                  'first_name': first_name,
                  'last_name': last_name,
                  'password1': password,
                  'password2': password}
        )

        self.assertRedirects(response, reverse('login'), 302)

        new_user = User.objects.get(username=username)

        self.assertEqual(new_user.username, username)
        self.assertEqual(new_user.first_name, first_name)
        self.assertEqual(new_user.last_name, last_name)

    #def test_user_update(self):

    #    user = User.objects.create(
    #    username=' Sum41',
    #    first_name='Deryck',
    #    last_name='Whibley',
    #    password='R0ckStar')

    #    data = {'first_name': 'Pavel',
    #            'last_name': 'Whibley'}


    #    response = self.client.post(reverse('user_update', kwargs={'pk': user.pk}), data)

    #    self.assertEqual(response.status_code, 200)

    def test_user_update(self):

        username = 'Sum41'
        first_name = 'Deryck'
        last_name = 'Whibley'
        password = 'R0ckStar'

        self.client.post(
            reverse('user_create'),
            data={'username': username,
                  'first_name': first_name,
                  'last_name': last_name,
                  'password1': password,
                  'password2': password}
        )

        self.client.post(
            reverse('login'),
            data={'username': username,
                  'password': password}
        )

        user = User.objects.get(username=username)

        changed_first_name = 'Pavel'
        response = self.client.post(
            reverse('user_update', kwargs={'pk': user.pk}),
            data={'username': username,
                  'first_name': changed_first_name,
                  'last_name': last_name,
                  'password1': password,
                  'password2': password}
        )

        #self.assertEqual(response, reverse('users'))
        self.assertRedirects(response, reverse('users'))

        user.refresh_from_db()
        self.assertEqual(user.first_name, changed_first_name)

    def test_user_delete(self):
        username = 'Nirvana'
        first_name = 'Kurt'
        last_name = 'Cobain'
        password = 'Sho0ter94'

        self.client.post(
            reverse('user_create'),
            data={'first_name': first_name,
                  'last_name': last_name,
                  'username': username,
                  'password1': password,
                  'password2': password}
        )

        self.client.post(
            reverse('login'),
            data={'username': username,
                  'password': password}
        )

        user = User.objects.get(username=username)

        response = self.client.post(
            reverse('user_delete', kwargs={'pk': user.pk})
        )

        self.assertRedirects(response, reverse('users'), 302)

        deleted_user = User.objects.filter(id=user.pk)
        self.assertNotIn(user.pk, deleted_user)
