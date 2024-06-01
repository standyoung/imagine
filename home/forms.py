from django.forms import ModelForm
from .models import ImageUpload

class ImageUploadForm(ModelForm):
    class Meta:
        model = ImageUpload
        fields = ['filename', 'img', 'img_caption']
        # Form을 템플릿에서 직접 생성할 수 있지만
        # Model Form을 이용하여 `ImageUploadForm`을 생성
