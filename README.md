# OnlineCourse

A Django-based online learning platform where learners can browse courses, create accounts, enroll in courses, complete assessments, and view their results. The project includes a relational data model for instructors, learners, courses, lessons, enrollments, questions, answer choices, and exam submissions.

## Features

- Browse courses ordered by enrollment count
- View course details, lessons, descriptions, and instructors
- Register, sign in, and sign out using Django authentication
- Enroll in courses and track enrollment totals
- Support multiple enrollment modes, including audit, honor, and beta
- Create course assessments with questions and multiple choices
- Submit answers and calculate an assessment grade
- Display exam results after submission
- Manage application data through the Django admin site
- Serve static and uploaded course media files
- Deploy with Gunicorn to a Python-compatible cloud platform

## Technology Stack

- **Backend:** Python, Django
- **Database:** SQLite by default; compatible with other Django-supported relational databases
- **Frontend:** HTML, CSS, JavaScript, and Bootstrap-based Django templates
- **Media processing:** Pillow
- **Production server:** Gunicorn
- **Deployment:** Includes configuration for IBM Cloud Foundry-style deployment
- **Runtime:** Python 3.8.13, as specified in `runtime.txt`

## Project Structure

```text
.
├── manage.py                 # Django command-line utility
├── myproject/                # Django project configuration and WSGI entry point
├── onlinecourse/             # Courses, enrollments, assessments, views, and templates
├── static/                   # Static assets and course media
├── requirements.txt          # Python dependencies
├── Procfile                  # Gunicorn process definition
├── manifest.yml              # Cloud Foundry deployment configuration
└── runtime.txt               # Python runtime version
```

## Getting Started

### Prerequisites

- Python 3.8 or a compatible Python environment
- `pip`
- Git

### 1. Clone the repository

```bash
git clone https://github.com/darksider225/tfjzl-final-cloud-app-with-database.git
cd tfjzl-final-cloud-app-with-database
```

### 2. Create and activate a virtual environment

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure the application

For local development, the project uses SQLite by default. Before deploying, configure environment-specific settings rather than committing secrets to source control.

At minimum, review the following settings in `myproject/settings.py`:

- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`
- `CSRF_TRUSTED_ORIGINS`
- Database connection settings
- Static and media storage settings

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Create an administrator account

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in your browser. The Django admin site is available at <http://127.0.0.1:8000/admin/>.

## Typical Workflow

1. Register a learner account or sign in.
2. Browse the available courses.
3. Open a course to review its information and lessons.
4. Enroll in the course.
5. Complete the course assessment.
6. Submit answers and review the calculated result.

Course and assessment data can be created through the Django admin interface. The relevant models include:

- `Instructor`
- `Learner`
- `Course`
- `Lesson`
- `Enrollment`
- `Question`
- `Choice`
- `Submission`

## Data Model

The assessment system associates questions with courses, choices with questions, and submissions with a learner's course enrollment. A submission can contain multiple selected choices, allowing questions with more than one correct answer.

Reference ER diagram:

![OnlineCourse ER Diagram](https://github.com/ibm-developer-skills-network/final-cloud-app-with-database/blob/master/static/media/course_images/onlinecourse_app_er.png)

## Deployment

The repository includes a `Procfile` for Gunicorn:

```text
web: gunicorn myproject.wsgi
```

It also includes a `manifest.yml` intended for Cloud Foundry-style deployments. Before deploying:

1. Replace placeholder routes in `manifest.yml` with your application routes.
2. Set production values for `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS`.
3. Configure a production database and persistent media storage where appropriate.
4. Run migrations on the deployed environment:

   ```bash
   python manage.py migrate
   ```

5. Collect static files if required by your hosting platform:

   ```bash
   python manage.py collectstatic --noinput
   ```

The included deployment files are a starting point and may need platform-specific adjustments.

## Development Notes

- Do not use `DEBUG = True` in production.
- Do not expose or reuse the development `SECRET_KEY` in a deployed application; generate a new secret and load it from an environment variable.
- Add the deployed host to `ALLOWED_HOSTS` and configure trusted origins for HTTPS.
- Use a production-ready database instead of SQLite for multi-user production workloads.
- Keep uploaded media separate from the application filesystem when the hosting platform uses ephemeral storage.

## License

This project is distributed under the terms of the license in the [`LICENSE`](LICENSE) file.
