from django.db import models
from django.contrib.auth.models import User

# from django.utils.translation import ugettext_lazy as _
# Permission, Group, _user_get_all_permissions, _user_has_perm, \
# _user_has_module_perms, AbstractBaseUser, BaseUserManager

# from django.utils import timezone
# from uuid import uuid4
# from django.core.mail import send_mail
# from django.contrib import auth


# class PermissionsMixin(models.Model):
#     """
#     Add the fields and methods necessary to support the Group and Permission
#     models using the ModelBackend.
#     """
#     is_superuser = models.BooleanField(
#         _('superuser status'),
#         default=False,
#         help_text=_(
#             'Designates that this user has all permissions without '
#             'explicitly assigning them.'
#         ),
#     )
#     groups = models.ManyToManyField(
#         Group,
#         verbose_name=_('groups'),
#         blank=True,
#         help_text=_(
#             'The groups this user belongs to. A user will get all permissions '
#             'granted to each of their groups.'
#         ),
#         related_name="custom_user_set",
#         related_query_name="user",
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         verbose_name=_('user permissions'),
#         blank=True,
#         help_text=_('Specific permissions for this user.'),
#         related_name="custom_user_set",
#         related_query_name="user",
#     )
#
#     class Meta:
#         abstract = True
#
#     def get_group_permissions(self, obj=None):
#         """
#         Return a list of permission strings that this user has through their
#         groups. Query all available auth backends. If an object is passed in,
#         return only permissions matching this object.
#         """
#         permissions = set()
#         for backend in auth.get_backends():
#             if hasattr(backend, "get_group_permissions"):
#                 permissions.update(backend.get_group_permissions(self, obj))
#         return permissions
#
#     def get_all_permissions(self, obj=None):
#         return _user_get_all_permissions(self, obj)
#
#     def has_perm(self, perm, obj=None):
#         """
#         Return True if the user has the specified permission. Query all
#         available auth backends, but return immediately if any backend returns
#         True. Thus, a user who has permission from a single auth backend is
#         assumed to have permission in general. If an object is provided, check
#         permissions for that object.
#         """
#         # Active superusers have all permissions.
#         if self.is_active and self.is_superuser:
#             return True
#
#         # Otherwise we need to check the backends.
#         return _user_has_perm(self, perm, obj)
#
#     def has_perms(self, perm_list, obj=None):
#         """
#         Return True if the user has each of the specified permissions. If
#         object is passed, check if the user has all required perms for it.
#         """
#         return all(self.has_perm(perm, obj) for perm in perm_list)
#
#     def has_module_perms(self, app_label):
#         """
#         Return True if the user has any permissions in the given app label.
#         Use simlar logic as has_perm(), above.
#         """
#         # Active superusers have all permissions.
#         if self.is_active and self.is_superuser:
#             return True
#
#         return _user_has_module_perms(self, app_label)
#
#
# class UserManager(BaseUserManager):
#     use_in_migrations = True
#
#     @classmethod
#     def normalize_email(cls, email):
#         if "@" in email:
#             return super().normalize_email(email)
#         elif email is None:
#             return
#         else:
#             raise ValueError("Not a valid email address")
#
#     def _create_user(self, email, password, **extra_fields):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError('The given email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, email=None, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)
#
#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#
#         return self._create_user(email, password, **extra_fields)
#
#
# class AbstractUser(AbstractBaseUser, PermissionsMixin):
#     """
#     An abstract base class implementing a fully featured User model with
#     admin-compliant permissions.
#
#     Email and password are required. Other fields are optional.
#     """
#     id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
#     email = models.EmailField(_('email address'), unique=True)
#     first_name = models.CharField(_('first name'), max_length=30)
#     last_name = models.CharField(_('last name'), max_length=30)
#     is_staff = models.BooleanField(
#         _('staff status'),
#         default=False,
#         help_text=_('Designates whether the user can log into this admin site.'),
#     )
#     is_active = models.BooleanField(
#         _('active'),
#         default=True,
#         help_text=_(
#             'Designates whether this user should be treated as active. '
#             'Unselect this instead of deleting accounts.'
#         ),
#     )
#     date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
#
#     objects = UserManager()
#
#     EMAIL_FIELD = 'email'
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']
#
#     class Meta:
#         verbose_name = _('user')
#         verbose_name_plural = _('users')
#         abstract = True
#
#     def clean(self):
#         super(AbstractUser, self).clean()
#         self.email = self.__class__.objects.normalize_email(self.email)
#
#     def get_full_name(self):
#         """
#         Returns the first_name plus the last_name, with a space in between.
#         """
#         full_name = '%s %s' % (self.first_name, self.last_name)
#         return full_name.strip()
#
#     def get_short_name(self):
#         """Returns the short name for the user."""
#         return self.first_name
#
#     def email_user(self, subject, message, from_email=None, **kwargs):
#         """
#         Sends an email to this User.
#         """
#         send_mail(subject, message, from_email, [self.email], **kwargs)
#
#
# class CustomUser(AbstractUser):
#     """
#     Email based User
#
#     Email, first name, last name and password are required. Other fields are optional.
#     """


class CompanyProfile(models.Model):
    # Choices
    NATION = (
        ('1', 'Indian'),
        ('2', 'Other'),
    )
    # Model
    name = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=30)  # add choices
    url = models.URLField()
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    country = models.CharField(max_length=15, choices=NATION)
    pincode = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user.email


class CompanyPerson(models.Model):
    name = models.CharField(max_length=30)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='persons')
    designation = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField()


class Resume(models.Model):
    file = models.FileField(upload_to='resume')
    verified = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def verified_status(self):
        return self.verified


class StudentProfile(models.Model):
    # Choices
    CATEGORY = (
        ('1', 'General'),
        ('2', 'OBC'),
        ('3', 'SC'),
        ('4', 'ST'),
    )
    HOSTELS = (
        ('1', 'B1'),
        ('2', 'B2'),
        ('3', 'G6'),
        ('4', 'G5'),
    )
    NATION = (
        ('1', 'Indian'),
        ('2', 'Other'),
    )
    # Validators

    # Model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=8)
    year = models.SmallIntegerField()
    cpi = models.FloatField()
    placed_status = models.BooleanField(default=False)
    placed_company = models.ForeignKey(CompanyProfile, on_delete=models.SET_NULL, null=True, blank=True)
    phone = models.CharField(max_length=15)
    parent_name = models.CharField(max_length=30)
    dob = models.DateField()
    category = models.CharField(max_length=10, choices=CATEGORY)
    blood_group = models.CharField(max_length=5)  # Choices
    jee_air = models.IntegerField()
    hostel_name = models.CharField(max_length=2, choices=HOSTELS, blank=True)
    room_no = models.SmallIntegerField(blank=True)
    hobbies = models.TextField()
    pd_status = models.BooleanField(default=False)
    nationality = models.CharField(max_length=10, choices=NATION)
    permanent_address = models.TextField()
    current_address = models.TextField()
    x_year = models.SmallIntegerField()
    x_board_name = models.CharField(max_length=30)
    x_percentage = models.CharField(max_length=10)
    xii_year = models.SmallIntegerField()
    xii_board_name = models.CharField(max_length=30)
    xii_percentage = models.CharField(max_length=10)
    ctc = models.IntegerField(null=True, blank=True, )
    resume_1 = models.ForeignKey(Resume, null=True, blank=True, on_delete=models.SET_NULL, related_name='resume_1')
    resume_2 = models.ForeignKey(Resume, null=True, blank=True, on_delete=models.SET_NULL, related_name='resume_2')
    resume_3 = models.ForeignKey(Resume, null=True, blank=True, on_delete=models.SET_NULL, related_name='resume_3')
    resume_4 = models.ForeignKey(Resume, null=True, blank=True, on_delete=models.SET_NULL, related_name='resume_4')
    resume_5 = models.ForeignKey(Resume, null=True, blank=True, on_delete=models.SET_NULL, related_name='resume_5')

    def __str__(self):
        return self.user.username
