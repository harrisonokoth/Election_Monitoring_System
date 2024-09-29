from django.urls import path
from .views import home, data_visualization, submit_report, submit_report_success, view_reports, statistics_dashboard  # Import your view

urlpatterns = [
    path('', home, name='home'),
    path('data_visualization/', data_visualization, name='data_visualization'),
    path('submit_report/', submit_report, name='submit_report'),
    path('submit_report_success/', submit_report_success, name='submit_report_success'),
    path('view_reports/', view_reports, name='view_reports'),
    path('statistics_dashboard/', statistics_dashboard, name='statistics_dashboard'), 
]
