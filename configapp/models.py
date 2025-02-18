from django.db import models

# Create your models here.
class Kurs(models.Model):
    title=models.CharField(max_length=100, verbose_name='kursning nomi')
    start_time = models.TimeField(verbose_name='Boshlanish vaqti')
    end_time = models.TimeField(verbose_name='Tugash vaqti')
    description = models.TextField(verbose_name='Tavsif')
    created_ed = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqt')
    updated_ed = models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqt')
    is_bool = models.BooleanField(default=True)


    class Meta:
        verbose_name='kurs'
        verbose_name_plural = 'kurslar'
        ordering = ['title']

    def __str__(self):
        return self.title





class Student(models.Model):
    full_name=models.CharField(max_length=100, verbose_name='tuliq ismi')
    phone_number=models.CharField(max_length=13, verbose_name='telefon numer')
    email=models.EmailField(unique=True, verbose_name='email')
    kurs=models.ManyToManyField(Kurs, related_name='students', verbose_name='kurs')
    created_ed=models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqt')
    updated_ed = models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqt')
    is_bool = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'talaba'
        verbose_name_plural = 'talabalar'
        ordering = ['full_name']

    def __str__(self):
        return self.full_name


