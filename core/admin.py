from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CarType, Post, User, Trip


class CarTypeAdmin(admin.ModelAdmin):
    list_display = ('model', 'contaminationRate')
    search_fields = ['model']


admin.site.register(CarType, CarTypeAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']


admin.site.register(Post, PostAdmin)


class TripAdmin(admin.ModelAdmin):
    list_display = ('user', 'start', 'end', 'points', 'date')
    list_filter = ('user',)
    search_fields = ['user', 'start', 'end']


admin.site.register(Trip, TripAdmin)

@admin.register(User)
class UserAdmin(UserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'cardId', 'points')}),
        ('Settings', {'fields':('carType', 'passengers')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

############################################################################
####################### debug objects ######################################
############################################################################
try:
    su = User.objects.create_superuser(first_name="Adminis", last_name="Trator", email="user@user.user", password="user")
    CarType.objects.create(model="A", contaminationRate=1)
    CarType.objects.create(model="B", contaminationRate=2)
    CarType.objects.create(model="C", contaminationRate=3)
    CarType.objects.create(model="D", contaminationRate=4)
    Post.objects.create(
        title="Campaña por la preservación de la naturaleza",
        image="/images/noticias/plantarArbol.jpg",
        imageAlt="Imagen de campaña de plantación de árboles 2018",
        content="Este año nos proponemos en el ayuntamiento de Zaragoza colabolar con la preservación de la naturaleza en la ciudad. Por ello creemos interesante, si estás en edad de 12 a 17 años, que participes con nosotros en esta gran labor ciudadana de plantación de árboles en las inmediaciones del barrio de Picarral, entre los días 10 y 20 de diciembre, para que, en unos años, podamos volver y admirar nuestra obra. Además, Picarral es una de las zonas de mayor densidad industrial en la urbe. ¿A qué estás esperando? Únete, te esperamos ",
        status=1,
        author=su,
    )
    Post.objects.create(
        title="Zaragoza, objetivo 0 contaminación",
        image="/images/noticias/contaminacion.jpg",
        imageAlt="Imagen de concienciación para reducir contaminación en las ciudades",
        content="Hoy en día los ciudadanos adquirimos más y más conciencia acerca de la importancia de preservar el entorno en el que vivimos. No obstante, parece que al vivir en la ciudad, eso se nos olvida, o no lo vemos como algo tan evidente como cuando vamos a pasar el fin de semana al monte. Sin embargo, nos afecta, y más de lo que creemos, ya que es en las ciudades donde mayor polución se acumula por metro cúbico. Por ese motivo, el ayuntamiento de Zaragoza con la colaboración de GreenPeace ha lanzado este año la propuesta \"Zaragoza, objetivo 0 contaminación\" en la que se pretende llegar en unos pocos años a ser una de las ciudades de España con mejor gestión de residuos y tratamiento de la polución ambiental. Estad atentos, ¡pronto surgirán campañas para todas las edades en las que podréis participar! ",
        status=1,
        author=su,
    )
    Post.objects.create(
        title="¿Cuánto contamina mi coche?",
        image="/images/noticias/coche.jpeg",
        imageAlt="Imagen de un coche en la que se cuestiona las emisiones contaminantes que emite",
        content="""Estamos de enhorabuena, y es que nuestra calculadora de rutas es todo un éxito. SIn embargo, muchos de vosotros nos preguntáis cómo puede uno saber la tasa de polución de su coche. SI bien estamos trabajando en una base de datos con la que podréis obviar poner ese dato por vuestra cuenta, ya que os daremos una lista de modelos de cohe, hasta entonces os dejamos aquí unos trucos que os pueden ayudar:

 * Google es vuestro amigo, lo sabe todo de todos (a veces incluso demasiado)
 * El manual de tu guantera es un buen aliado
 * Pásate por el concesionario...de paso quizá veas algún coche eléctrico interesante""",
        status=1,
        author=su,
    )
except:
    pass
