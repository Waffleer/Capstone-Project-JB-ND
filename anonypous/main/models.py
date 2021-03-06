from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, PROTECT
from django.db.models.fields import CharField
# Create your models here.

class documentcode(models.Model):
    code = models.CharField(max_length=16)

    def __str__(self):
        return f'''{self.code}'''

class profile(models.Model):
    email = models.EmailField(default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30, default='')
    lastname = models.CharField(max_length=30, default='')
    bio = models.TextField(default='no bio...')

    #true = teacher account, false = student account
    teacher = models.BooleanField(default=False)
    submissions = models.ManyToManyField(documentcode, blank=True)

    tagsNum = models.IntegerField(default=0)
    assignmentTagsNum = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'''{self.email}'''

class tags(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=PROTECT, default='')
    number = models.IntegerField(default=0)

    def __str__(self):
        return f'''{self.name}'''

class assignmentTags(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=PROTECT, default='')
    number = models.IntegerField(default=0)

    def __str__(self):
        return f'''{self.name}'''
    
class doc(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=PROTECT, default='')
    code = models.OneToOneField(documentcode, on_delete=CASCADE, default='')
    codestr = models.CharField(max_length=30, default='')

    text = models.TextField(default='')
    submissionDate = models.DateTimeField(null=True, blank=True)

    comment = models.TextField(default='')
    score = models.FloatField(blank=True, null=True)

    submitted = models.BooleanField(default=False)

    open = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'''Doc - {self.code}'''

class assignmentcode(models.Model):
    code = models.CharField(max_length=17)

    def __str__(self):
        return f'''{self.code}'''

class assignmentObj(models.Model):
    name = models.CharField(max_length=30)

    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    ownerstr = models.CharField(max_length=30, default='')

    code = models.OneToOneField(assignmentcode, on_delete=models.CASCADE, default='')
    codestr = models.CharField(max_length=30, default='')
    pointValue = models.IntegerField(default='-1')
    dueDate = models.DateTimeField(null=True, blank=True)

    submissions = models.ManyToManyField(doc, blank=True)
    instructions = models.TextField(default='Instructions')
    open = models.BooleanField(default=True)
    submitted = models.BooleanField(default=False)

    tags = models.ManyToManyField(assignmentTags, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'''{self.code}'''


class classcode(models.Model):
    code = models.CharField(max_length=6)

    def __str__(self):
        return f'''{self.code}'''

class classes(models.Model):
    name = models.CharField(max_length=30)

    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    ownerstr = models.CharField(max_length=30, default='')
    description = models.TextField(default='Description')
    code = models.OneToOneField(classcode, on_delete=CASCADE)
    codestr = models.CharField(max_length=6, default='')

    students = models.ManyToManyField(profile, blank=True)
    assignments = models.ManyToManyField(assignmentObj, blank=True)
    subject = models.CharField(max_length=10, default='')
    color = models.CharField(default='', max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    year = models.IntegerField(default=0000)

    tags = models.ManyToManyField(tags, blank=True)

    def __str__(self):
        return f'''{self.code}'''

