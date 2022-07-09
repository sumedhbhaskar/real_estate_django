
from django.contrib import admin
from django.urls import path
from listings import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'real_estate'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.ListingList.as_view(),name="listings_list"),
    # path("",views.listings_list),

    # path("create/",views.listings_create),
    path('create/',views.ListingCreate.as_view()),

    # path("<int:pk>/",views.listings_retrive),
    path('<int:pk>/',views.ListingDetails.as_view(),name="listing_detail"),

    path("update/<int:pk>",views.listings_update),
    path("delete/<int:pk>",views.delete_listings),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


