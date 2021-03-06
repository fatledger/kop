# coding=utf-8

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.my_user_name, filename)

# Create your models here.
# @python_2_unicode_compatible # only if you need to support Python 2

class UserProfile(models.Model):
    my_user_name = models.CharField(max_length=100)
    create_date = models.DateTimeField('date created')
    phone = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    company = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)

class Mydata(models.Model):
    data_name = models.CharField(max_length=200)
    my_user_name = models.CharField(max_length=100)
    create_date = models.DateTimeField('date created')
    smoke_status = models.CharField(max_length=10, null=True)
    gender = models.CharField(max_length=2, null=True)
    sick_type = models.CharField(max_length=10, null=True)
    life_status = models.CharField(max_length=10, null=True)
    ICDO3 = models.IntegerField(default=0)
    patho_status = models.CharField(max_length=5, null=True)
    data_des = models.CharField(max_length=200, null=True)
    genome_file = models.FileField(upload_to=user_directory_path, null=True)
    meth_file = models.FileField(upload_to=user_directory_path, null=True)
    micro_file = models.FileField(upload_to=user_directory_path, null=True)
    mRNA_file = models.FileField(upload_to=user_directory_path, null=True)

    def __str__(self):
        return self.data_des

    def getGenderStr(self):
        if self.gender == u'M':
            return u'男'
        else:
            return u'女'

    def getSmokeStr(self):
        if self.smoke_status == 'NS':
            return 'Non-smoker'
        elif self.smoke_status == 'SF15':
            return 'Smoker For <= 15 Years'
        elif self.smoke_status == 'SF16':
            return 'Smoker For > 15 Years'
        else:
            return 'N/A'

    def getLifeStatusStr(self):
        if self.life_status == 'L':
            return u'在世'
        elif self.life_status == 'O':
            return u'过世'        
        else:
            return 'N/A'

    def getSickTypeStr(self):
        if self.sick_type == 'LAML':
            return u'急性髓系白血病'
        elif self.sick_type == 'ACC':
            return u'肾上腺皮质癌'
        elif self.sick_type == 'BLCA':
            return u'膀胱尿路上皮癌'
        elif self.sick_type == 'LGG':
            return u'脑低级神经胶质瘤'
        elif self.sick_type == 'BRCA':
            return u'乳腺浸润性癌'
        elif self.sick_type == 'CESC':
            return u'宫颈癌'
        elif self.sick_type == 'CHOL':
            return u'胆管癌'
        elif self.sick_type == 'COAD':
            return u'结肠癌'
        elif self.sick_type == 'ESCA':
            return u'食管癌'
        elif self.sick_type == 'GBM':
            return u'胶质母细胞瘤'
        elif self.sick_type == 'HNSC':
            return u'头颈部鳞状细胞癌'
        elif self.sick_type == 'KICH':
            return u'肾嫌色'
        elif self.sick_type == 'KIRC':
            return u'肾透明细胞癌'
        elif self.sick_type == 'KIRP':
            return u'肾乳头细胞癌'
        elif self.sick_type == 'LIHC':
            return u'肝癌'
        elif self.sick_type == 'LUAD':
            return u'肺腺癌'
        elif self.sick_type == 'LUSC':
            return u'肺鳞癌'
        elif self.sick_type == 'DLBC':
            return u'淋巴肿瘤弥漫大B细胞淋巴瘤'
        elif self.sick_type == 'MV':
            return u'间皮瘤'
        elif self.sick_type == 'OV':
            return u'卵巢浆液性囊腺癌'
        elif self.sick_type == 'PAAD':
            return u'胰腺癌'
        elif self.sick_type == 'PCPG':
            return u'嗜铬细胞瘤和副神经节瘤'
        elif self.sick_type == 'PRAD':
            return u'前列腺癌'
        elif self.sick_type == 'READ':
            return u'直肠癌'
        elif self.sick_type == 'SARC':
            return u'肉瘤'
        elif self.sick_type == 'SKCM':
            return u'皮肤黑色素瘤'
        elif self.sick_type == 'STAD':
            return u'胃癌'
        elif self.sick_type == 'TGCT':
            return u'睾丸生殖细胞肿瘤'
        elif self.sick_type == 'THYM':
            return u'胸腺瘤'
        elif self.sick_type == 'THCA':
            return u'甲状腺癌'
        elif self.sick_type == 'UCS':
            return u'子宫癌肉瘤'
        elif self.sick_type == 'UCEC':
            return u'子宫内膜癌'
        elif self.sick_type == 'UVM':
            return u'葡萄膜黑色素瘤'
        else:
            return 'N/A'    
        
class MyDataQuery(models.Model):    
    my_user_name = models.CharField(max_length=100)
    mydata_id = models.IntegerField()
    data_name = models.CharField(max_length=200)
    smoke_status = models.CharField(max_length=10, null=True)
    gender = models.CharField(max_length=2, null=True)
    sick_type = models.CharField(max_length=10, null=True)
    life_status = models.CharField(max_length=10, null=True)
    ICDO3 = models.IntegerField(default=0)
    patho_status = models.CharField(max_length=5, null=True)
    created_date = models.DateTimeField('date created')
    genome_file = models.CharField(max_length=256)
    status_id = models.IntegerField(default=0)
    query_type = models.IntegerField(default=0)
	
    def __str__(self):
        return self.my_user_name

class MyBalanceInfo(models.Model):
    my_user_name = models.CharField(max_length=100)
    deposit = models.FloatField(default=0)
    balance = models.FloatField(default=0)
    price = models.FloatField(default=0)
    price_start_date = models.DateTimeField('start date')
    price_end_date = models.DateTimeField('end date')
    created_date = models.DateTimeField('date created')

    def __str__(self):
        return self.my_user_name

class ContactInfo(models.Model):    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    tittle = models.CharField(max_length=50, null=True)
    company = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    created_date = models.DateTimeField('date created')
    description = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name
