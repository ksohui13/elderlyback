from django.db import models
from mainshop.models import TimeStampModel
from accounts.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

MainCategory_choices = (
    (0, 'Food'),
    (1, 'living'),
    (2, 'culture'),
    (3, '')
)


# # 카테고리 : 푸드, 리빙, 교육/문화
class Category(TimeStampModel):
    category = models.CharField(max_length=100, default='3')

    class Meta:
        db_table = 'main_categories'


#상품
class Product(TimeStampModel):
    product_id = models.AutoField(primary_key=True)                 #상품 번호
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    product_name = models.TextField()                               #상품명
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=True, default=3)
    product_des = models.TextField()                                #상품 설명
    detail_description = models.TextField()                         #상품상세설명
    ingredient = models.TextField()                                 #원재료
    price_origin = models.IntegerField(default=0)                    #정가
    price_sale = models.IntegerField(default=0)                      #노인 복지 스토어 가격
    discount = models.IntegerField(default=0)                      #정가 - 복지스토어 가격 (할인가격)
    product_sotck = models.IntegerField(default=0)                   #재고
    thumbnail = models.ImageField(upload_to="", null = True, blank=True, default='') #이미지 파일 업로드
    is_active = models.BooleanField('활성화 여부', default=True)
    
    class Meta:
        db_table = 'products'

#리뷰
class Review(TimeStampModel):
    user = models.ForeignKey('accounts.User',verbose_name="작성자", on_delete=models.SET_NULL, null=True)  #유저
    product = models.ForeignKey('Product', verbose_name="상품", on_delete=models.CASCADE) #리뷰가 적힐 제품 : 상속
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)]) #리뷰 별점 0~5점
    review_content = models.TextField()                              #리뷰 내용

    class Meta:
        db_table = 'product_review'

    def __str__(self):
        return f'Review : {self.product.product_name} - {self.user.email} ({self.rating})'


#상품문의
class ProductQuest(TimeStampModel):
    qusetid = models.AutoField(primary_key=True, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', verbose_name="상품", on_delete=models.CASCADE)
    questtitle = models.CharField(max_length=50)
    questcontent = models.TextField()
    questimage = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return self.questtitle

#상품문의 댓글
class QuestComment(models.Model):
    quest_id = models.ForeignKey(ProductQuest, related_name="qcomment", on_delete=models.CASCADE, db_column="qid")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name="reply", on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField()

    def __str__(self) -> str:
        return self.comment
    

############################################################################        
# # 카테고리 : 푸드, 리빙, 교육/문화
# class MainCategor1y(TimeStampModel):
#     main_categor1y = models.CharField(max_length=50)
#     # main_category11 = models.SmallIntegerField(choices=MainCategory_choices)

#     class Meta:
#         db_table = 'main_categories'

# # 서브 카테고리 : 유제품, 가공식품,...,/의류, 가전제품,.../연극, 콘서트,...등
# # 현재는 계획x
# class SubCategory(TimeStampModel):
#     main_categor1y = models.ForeignKey('MainCategor1y', on_delete=models.SET_NULL, null=True)
#     sub_categor1y = models.CharField(max_length=50)

#     class Meta:
#         db_table = 'sub_categories'

# # 상품 이미지
# class ProductImg(TimeStampModel):
#     image_url    = models.URLField(null=True, blank=True)                                        #파일 url
#     is_thumbnail = models.BooleanField(default=False)                       #썸네일 여부
#     product      = models.ForeignKey('Product', on_delete=models.CASCADE)   #등록할 제품
    
#     class Meta:
#         db_table = 'product_images'
