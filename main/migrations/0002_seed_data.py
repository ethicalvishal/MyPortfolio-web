from django.db import migrations


def seed_data(apps, schema_editor):
    Profile = apps.get_model('main', 'Profile')
    Education = apps.get_model('main', 'Education')
    Skill = apps.get_model('main', 'Skill')
    Project = apps.get_model('main', 'Project')
    BlogPost = apps.get_model('main', 'BlogPost')

    Profile.objects.get_or_create(pk=1, defaults=dict(
        full_name="Vishal Kumar",
        role_title="Python Full Stack Developer",
        tagline="I build web applications using Python, Django, MySQL and modern technologies.",
        bio=(
            "Hi, I'm Vishal Kumar, a passionate developer currently learning Django and "
            "building real-world projects. I enjoy solving problems and developing web "
            "applications using modern technologies."
        ),
        email="vishalkumarmth091@gmail.com",
        phone="9709851977",
        location="India",
        profile_image="images/Vishal.jpg",
        resume_file="resume/Vishal_resume.pdf",
        resume_preview_image="images/resume-preview.png",
        github_url="https://github.com/ethicalvishal",
        linkedin_url="https://www.linkedin.com/in/vishal-kumar-python/",
        years_experience=1,
        projects_completed=3,
    ))

    Education.objects.get_or_create(
        institution="BCA Program", degree="Bachelor of Computer Applications",
        start_year="2023", end_year="", order=1,
        description="Currently pursuing BCA alongside self-driven full stack projects.",
    )

    skills = [
        ("Python", "backend", 80, 1),
        ("Django", "backend", 75, 2),
        ("REST APIs", "backend", 65, 3),
        ("MySQL", "database", 70, 1),
        ("MongoDB", "database", 55, 2),
        ("HTML", "frontend", 85, 1),
        ("CSS", "frontend", 75, 2),
        ("JavaScript", "frontend", 60, 3),
        ("Bootstrap", "frontend", 70, 4),
        ("Git & GitHub", "tools", 65, 1),
    ]
    for name, category, proficiency, order in skills:
        Skill.objects.get_or_create(
            name=name, category=category,
            defaults=dict(proficiency=proficiency, order=order),
        )

    projects = [
        dict(
            title="Expense Tracker",
            slug="expense-tracker",
            short_description="A Django-based web app to track daily expenses with authentication and CRUD operations.",
            description=(
                "A Django-based web app to track daily expenses with authentication, "
                "CRUD operations, and database integration. Currently improving UI and features."
            ),
            tech_stack="Python, Django, MySQL, Bootstrap",
            status="in_progress",
            is_featured=True,
            order=1,
        ),
        dict(
            title="Job Portal System",
            slug="job-portal-system",
            short_description="A job portal platform with user & recruiter dashboards, job posting, and search.",
            description=(
                "A job portal platform with user and recruiter dashboards, job posting, "
                "and search functionality. Currently in development."
            ),
            tech_stack="Django, Bootstrap, JavaScript",
            status="in_progress",
            is_featured=True,
            order=2,
        ),
        dict(
            title="InstaTubeAI",
            slug="instatubeai",
            short_description="A social media platform concept with AI-based features for content and interaction.",
            description=(
                "A social media platform idea with AI-based features for content and "
                "interaction. Currently at the concept stage."
            ),
            tech_stack="AI, Django, React (Planned)",
            status="concept",
            is_featured=True,
            order=3,
        ),
    ]
    for p in projects:
        Project.objects.get_or_create(slug=p["slug"], defaults=p)

    BlogPost.objects.get_or_create(
        slug="why-i-rebuilt-my-portfolio-with-django",
        defaults=dict(
            title="Why I switched my portfolio from a single page to a full Django site",
            excerpt="A quick look at why separate pages, an admin dashboard, and a blog made this portfolio easier to grow.",
            content=(
                "When I first built this portfolio, everything lived on one long page. "
                "It worked, but every update meant editing HTML directly.\n\n"
                "Rebuilding it as a proper multi-page Django site means every section — "
                "About, Skills, Projects, Blog — now has its own page, and every bit of "
                "content is editable from the admin dashboard without touching code."
            ),
            is_published=True,
        ),
    )


def unseed_data(apps, schema_editor):
    Profile = apps.get_model('main', 'Profile')
    Education = apps.get_model('main', 'Education')
    Skill = apps.get_model('main', 'Skill')
    Project = apps.get_model('main', 'Project')
    BlogPost = apps.get_model('main', 'BlogPost')
    Profile.objects.filter(pk=1).delete()
    Education.objects.all().delete()
    Skill.objects.all().delete()
    Project.objects.all().delete()
    BlogPost.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data, unseed_data),
    ]