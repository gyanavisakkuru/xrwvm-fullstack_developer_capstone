# Uncomment the imports before you add the code
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.urls import path  # Import path from django.urls


app_name = 'djangoapp'
urlpatterns = [
    # # path for registration
    path(route='Register', view=views.Register, name='Register'),


    # path for login
    path(route='login', view=views.login_user, name='login'),
    path(route='logout', view=views.logout_request, name='logout'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
