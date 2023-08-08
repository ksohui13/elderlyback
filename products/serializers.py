from rest_framework import serializers
from products.models import Product, Review, ProductQuest, QuestComment

#router
#상품등록
class ProductRouterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = '__all__' # 전부다 넣고싶을 때, 각각 넣으려면 [ ]
        fields = ['product_name', 'category', 'product_des', 'detail_description', 'ingredient', 
                    'price_origin', 'price_sale', 'product_sotck', 'thumbnail']
        

#리뷰
class ReivewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['product', 'rating', 'review_content']



#상품문의 답변
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.email')

    class Meta:
        model = QuestComment
        fields = '__all__'
        read_only_fields = ['quest', 'user']


#상품문의
class PrdQuestSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.email')
    comment = CommentSerializer(many=True, read_only = True)

    class Meta:
        model = ProductQuest
        #fields = ['product', 'questtitle', 'questcontent', 'questimage']
        fields = '__all__'
        read_only_fields = ['user', 'comment']

