from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Base(models.Model):
    name = models.CharField(max_length=55, unique=True)
    description = RichTextUploadingField(config_name='special',
                                     external_plugin_resources=[
                                         (
                                             'youtube',
                                             '/static/ckeditor_plugins/youtube/youtube/',
                                             'plugin.js'
                                         ),
                                         (
                                             'pastecode',
                                             '/static/ckeditor_plugins/pastecode/',
                                             'plugin.js'
                                         ),
                                     ],
                                     )
    image = models.ImageField(upload_to='documentation/images/', blank=True)
    url = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Language(Base):
    manual_order = models.IntegerField(default=1)
    icon = models.CharField(max_length=55, blank=True)

    def __str__(self):
        return self.name


class Framework(Base):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Topic(models.Model):
    title = models.CharField(max_length=55)
    slug = models.CharField(max_length=55, default='')
    sub_title = models.CharField(max_length=55, blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    framework = models.ForeignKey(Framework, on_delete=models.CASCADE, null=True, blank=True)
    content = RichTextUploadingField(config_name='special',
                                     external_plugin_resources=[
                                         (
                                             'youtube',
                                             '/static/ckeditor_plugins/youtube/youtube/',
                                             'plugin.js'
                                         ),
                                         (
                                             'pastecode',
                                             '/static/ckeditor_plugins/pastecode/',
                                             'plugin.js'
                                         ),
                                     ],
                                     )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['title', 'language', 'framework']

    def __str__(self):
        return self.title
