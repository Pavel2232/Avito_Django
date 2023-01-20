from rest_framework import serializers

from ads.models import Ad,Comment





class CommentSerializer(serializers.ModelSerializer):

    author_id = serializers.SerializerMethodField(read_only=True)
    author_first_name = serializers.SerializerMethodField(read_only=True)
    author_last_name = serializers.SerializerMethodField(read_only=True)
    author_image = serializers.SerializerMethodField(read_only=True)
    def get_author_image(self,obj):
        return str(obj.author.image)

    def get_author_last_name(self,obj):
        return str(obj.author.last_name)
    def get_author_first_name(self,obj):
        return str(obj.author.first_name)
    def get_author_id(self,obj):
        return str(obj.author.id)
    class Meta:
        model = Comment
        fields = ['pk','text','author_id','created_at','author_first_name','author_last_name','ad_id','author_image']



class AdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = ['pk','image','title','price','description']


class AdDetailSerializer(serializers.ModelSerializer):



    author = serializers.SlugRelatedField(read_only=True,slug_field='first_name')
    phone = serializers.SerializerMethodField(read_only=True)
    author_last_name = serializers.SerializerMethodField(read_only=True)
    author_id = serializers.SerializerMethodField(read_only=True)
    def get_phone(self,obj):
        return str(obj.author.phone)

    def get_author_last_name(self,obj):
        return str(obj.author.last_name)
    def get_author_id(self,obj):
        return str(obj.author.id)

    class Meta:
        model = Ad
        fields = ['pk','image','title','price','phone','description','author','author_last_name','author_id']


class Ad_by_User(serializers.ModelSerializer):
    pass




