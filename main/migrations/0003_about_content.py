from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import migrations, models


def seed_about_content(apps, schema_editor):
    Profile = apps.get_model('main', 'Profile')
    Skill = apps.get_model('main', 'Skill')
    Service = apps.get_model('main', 'Service')

    profile = Profile.objects.filter(pk=1).first()
    if profile:
        if not profile.availability_text:
            profile.availability_text = 'Available for opportunities'
        profile.save(update_fields=['availability_text'])

    icons = {
        'Python': 'devicon-python-plain',
        'Django': 'devicon-django-plain',
        'REST APIs': 'bi bi-braces',
        'HTML': 'devicon-html5-plain',
        'CSS': 'devicon-css3-plain',
        'JavaScript': 'devicon-javascript-plain',
        'Bootstrap': 'devicon-bootstrap-plain',
        'MySQL': 'devicon-mysql-original',
        'MongoDB': 'devicon-mongodb-plain',
        'Git & GitHub': 'devicon-github-original',
    }
    for name, icon in icons.items():
        Skill.objects.filter(name=name, icon_class='').update(icon_class=icon)

    defaults = [
        ('Django Web Development', 'Build structured, database-backed web applications with Django.', 'bi bi-window-stack', 1),
        ('REST API Development', 'Create clean API endpoints for web and mobile applications.', 'bi bi-braces', 2),
        ('Database Integration', 'Connect applications with relational and NoSQL databases.', 'bi bi-database', 3),
        ('Responsive UI', 'Turn ideas into clean, responsive interfaces that work across devices.', 'bi bi-phone', 4),
    ]
    for title, description, icon_class, order in defaults:
        Service.objects.get_or_create(title=title, defaults={
            'description': description,
            'icon_class': icon_class,
            'order': order,
            'is_active': True,
        })


def reverse_about_content(apps, schema_editor):
    Service = apps.get_model('main', 'Service')
    Service.objects.filter(title__in=[
        'Django Web Development', 'REST API Development', 'Database Integration', 'Responsive UI'
    ]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0002_seed_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='availability_text',
            field=models.CharField(blank=True, default='Available for opportunities', max_length=120),
        ),
        migrations.AddField(
            model_name='profile',
            name='currently_learning',
            field=models.CharField(blank=True, default='', help_text='Shown on the About page, e.g. React, APIs, cloud deployment', max_length=300),
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160)),
                ('description', models.CharField(blank=True, max_length=300)),
                ('year', models.CharField(blank=True, max_length=20)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={'ordering': ['order', '-id']},
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180)),
                ('issuer', models.CharField(max_length=150)),
                ('issue_date', models.CharField(blank=True, max_length=30)),
                ('credential_id', models.CharField(blank=True, max_length=120)),
                ('credential_url', models.URLField(blank=True)),
                ('certificate_image', models.ImageField(blank=True, null=True, upload_to='images/certifications/')),
                ('description', models.CharField(blank=True, max_length=300)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={'ordering': ['order', '-id']},
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=280)),
                ('icon_class', models.CharField(blank=True, default='bi bi-code-slash', max_length=80)),
                ('order', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={'ordering': ['order', 'title'], 'verbose_name': 'What I Do', 'verbose_name_plural': 'What I Do'},
        ),
        migrations.AlterField(
            model_name='skill',
            name='proficiency',
            field=models.PositiveIntegerField(default=70, help_text='Skill level as a percentage, 0-100.', validators=[MinValueValidator(0), MaxValueValidator(100)]),
        ),
        migrations.RunPython(seed_about_content, reverse_about_content),
    ]
