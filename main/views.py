from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ContactForm
from .models import Profile, Education, Experience, Skill, Service, Certification, Achievement, Project, BlogPost


def home(request):
    context = {
        "profile": Profile.get_instance(),
        "featured_projects": Project.objects.filter(is_featured=True)[:3],
        "top_skills": Skill.objects.all()[:8],
        "latest_posts": BlogPost.objects.filter(is_published=True)[:3],
        "services": Service.objects.filter(is_active=True)[:6],
    }
    return render(request, "main/home.html", context)


def about(request):
    context = {
        "profile": Profile.get_instance(),
        "education": Education.objects.all(),
        "experience": Experience.objects.all(),
        "services": Service.objects.filter(is_active=True)[:6],
        "certifications": Certification.objects.all(),
        "achievements": Achievement.objects.all(),
    }
    return render(request, "main/about.html", context)


def skills(request):
    all_skills = Skill.objects.all()
    grouped = []
    for code, label in Skill.CATEGORY_CHOICES:
        items = [s for s in all_skills if s.category == code]
        if items:
            grouped.append({"code": code, "label": label, "skills": items})

    context = {
        "profile": Profile.get_instance(),
        "grouped_skills": grouped,
    }
    return render(request, "main/skills.html", context)


def projects(request):
    context = {
        "profile": Profile.get_instance(),
        "projects": Project.objects.all(),
    }
    return render(request, "main/projects.html", context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    context = {
        "profile": Profile.get_instance(),
        "project": project,
        "related_projects": Project.objects.exclude(pk=project.pk)[:3],
    }
    return render(request, "main/project_detail.html", context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks! Your message has been sent — I'll get back to you soon.")
            return redirect("contact")
        messages.error(request, "Please fix the errors below and try again.")
    else:
        form = ContactForm()

    context = {
        "profile": Profile.get_instance(),
        "form": form,
    }
    return render(request, "main/contact.html", context)


def blog_list(request):
    post_list = BlogPost.objects.filter(is_published=True)
    paginator = Paginator(post_list, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "profile": Profile.get_instance(),
        "page_obj": page_obj,
    }
    return render(request, "main/blog_list.html", context)


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    context = {
        "profile": Profile.get_instance(),
        "post": post,
        "recent_posts": BlogPost.objects.filter(is_published=True).exclude(pk=post.pk)[:4],
    }
    return render(request, "main/blog_detail.html", context)
