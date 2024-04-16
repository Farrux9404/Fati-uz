from rest_framework import serializers
from centers_departments import Centralsection, Departmenthistory, Members, Picture, Video, Research

class CentralsectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Centralsection
        fields = ['title', 'file', 'status', 'order']


class DepartmenthistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Departmenthistory
        fields = ['title', 'file', 'status', 'center_id', 'order']


class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ['id', 'title', 'file', 'birth_date', 'status', 'position', 'academic_degree', 'email', 'content', 'link', 'center_id', 'order']


    def to_representation(self, instance):
        data = super().to_representation(instance)
        members = instance.members.all()

        if members:
            request = self.context.get('request')
            data['members'] = [{'fullname': member.full_name,
                                    'activity_institution': member.activity_institution,
                                    'year_of_visit': member.year_of_visit} for member in members]

        return data



class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ['title', 'base_file', 'image', 'status', 'center_id', 'order']


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['title', 'image', 'status', 'center_id', 'order']


class ResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Research
        fields = ['title', 'base_file', 'content', 'status', 'center_id', 'order']