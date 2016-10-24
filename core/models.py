import uuid

from django.db import models


class Proc(models.Model):
    long_id = models.CharField(max_length=36, default=uuid.uuid4)
    name = models.CharField(max_length=30)
    state = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    start_date = models.DateField()
    status = models.BooleanField()
    contact_person = models.ForeignKey(
        'Person', blank=True, null=True, related_name='+')
    delivery_person = models.ForeignKey(
        'Person', blank=True, null=True, related_name='+')
    last_updated = models.DateField(auto_now=True)
    icon = models.URLField(max_length=1000, blank=True)

    def __str__(self):
        return self.name


class Bread(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    start_term = models.DateField()
    end_term = models.DateField()
    proc = models.ForeignKey(Proc)

    def __str__(self):
        return str(self.proc)


class Hat(models.Model):
    long_id = models.CharField(max_length=36, unique=True, default=uuid.uuid4)
    grant = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    issue_date = models.DateField()
    proc = models.ForeignKey(Proc)

    def __str__(self):
        return '%s, %s' % (self.proc, self.long_id)


class Money(models.Model):
    class Meta:
        verbose_name_plural = "money"
    month = models.CharField(max_length=30)
    gains = models.DecimalField(max_digits=7, decimal_places=2)
    losses = models.DecimalField(max_digits=7, decimal_places=2)
    checked = models.BooleanField()
    link = models.URLField(blank=True)
    proc = models.ForeignKey(Proc)

    def __str__(self):
        return '%s, %s' % (self.proc, self.month)


class Doc(models.Model):
    long_id = models.CharField(max_length=36, unique=True, default=uuid.uuid4)
    effective = models.DateField()
    expires = models.DateField()
    checked = models.BooleanField()
    link = models.URLField(blank=True)
    proc = models.ForeignKey(Proc)

    def __str__(self):
        return '%s, %s' % (self.proc, self.long_id)


class Person(models.Model):
    class Meta:
        verbose_name_plural = "people"
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    title = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)
    icon = models.URLField(max_length=1000, blank=True)

    def __str__(self):
        return self.name
