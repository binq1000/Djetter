from django.contrib.auth.models import User, Group
from rest_framework import serializers

from tutorial.models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet, Account, Kweet


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Snippet
        fields = ('url', 'id', 'title', 'code', 'linenos', 'language', 'style')


class KweetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kweet
        fields = ('url', 'id', 'message', 'poster', 'datePosted')


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    kweets = KweetSerializer(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ('url', 'id', 'firstname', 'lastname', 'bio', 'kweets', 'followers')
