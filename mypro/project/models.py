from django.db import models

product_chioce = (
    ('','Choose your product'),
    ('Ecommerce','Ecommerce'),
    ('Social Media', 'Social Media'),
    ('SAAS','SAAS'),
    ('Search Engine','Search Engine'),
    ('Fintech','fintech'),
    ('others','Others'),
)

target_chioce = (
    ('','Choose target_name'),
    ('Male','Male'),
    ('Female', 'Female'),
    ('Upper Class','Upper Class'),
    ('Middle Class','Middle Class'),
    ('18 to 45', '18 to 45'),
    ('45 to 64','45 to 64'),
)

# Create your models here.
class TargetAudience(models.Model):
    target_name = models.CharField(max_length=50, choices=target_chioce, default=0)

    class Meta:
        verbose_name = 'TargetAudience'
        verbose_name_plural = 'TargetAudience'

    def __str__(self):
        return self.target_name

class ProjectRequirements(models.Model):
    product = models.CharField(max_length=100, choices=product_chioce, default='')
    solution_description = models.TextField(max_length=500)
    project_target = models.ManyToManyField(TargetAudience, default='')
    code_language_preference = models.BooleanField(default=False)
    code_language = models.CharField(max_length=50)
    have_buildups = models.BooleanField(default=False)
    buildups = models.FileField(upload_to='uploads/buildups')
    have_design_elements = models.BooleanField(default=False)
    design_elements = models.FileField(upload_to='uploads/design_elements')

    class Meta:
        verbose_name = 'ProjectRequirements'
        verbose_name_plural = 'ProjectRequirements'

    def __str__(self):
        return self.product
