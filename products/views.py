from rest_framework import viewsets
from products.models import Product, Review, QuestComment, ProductQuest
from products.serializers import ProductRouterSerializer, ReivewSerializer, CommentSerializer, PrdQuestSerializer

from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly


from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend

#라우터 방식
#페이지네이션
class ProductPagination(PageNumberPagination):
    page_size = 15

#로그인만 글쓰기 가능
#상품 등록/수정/삭제
class ProductViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] 
    pagination_class = ProductPagination

    #검색
    filter_backends = [SearchFilter]
    SearchFilter = ['product_name', 'category']

    #필터
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_name', 'category', 'category_id']

    queryset = Product.objects.all()
    serializer_class = ProductRouterSerializer

    #상품 찾기
    def get_queryset(self):
        qs = super().get_queryset() 

        search_name = self.request.query_params.get('product_name',) 
        if search_name:
            qs = qs.filter(name__icontains=search_name) #대소문자 구분없이 검색
        return qs
    
    #상품 등록
    def create_product(self, serializer):
        serializer.save(user=self.request.user)


#리뷰 등록
class ReviewViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] 
    pagination_class = ProductPagination

    #검색
    filter_backends = [SearchFilter]
    SearchFilter = ['rating', 'review_content']

    #필터
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product', 'review_content']

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['review_content']

    queryset = Review.objects.all()
    serializer_class = ReivewSerializer

    
    #상품 등록
    def create_review(self, serializer):
        serializer.save(user=self.request.user)

#상품문의
class ProQuestViewSet(viewsets.ModelViewSet):
    queryset = ProductQuest.objects.all()
    serializer_class = PrdQuestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


#상품문의답변
class CommentViewSet(viewsets.ModelViewSet):
    queryset = QuestComment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


