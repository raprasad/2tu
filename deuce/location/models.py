from django.db import models


class Building(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
    
class Location(models.Model):
    
    building = models.ForeignKey(Building)
    
    name = models.CharField(max_length=255, )
    latitude = models.DecimalField(max_digits=12, decimal_places=8)
    longitude = models.DecimalField(max_digits=12, decimal_places=8)
    altitude = models.DecimalField(max_digits=12, decimal_places=2, help_text='in meters', default=0)

    slug = models.SlugField(blank=True)
    visible = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.building)
     
    class Meta:
        ordering = ['building', 'name']
        
        
        
        
    
    
        
