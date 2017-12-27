#coding:utf-8
import time
import requests
import json
import logging
import redis
import urllib2
import hashlib
import MySQLdb
from warnings import filterwarnings
filterwarnings('ignore', category = MySQLdb.Warning)
class preConditionForTest(object):
    """
    测试环境，常州账号数据准备测试：
    1.发放优惠券, 满30减5
    2.发放红包，满40减10
    3.发放达豆，默认2000
    4.上架物品, 价格50,数量100
    5.本地存储用户名，logindevice表
    6.本地存储上架物品，productcz表
    7.本地存储优惠码，coupon表
    8.清除购物车redis缓存信息
    """
    def __init__(self):
        self.headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
                      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}
        """
        server_url:测试环境后台url     
        url_username:后台登陆账号
        url_password:后台登陆密码
        """
        self.server_url = 'http://192.168.1.251:31000'
        self.url_username= '13111111111'
        self.url_password='123456'
        """
        test_db_ip:测试环境ip，默认端口3306
        test_user:用户名
        test_passwd:密码
        test_mainDb:测试环境 数据库
        """
        self.test_db_ip = '192.168.1.101'
        self.test_user = 'dddev'
        self.test_passwd = '123456'
        self.test_mainDb='ctcdb_new_test'
        """
        redis_db_ip:缓存数据库redis地址
        redis_port:redis端口
        redis_db:数据库0
        """
        self.redis_db_ip='192.168.1.101'
        self.redis_port=6379
        self.redis_db=0
        """
        local_ip:本地数据库192.168.1.38，默认localhost,端口3306
        local_user:用户名
        local_passwd:密码
        local_mainDb:本地数据库名
        """
        self.local_ip='192.168.1.38'
        self.local_user='root'
        self.local_passwd='admin'
        self.local_mainDb='dianda_test'
        """
        cityId:常州城市码
        """
        self.cityId=320400
        """
        dadouCount:发放达豆数量
        """
        self.dadouCount=2000
        """
        device_login:设备登陆密码
        """
        self.device_login='123456'
        """
        coupon_value:优惠券金额
        coupon_quantity:优惠券发放数量
        coupon_useBaseLine:使用金额条件
        coupon_instruction:描述
        """
        self.coupon_value=5
        self.coupon_quantity=5
        self.coupon_useBaseLine=30
        self.coupon_instruction=u'满30减5'
        """
        redGift_value:红包金额
        redGift_quantity:红包发放数量
        redGift_ownLimit:红包拥有限制量
        redGift_useBaseLine:红包使用条件
        redGift_instruction:描述
        """
        self.redGift_value=10
        self.redGift_quantity=5
        self.redGift_ownLimit=5
        self.redGift_useBaseLine=40
        self.redGift_instruction=u'满40减10'
        """
        product_price:上架产品的价格
        procuct_limit:上架产品的数量
        """
        self.product_price=50
        self.procuct_limit=100
        """
        conn_test:初始化链接测试环境数据库
        conn_local:初始化链接本地数据库
        """
        self.conn_test = MySQLdb.connect(host=self.test_db_ip, user=self.test_user, passwd=self.test_passwd, port=3306,charset="utf8")
        self.conn_local = MySQLdb.connect(host=self.local_ip, user=self.local_user, passwd=self.local_passwd, port=3306, charset="utf8")

        """
        session:初始化session节点
        """
        self.session=requests.Session()
        """
        初始化log格式
        """
        logging.basicConfig(
                            level=logging.DEBUG,
                            format='[%(asctime)s] [%(levelname)s] %(message)s',
                            datefmt='%Y_%m_%d %H:%M:%S',
        )
    @classmethod
    def changeIntoStr(cls,data,str_data=''):
        if isinstance(data, unicode):
            str_data = data.encode('utf-8')
        elif isinstance(data, str):
            str_data = data
        return str_data

    @classmethod
    def returnMd5(cls,pwd):
        md = hashlib.md5()
        md.update(pwd)
        return md.hexdigest()

    @staticmethod
    def createTime():
        """
        :return: 返回发放开始时间，发放结束时间，可使用开始时间，可使用结束时间
        """
        grantStart = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()- 1* 60 * 60))
        useStart = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()- 2* 60 * 60))
        useEnd = grantEnd = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 24 * 60 * 60))
        return grantStart, grantEnd, useStart, useEnd

    @staticmethod
    def createName():
        """
        :return:返回自动创建名字
        """
        couponName = u'自动测' + str(int(time.time()))
        return couponName

    def newCoupon(self):
        """
        创建优惠码
        :return:
        """
        couponName=self.createName()
        grantStart,grantEnd,useStart,useEnd=self.createTime()
        #登陆后台
        login_url='{0}/users/login'.format(self.server_url)
        login_data={'userName':self.url_username,'password':self.url_password}
        login_response=self.session.post(url=login_url,data=login_data,headers=self.headers)
        #选择城市
        changzhou_url='{0}/users/updateAgency'.format(self.server_url)
        changzhou_data={'cityId':self.cityId,'agencyId':3}
        chanzhou_response=self.session.post(url=changzhou_url,data=changzhou_data,headers=self.headers)
        #创建单
        youhuiquan_url='{0}/json/management/coupon/addCoupon'.format(self.server_url)
        """
        type：2, 优惠码
        grantType:-1 无兑换条件
        lifeTime:-1 无领取时间限制
        """
        youhuiquan_data={'couponName':couponName,'type':2,'grantType':'-1','value':self.coupon_value,'grantStart':grantStart,
                         'grantEnd':grantEnd,'useStart':useStart,'useEnd':useEnd,
                         'lifeTime':'-1','quantity':self.coupon_quantity,'useBaseLine':self.coupon_useBaseLine,'instruction':self.coupon_instruction}
        youhuiquan_response=self.session.post(youhuiquan_url,data=youhuiquan_data,headers=self.headers)
        youhuiquan_strdata = self.changeIntoStr(youhuiquan_response.text)
        youhuiquan_json=json.loads(youhuiquan_strdata)
        #点击导出
        daochu_url='{0}/json/management/coupon/queryCoupon?id={1}'.format(self.server_url,str(youhuiquan_json['gift']['id']))
        daochu_response=self.session.get(url=daochu_url,headers=self.headers)
        daochu_data=self.changeIntoStr(daochu_response.text)
        testdata=json.loads(daochu_data)
        #拼接下载url地址
        test_url = '{7}/json/management/coupon/code/generate?couponCodeBaseSettingId={0}' \
            '&name={1}&useStart={2}&useEnd={3}&quantity={4}&value={5}&useBaseLine={6}'.format(  testdata['data']['id'],
                                                                                                urllib2.quote(testdata['data']['couponName'].encode('utf-8')),
                                                                                                testdata['data']['useStartTime'],
                                                                                                testdata['data']['useEndTime'],
                                                                                                testdata['data']['grantCount'],
                                                                                                testdata['data']['value'],
                                                                                                testdata['data']['useBaseLine'],
                                                                                                self.server_url)
        self.session.get(url=test_url,headers=self.headers)
        return youhuiquan_json['gift']['id'],youhuiquan_data['couponName']

    def connectTestMysql(self):
        """
        链接测试环境数据库
        :returns:返回优惠码信息,giftID,couponName
        """
        giftID,couponName=self.newCoupon()
        cur = self.conn_test.cursor()
        self.conn_test.select_db(self.test_mainDb)
        count = cur.execute('select code from coupon_codes WHERE CouponCodeBaseSettingId = {0}'.format(giftID))
        info = cur.fetchmany(count)
        self.conn_test.commit()
        cur.close()
        return info,giftID,couponName

    def createCouponTabel(self):
        """
        本地数据库 创建Coupon表
        """
        getData,_id,name=self.connectTestMysql()
        cur = self.conn_local.cursor()
        self.conn_local.select_db('dianda_test')
        cur.execute('create table if not exists Coupon(id int ,couponName varchar(20),coupon_id int(10),coupon_code VARCHAR(20),PRIMARY KEY(id))')
        cur.execute('delete from Coupon')
        for data in getData:
            logging.info(str(data[0]))
            cur.execute("insert into Coupon(id,couponName,coupon_id,coupon_code)values('%d','%s','%d','%s')" % (getData.index(data), name, _id, data[0]))
        self.conn_local.commit()
        cur.close()

    def createNewRedGift(self):
        """
        创建红包
        :return:
        """
        name = self.createName()
        grantStart, grantEnd, useStart, useEnd = self.createTime()
        #登录
        login_url = '{0}/users/login'.format(self.server_url)
        login_data = {'userName':self.url_username,'password':self.url_password}
        login_response = self.session.post(url=login_url, data=login_data, headers=self.headers)
        #切换城市
        changzhou_url = '{0}/users/updateAgency'.format(self.server_url)
        changzhou_data = {'cityId': self.cityId, 'agencyId': 3}
        chanzhou_response = self.session.post(url=changzhou_url, data=changzhou_data, headers=self.headers)
        #新增红包
        redgift_url = '{0}/json/management/promotional/coupon/redgift/add'.format(self.server_url)
        """
        ownLimit:用户拥有限制数量
        vipRank:vip无限制
        lifeTime:使用周期不限制
        """
        redgift_data = {'name': name, 'type': u'普通红包', 'value': self.redGift_value, 'grantStart': grantStart,
                        'grantEnd': grantEnd, 'useStart': useStart, 'useEnd': useEnd,'lifeTime':-1,
                        'quantity': self.redGift_quantity, 'ownLimit': self.redGift_ownLimit, 'useBaseLine': self.redGift_useBaseLine,
                        'vipRank': '-1','instruction': self.redGift_instruction}
        redgift_response = self.session.post(redgift_url, data=redgift_data, headers=self.headers)
        redgift_str=self.changeIntoStr(redgift_response.text)
        redgift_json = json.loads(redgift_str)
        logging.info(str(redgift_json))
        return redgift_json

    def searchTestStoreUser(self):
        """
        搜索测试环境数据库stores账户信息
        """
        pwd_MD5=self.returnMd5(self.device_login)
        cur = self.conn_test.cursor()
        self.conn_test.select_db(self.test_mainDb)
        count=cur.execute('select id,storeUser,storePwd,storeName,storePhoneNum,storeState,dadou,CityId,isFirstLogin from stores WHERE storeState= 1 AND CityId = {0} AND storePwd = "{1}" AND LENGTH(storePhoneNum)=11 '.format(self.cityId, pwd_MD5))
        info = cur.fetchmany(count)
        self.conn_test.commit()
        cur.close()
        return info[3]

    def createLoginDeviceTabel(self):
        """
        本地数据库 创建logindevice表
        """
        _id, storeUser, storePwd, storeName, storePhoneNum, storeState, dadou, CityId, isFirstLogin = self.searchTestStoreUser()
        cur = self.conn_local.cursor()
        self.conn_local.select_db(self.local_mainDb)
        cur.execute('create table if not exists logindevice(id int ,storeUser varchar(20),storePwd varchar(50),storeName varchar(20),storePhoneNum varchar(15),storeState varchar(5),dadou varchar(10),CityId VARCHAR(10),isFirstLogin VARCHAR(5),PRIMARY KEY(id))')
        cur.execute("delete from logindevice")
        cur.execute("insert into logindevice(id,storeUser,storePwd,storeName,storePhoneNum,storeState,dadou,CityId,isFirstLogin)values('%d','%s','%s','%s','%s','%s','%s','%s','%s')" % (_id, storeUser, storePwd, storeName, storePhoneNum, storeState, dadou, CityId, isFirstLogin))
        logging.info(str(_id))
        self.conn_local.commit()
        cur.close()

    def UpdateTestUserDadou(self):
        """
        更新账号达豆数量,默认改为2000
        """
        testID=self.getLocalLoginDeviceID()
        cur = self.conn_test.cursor()
        self.conn_test.select_db('ctcdb_new_test')
        cur.execute("update stores set dadou={0} where id = {1}".format(self.dadouCount, testID[0]))
        # cur.execute('select dadou from stores WHERE id= {0}'.format(testID[0]))
        # info = cur.fetchone()
        # print info
        self.conn_test.commit()
        cur.close()

    def getLocalLoginDeviceID(self):
        """
        获取当前账号id
        :return: info
        """
        cur = self.conn_local.cursor()
        self.conn_local.select_db(self.local_mainDb)
        cur.execute('select id from logindevice')
        info = cur.fetchone()
        self.conn_local.commit()
        cur.close()
        return info

    def clean_redis(self):
        """
        清空缓存购物车信息
        """
        rd = redis.Redis(host=self.redis_db_ip, port=self.redis_port, db=self.redis_db)
        testID = self.getLocalLoginDeviceID()
        key_ = 'cart:{0}'.format(testID[0])
        if rd.exists(key_):
            rd.delete(key_)

    def newProduct(self):
        """
        新建上架商品
        """
        publish_Name = self.createName()
        publish_time = self.createTime()
        #登录
        login_url = '{0}/users/login'.format(self.server_url)
        login_data = {'userName':self.url_username,'password':self.url_password}
        login_response = self.session.post(url=login_url, data=login_data, headers=self.headers)
        #选择常州
        changzhou_url = '{0}/users/updateAgency'.format(self.server_url)
        changzhou_data = {'cityId': self.cityId, 'agencyId': 3}
        chanzhou_response = self.session.post(url=changzhou_url, data=changzhou_data, headers=self.headers)
        # 排序单
        """
        'order[0][dir]': 'desc' 按可用库存排序
        """
        kucun_url = '{0}/api/goods/stock/list'.format(self.server_url)
        kucun_data = {'draw': 2, 'order[0][dir]': 'desc'}
        kucun_response = self.session.post(url=kucun_url, data=kucun_data, headers=self.headers)
        kucun_str = self.changeIntoStr(kucun_response.text)
        kucun_json = json.loads(kucun_str)
        product_id = []
        for q in kucun_json['data']:
            if q['qoa'] > 1000:
                product_id.append(q['id'])
        if product_id:
            good_id = product_id[0]
            #上架操作
            publish_url = '{0}/api/goods/shelve/publish'.format(self.server_url)
            """
            catalogId:商品分类
            areaPriceStr:价格定位
            """
            publish_data = {'isDirectSell': '0', 'combos[0][isFree]': '0', 'comboType': '0', 'catalogId': '3010000','vip': '0', 'yjPrice': '0', 'id': good_id,
                            'isHotFirst': '0', 'title': publish_Name, 'specification': '1','combos[0][id]': good_id,'type': '0', 'combos[0][originalPrice]': '0',
                            'onSale': '0', 'dadou': '0','price': self.product_price, 'isAllFirst': '0','startTime': publish_time[0], 'isOrderLimit': 'unlimited', 'isTypeFirst': '0',
                            'endTime': publish_time[1], 'combos[0][packageNum]': '1','amount': '1', 'limit': self.procuct_limit, 'isDiscount': '1',
                            'areaPriceStr': '101:{0}#103:{1}#111:{2}#115:{3}#141:{4}#142:{5}#147:{6}#151:{7}#152:{8}#155:{9}#160:{10}#'.format(self.product_price,self.product_price,self.product_price,
                                                                                                                                               self.product_price,self.product_price,self.product_price,
                                                                                                                                               self.product_price,self.product_price,self.product_price,
                                                                                                                                               self.product_price,self.product_price),
                            'combos[0][unit]': '1', 'notSoldPriceArea': '[]', 'combos[0][price]': '0'}
            publish_response = self.session.post(url=publish_url, data=publish_data, headers=self.headers)
            publish_str = self.changeIntoStr(publish_response.text)
            publish_json = json.loads(publish_str)
            if publish_json['status'] == 1:
                search_id_url = '{0}/json/goods/shelve/list'.format(self.server_url)
                search_id_data = {'name': publish_Name}
                search_id_response = self.session.post(url=search_id_url, data=search_id_data, headers=self.headers)
                search_id_str = self.changeIntoStr(search_id_response.text)
                search_id_json = json.loads(search_id_str)
                if search_id_json['recordsTotal'] == 1:
                    on_sell_data = [search_id_json['data'][0]['id'], search_id_json['data'][0]['name'], self.product_price, self.procuct_limit,good_id, self.cityId]
                    return on_sell_data

    def createProductTable(self):
        """
        本地数据库 创建productcz表
        """
        CZ_data=self.newProduct()
        if CZ_data:
            cur = self.conn_local.cursor()
            self.conn_local.select_db(self.local_mainDb)
            cur.execute('create table if not exists productcz(id int ,name varchar(50),price VARCHAR(10),`limit` int(10),GoodId int(10),CityId int(10), PRIMARY KEY(id))')
            cur.execute('delete from productcz')
            cur.execute("insert into productcz(id,name,price,`limit`,GoodId,CityId)values('%d','%s','%s','%d','%d','%d')" % (CZ_data[0], CZ_data[1], CZ_data[2], CZ_data[3], CZ_data[4], CZ_data[5]))
            logging.info(str(CZ_data[0]))
            self.conn_local.commit()
            cur.close()

    def mainrun(self):
        """
        主函数运行
        """
        preConditionForTest().createCouponTabel()
        preConditionForTest().createNewRedGift()
        preConditionForTest().createLoginDeviceTabel()
        preConditionForTest().UpdateTestUserDadou()
        preConditionForTest().createProductTable()
        preConditionForTest().clean_redis()
if __name__=="__main__":
    preConditionForTest().mainrun()