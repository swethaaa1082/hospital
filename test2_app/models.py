from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.db import models
# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'department'
        verbose_name_plural = 'departments'

    def get_url(self):
        return reverse("doctors_by_department", args=[self.slug])

    def __str__(self):
            return '{}'.format(self.name)

class Doctor(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    img = models.ImageField(upload_to='department')
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    position=models.CharField(max_length=200)
    time=models.DecimalField(max_digits=10,decimal_places=2)
    available=models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'doctor'
        verbose_name_plural = 'doctors'
    def get_url(self):
         return reverse("DoctDetail", args=[self.department.slug,self.slug])
    def __str__(self):
        return '{}'.format(self.name)
class Task(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=100)
    email=models.EmailField()
    department=models.CharField(max_length=200)
    msg=models.TextField()


