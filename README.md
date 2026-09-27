💼 Vishal Portfolio Website

A multi-page personal portfolio built with Django, Bootstrap 5, and a fully
admin-controlled content system — no code edits needed to update your bio,
skills, projects, or blog.

---

📌 Pages

- **Home** — hero, stats, featured skills, featured projects, latest blog posts
- **About** — full bio, what I do, experience, education, certifications, achievements, current learning
- **Skills** — skills grouped by category, real technology icons, animated proficiency bars
- **Projects** — full project grid + individual project detail pages
- **Blog** — full blog with individual post pages and pagination
- **Contact** — working contact form (messages are saved and visible in the admin dashboard)

---

🛠 Admin dashboard — control everything

Every piece of content on the site is editable from `/admin/`:

| Section          | What you control                                      |
|-------------------|--------------------------------------------------------|
| **Profile**       | Name, title, tagline, full bio, contact info, resume, photo, social links, stats, availability, current learning |
| **Education**     | Add/remove/reorder education entries                   |
| **Experience**    | Add/remove/reorder work experience entries              |
| **What I Do**    | Manage service cards shown on Home/About                |
| **Certifications** | Add certificate name, issuer, date, credential link/image |
| **Achievements** | Add milestones, awards or learning highlights            |
| **Skills**        | Add skills, set category + proficiency %                |
| **Projects**      | Add projects, mark as featured, set status, tech stack   |
| **Blog Posts**    | Write, publish/unpublish, and edit blog posts            |
| **Contact Messages** | Read messages submitted through the contact form     |

No template or Python edits are needed for routine updates — just log in to
the admin dashboard.

---

🛠 Tech Stack

- Python / Django 6
- SQLite by default (MySQL optional, see below)
- Bootstrap 5 + Bootstrap Icons
- Custom design system (Fraunces / Inter / JetBrains Mono, "drafting table" theme)
- WhiteNoise for static files in production

---

⚙️ Local setup

```bash
# 1. Clone the repository
git clone https://github.com/ethicalvishal/myPortfolio.git
cd MyPortFolio

# 2. Create and activate a virtual environment
python -m venv env
env\Scripts\activate        # Windows
source env/bin/activate     # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
copy .env.example .env      # Windows
cp .env.example .env        # macOS/Linux
# then edit .env and set a real DJANGO_SECRET_KEY (see below)

# 5. Apply migrations (creates the DB + loads starter content)
python manage.py migrate

# 6. Create an admin account
python manage.py createsuperuser

# 7. Run the server
python manage.py runserver
```

Then visit `http://127.0.0.1:8000/` for the site and
`http://127.0.0.1:8000/admin/` to manage content.

**Generate a real secret key** (paste the output into `.env`):
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

🗄 Using MySQL instead of SQLite

SQLite is the default (zero setup). To use MySQL, install `mysqlclient`
(`pip install mysqlclient`), then set these in your `.env`:

```
DJANGO_DB_ENGINE=mysql
DJANGO_DB_NAME=portfolio
DJANGO_DB_USER=root
DJANGO_DB_PASSWORD=your-password
DJANGO_DB_HOST=localhost
DJANGO_DB_PORT=3306
```

---

🚀 Deployment notes

- Set `DJANGO_DEBUG=False` and `DJANGO_ALLOWED_HOSTS` to your real domain(s)
  in production — never leave `DEBUG=True` or `ALLOWED_HOSTS=*` on a live site.
- `DJANGO_SECRET_KEY` must be set as a real environment variable on your host
  (Render, Railway, etc.) — it should never be committed to git.
- On most free-tier hosts, local disk storage (including `media/` uploads)
  is wiped on every deploy/restart. For production, connect `media/` to
  persistent storage (e.g. Cloudinary or S3) if you'll be uploading images
  through the admin dashboard regularly.
- `build.sh` already runs `collectstatic` and `migrate` on deploy.

---

📌 Future Improvements

- Add tags/categories to blog posts
- Add a project image gallery (multiple images per project)
- Add dark mode toggle
- Email notification on new contact messages

---

👨‍💻 Author

Vishal Kumar

- GitHub: https://github.com/ethicalvishal
- LinkedIn: https://www.linkedin.com/in/vishal-kumar-python/

---

⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!
