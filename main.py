# 从fastapi库中 导入Fastapi 还有Form表单 还有Request请求
from fastapi import FastAPI, Request, Form
from starlette import status
# 重定向
from starlette.responses import RedirectResponse
# 导入模板引擎
from fastapi.templating import Jinja2Templates
# 导入静态文件支持
from starlette.staticfiles import StaticFiles
# 导入数据库ORM
from tortoise.contrib.fastapi import register_tortoise
# 导入用户表模型
from dao.models import User
# 导入分类表模型
from dao.models import Class
# 导入商品表模型
from dao.models import Commodity
# 导入订单表模型
from dao.models import Order

# 绑定app
app = FastAPI()
# 设置模板文件夹路径
template = Jinja2Templates("pages")
# 挂载静态文件夹, 'static' 为你的静态文件夹路径
app.mount("/static", StaticFiles(directory="static"), name="static")
# 连接数据库
register_tortoise(app,
                  db_url="mysql://shop_9527:HSArrWcBiA3YKjmF@120.25.216.91:3306/shop_9527",
                  modules={"models": ['dao.models']},
                  add_exception_handlers=True,
                  generate_schemas=True
                  )


# 首页路由
@app.get("/")
# 必须带入一个变量，并且值是等于Request
async def index(req: Request):
    # 获取所有的todes
    all_users = await User.all()
    # 基于模板引擎返回首页 必须带入context，并且把req的变量通过request传给 页面
    return template.TemplateResponse("index.html", context={"request": req, "User": all_users})


# 商店路由
@app.get("/shop")
# 必须带入一个变量，并且值是等于Request
def shop(req: Request):
    # 基于模板引擎返回首页 必须带入context，并且把req的变量通过request传给 页面
    return template.TemplateResponse("shop.html", context={"request": req})


# 兑换码路由
@app.get("/code")
# 必须带入一个变量，并且值是等于Request
def code(req: Request):
    # 基于模板引擎返回首页 必须带入context，并且把req的变量通过request传给 页面
    return template.TemplateResponse("code.html", context={"request": req})


# 详情页路由
@app.get("/details")
# 必须带入一个变量，并且值是等于Request
def details(req: Request):
    # 基于模板引擎返回首页 必须带入context，并且把req的变量通过request传给 页面
    return template.TemplateResponse("details.html", context={"request": req})


# 登录页面
@app.get("/login")
def login(req: Request):
    return template.TemplateResponse("login.html", context={"request": req})


# 登录接口
@app.post("/login")
async def login(req: Request, username: str = Form(None), password: str = Form(None)):
    user = await User.filter(username=username).first()
    if user and user.password == password:
        # 登录成功，重定向到首页或其他页面
        return RedirectResponse(url='/admin', status_code=status.HTTP_302_FOUND)
    else:
        # 登录失败，返回登录页面并显示错误信息
        error_message = "温馨提示：账号或密码错误"
        return template.TemplateResponse("login.html", context={"request": req, "error": error_message})


# 后台管理-启动台页面接口
@app.get("/admin")
def admin(req: Request):
    username = "ponon"
    return template.TemplateResponse("admin.html", context={"request": req, "username": username})


# 后台管理-分类管理
@app.get("/admin_class")
async def adminclass(req: Request):
    # 获取所有的todes
    all_class = await Class.all()
    username = "ponon"
    return template.TemplateResponse("admin_class.html",
                                     context={"request": req, "allclass": all_class, "username": username})


# 后台管理-添加分类
@app.get("/admin_addclass")
async def adminaddclass(req: Request):
    # 获取所有的todes
    username = "ponon"
    return template.TemplateResponse("admin_addclass.html", context={"request": req, "username": username})


# 后台管理-添加分类-提交接口
@app.post("/class")
async def create_class(class_name: str = Form(None)):
    await Class(class_name=class_name).save()
    return RedirectResponse("/admin_class", status_code=status.HTTP_302_FOUND)


# 后台管理-产品管理
@app.get("/admin_product")
async def allproduct(req: Request):
    # 获取所有商品
    all_commodities = await Commodity.all()
    # 设置用户名
    username = "ponon"
    return template.TemplateResponse("admin_product.html",
                                     context={"request": req, "all_commodities": all_commodities, "username": username})


# 后台管理-添加分类
@app.get("/admin_addproduct")
async def adminaddproduct(req: Request):
    username = "ponon"
    return template.TemplateResponse("admin_addproduct.html", context={"request": req, "username": username})


# 后台管理-产品管理-提交接口
@app.post("/product")
async def create_product(class_name: str = Form(None)):
    await Class(class_name=class_name).save()
    return RedirectResponse("/admin_class", status_code=status.HTTP_302_FOUND)


# 后台管理-订单管理
@app.get("/admin_order")
async def allorder(req: Request):
    # 获取所有商品
    allorder = await Order.all()
    # 设置用户名
    username = "ponon"
    return template.TemplateResponse("admin_order.html",
                                     context={"request": req, "allorder": allorder, "username": username})
