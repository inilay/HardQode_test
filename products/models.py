from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrolled_products = models.ManyToManyField('Product', blank=True)

    def __str__(self):
        return self.user.username
    

class Lesson(models.Model):
    lesson_name = models.CharField(max_length=255)
    link_to_video = models.URLField()
    lesson_duration = models.DurationField()

    def __str__(self):
        return self.lesson_name


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    lessons = models.ManyToManyField(Lesson, blank=True)

    def __str__(self):
        return self.product_name


class LessonView(models.Model):
    view_time = models.DurationField()
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    last_view = models.DateTimeField(null=True)

    @property
    def lesson_status(self):
        return 'Viewed' if self.view_time.total_seconds() / self.lesson.lesson_duration.total_seconds() >= 0.8 else 'Not viewed'

    def __str__(self):
        return f'{self.user_profile.user.username} LessonView for {self.lesson.lesson_name}'


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance
        )