from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'accounts', views.AccountViewSet)

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('', include(router.urls)),
    # Include other viewsets as needed
    path('accounts/', views.AccountViewSet.as_view({'get': 'list', 'post': 'create'}), name='account-list'),
    path('accounts/<int:pk>/', views.AccountViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='account-detail'),
    path('account-types/', views.AccountTypeViewSet.as_view({'get': 'list', 'post': 'create'}), name='account-type-list'),
    path('account-categories/', views.AccountCategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='account-category-list'),
    path('industries/', views.IndustryViewSet.as_view({'get': 'list', 'post': 'create'}), name='industry-list'),
    path('type-of-businesses/', views.TypeOfBusinessViewSet.as_view({'get': 'list', 'post': 'create'}), name='type-of-business-list'),
    path('account-addresses/', views.AccountAddressViewSet.as_view({'get': 'list', 'post': 'create'}), name='account-address-list'),
    path('account-pics/', views.AccountPICViewSet.as_view({'get': 'list', 'post': 'create'}), name='account-pic-list'),
    path('account-banks/', views.AccountBankViewSet.as_view({'get': 'list', 'post': 'create'}), name='account-bank-list'),
    path('banks/', views.BankViewSet.as_view({'get': 'list', 'post': 'create'}), name='bank-list'),
    path('banks/categories/', views.BankCategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='bank-category-list'),
    path('account-types/<int:pk>/', views.AccountTypeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='account-type-detail'),
    path('account-categories/<int:pk>/', views.AccountCategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='account-category-detail'),
    path('industries/<int:pk>/', views.IndustryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='industry-detail'),
    path('type-of-businesses/<int:pk>/', views.TypeOfBusinessViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='type-of-business-detail'),
    path('account-addresses/<int:pk>/', views.AccountAddressViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='account-address-detail'),
    path('account-pics/<int:pk>/', views.AccountPICViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='account-pic-detail'),
    path('account-banks/<int:pk>/', views.AccountBankViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='account-bank-detail'),
    path('banks/<int:pk>/', views.BankViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='bank-detail'),
    path('banks/categories/<int:pk>/', views.BankCategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='bank-category-detail'),

]