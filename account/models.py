from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email)  # book = Book(title='bla bla', author_id = 3, category = 'comedy') -> comedy.save()
        user.set_password(password)
        user.create_activation_code()
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class MyUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=50, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    objects = MyUserManager()

    def __str__(self):
        return self.email


    def create_activation_code(self):
        """
        шифрование
        1. hashlib.md5(self.email + str(self.id)).encode() -> hexdigest() - переваривание, хэширование кода
        test@test.com155 -> dsadsdsddopkoko212ok1o2k13231o23k

        2. get_random_string(50, allowed_char=['which symbols are allowed in this string'])

        3. UUID

        4. datetime.datetime.now() or time.time() + timestamp() 01.01.1970 - сколько секунд с этого времени прошло
        """
        import hashlib
        string = self.email + str(self.id)
        encode_string = string.encode()
        md5_object = hashlib.md5(encode_string)
        activation_code = md5_object.hexdigest()
        self.activation_code = activation_code


#TODO: create activation code

