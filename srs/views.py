# views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from datetime import datetime
from .models import Leave
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from datetime import datetime
from .models import Leave
from django.db.models import Q


def index(request):
    if request.method == 'POST':
        leave_type = request.POST.get('leaveType')
        start_date_str = request.POST.get('startDate')
        end_date_str = request.POST.get('endDate')
        description = request.POST.get('description')

        # Validate and save to the database
        if leave_type and start_date_str and end_date_str and description:
            # Parse date strings into datetime objects
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()

            Leave.objects.create(
                leave_type=leave_type,
                start_date=start_date,
                end_date=end_date,
                description=description
            )

            # Redirect to the 'view_leave' page after successfully adding a leave
            return redirect('view_leave')

    # Handle GET request or render a different page
    return render(request, 'index.html')
           

    # Handle GET request or render a different page
    return render(request, 'index.html') 


def view_leave(request):
    # Fetch all leave records from the database
    leaves = Leave.objects.all()

    # Handle search query
 

    # Pass the leaves to the template for rendering
    return render(request, 'view_leave.html', {'leaves': leaves})



def update_view_leave(request, leave_id):
    leave = get_object_or_404(Leave, id=leave_id)

    if request.method == 'POST':
        # Process the form data when the form is submitted
        leave.leave_type = request.POST.get('leave_type')
        leave.start_date = request.POST.get('start_date')
        leave.end_date = request.POST.get('end_date')
        leave.description = request.POST.get('description')

        # Save the leave object directly, assuming your form is correctly configured
        leave.save()

        # Redirect to the 'view_leave' page
        return redirect('view_leave')

    else:
        # Render the update form
        return render(request, 'update_view_leave.html', {'leave': leave})


def delete_leave(request, leave_id):
    # Get the leave object to be deleted
    leave = get_object_or_404(Leave, id=leave_id)

    # Delete the leave object
    leave.delete()

    # Redirect to the 'view_leave' page after deletion
    return redirect('view_leave')
