from django.db import models


class Order(models.Model):
    farmer_phone = models.CharField('농장주 핸드폰 번호',max_length=11)
    from_name = models.CharField('보내는 분 이름',max_length=50)
    from_phone = models.CharField('보내는 분 번호',max_length=11,help_text='가급적 핸드폰 번호로 입력 부탁드립니다.')
    to_name = models.CharField('받는 분 이름',max_length=50)
    to_phone = models.CharField('받는 분 번호',max_length=11,help_text='가급적 핸드폰 번호로 입력 부탁드립니다.')
    to_address = models.CharField('받는 분 주소',max_length=100,help_text='정확한 주소를 입력해주세요. 주소 입력 후 한번 더 확인 부탁드립니다.')
    quantity = models.PositiveIntegerField('주문 수량')
    grade = models.CharField('상품 등급',max_length=50)
    price = models.PositiveIntegerField('주문 가격')
    order_date = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ('-order_date',)
