from tortoise import Model, fields


# 用户表
class User(Model):
    # 对应数据库中的一个用户表
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=100)
    password = fields.CharField(max_length=100)


# 商品表
class Commodity(Model):
    # 对应数据库中的一个表
    id = fields.IntField(pk=True)  # 商品ID
    name = fields.CharField(max_length=500, description='商品名称')  # 商品名称
    price = fields.DecimalField(max_digits=10, decimal_places=2, description='商品价格')  # 商品价格
    brief = fields.TextField(description='商品简介')  # 商品简介
    details = fields.TextField(description='商品详情')  # 商品详情
    classification = fields.IntField(description='商品分类')  # 商品分类
    download_link = fields.CharField(max_length=1000, null=True, description='下载链接')  # 下载链接，如果有的话
    demo_link = fields.CharField(max_length=1000, null=True, description='DEMO链接')  # DEMO链接，如果有的话
    created_at = fields.DatetimeField(auto_now_add=True, description='上传时间')  # 上传时间


# 订单表
class Order(Model):
    id = fields.BigIntField(pk=True, description='订单id')  # 订单ID
    product_id = fields.BigIntField(description='商品id')  # 商品ID
    product_name = fields.CharField(max_length=255, null=True, description='商品名称')  # 商品名称
    email = fields.CharField(max_length=255, null=True, description='邮箱')  # 客户邮箱
    price = fields.IntField(null=True, description='价格(分)')  # 价格
    create_time = fields.DatetimeField(auto_now=True, description='创建时间')  # 创建时间
    pay_time = fields.DatetimeField(null=True, description='付款时间')  # 支付时间
    status = fields.IntField(null=True, description='状态: 1.已下单, 2.已付款')  # 状态


# 分类表
class Class(Model):
    id = fields.IntField(pk=True)  # 分类ID
    class_name = fields.CharField(max_length=255, null=True, description='分类名称')  # 分类名称
    class_create_time = fields.DatetimeField(auto_now=True, description='创建时间')  # 创建时间
