from django.conf import settings

from . import VERSION


def google_analytics(request):
    """
    Add Google Analytics ID to the context.
    """
    return {"GOOGLE_ANALYTICS_ID": settings.GOOGLE_ANALYTICS_ID}


def build_version(request):
    """
    Add version to the context.
    """
    return {"BUILD_VERSION": VERSION}
