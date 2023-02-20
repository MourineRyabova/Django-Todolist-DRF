from rest_framework.routers import DefaultRouter
from todolist.views import ToDoViewSet

app_name = 'todolist'

router = DefaultRouter()
router.register(prefix = 'tasks', viewset = ToDoViewSet, basename = 'tasks')
urlpatterns = router.urls