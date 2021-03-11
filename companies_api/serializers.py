from .serializers_base import CompanySerializerBase
from locations_api.serializers_base import LocationSerializerBase
from contacts_api.serializers import ContactSerializer

class CompanySerializer(CompanySerializerBase): # serializers.ModelSerializer just tells django to convert sql to JSON
    headquarters = LocationSerializerBase()
    employees = ContactSerializer(many=True)

    class Meta(CompanySerializerBase.Meta):
        fields = CompanySerializerBase.Meta.fields + ('headquarters', 'employees')
