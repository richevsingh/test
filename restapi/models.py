from django.db import models


class snapp(models.Model):
#    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paragraph = models.CharField(max_length=225, null=True, blank=False)
    label = models.CharField(max_length=225, null=True, blank=False)
    textbox = models.CharField(max_length=225, null=True, blank=False)
    userid = models.IntegerField(max_length=25, blank=False, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return "{}".format(self.paragraph)