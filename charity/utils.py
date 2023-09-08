from charity.models import Institution


def filter_foundations(categories):
    foundations = Institution.objects.all()
    for category in categories:
        foundations = foundations.filter(categories__name=category)
    if foundations.exists():
        return foundations
    return False
