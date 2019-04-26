# -FLOW TO CREATING MODELS-
# 1.Create A Blog Models
# 2.Add the Blog App to Settings
# 3.Make Migration
# 4.Migrate
# 5.Add to admin


from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:80]

    def pud_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')