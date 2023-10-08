from django.http import JsonResponse
from . import models


def main(request):
    request_data = dict(request.GET)
    match request_data['type'][0]:
        case 'new_user':
            print('done')
            new_user = models.PersonalData(name=request_data['name'][0],
                                           surname=request_data['surname'][0],
                                           fatherName=request_data['fatherName'][0],
                                           birthday=request_data['birthday'][0],
                                           region=request_data['region'][0],
                                           street=request_data['street'][0],
                                           home=request_data['home'][0],
                                           flat=request_data['flat'][0],
                                           phone=int(request_data['phone'][0]),
                                           vk=request_data['vk'][0],
                                           permission=request_data['permission'][0]
                                           )
            new_user.save()

    return JsonResponse(request_data)
