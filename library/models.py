from django.db import models


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)



class Category(BaseModel):
    title = models.CharField(max_length=250)
    parent_id = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=150)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Dissertationabstract(BaseModel):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/library/dissertation_abstract')
    file = models.FileField(upload_to='images/library/dissertation_abstract', blank=True, null=True)
    status = models.CharField(max_length=150)
    content = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)
    center_id = models.ForeignKey(Category, related_name='dissertation_abstract', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title




class JournalUzbekistan(BaseModel):
    title = models.CharField(max_length=250)
    status = models.CharField(max_length=150)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title