from django.db import models

COURSE_DESCRIPTION = {
    ('Math','Math'),
    ('Physics','Physics'),
    ('English','English'),
}

class djangoClasses(models.Model):
# Create your models here.
    title = models.CharField(max_length=30, choices=COURSE_DESCRIPTION)         # Indicates course (e.g., Math)
    course_number = models.PositiveSmallIntegerField(default=0, max_length=3)   # Indicates course no. (from 000-999).
    instructor_name = models.CharField(max_length=70, default="", blank=True, null=False)
    duration = models.FloatField(default=0, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.title

