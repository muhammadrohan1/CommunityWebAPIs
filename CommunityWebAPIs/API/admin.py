from django.contrib import admin

# Register your models here.
from .models import Community
from .models import ResidentInfo
from .models import BusinessInfo
from .models import Categories
from .models import ComunityCategories
from .models import Bussiness_Categories
from .models import Resident_Categories


admin.site.register(Community)
admin.site.register(ResidentInfo)
admin.site.register(BusinessInfo)
admin.site.register(Categories)
admin.site.register(ComunityCategories)
admin.site.register(Bussiness_Categories)
admin.site.register(Resident_Categories)