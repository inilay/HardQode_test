from rest_framework import serializers
from .models import Product, Profile, Lesson, LessonView
from django.db.models import Prefetch
from .utils import get_object
from datetime import timedelta

class LessonViewSerializer(serializers.Serializer):
    view_time = serializers.DurationField()
    lesson_status = serializers.CharField()

class LessonSerializer(serializers.Serializer):
    lesson_name = serializers.CharField()
    link_to_video = serializers.URLField()
    lesson_view = LessonViewSerializer(source='lessonview_set', many=True)

class ProductSerializer(serializers.Serializer):
    product_name = serializers.CharField()
    lessons = LessonSerializer(many=True)

# 1 Задание
def user_lessons_serialize(profile: Profile):
    products = profile.enrolled_products.prefetch_related(
        Prefetch('lessons__lessonview_set', queryset=LessonView.objects.filter(user_profile=profile))
    ).all()
    result = ProductSerializer(products, many=True).data
    return result

# 2 Задание
def product_serialize(product_id: int, profile: Profile):
    product = profile.enrolled_products.prefetch_related(
        Prefetch('lessons__lessonview_set', queryset=LessonView.objects.filter(user_profile=profile))
    ).get(id=product_id)
    result = ProductSerializer(product).data
  
    return result

class ProductsStatisticSerializer(serializers.Serializer):
    product_name = serializers.CharField()
    product_owner = serializers.StringRelatedField()

    view_statistic = serializers.SerializerMethodField()
    profiles_statistic = serializers.SerializerMethodField()

    def get_profiles_statistic(self, obj):
        product_profiles = obj.profile_set.count()
        return {'total_profiles': product_profiles, 'acquisition_percentage': round(product_profiles / self.context['total_profiles'] * 100, 2)}

    def get_view_statistic(self, obj):
        total_view = 0
        total_view_time = timedelta()
        for profile in obj.profile_set.select_related('user').all():
            for lesson_view in profile.lessonview_set.all():
                if lesson_view.lesson_status == "Viewed":
                    total_view += 1
                total_view_time += lesson_view.view_time
        return {'total_view': total_view, 'total_view_time_in_min': total_view_time.total_seconds() / 60}


# 3 Задание
def products_serialize():
    total_profiles = Profile.objects.count()
    result = ProductsStatisticSerializer(Product.objects.select_related('product_owner', 'product_owner__user').all(), many=True,
     context={'total_profiles': total_profiles}).data
    
    return result