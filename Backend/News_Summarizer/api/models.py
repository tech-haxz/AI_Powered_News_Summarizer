from django.db import models

# Create your models here.
#Write models for storing summarized articles if needed in future expansions
class SummarizedArticle(models.Model):
    url = models.URLField(unique=True)
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url