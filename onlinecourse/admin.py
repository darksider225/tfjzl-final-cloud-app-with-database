from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# <HINT> Register QuestionInline and ChoiceInline classes here

# Inline class to allow editing Lessons directly inside the Course admin page
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5  # number of empty lesson forms shown by default

# Inline class to allow editing Questions directly inside another model’s admin page
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2  # number of empty question forms shown by default

# Inline class to allow editing Choices directly inside the Question admin page
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2  # number of empty choice forms shown by default

# Register your models here.

# Custom admin for Course model
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]  # show lessons inline when editing a course
    list_display = ('name', 'pub_date')  # show these fields in the course list view
    list_filter = ['pub_date']  # add filter sidebar for publication date
    search_fields = ['name', 'description']  # enable search by name or description

# Custom admin for Question model
class QuestionAdmin(admin.ModelAdmin):  # fixed typo: was 'admmin.ModelAdmin'
    inlines = [ChoiceInline]  # show choices inline when editing a question
    list_display = ['content']  # show question content in the list view

# Custom admin for Lesson model
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']  # show lesson title in the list view

# <HINT> Register Question and Choice models here

# Register models with their custom admin configurations
admin.site.register(Course, CourseAdmin)     # Course with custom admin
admin.site.register(Lesson, LessonAdmin)     # Lesson with custom admin
admin.site.register(Instructor)              # Instructor with default admin
admin.site.register(Learner)                 # Learner with default admin
admin.site.register(Question, QuestionAdmin) # Question with custom admin
admin.site.register(Choice)                  # Choice with default admin
admin.site.register(Submission)              # Submission with default admin
