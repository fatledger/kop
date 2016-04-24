# coding=utf-8

from django import forms

# Create your forms here.
# @python_2_unicode_compatible
class UserForm(forms.Form):
    user_name = forms.CharField(label=u'用户名', max_length=100)
    email = forms.EmailField(label=u'电子邮件')
    password1 = forms.CharField(label=u'密码', max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(label=u'密码确认', max_length=100, widget=forms.PasswordInput)    
    first_name = forms.CharField(label=u'名', max_length=100, required=False)
    last_name = forms.CharField(label=u'姓', max_length=100, required=False)
    phone = forms.CharField(label=u'电话', max_length=100,required=False)
    title = forms.CharField(label=u'职务', max_length=100,required=False)
    company = forms.CharField(label=u'公司', max_length=100,required=False)
    address = forms.CharField(label=u'地址', max_length=100,required=False)
    city = forms.CharField(label=u'城市', max_length=100,required=False)
    state = forms.CharField(label=u'省份', max_length=100,required=False)
    country = forms.CharField(label=u'国家', max_length=100,required=False)

class UserProfileForm(forms.Form):    
    phone = forms.CharField(label=u'电话', max_length=100,required=False)
    title = forms.CharField(label=u'职务', max_length=100,required=False)
    company = forms.CharField(label=u'公司', max_length=100,required=False)
    address = forms.CharField(label=u'地址', max_length=100,required=False)
    city = forms.CharField(label=u'城市', max_length=100,required=False)
    state = forms.CharField(label=u'省份', max_length=100,required=False)
    country = forms.CharField(label=u'国家', max_length=100,required=False)

class DataForm(forms.Form):
    CANCER_TYPE_CHOICES = (('LAML',u'急性髓系白血病'),('ACC',u'肾上腺皮质癌'),
    ('BLCA',u'膀胱尿路上皮癌'),('LGG',u'脑低级神经胶质瘤'),('BRCA',u'乳腺浸润性癌'),('CESC',u'宫颈癌'),
    ('CHOL',u'胆管癌'),('COAD',u'结肠癌'),('ESCA',u'食管癌'),('GBM',u'胶质母细胞瘤'),('HNSC',u'头颈部鳞状细胞癌'),
    ('KICH',u'肾嫌色'),('KIRC',u'肾透明细胞癌'),('KIRP',u'肾乳头细胞癌'),('LIHC',u'肝癌'),('LUAD',u'肺腺癌'), ('LUSC',u'肺鳞癌'),
    ('DLBC', u'淋巴肿瘤弥漫大B细胞淋巴瘤'), ('MV',u'间皮瘤'), ('OV', u'卵巢浆液性囊腺癌'), ('PAAD', u'胰腺癌'),
    ('PCPG', u'嗜铬细胞瘤和副神经节瘤'), ('PRAD', u'前列腺癌'), ('READ', u'直肠癌'), ('SARC',u'肉瘤'), ('SKCM',u'皮肤黑色素瘤'),
    ('STAD', u'胃癌'), ('TGCT', u'睾丸生殖细胞肿瘤'), ('THYM', u'胸腺瘤'), ('THCA', u'甲状腺癌'), ('UCS', u'子宫癌肉瘤'),
    ('UCEC', u'子宫内膜癌'), ('UVM', u'葡萄膜黑色素瘤'), ('NA', 'N/A'))

    SMOKER_TYPE_CHOICES = (
        ('NS','Non-smoker'),
        ('SF15','Smoker For <= 15 Years'),
        ('SF16','Smoker For > 15 Years'),
        ('NA', 'N/A')
    )
    GENDER_TYPE_CHOICES = (('M', u'男'),('F', u'女'),('N', 'N/A'))
    PATHO_TYPE_CHOICES = (('I', u'I 期'),('II', u'II期'),('III', u'III期'),('IV', u'IV期'), ('N', 'N/A'))
    LIFE_STATUS_CHOICES = (('L', u'在世'), ('D', u'过世'), ('NA', 'N/A'))

    data_name = forms.CharField(label=u'数据名称', max_length=200)    
    smoke_status = forms.CharField(label=u'吸烟史', max_length=10, required=False, widget=forms.Select(choices=SMOKER_TYPE_CHOICES))
    gender = forms.CharField(label='性别', max_length=2, required=False, widget=forms.Select(choices=GENDER_TYPE_CHOICES))
    sick_type = forms.CharField(label=u'癌症类型', max_length=10, required=False, widget=forms.Select(choices=CANCER_TYPE_CHOICES))
    life_status = forms.CharField(label=u'生存状态', max_length=10, required=False, widget=forms.Select(choices=LIFE_STATUS_CHOICES))
    ICDO3 = forms.IntegerField(label='ICD-O-3')
    patho_status = forms.CharField(label=u'病理状态', max_length=5, required=False, widget=forms.Select(choices=PATHO_TYPE_CHOICES))
    data_des = forms.CharField(label=u'描述', max_length=200, required=False)
    #genome_file = forms.FileField(label=u'基因组序列', required=False)
    #meth_file = forms.FileField(label=u'DNA甲基化', required=False)
    #micro_file = forms.FileField(label=u'微小RNA表达量', required=False)
    #mRNA_file = forms.FileField(label=u'mRNA表达量', required=False)

class UploadFileForm(forms.Form):
    genome_file = forms.FileField(label=u'基因组序列')

class RequestForm(forms.Form):
    name = forms.CharField(label=u'姓名', max_length=100)
    email = forms.EmailField(label=u'电子邮件')    
    title = forms.CharField(label=u'职务', max_length=50,required=False)
    company = forms.CharField(label=u'公司', max_length=100,required=False)
    address = forms.CharField(label=u'地址', max_length=100,required=False)
    city = forms.CharField(label=u'城市', max_length=50,required=False)
    state = forms.CharField(label='省份', max_length=50,required=False)
    country = forms.CharField(label=u'国家', max_length=50,required=False)
    phone = forms.CharField(label=u'电话', max_length=50,required=False)
    description = forms.CharField(label=u'信息', max_length=500,widget=forms.Textarea, required=False)

class ChangePWForm(forms.Form):
    oldpassword = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'type':'password', 'placeholder':'your old Password',  'class' : 'span'}))
    newpassword1 = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'type':'password', 'placeholder':'New Password',  'class' : 'span'}))
    newpassword2 = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'type':'password', 'placeholder':'Confirm New Password',  'class' : 'span'}))
    
    def clean(self):
        if 'newpassword1' in self.cleaned_data and 'newpassword2' in self.cleaned_data:
            if self.cleaned_data['newpassword1'] != self.cleaned_data['newpassword2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data
