from django.db import models


class Employee(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    employee_id = models.CharField(
        max_length=20,
        unique=True,
        blank=True
    )

    email = models.EmailField(unique=True)

    username = models.CharField(
        max_length=100,
        unique=True
    )

    password = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.employee_id:
            last_employee = Employee.objects.order_by('-id').first()

            if last_employee and last_employee.employee_id:
                last_id = int(last_employee.employee_id.replace("EMP", ""))
                self.employee_id = f"EMP{last_id + 1:03d}"
            else:
                self.employee_id = "EMP001"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Leave(models.Model):

    STATUS = (
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
    )

    LEAVE_TYPES = (
        ("Casual Leave", "Casual Leave"),
        ("Sick Leave", "Sick Leave"),
        ("Earned Leave", "Earned Leave"),
        ("Work From Home", "Work From Home"),
    )

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    leave_type = models.CharField(
        max_length=50,
        choices=LEAVE_TYPES
    )

    from_date = models.DateField()

    to_date = models.DateField()

    reason = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="Pending"
    )

    applied_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.employee} - {self.leave_type}"