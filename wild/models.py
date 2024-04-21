from django.db import models

class Question(models.Model):
    # Define fields for the Question model
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
