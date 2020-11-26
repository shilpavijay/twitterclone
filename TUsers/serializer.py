from rest_framework import serializers
from TUsers.models import TUser

class TUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TUser
        fields = '__all__'

    # def get_follower(self, obj):
    #     context = self.context
    #     request = context.get("request")
    #     qs = request.user.following_user.all()
    #     data = [{'id': obj.pk, 'username': obj.username} for obj in qs]
    #     return data        