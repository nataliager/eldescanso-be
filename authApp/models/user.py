from django.db import models #permite crear los modelos
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager #manejo de usuario autendicacion
from django.contrib.auth.hashers import make_password #crear contraseñas

#se crean los usuarios en el sistema de utenticacion 
class UserManager(BaseUserManager): #hereda de BaseUserManager -> gestiona la autenticacion de los ususarios
    
    #crea usuario lo guarda en la BD y retorna el usuario
    def create_user(self, username, password=None): #Crear usuario
        
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username) #model: funcion de BaseUserManager(usuario de utenticacion)
        user.set_password(password)
        user.save(using=self._db) #guarda el usuario en la BD
        return user

    #crea un usuario administrador 
    def create_superuser(self, username, password):
        
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

#modelo de user 
class User(AbstractBaseUser, PermissionsMixin): #herencia multiple 
    
    #Creacion de atributos para las tablas de la BD
    id = models.CharField (max_length = 13, primary_key= True, unique=True, null=False)
    rol = models.CharField('Rol', max_length = 20, null=False)
    nombre = models.TextField('Nombre', max_length = 50, null=False)
    username = models.CharField('Username',unique=True, max_length = 20,null=False) #varchar
    password = models.CharField('Password', max_length = 256,null=False)
    telefono = models.CharField('Telefono', max_length = 15,null=False) 

    #crear usuario 
    def save(self, **kwargs): #**kwargs: diccionario parejas llave:valor
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN' #esconder la contraseña (valor secreto)
        self.password = make_password(self.password, some_salt) #oculta la contraseña
        super().save(**kwargs) #voy a la clase padre y guardo los atributos 

    objects = UserManager() #obejetos para la autentiacion
    USERNAME_FIELD = 'username' 