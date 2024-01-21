from django.urls import path
from .views import (
    HomeView, BaseEmailView,
    MemberCreatedView,
    ApplicantCreatedView, ApplicantAcceptedView,
    WaitListCreatedView,
    RecommendationOnScanView,
    SubscriptionCreatedView, SubscriptionUpdateView,
)

app_name = 'emails'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('base/', BaseEmailView.as_view(), name='base'),
    path('company/member_created/', MemberCreatedView.as_view(), name='member_created'),
    path('onboarding/applicant_created/', ApplicantCreatedView.as_view(), name='applicant_created'),
    path('onboarding/applicant_accepted/', ApplicantAcceptedView.as_view(), name='applicant_accepted'),
    path('onboarding/waitlist_created/', WaitListCreatedView.as_view(), name='waitlist_created'),
    path('recommendations/email_customer_over_scan/', RecommendationOnScanView.as_view(), name='recommendation_on_scan'),
    path('saas/subscription_created/', SubscriptionCreatedView.as_view(), name='subscription_created'),
    path('saas/subscription_update/', SubscriptionUpdateView.as_view(), name='subscription_update'),

]
