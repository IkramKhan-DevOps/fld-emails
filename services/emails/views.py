from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "emails/home.html"


class BaseEmailView(TemplateView):
    template_name = "emails/base.html"


""" Company ----------------------------------------------------------------------------------------------- (emails) """


class MemberCreatedView(TemplateView):
    template_name = "emails/company/member_created.html"


""" Onboarding -------------------------------------------------------------------------------------------- (emails) """


class ApplicantCreatedView(TemplateView):
    template_name = "emails/onboarding/applicant_created.html"


class ApplicantAcceptedView(TemplateView):
    template_name = "emails/onboarding/applicant_accepted.html"


class WaitListCreatedView(TemplateView):
    template_name = "emails/onboarding/waitlist_created.html"


""" Recommendations --------------------------------------------------------------------------------------- (emails) """


class RecommendationOnScanView(TemplateView):
    template_name = "emails/recommendations/email_customer_over_scan.html"


""" SAAS (Subscriptions) ---------------------------------------------------------------------------------- (emails) """


class SubscriptionCreatedView(TemplateView):
    template_name = "emails/saas/subscription_create.html"


class SubscriptionUpdateView(TemplateView):
    template_name = "emails/saas/subscription_update.html"

