from django.db import models

class Todo(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length = 300)

    def __str__(self):
        return '{}'.format(self.text)
        
    class Meta:
        verbose_name_plural = 'Todos'