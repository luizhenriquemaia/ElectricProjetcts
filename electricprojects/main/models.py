from django.db import models


class a01MethodsRef(models.Model):
    id = models.AutoField(primary_key=True)
    reference = models.CharField(max_length=3)
    description = models.CharField(max_length=255)


class a02MethodsInst(models.Model):
    id = models.AutoField(primary_key=True)
    method = models.CharField(max_length=10)
    description = models.CharField(max_length=500)
    maximum_diameter = models.IntegerField(default=0)
    cable_type = models.CharField(max_length=10, null=True)
    reference_method = models.ForeignKey(a01MethodsRef, on_delete=models.CASCADE)


class a03IsolationType(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)


class a04TemperatureConductors(models.Model):
    id = models.AutoField(primary_key=True)
    isolation_type = models.ForeignKey(a03IsolationType, on_delete=models.CASCADE)
    max_temperature = models.IntegerField()
    overload_temperature = models.IntegerField()
    short_circuit_temperature = models.IntegerField()


class a05NumberOfChargedConductors(models.Model):
    id = models.AutoField(primary_key=True)
    circuit_esqueme = models.CharField(max_length=255)
    number = models.IntegerField()


class a06CurrentCapacity(models.Model):
    id = models.AutoField(primary_key=True)
    nominal_section = models.DecimalField(max_digits=12, decimal_places=4)
    reference_method = models.ForeignKey(a01MethodsRef, on_delete=models.CASCADE)
    number_of_charged_conductors = models.IntegerField()
    cable_type = models.CharField(max_length=20)
    capacity = models.DecimalField(max_digits=12, decimal_places=4)
    isolation_type = models.ForeignKey(a03IsolationType, on_delete=models.CASCADE)


class a07TemperatureCorrection(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=20)
    temperature = models.IntegerField()
    isolation_type = models.ForeignKey(a03IsolationType, on_delete=models.CASCADE)


class a08UndergroundCorrection(models.Model):
    id = models.AutoField(primary_key=True)
    thermal_resistivity = models.DecimalField(max_digits=3, decimal_places=1)
    correction_factory = models.DecimalField(max_digits=4, decimal_places=2)


class a08GroupingForms(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=500)
    reference_method = models.ForeignKey(a01MethodsRef, on_delete=models.CASCADE)


class a09GroupingCorrection(models.Model):
    id = models.AutoField(primary_key=True)
    reference_method = models.ForeignKey(a01MethodsRef, on_delete=models.CASCADE)
    circuit_number = models.IntegerField()



