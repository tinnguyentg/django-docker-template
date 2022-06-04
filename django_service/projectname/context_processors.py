from django.conf import settings


def google_analytics(request):
    """
    Add Google Analytics ID to the context.
    """
    return {"GOOGLE_ANALYTICS_ID": settings.GOOGLE_ANALYTICS_ID}
