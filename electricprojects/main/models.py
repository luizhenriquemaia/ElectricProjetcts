from django.db import models


class a01MethodsRef(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    reference = models.CharField(max_length=3)
    description = models.CharField(max_length=255)
    objects = models.Manager()


class a02MethodsInst(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    method = models.CharField(max_length=10)
    description = models.CharField(max_length=500)
    maximum_diameter = models.IntegerField(null=True)
    cable_type = models.CharField(max_length=10, null=True)
    reference_method = models.ForeignKey(a01MethodsRef, on_delete=models.CASCADE)
    objects = models.Manager()


class a03IsolationType(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    description = models.CharField(max_length=255)
    max_temperature = models.IntegerField(default=1)
    overload_temperature = models.IntegerField(default=1)
    short_circuit_temperature = models.IntegerField(default=1)
    objects = models.Manager()


class a04NumberOfChargedConductors(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    circuit_esqueme = models.CharField(max_length=255)
    number = models.IntegerField(default=1)
    objects = models.Manager()


class a05CurrentCapacity(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    nominal_section = models.DecimalField(max_digits=12, decimal_places=4)
    reference_method = models.ForeignKey(a01MethodsRef, on_delete=models.CASCADE)
    number_of_charged_conductors = models.IntegerField(default=1)
    cable_type = models.CharField(max_length=20)
    capacity = models.DecimalField(max_digits=12, decimal_places=4)
    isolation_type = models.ForeignKey(a03IsolationType, on_delete=models.CASCADE)
    objects = models.Manager()


class a06TemperatureCorrection(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    location = models.CharField(max_length=20)
    temperature = models.IntegerField(default=1)
    isolation_type = models.ForeignKey(a03IsolationType, on_delete=models.CASCADE)
    factor = models.DecimalField(max_digits=12, decimal_places=4, default=1)
    objects = models.Manager()


class a07UndergroundCorrection(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    thermal_resistivity = models.DecimalField(max_digits=3, decimal_places=1)
    correction_factory = models.DecimalField(max_digits=4, decimal_places=2)
    objects = models.Manager()


class a08GroupingForms(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    description = models.CharField(max_length=500)
    reference_method = models.ForeignKey(a01MethodsRef, on_delete=models.CASCADE)
    objects = models.Manager()


class a09GroupingCorrection(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    group_form = models.ForeignKey(a08GroupingForms, on_delete=models.CASCADE, default=1)
    circuit_number = models.IntegerField(default=1)
    factor = models.DecimalField(max_digits=12, decimal_places=4, default=1)
    objects = models.Manager()



