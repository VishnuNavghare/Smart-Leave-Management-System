from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Leave
from .forms import LeaveForm


def home(request):
    return render(request, "home.html")



def register(request):
    if request.method == "POST":

        Employee.objects.create(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            email=request.POST["email"],
            username=request.POST["username"],
            password=request.POST["password"],
        )

        return redirect("login")

    return render(request, "register.html")



def login_page(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        try:
            employee = Employee.objects.get(
                username=username,
                password=password
            )

            request.session["employee_id"] = employee.id

            return redirect("dashboard")

        except Employee.DoesNotExist:

            return render(request, "login.html", {
                "error": "Invalid Username or Password"
            })

    return render(request, "login.html")



def dashboard(request):

    employee_id = request.session.get("employee_id")

    if not employee_id:
        return redirect("login")

    employee = Employee.objects.get(id=employee_id)

    leaves = Leave.objects.filter(employee=employee)

    context = {
        "employee": employee,
        "employee_name": f"{employee.first_name} {employee.last_name}",
        "total": leaves.count(),
        "pending": leaves.filter(status="Pending").count(),
        "approved": leaves.filter(status="Approved").count(),
        "rejected": leaves.filter(status="Rejected").count(),
    }

    return render(request, "dashboard.html", context)



def apply_leave(request):

    employee_id = request.session.get("employee_id")

    if not employee_id:
        return redirect("login")

    employee = Employee.objects.get(id=employee_id)

    if request.method == "POST":

        form = LeaveForm(request.POST)

        if form.is_valid():
            leave = form.save(commit=False)
            leave.employee = employee
            leave.save()

            return redirect("my_leave")

    else:
        form = LeaveForm()

    return render(request, "apply_leave.html", {
        "form": form
    })


def my_leave(request):

    employee_id = request.session.get("employee_id")

    if not employee_id:
        return redirect("login")

    employee = Employee.objects.get(id=employee_id)

    leaves = Leave.objects.filter(employee=employee)

    search = request.GET.get("search")

    if search:
        leaves = leaves.filter(
            leave_type__icontains=search
        )

    status = request.GET.get("status")

    if status:
        leaves = leaves.filter(status=status)

    return render(request, "my_leave.html", {
        "employee": employee,
        "leaves": leaves
    })


def profile(request):

    employee_id = request.session.get("employee_id")

    if not employee_id:
        return redirect("login")

    employee = Employee.objects.get(id=employee_id)

    return render(request, "profile.html", {
        "employee": employee
    })


def edit_profile(request):

    employee_id = request.session.get("employee_id")

    if not employee_id:
        return redirect("login")

    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == "POST":

        employee.first_name = request.POST["first_name"]
        employee.last_name = request.POST["last_name"]
        employee.email = request.POST["email"]
        employee.username = request.POST["username"]

        employee.save()

        return redirect("profile")

    return render(request, "edit_profile.html", {
        "employee": employee
    })


def logout_page(request):
    request.session.flush()
    return redirect("login")