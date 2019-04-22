# -FLOW TO CREATING MODELS-
# 1.Create A Blog Models
# 2.Add the Blog App to Settings
# 3.Create Migration
# 3.Migrate
# 4.Add to the admin


from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
