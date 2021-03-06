from django.conf.urls.defaults import patterns, include, url
from carpooling.views import login, overview, user, route, user_routes, user_routes_history

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    ('^login/$',login),
    ('^overview/$',overview),
    ('^user/(\d{0,4})$',user),
    ('^route/(\d{0,4})$',route),    
    ('^routes/(\d{0,4})$',user_routes),
    ('^history/(\d{0,4})$',user_routes_history),   

    # Examples:
    # url(r'^$', 'opencarpooling.views.home', name='home'),
    # url(r'^opencarpooling/', include('opencarpooling.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
