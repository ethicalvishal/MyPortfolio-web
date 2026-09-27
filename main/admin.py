from django.contrib import admin
from .models import (
    Profile, Education, Experience, Skill, Service, Certification, Achievement, Project, BlogPost, ContactMessage,
)

admin.site.site_header = "Vishal Portfolio — Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Manage your site content"


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Only one row ever exists — edit it to change everything shown
    on the homepage and about page (name, bio, resume, socials, etc.)."""
    list_display = ("full_name", "role_title", "email", "phone")

    fieldsets = (
        ("Identity", {"fields": ("full_name", "role_title", "tagline", "bio")}),
        ("Contact", {"fields": ("email", "phone", "location")}),
        ("Media", {"fields": ("profile_image", "resume_file", "resume_preview_image")}),
        ("Social links", {"fields": ("github_url", "linkedin_url", "instagram_url", "twitter_url")}),
        ("Stats (shown on homepage)", {"fields": ("years_experience", "projects_completed")}),
        ("About extras", {"fields": ("currently_learning", "availability_text")}),
    )

    def has_add_permission(self, request):
        # Singleton: block adding a second profile row.
        return not Profile.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "institution", "start_year", "end_year", "order")
    list_editable = ("order",)
    ordering = ("order",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("role", "company", "start_date", "end_date", "order")
    list_editable = ("order",)
    ordering = ("order",)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "proficiency", "order")
    list_filter = ("category",)
    list_editable = ("proficiency", "order")
    search_fields = ("name",)
    ordering = ("category", "order")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "order")
    list_filter = ("is_active",)
    list_editable = ("is_active", "order")
    search_fields = ("title", "description")
    ordering = ("order", "title")


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("name", "issuer", "issue_date", "order")
    list_editable = ("order",)
    search_fields = ("name", "issuer", "credential_id")
    ordering = ("order", "-id")


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("title", "year", "order")
    list_editable = ("order",)
    search_fields = ("title", "description")
    ordering = ("order", "-id")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "is_featured", "order", "created_at")
    list_filter = ("status", "is_featured")
    list_editable = ("is_featured", "order")
    search_fields = ("title", "tech_stack")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("order", "-created_at")


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "published_at")
    list_filter = ("is_published",)
    list_editable = ("is_published",)
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_at"
    ordering = ("-published_at",)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at", "is_read")
    list_filter = ("is_read", "created_at")
    list_editable = ("is_read",)
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("name", "email", "subject", "message", "created_at")
    ordering = ("-created_at",)

    def has_add_permission(self, request):
        # Messages only ever come in through the public contact form.
        return False
