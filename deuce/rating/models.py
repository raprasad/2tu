from django.db import models
from location.models import Location
from django.contrib.auth.models import User

rating_choices = map(lambda x: (x,x), range(1,11))

class Rating(models.Model):
    user = models.ForeignKey(User)
    location = models.ForeignKey(Location)
    units = models.IntegerField(choices=rating_choices)

    def __unicode__(self):
        return '%s %s (%s)' % (self.user, self.units, self.location)

    class Meta:
        ordering = ['location', '-units', 'user']
