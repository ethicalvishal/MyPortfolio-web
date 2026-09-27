import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='Vishal Kumar', max_length=100)),
                ('role_title', models.CharField(default='Python Full Stack Developer', help_text="Shown under your name on the homepage, e.g. 'Python Full Stack Developer'", max_length=150)),
                ('tagline', models.CharField(blank=True, help_text='One-line hook shown on the homepage hero section.', max_length=250)),
                ('bio', models.TextField(blank=True, help_text='Longer paragraph(s) shown on the About page.')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('resume_file', models.FileField(blank=True, null=True, upload_to='resume/')),
                ('resume_preview_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('github_url', models.URLField(blank=True)),
                ('linkedin_url', models.URLField(blank=True)),
                ('instagram_url', models.URLField(blank=True)),
                ('twitter_url', models.URLField(blank=True)),
                ('years_experience', models.PositiveIntegerField(default=0)),
                ('projects_completed', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profile',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=150)),
                ('degree', models.CharField(max_length=150)),
                ('start_year', models.CharField(max_length=10)),
                ('end_year', models.CharField(blank=True, help_text='Leave blank if ongoing', max_length=10)),
                ('description', models.CharField(blank=True, max_length=300)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['order', '-start_year'],
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=150)),
                ('role', models.CharField(max_length=150)),
                ('start_date', models.CharField(max_length=20)),
                ('end_date', models.CharField(blank=True, help_text='Leave blank if this is your current role', max_length=20)),
                ('description', models.CharField(blank=True, max_length=300)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['order', '-start_date'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('category', models.CharField(choices=[('backend', 'Backend'), ('frontend', 'Frontend'), ('database', 'Database'), ('tools', 'Tools & Platforms'), ('other', 'Other')], default='backend', max_length=20)),
                ('proficiency', models.PositiveIntegerField(default=70, help_text='Skill level as a percentage, 0-100.')),
                ('icon_class', models.CharField(blank=True, help_text="Optional Bootstrap Icons class, e.g. 'bi-filetype-py'", max_length=60)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['category', 'order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=170, unique=True)),
                ('short_description', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('tech_stack', models.CharField(help_text="Comma separated, e.g. 'Python, Django, MySQL, Bootstrap'", max_length=250)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='images/projects/')),
                ('github_url', models.URLField(blank=True)),
                ('live_url', models.URLField(blank=True)),
                ('status', models.CharField(choices=[('live', 'Live'), ('in_progress', 'In Progress'), ('concept', 'Concept')], default='in_progress', max_length=20)),
                ('is_featured', models.BooleanField(default=False, help_text='Show on the homepage')),
                ('order', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['order', '-created_at'],
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=220, unique=True)),
                ('excerpt', models.CharField(blank=True, max_length=300)),
                ('content', models.TextField()),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='images/blog/')),
                ('is_published', models.BooleanField(default=True)),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-published_at'],
            },
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(blank=True, max_length=150)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
