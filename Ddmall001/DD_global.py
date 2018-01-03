import requests,time
class global_system():
    def __init__(self):
        self.global_url='http://192.168.1.251:39000'
        self.session = requests.session()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}

    def create_product(self):
        self.name = input('输入商品名：') + '_' + str(int((time.time())))
        # 登录全局系统
        login_data = {
            'userName' : 12345678910,
            'password' : 123456
        }
        login = self.session.post(url=self.global_url + '/users/login',data=login_data,headers = self.headers)
        # 切换城市
        city_data = {
            'cityId' : 320200,
            'agencyId' : 17
        }
        cut_city = self.session.post(url=self.global_url + '/users/updateAgency',data=city_data,headers = self.headers)
        # 添加商品
        add_data = {
            'brandId':'2436',
            'country':'中国',
            'name': self.name,
            'catalog':['0','4090100','2'],
            'packType':'0',
            'barCode':'123456',
            'catalogId':'4090100',
            'specification':'12瓶/箱',
            'unit':'1',
            'tax':'17',
            'length':'1',
            'width':'1',
            'height':'1',
            'volume':'1.00',
            'weight':'1',
            'termOfValidity':'180',
            'timeUnit':'2',
            'transProportion':'1',
            'introduction':'<p>test</p>',
        }
        add_product = self.session.post(url=self.global_url + '/goods/add',data=add_data,headers = self.headers)
        # 提取库存编号
        with open('data','rt')as f:
            data = eval(f.read())
        goods_list = self.session.post(url=self.global_url + '/goods/list/Json',data=data)
        goods_json = goods_list.json()
        for good_json in goods_json['data']:
            if self.name == good_json['name']:
                self.good_id = good_json['id']
                print('商品名称:%s\t库存编号:%d'%(self.name,self.good_id))
                break
        # 提交新品图片处理
        submit_product = self.session.post(url=self.global_url + '/goods/submitImg',data={'id':self.good_id},headers = self.headers)
        # 上传图片
        files_data = {
            'id':self.good_id,
            'imagePaths':-1,
            'images':'0'
        }
        files_jpg = {'image0':('1.jpg',open('1.jpg','rb'),'image/jpeg')}
        commit_file = self.session.post(self.global_url + '/goods/addFile',data=files_data,files=files_jpg,headers = self.headers)
        print(commit_file.status_code)


if __name__=='__main__':
    global_os = global_system()
    global_os.create_product()

