from django.db import models


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)


class Centralsection(BaseModel):
    title = models.CharField(max_length=250)
    file = models.FileField(upload_to='images/centers_departments/centralsection')
    status = models.CharField(max_length=150)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Central section'
        verbose_name_plural = 'Central sections'

    def __str__(self):
        return self.title or ''


class Departmenthistory(BaseModel):
    title = models.CharField(max_length=250)
    file = models.FileField(upload_to='images/centers_departments/departmenthistory', blank=True, null=True)
    status = models.CharField(max_length=150)
    content = models.TextField()
    center_id = models.ForeignKey(Centralsection, related_name='departmen_thistory', on_delete=models.CASCADE, blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Department history'
        verbose_name_plural = 'Department historys'

    def __str__(self):
        return self.title or ''


class Members(BaseModel):
    title = models.CharField(max_length=250)
    file = models.FileField(upload_to='images/centers_departments/members', blank=True, null=True)
    birth_date = models.IntegerField()
    status = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    academic_degree = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, blank=True, null=True)
    content = models.TextField()
    link = models.URLField()  # Pilus belgisini olib tashlandi
    center_id = models.ForeignKey(Centralsection, related_name='members', on_delete=models.CASCADE, blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    def __str__(self):
        return self.title or ''


class MembersExpert(BaseModel):
    expert_member = models.ForeignKey(Members, on_delete=models.CASCADE, related_name='members_expert', blank=True, null=True)
    full_name = models.CharField(max_length=250)
    activity_institution = models.CharField(max_length=250)
    year_of_visit = models.IntegerField()





class Picture(BaseModel):
    title = models.CharField(max_length=250)
    base_file = models.FileField(upload_to='images/centers_departments/picture', blank=True, null=True)
    image = models.ImageField(upload_to='images/centers_departments/picture')
    status = models.CharField(max_length=150)
    center_id = models.ForeignKey(Centralsection, related_name='picture', on_delete=models.CASCADE, blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Picture'
        verbose_name_plural = 'Pictures'

    def __str__(self):
        return self.title or ''


class Video(BaseModel):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/centers_departments/video')
    status = models.CharField(max_length=150)
    center_id = models.ForeignKey(Centralsection, related_name='video', on_delete=models.CASCADE, blank=True, null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title or ''


class Research(BaseModel):
    title = models.CharField(max_length=250)
    base_file = models.FileField(upload_to='images/centers_departments/research', blank=True, null=True)
    content = models.TextField()
    status = models.CharField(max_length=150)
    center_id = models.ForeignKey(Centralsection, related_name='research', on_delete=models.CASCADE, blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Research'
        verbose_name_plural = 'Researchs'

    def __str__(self):
        return self.title or ''
