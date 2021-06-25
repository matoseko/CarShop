from django.conf.urls.static import static
from django.urls import path

from EshopCar import settings
from viewer import views
from viewer.views import HomeView, ProductView, OrderSummaryView, CheckoutView, PaymentView, add_to_cart, \
    remove_from_cart, reduce_quantity_item, ProductCreateView, ProductUpdateView, ProductDeleteView, CarbrandListView, \
    search_product, ProductDetailView, SignUpView

app_name = 'viewer'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<pk>/', ProductView.as_view(), name='product'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('add-to-cart/<pk>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<pk>/', remove_from_cart, name='remove-from-cart'),
    path('reduce-quantity-item/<pk>/', reduce_quantity_item, name='reduce-quantity-item'),
    path('create', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),
    path('brands/<str:brand>', CarbrandListView.as_view(), name='brands_products'),
    path('search/', search_product, name='search'),
    path('<int:pk>/', ProductDetailView.as_view(), name='products_detail'),
    path('accounts/sign-up/', SignUpView.as_view(), name='sign_up'),
    path('contact', views.contact, name='contact')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)