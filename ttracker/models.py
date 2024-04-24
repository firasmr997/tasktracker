from django.db import models


# Create your models here.

class EmployeurType(models.TextChoices):
    # list Of possibility
    # The left member is the value stored in the database and using in the code
    # The right member is the value displayed in the admin interface
    SUPERADMIN = 'Super Admin'
    ADMIN = 'Admin'
    USER = 'User'


class Employeur(models.Model):
    id = models.CharField(primary_key=True, max_length=100, unique=True)
    Nom = models.CharField(max_length=100)
    Prenom = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100, unique=True)
    Username = models.CharField(max_length=100, unique=True)
    Poste = models.CharField(max_length=100)
    type = models.CharField(choices=EmployeurType.choices, max_length=11)

    # inner class could be added to each model
    # it must be located just after the last field definition
    # the class provides some extra information like
    # the table name using db_table property
    #
    class Meta:
        verbose_name = 'Employeur'
        verbose_name_plural = 'Employeurs'
        db_table = 'employeur'
        ordering = ['Username']  # asc order
        # ordering=['-manufacturer','-model'] #desc order

    def __str__(self):
        return f'{self.Username}-{self.id}'


class Task(models.Model):
    id = models.CharField(primary_key=True, max_length=100, unique=True)
    Titre = models.CharField(max_length=100)
    Description = models.TextField()
    DateDebut = models.DateField()
    DateFin = models.DateField()
    Employeur = models.ManyToManyField(Employeur)

    class Meta:
        db_table = 'tasks'

    def __str__(self) -> str:
        return f'{self.Titre} - {self.id}'


class EmployeurTask(models.Model):
    employeur = models.ForeignKey(Employeur, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)


class Meta:
    db_table = 'employeur_tasks'
    unique_together = ('employeur', 'tasks')


def __str__(self) -> str:
    return f'{self.employeur.id} - {self.task.id}'


class Penalite(models.Model):
    id = models.CharField(primary_key=True, max_length=100, unique=True)
    NbrPenalite = models.IntegerField()
    DatePenalite = models.DateField()
    Employeur = models.ForeignKey(Employeur, on_delete=models.CASCADE)
    Task = models.OneToOneField(Task, on_delete=models.CASCADE)

    class Meta:
        db_table = 'penalites'

    def __str__(self) -> str:
        return f'{self.NbrPenalite} - {self.id}'
