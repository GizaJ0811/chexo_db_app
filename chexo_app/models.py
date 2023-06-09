from django.db import models
from django.urls import reverse


class DojoList(models.Model):
    dojo_name = models.CharField(max_length=30, unique=True)

    @property
    def member_list(self):
        return list(MemberList.objects.filter(dojo_id=self.pk).values())

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self) -> str:
        return self.dojo_name


class MemberList(models.Model):
    name = models.CharField(max_length=30)
    birth_date = models.DateField()
    dojo = models.ForeignKey(DojoList, on_delete=models.CASCADE)
    kyu = models.IntegerField(default=8)

    def get_absolute_url(self):
        return reverse("member-update", args=[str(self.dojo_id), str(self.pk)])

    def __str__(self) -> str:
        return f"Name: {self.name}, Dojo: {self.dojo}, Kyu: {self.kyu}"
