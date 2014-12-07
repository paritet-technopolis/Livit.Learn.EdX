import requests

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import Http404

from edxmako.shortcuts import render_to_response

from student.models import UserProfile


def get_base_url():
    from django.conf import settings
    return settings.LABSTER_BACKOFFICE_BASE_URL


def get_labs(token, format='json'):
    headers = {
        'authorization': "Token {}".format(token),
    }
    lab_list_url = '{}/api/products/'.format(get_base_url())

    resp = requests.get(lab_list_url, headers=headers)
    assert resp.status_code == 200, resp.status_code

    if format == 'string':
        return resp.content
    return resp.json()


def get_payment(payment_id, token, format='json'):
    headers = {
        'authorization': "Token {}".format(token),
    }
    payment_url = '{}/api/payments/{}/'.format(get_base_url(), payment_id)
    resp = requests.get(payment_url, headers=headers)
    assert resp.status_code == 200, resp.status_code

    if format == 'string':
        return resp.content
    return resp.json()


def create_user(user, name, format='json'):
    post_data = {
        'email': user.email,
        'username': user.username,
        'first_name': name,
        'external_id': user.id,
    }
    create_user_url = '{}/api/users/create/'.format(get_base_url())

    resp = requests.post(create_user_url, data=post_data)
    assert resp.status_code in range(200, 205), resp.status_code

    if format == 'string':
        return resp.content
    return resp.json()


def get_backoffice_urls():
    base_url = settings.LABSTER_BACKOFFICE_JS_BASE_URL
    duplicate_labs_url = '//{}/labster/api/course/duplicate-from-labs/'\
        .format(settings.CMS_BASE)

    urls = {
        'buy_lab': '{}/api/payments/create/'.format(base_url),
        'payment': '{}/api/payments/'.format(base_url),
        'license': '{}/api/licenses/'.format(base_url),
        'renew_license_bill': '{}/api/licenses/get_license_bill/'.format(base_url),
        'product': '{}/api/products/'.format(base_url),
        'country': '{}/api/countries/'.format(base_url),
        'product_group': '{}/api/product_groups/'.format(base_url),
        'duplicate_labs': duplicate_labs_url,
    }

    return urls


@login_required
def home(request):
    template_name = 'labster/backoffice.html'
    user_profile = UserProfile.objects.get(user=request.user)
    bo_user = create_user(request.user, user_profile.name, format='json')

    token = bo_user['token']
    lab_list = get_labs(token=token, format='string')
    backoffice = {
        'user_id': bo_user['id'],
        'user_country': user_profile.country,
        'user_edu_level': user_profile.user_school_level
    }

    backoffice_urls = get_backoffice_urls()
    stripe_publishable_key = settings.STRIPE_PUBLISHABLE_KEY
    context = {
        'lab_list': lab_list,
        'token': token,
        'backoffice': backoffice,
        'backoffice_urls': backoffice_urls,
        'stripe_publishable_key': stripe_publishable_key,
    }
    return render_to_response(template_name, context)