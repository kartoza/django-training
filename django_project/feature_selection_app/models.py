from django.db import models


class DoodleType(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'doodletype'
        verbose_name = ('Doodle Type')
        verbose_name_plural = ('Doodle Types')
        ordering = ('name',)


class Doodle(models.Model):
    name = models.CharField(max_length=255)
    doodle_type = models.ForeignKey(
        DoodleType) # , default=DoodleType.objects.get(id=1))
    doodle_date = models.DateTimeField(
        'DateAdded', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = ('Doodle')
        verbose_name_plural = ('Doodles')
        ordering = ('doodle_date',)

    def evaporate(self):
        """Make a doodle disaappear"""
        return "I am %s, I am disappear.......ing" % self.name
