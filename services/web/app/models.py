from django.db import models

class Municipality(models.Model):
    municode = models.IntegerField(unique=True)
    muniname = models.TextField()
    address_street = models.TextField(blank=True, null=True)
    address_city = models.TextField(blank=True, null=True)
    address_state = models.TextField(blank=True, null=True)
    address_zip = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    fax = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)
    activeinprogram = models.BooleanField(blank=True, null=True)
    defaultcodeset = models.IntegerField()
    occpermitissuingsource_sourceid = models.IntegerField()
    novprintstyle_styleid = models.IntegerField(blank=True, null=True)
    enablecodeenforcement = models.BooleanField(blank=True, null=True)
    enableoccupancy = models.BooleanField(blank=True, null=True)
    enablepublicceactionreqsub = models.BooleanField(blank=True, null=True)
    enablepublicceactionreqinfo = models.BooleanField(blank=True, null=True)
    enablepublicoccpermitapp = models.BooleanField(blank=True, null=True)
    enablepublicoccinspectodo = models.BooleanField(blank=True, null=True)
    munimanager_userid = models.IntegerField(blank=True, null=True)
    office_propertyid = models.IntegerField(blank=True, null=True)
    profile_profileid = models.IntegerField(blank=True, null=True)
    primarystaffcontact_userid = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    lastupdatedts = models.DateTimeField(blank=True, null=True)
    lastupdated_userid = models.IntegerField(blank=True, null=True)
    defaultoccperiod = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municipality'
