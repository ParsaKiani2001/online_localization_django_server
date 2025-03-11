import base64
import uuid

from rest_framework import serializers

from app.models import DictionaryModel,LanguageModel

class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = DictionaryModel
        fields = '__all__'
        serialized_fields = '__all__'

    def update(self, instance, validated_data):
        instance.values = validated_data.get('values',instance.values)
        instance.save()

class LanguageSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(default=uuid.uuid4)
    show_language_icon = serializers.CharField(required=False,write_only=True)
    language_icon = serializers.SerializerMethodField()
    class Meta:
        model = LanguageModel
        fields = '__all__'

    def get_language_icon(self, obj):
        if obj.show_language_icon:
            return base64.b64encode(obj.show_language_icon)
        return None

    def update(self, instance, validated_data):
        print(len(validated_data))
        if 'show_language_icon' in validated_data:
            base64_data = validated_data.get('show_language_icon')
            if base64_data:
                instance.show_language_icon = base64.b64decode(base64_data)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.name = validated_data.get('name', instance.name)
        instance.local = validated_data.get('local', instance.local)
        instance.show_lang = validated_data.get('show_lang', instance.show_lang)
        instance.save()
        return instance


    def create(self, validated_data):
        if 'show_language_icon' in validated_data:
            base64_data = validated_data.pop('show_language_icon')
            if base64_data:
                validated_data['show_language_icon'] = base64.b64decode(base64_data)
        old_lang = LanguageModel.objects.filter(name = validated_data['name'])
        lang =  LanguageModel.objects.create(**validated_data)
        if old_lang.exists():
            old_dicts = DictionaryModel.objects.filter(local = old_lang.last().id)
            for index in old_dicts:
                DictionaryModel.objects.create(
                    keys=index.keys,
                    values=index.values,
                    local=lang
                )
        return lang