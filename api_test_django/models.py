from django.db import models

class Base(models.Model):
    creation_date = models.DateField(auto_now=True)
    update_date = models.DateField(auto_now=True)
    isActive = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Course(Base):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['id']

    def __str__(self):
        return self.title
    

class Evaluation(Base):
    course = models.ForeignKey(Course, related_name='evaluations', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comments = models.TextField(blank=True, default='')
    evaluation = models.DecimalField(max_digits=2,decimal_places=1)

    class Meta:
        verbose_name = 'Evaluation'
        verbose_name_plural = 'Evaluations'
        unique_together = [ 'email', 'course' ]
        ordering = ['id']

    def __str__(self):
        return f'{self.name} evaluated the course {self.course} with: {self.evaluation}'