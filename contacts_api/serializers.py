from .serializers_base import ContactSerializerBase
from locations_api.serializers_base import LocationSerializerBase
from companies_api.serializers_base import CompanySerializerWithHeadquarters

class ContactSerializer(ContactSerializerBase): # serializers.ModelSerializer just tells django to convert sql to JSON
    home = LocationSerializerBase()
    company_set = CompanySerializerWithHeadquarters(many=True)

    class Meta(ContactSerializerBase.Meta):
        fields = ContactSerializerBase.Meta.fields + ('home', 'company_set')
