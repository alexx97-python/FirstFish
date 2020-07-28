from django.db import models
import uuid


class News(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=300, blank=False, null=False, verbose_name='Title', )
    content = models.TextField(blank=False, verbose_name="Main Content")
    published = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news/', default='null')
    rubric = models.ForeignKey('Rubric', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'Newses'
        ordering = ['published']

    def __str__(self):
        return self.title


class Rubric(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Rubrics')

    class Meta:
        verbose_name = 'Rubric'
        verbose_name_plural = 'Rubrics'
        ordering = ['name']

    def __str__(self):
        return self.name