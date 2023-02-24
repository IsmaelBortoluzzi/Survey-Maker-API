from rest_framework.relations import PrimaryKeyRelatedField


class DocumentPrimaryKeyRelatedField(PrimaryKeyRelatedField):
    def to_representation(self, value):
        if self.pk_field is not None:
            return self.pk_field.to_representation(str(value.pk))
        return str(value.pk)