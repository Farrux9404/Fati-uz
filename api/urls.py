from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path


# library
# from library.views import listUser,detailUser
from api.views_crud.dissertationabstract import listUser,detailUser
from api.views_crud.category import category_listUser,category_detailUser
from api.views_crud.journalUzbekistan import journal_listUser,journal_detailUser



schema_view = get_schema_view(
   openapi.Info(
      title="Your API",
      default_version='v1',
      description="Description of your API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@yourapi.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)




urlpatterns = [

    # swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # library
    path('dissertation/', listUser, name='dissertation'),
    path('dissertation/<int:id>/', detailUser, name='dissertation'),
    path('category/', category_listUser, name='category'),
    path('category/<int:id>/', category_detailUser, name='category'),
    path('journal/', journal_listUser, name='journal'),
    path('journal/<int:id>/', journal_detailUser, name='journal_detail_user'),
    
]  