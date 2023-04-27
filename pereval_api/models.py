from django.db import models

NEW = 'new'
PENDING = 'pending'
ACCEPTED = 'accepted'
REJECTED = 'rejected'
STATUS = [
    ("new", "новый"),
    ("pending",  "модератор взял в работу"),
    ("accepted", "модерация прошла успешно"),
    ("rejected",  "модерация прошла, информация не принята"),
    ]


class Users(models.Model):
    email = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


class Pereval_added(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    users = models.ForeignKey(Users, null=True, on_delete=models.SET_NULL)
    beautyTitle = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    other_titles = models.CharField(max_length=300)
    connect = models.CharField(max_length=50)
    add_time = models.DateTimeField(auto_now_add=True)
    coord_id = models.ForeignKey(Coords, null=True, on_delete=models.CASCADE)
    winter_level = models.CharField(max_length=6)
    spring_level = models.CharField(max_length=6)
    summer_level = models.CharField(max_length=6)
    autumn_level = models.CharField(max_length=6)
    status = models.CharField(choices=STATUS, default='new', max_length=10)

class Pereval_images(models.Model):
    pereval_added = models.ForeignKey(Pereval_added,
                                      related_name='images',
                                      on_delete=models.CASCADE)
    image_name = models.CharField(max_length=300)
    image = models.BinaryField(db_column='image')