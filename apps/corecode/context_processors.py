from .models import AcademicSession, AcademicTerm


def site_defaults(request):
    current_session = AcademicSession.objects.get(current=True)
    current_term = AcademicTerm.objects.get(current=True)
    contexts = {
        "current_session": current_session.name,
        "current_term": current_term.name,
    }

    return contexts
