from django.contrib import admin
from apps.historylearn.models import Singup,Login,User,Player,Game,Ranking,Inventary,Store
# Register your models here.
admin.site.register(Singup)
admin.site.register(Login)
admin.site.register(User)
admin.site.register(Player)
admin.site.register(Game)
admin.site.register(Ranking)
admin.site.register(Inventary)
admin.site.register(Store)
