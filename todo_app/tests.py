from django.contrib.auth import get_user_model
from django.test import Client
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from todo_app.models import Task, Tag


class IndexViewTests(TestCase):
    def setUp(self):
        self.task1 = Task.objects.create(content="Task 1", is_done=False)
        self.task2 = Task.objects.create(content="Task 2", is_done=True)

    def test_index_view_status_code(self):
        response = self.client.get(reverse("todo:index"))
        self.assertEqual(response.status_code, 200)

    def test_index_view_uses_correct_template(self):
        response = self.client.get(reverse("todo:index"))
        self.assertTemplateUsed(response, "todo/index.html")

    def test_index_view_displays_tasks(self):
        response = self.client.get(reverse("todo:index"))
        self.assertContains(response, "Task 1")
        self.assertContains(response, "Task 2")


class TagListViewTests(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(name="Tag 1")
        self.tag2 = Tag.objects.create(name="Tag 2")

    def test_tag_list_view_status_code(self):
        response = self.client.get(reverse("todo:tag-list"))
        self.assertEqual(response.status_code, 200)

    def test_tag_list_view_uses_correct_template(self):
        response = self.client.get(reverse("todo:tag-list"))
        self.assertTemplateUsed(response, "todo/tag_list.html")

    def test_tag_list_view_displays_tags(self):
        response = self.client.get(reverse("todo:tag-list"))
        self.assertContains(response, "Tag 1")
        self.assertContains(response, "Tag 2")


class TagCreateViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="12345",
            email="john@example.com",
        )
        self.client.login(username="testuser", password="12345")
        self.tag1 = Tag.objects.create(name="Tag 1")
        self.tag2 = Tag.objects.create(name="Tag 2")

    def test_tag_create_view_status_code(self):
        response = self.client.get(reverse("todo:tag-create"))
        self.assertEqual(response.status_code, 200)

    def test_tag_create_view_uses_correct_template(self):
        response = self.client.get(reverse("todo:tag-create"))
        self.assertTemplateUsed(response, "todo/tag_form.html")

    def test_can_create_tag(self):
        response = self.client.post(
            reverse("todo:tag-create"), data={"name": "New Tag"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Tag.objects.filter(name="New Tag").exists())


class TagUpdateViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="12345",
            email="john@example.com",
        )
        self.client.login(username="testuser", password="12345")
        self.tag = Tag.objects.create(name="Tag 1")

    def test_tag_update_view_status_code(self):
        response = self.client.get(
            reverse("todo:tag-update", args=[self.tag.id])
        )
        self.assertEqual(response.status_code, 200)

    def test_tag_update_view_uses_correct_template(self):
        response = self.client.get(
            reverse("todo:tag-update", args=[self.tag.id])
        )
        self.assertTemplateUsed(response, "todo/tag_form.html")

    def test_can_update_tag(self):
        response = self.client.post(
            reverse("todo:tag-update", args=[self.tag.id]),
            data={"name": "Updated Tag"},
        )
        self.assertEqual(response.status_code, 302)
        self.tag.refresh_from_db()
        self.assertEqual(self.tag.name, "Updated Tag")


class TagDeleteViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="12345",
            email="john@example.com",
        )
        self.client.login(username="testuser", password="12345")
        self.tag = Tag.objects.create(name="Tag 1")

    def test_tag_delete_view_status_code(self):
        response = self.client.get(
            reverse("todo:tag-delete", args=[self.tag.id])
        )
        self.assertEqual(response.status_code, 200)

    def test_tag_delete_view_uses_correct_template(self):
        response = self.client.get(
            reverse("todo:tag-delete", args=[self.tag.id])
        )
        self.assertTemplateUsed(response, "todo/tag_confirm_delete.html")

    def test_can_delete_tag(self):
        response = self.client.post(
            reverse("todo:tag-delete", args=[self.tag.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Tag.objects.filter(id=self.tag.id).exists())


class TaskCreateViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="12345",
            email="john@example.com",
        )
        self.client.login(username="testuser", password="12345")
        self.tag = Tag.objects.create(name="Tag 1")

    def test_task_create_view_status_code(self):
        response = self.client.get(reverse("todo:task-create"))
        self.assertEqual(response.status_code, 200)

    def test_task_create_view_uses_correct_template(self):
        response = self.client.get(reverse("todo:task-create"))
        self.assertTemplateUsed(response, "todo/task_form.html")

    def test_can_create_task(self):
        response = self.client.post(
            reverse("todo:task-create"),
            data={
                "content": "New Task",
                "dead_line_time": timezone.now(),
                "tags": [self.tag.id],
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(content="New Task").exists())


class TaskUpdateViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="12345",
            email="john@example.com",
        )
        self.client.login(username="testuser", password="12345")
        self.task = Task.objects.create(content="Task 1")

    def test_task_update_view_status_code(self):
        response = self.client.get(
            reverse("todo:task-update", args=[self.task.id])
        )
        self.assertEqual(response.status_code, 200)

    def test_task_update_view_uses_correct_template(self):
        response = self.client.get(
            reverse("todo:task-update", args=[self.task.id])
        )
        self.assertTemplateUsed(response, "todo/task_form.html")

    def test_can_update_task(self):
        response = self.client.post(
            reverse("todo:task-update", args=[self.task.id]),
            data={
                "content": "Updated Task",
                "dead_line_time": timezone.now(),
            },
        )
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.content, "Updated Task")


class TaskDeleteViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="12345",
            email="john@example.com",
        )
        self.client.login(username="testuser", password="12345")
        self.task = Task.objects.create(content="Task 1")

    def test_task_delete_view_status_code(self):
        response = self.client.get(
            reverse("todo:task-delete", args=[self.task.id])
        )
        self.assertEqual(response.status_code, 200)

    def test_task_delete_view_uses_correct_template(self):
        response = self.client.get(
            reverse("todo:task-delete", args=[self.task.id])
        )
        self.assertTemplateUsed(response, "todo/task_confirm_delete.html")

    def test_can_delete_task(self):
        response = self.client.post(
            reverse("todo:task-delete", args=[self.task.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())


class ChangeTaskStatusViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="12345",
            email="john@example.com",
        )
        self.client.login(username="testuser", password="12345")
        self.task = Task.objects.create(content="Task 1", is_done=False)

    def test_change_task_status(self):
        response = self.client.get(
            reverse("todo:change-task-status", args=[self.task.id])
        )
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertTrue(self.task.is_done)
        response = self.client.get(
            reverse("todo:change-task-status", args=[self.task.id])
        )
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertFalse(self.task.is_done)
