import uuid
from django.db import models
from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Projects(models.Model):
    title = models.CharField('name', max_length=100)
    resume = models.CharField('resume', max_length=256)
    deploy = models.URLField('deploy', max_length=256, blank=True)
    github = models.URLField('github', max_length=256, blank=True)
    description = models.TextField("description", blank=True)
    repository = models.BooleanField('active', default=True)
    img = StdImageField("Image", blank=True, upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480,'crop': True}})

    class Meta:
        verbose_name = 'projects'
        verbose_name_plural = 'project'

    def __str__(self):
        return self.title


