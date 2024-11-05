import matplotlib
matplotlib.use('Agg')


import matplotlib.pyplot as plt
from django.utils import timezone
from .models import Visitor
import io
import base64


def generate_charts():
    total_visitors = Visitor.objects.all().count()
    checked_in = Visitor.objects.filter(status='check-in').count()
    checked_out = Visitor.objects.filter(status='check-out').count()
    today = timezone.now().date()
    today_visit = Visitor.objects.filter(date=today).count()

    # Create a pie chart for checked-in and checked-out visitors
    pie_labels = ['Checked In', 'Checked Out']
    pie_values = [checked_in, checked_out]

    plt.figure(figsize=(5, 5))
    plt.pie(pie_values, labels=pie_labels, autopct='%1.1f%%', startangle=90, colors=['yellow', 'red'])
    plt.title('Check-in vs Check-out Visitors')

    # Save the pie chart to a BytesIO object
    buf_pie = io.BytesIO()
    plt.savefig(buf_pie, format='png')
    plt.close()
    buf_pie.seek(0)

    # Encode the pie chart image to base64
    pie_image = base64.b64encode(buf_pie.read()).decode('utf-8')

    # Create a bar chart for total visitors, checked-in, checked-out, and today's visitors
    bar_labels = ['Total Visitors', 'Checked In', 'Checked Out', 'Today\'s Visitors']
    bar_values = [total_visitors, checked_in, checked_out, today_visit]

    plt.figure(figsize=(5,5))
    plt.bar(bar_labels, bar_values, color=['blue', 'green', 'orange', 'red'])
    plt.title('Visitor Statistics')
    plt.xlabel('Categories')
    plt.ylabel('Number of Visitors')

    # Save the bar chart to a BytesIO object
    buf_bar = io.BytesIO()
    plt.savefig(buf_bar, format='png')
    plt.close()
    buf_bar.seek(0)

    # Encode the bar chart image to base64
    bar_image = base64.b64encode(buf_bar.read()).decode('utf-8')

    return  {
        'total_visitors': total_visitors,
        'checked_in': checked_in,
        'checked_out': checked_out,
        'today_visit': today_visit,
        'pie_image': pie_image,
        'bar_image': bar_image,
    }

