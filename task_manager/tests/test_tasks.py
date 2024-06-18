from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from task_manager.tasks.models import Task

class CRUDTest(TestCase):
    model = get_user_model()

    def setUp(self):
        self.client = Client()
        self.user = self.model.objects.create_user(username='Test', password='password')

    def test_create_task(self):
        name = 'To capture the world'
        status = 'In work'

        self.client.force_login(self.user)

        self.client.post(reverse('status_create'),
                                    data={'name': status})

        response = self.client.post(reverse('task_create'),
                                    data={'name': name,
                                          'status': status})

        self.assertRedirects(response, reverse('tasks'))

        new_task = Task.objects.get(name=name)
        all_tasks = Task.objects.all()

        self.assertIn(new_task, all_tasks)

    def test_read_status(self):
        name = 'To capture the world'
        status = 'In work'

        self.client.force_login(self.user)

        self.client.post(reverse('status_create'),
                                    data={'name': status})

        response = self.client.post(reverse('task_create'),
                                    data={'name': name,
                                          'status': status})

        self.assertRedirects(response, reverse('tasks'))




    def test_update_status(self):
        name = 'To capture the world'
        status = 'In work'

        self.client.force_login(self.user)

        self.client.post(reverse('status_create'),
                                    data={'name': status})

        self.client.post(reverse('task_create'),
                                    data={'name': name,
                                          'status': status})

        task = Task.objects.get(name=name)

        changed_task = 'To save the world'

        response = self.client.post(reverse('task_update', kwargs={'pk': task.pk}),
        data={'name': changed_task})


        self.assertRedirects(response, reverse('tasks'))

        status.refresh_from_db()

        self.assertEqual(task.name, changed_task)

    def test_delete_status(self):
        name = 'To capture the world'
        status = 'In work'

        self.client.force_login(self.user)

        self.client.post(reverse('status_create'),
                                    data={'name': status})

        self.client.post(reverse('task_create'),
                                    data={'name': name,
                                          'status': status})

        task = Task.objects.get(name=name)

        response = self.client.post(reverse('task_delete', kwargs={'pk': task.pk}))

        self.assertRedirects(response, reverse('tasks'))

        deleted_task = Task.objects.filter(id=task.pk)
        self.assertNotIn(task.pk, deleted_task)