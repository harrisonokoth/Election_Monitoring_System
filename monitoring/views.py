# monitoring/views.py
from django.db import models                          
from django.shortcuts import render, redirect
from .forms import ReportForm
from .models import Report
from django.utils import timezone  

def home(request):
    return render(request, 'home.html')  # Rendering the home template
def data_visualization(request):
    reports = Report.objects.all().values('location', 'title', 'date_reported')  #We can  adjust fields as needed
    context = {
        'reports': list(reports),  # Converting QuerySet to a list
    }
    return render(request, 'data_visualization.html', context)
def submit_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)  # We Save the form data to a Report instance
            report.date_reported = timezone.now()  # Set the current date and time
            report.save()  # Now we save the report instance to the database
            return redirect('submit_report_success')  # Redirect to success page
    else:
        form = ReportForm()
    return render(request, 'report_form.html', {'form': form})

def view_reports(request):
    reports = Report.objects.all() 
    context = {
        'reports': reports,
    }
    return render(request, 'view_reports.html', context)  
def submit_report_success(request):
    return render(request, 'submit_report_success.html')  # Rendering the success template
def statistics_dashboard(request):
    # Logic for statistics in the dashboard
    total_reports = Report.objects.count()  # Total number of reports
    reports_by_location = Report.objects.values('location').annotate(count=models.Count('id')).order_by('-count')  # Number of reports by location
    common_issues = Report.objects.values('title').annotate(count=models.Count('id')).order_by('-count')[:5]  # Most common issues reported
    recent_reports = Report.objects.order_by('-date_reported')[:5]  # Recent reports

    context = {
        'total_reports': total_reports,
        'reports_by_location': list(reports_by_location),  # Converting to list for easy use in templates
        'common_issues': list(common_issues),  # Converting to list
        'recent_reports': recent_reports,  # Recent reports
    }
    
    return render(request, 'statistics_dashboard.html', context)  

def submit_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect or show a success message
    else:
        form = ReportForm()

    return render(request, 'report_form.html', {'form': form})