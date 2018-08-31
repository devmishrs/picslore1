from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import(
    AbstractBaseUser, 
    BaseUserManager,
    PermissionsMixin,
)

USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'
now = timezone.now()



class UserManager(BaseUserManager):
    def _create_user(self, username, password, email, first_name, last_name):
        if not username:
            raise ValidationError('User must have a username.')
        else:
            username = username.lower()
        if not password:
            raise ValueError('Password required!')
        if not email:
            raise ValueError('Email required!')
        else:
            email = self.normalize_email(email)

        user = self.model(
            username = username,
            email = email,
            first_name = first_name,
            last_name = last_name,
            is_active = True
        )
        
        user.set_password(password)
        user.save(using = self._db)
        #user.save()
        return user

    # def create_user(self, username, password, email, first_name, last_name,  **extra_fields):
    #     extra_fields.setdefault('is_staff', False)
    #     extra_fields.setdefault('is_superuser', False)
    #     return self._create_user(
    #         username = username,
    #         password = password,
    #         email = email,
    #         first_name = first_name,
    #         last_name = last_name,
    #         is_active = True,
    #         **extra_fields
    #     )

    def create_user(self, username, password, email, first_name, last_name):
        user = self._create_user(
            username = username,
            password = password,
            email = email,
            first_name = first_name,
            last_name = last_name
        )
        user.is_superuser = False
        user.is_staff = False
        user.save(using = self._db)
        return user

    
    def create_superuser(self, username, password, email, first_name, last_name):
        user = self._create_user(
            username = username,
            password = password,
            email = email,
            first_name = first_name,
            last_name  = last_name,
        ) 
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)
        return user

    def search(self, query = None):
        qs = self.get_queryset()
        if query is not None:
            or_lookups = (
                Q(username__iexact = query)|
                Q(first_name__icontain = query)
            )
            qs = User.objects.filter(or_lookups).distinct()
        return qs


            


class User(AbstractBaseUser, PermissionsMixin ):

    username = models.CharField(
        max_length = 28,
         validators = [RegexValidator(regex=USERNAME_REGEX,)], 
         unique = True
         )
    email = models.EmailField("Enter E-mail",unique = True)
    first_name = models.CharField("First Name ", max_length = 25)
    last_name = models.CharField("Last Name", max_length = 25)
    phone_number = PhoneNumberField()
    created = models.DateTimeField(auto_now_add=now)
    is_active = models.BooleanField('Active',default = True)
    is_superuser = models.BooleanField('Superuser',default = False)
    is_staff = models.BooleanField('Staff',default = False)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']


    def __str__(self):
        return self.first_name

    def get_username(self):
        return self.username

    def get_full_name(self):
        return self.first_name+ ' '+self.last_name

    full_name = property(get_full_name)

    def get_short_name(self):
        return self.first_name

    def has_perms(self, perm, obj=None):
        return True

    def has_module_perms(self, app_lable):
        return True

    @property
    def active(self):
        return self.is_active

    @property
    def superuser(self):
        return self.is_superuser
    @property
    def staff(self):
        return self.is_staff







