from django.db import models

def cube_default():
    return Cube.objects.get_or_create(name="X Man Tornado V2")[0]

def eventType_default():
    return EventType.objects.get_or_create(name="3x3")[0]

class Cube(models.Model):
    name = models.CharField(primary_key=True, max_length=200)

class EventType(models.Model):
    name = models.CharField(primary_key=True, max_length=200)

class Tag(models.Model):
    name = models.CharField(primary_key=True, max_length=200)

class Session(models.Model):
    id = models.AutoField(primary_key=True)
    startDateTime = models.DateTimeField(null=True)
    endDateTime = models.DateTimeField(null=True)
    cubeUsed = models.ForeignKey(Cube, on_delete=models.RESTRICT, default=cube_default)
    note = models.CharField(max_length=600, null=True)
    eventType = models.ForeignKey(EventType, default=eventType_default, on_delete=models.RESTRICT)


class Attempt(models.Model):
    id = models.AutoField(primary_key=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    time = models.FloatField()
    datetime = models.DateTimeField(null=True)
    scramble = models.CharField(max_length=300)
    plusTwo = models.BooleanField()
    DNF = models.BooleanField()
    note = models.CharField(max_length=600, null=True)
    tags = models.ManyToManyField(Tag)

class SessionJSON(models.Model):
    upload = models.FileField(upload_to="sessions")