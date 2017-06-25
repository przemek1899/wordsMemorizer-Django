from rest.viewset.views import UserViewSet, GroupViewSet, ExpressionViewSet
from rest_framework import routers


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet, base_name='group-list')
router.register(r'expressions', ExpressionViewSet, base_name='expression-list')
