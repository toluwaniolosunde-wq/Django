from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name','code', 'description']



    # name= serializers.CharField(max_length = 55, required=True)
    # code= serializers.CharField(max_length = 55, required=True)
    # description