from charity.models import Institution, Category


def filter_foundations(categories):
    foundations = Institution.objects.all()
    for category in categories:
        category = Category.objects.get(id=category)
        foundations = foundations.filter(categories=category)
    if foundations.exists():
        return foundations
    return False


def get_categories(categories):
    lst = []
    for category in categories:
        cat = Category.objects.get(id=category)
        lst.append(cat)
    return lst


def session_data(request):
    address = request.session.get('address')
    city = request.session.get('city')
    postcode = request.session.get('postcode')
    data = request.session.get('data')
    time = request.session.get('time')
    phone = request.session.get('phone')
    more_info = request.session.get('more_info')
    foundation = request.session.get('foundation')
    foundation = Institution.objects.get(id=foundation)
    bags = request.session.get('bags')
    categories = request.session.get('categories')
    categories = get_categories(categories)
    return address, city, postcode, data, time, phone, more_info, foundation, bags, categories
