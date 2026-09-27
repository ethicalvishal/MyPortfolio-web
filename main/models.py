from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Profile(models.Model):
    """Singleton-style model holding the site owner's core info.
    Controlled entirely from the admin dashboard — no code changes needed
    to update the headline, bio, contact details, resume, or social links.
    """
    full_name = models.CharField(max_length=100, default="Vishal Kumar")
    role_title = models.CharField(
        max_length=150, default="Python Full Stack Developer",
        help_text="Shown under your name on the homepage, e.g. 'Python Full Stack Developer'"
    )
    tagline = models.CharField(
        max_length=250, blank=True,
        help_text="One-line hook shown on the homepage hero section."
    )
    bio = models.TextField(
        blank=True, help_text="Longer paragraph(s) shown on the About page."
    )
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)

    profile_image = models.ImageField(upload_to="images/", blank=True, null=True)
    resume_file = models.FileField(upload_to="resume/", blank=True, null=True)
    resume_preview_image = models.ImageField(upload_to="images/", blank=True, null=True)

    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)

    years_experience = models.PositiveIntegerField(default=0)
    projects_completed = models.PositiveIntegerField(default=0)
    currently_learning = models.CharField(
        max_length=300, blank=True,
        help_text="Shown on the About page, e.g. React, APIs, cloud deployment"
    )
    availability_text = models.CharField(
        max_length=120, default="Available for opportunities", blank=True
    )

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        # Keep this a true singleton: always overwrite row with pk=1.
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_instance(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class Education(models.Model):
    institution = models.CharField(max_length=150)
    degree = models.CharField(max_length=150)
    start_year = models.CharField(max_length=10)
    end_year = models.CharField(max_length=10, blank=True, help_text="Leave blank if ongoing")
    description = models.CharField(max_length=300, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-start_year"]

    def __str__(self):
        return f"{self.degree} — {self.institution}"


class Experience(models.Model):
    company = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    start_date = models.CharField(max_length=20)
    end_date = models.CharField(max_length=20, blank=True, help_text="Leave blank if this is your current role")
    description = models.CharField(max_length=300, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-start_date"]

    def __str__(self):
        return f"{self.role} at {self.company}"


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("backend", "Backend"),
        ("frontend", "Frontend"),
        ("database", "Database"),
        ("tools", "Tools & Platforms"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=60)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="backend")
    proficiency = models.PositiveIntegerField(
        default=70,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Skill level as a percentage, 0-100."
    )
    icon_class = models.CharField(
        max_length=60, blank=True,
        help_text="Optional icon class. Leave blank for automatic Python/Django/HTML/CSS/etc. icon mapping."
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["category", "order", "name"]

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

    @property
    def resolved_icon_class(self):
        if self.icon_class:
            return self.icon_class
        key = self.name.lower().replace(" ", "-").replace("&", "and")
        mapping = {
    "python": "devicon-python-plain",
    "django": "devicon-django-plain",
    "rest-apis": "bi bi-braces",
    "html": "devicon-html5-plain",
    "css": "devicon-css3-plain",
    "javascript": "devicon-javascript-plain",
    "bootstrap": "devicon-bootstrap-plain",
    "mysql": "devicon-mysql-original",
    "mongodb": "devicon-mongodb-plain",
    "git-and-github": "devicon-github-original",
    "git": "devicon-git-plain",
    "github": "devicon-github-original",
    "docker": "devicon-docker-plain",
    "react": "devicon-react-original",
}
        return mapping.get(key, "bi bi-code-slash")


class Service(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=280)
    icon_class = models.CharField(max_length=80, default="bi bi-code-slash", blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "title"]
        verbose_name = "What I Do"
        verbose_name_plural = "What I Do"

    def __str__(self):
        return self.title


class Certification(models.Model):
    name = models.CharField(max_length=180)
    issuer = models.CharField(max_length=150)
    issue_date = models.CharField(max_length=30, blank=True)
    credential_id = models.CharField(max_length=120, blank=True)
    credential_url = models.URLField(blank=True)
    certificate_image = models.ImageField(upload_to="images/certifications/", blank=True, null=True)
    description = models.CharField(max_length=300, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-id"]

    def __str__(self):
        return f"{self.name} — {self.issuer}"


class Achievement(models.Model):
    title = models.CharField(max_length=160)
    description = models.CharField(max_length=300, blank=True)
    year = models.CharField(max_length=20, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-id"]

    def __str__(self):
        return self.title


class Project(models.Model):
    STATUS_CHOICES = [
        ("live", "Live"),
        ("in_progress", "In Progress"),
        ("concept", "Concept"),
    ]

    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=170, unique=True, blank=True)
    short_description = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    tech_stack = models.CharField(
        max_length=250, help_text="Comma separated, e.g. 'Python, Django, MySQL, Bootstrap'"
    )
    thumbnail = models.ImageField(upload_to="images/projects/", blank=True, null=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="in_progress")
    is_featured = models.BooleanField(default=False, help_text="Show on the homepage")
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(",") if t.strip()]


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    excerpt = models.CharField(max_length=300, blank=True)
    content = models.TextField()
    cover_image = models.ImageField(upload_to="images/blog/", blank=True, null=True)
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.subject or 'No subject'}"
