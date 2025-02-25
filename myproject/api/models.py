from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=255, unique=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.login

class Dictionary(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Credit(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='credits')
    issuance_date = models.DateField()
    return_date = models.DateField()
    actual_return_date = models.DateField(null=True, blank=True)
    body = models.DecimalField(max_digits=10, decimal_places=2)
    percent = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Credit {self.id} for {self.user.login}"

class Plan(models.Model):
    id = models.AutoField(primary_key=True)
    period = models.DateField()
    sum = models.DecimalField(max_digits=10, decimal_places=2)
    category_id = models.ForeignKey(Dictionary, on_delete=models.CASCADE, related_name='plans')

    def __str__(self):
        return f"Plan {self.id} - {self.period}"

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    sum = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    credit_id = models.ForeignKey(Credit, on_delete=models.CASCADE, related_name='payments')
    type_id = models.ForeignKey(Dictionary, on_delete=models.CASCADE, related_name='payments')

    def __str__(self):
        return f"Payment {self.id} for Credit {self.credit_id}"