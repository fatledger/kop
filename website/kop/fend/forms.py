# coding=utf-8

from django import forms

# Create your forms here.
class UserForm(forms.Form):
    user_name = forms.CharField(label='用户名', max_length=100)
    email = forms.EmailField(label='电子邮件')
    password1 = forms.CharField(label='密码', max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(label='密码确认', max_length=100, widget=forms.PasswordInput)    
    first_name = forms.CharField(label='名', max_length=100, required=False)
    last_name = forms.CharField(label='姓', max_length=100, required=False)
    phone = forms.CharField(label='电话', max_length=100,required=False)
    title = forms.CharField(label='职务', max_length=100,required=False)
    company = forms.CharField(label='公司', max_length=100,required=False)
    address = forms.CharField(label='地址', max_length=100,required=False)
    city = forms.CharField(label='城市', max_length=100,required=False)
    state = forms.CharField(label='省份', max_length=100,required=False)
    country = forms.CharField(label='国家', max_length=100,required=False)

class UserProfileForm(forms.Form):    
    phone = forms.CharField(label='电话', max_length=100,required=False)
    title = forms.CharField(label='职务', max_length=100,required=False)
    company = forms.CharField(label='公司', max_length=100,required=False)
    address = forms.CharField(label='地址', max_length=100,required=False)
    city = forms.CharField(label='城市', max_length=100,required=False)
    state = forms.CharField(label='省份', max_length=100,required=False)
    country = forms.CharField(label='国家', max_length=100,required=False)

class DataForm(forms.Form):
    CANCER_TYPE_CHOICES = (('LAML','急性髓系白血病'),('ACC','肾上腺皮质癌'),
    ('BLCA','膀胱尿路上皮癌'),('LGG','脑低级神经胶质瘤'),('BRCA','乳腺浸润性癌'),('CESC','宫颈癌'),
    ('CHOL','胆管癌'),('COAD','结肠癌'),('ESCA','食管癌'),('GBM','胶质母细胞瘤'),('HNSC','头颈部鳞状细胞癌'),
    ('KICH','肾嫌色'),('KIRC','肾透明细胞癌'),('KIRP','肾乳头细胞癌'),('LIHC','肝癌'),('LUAD','肺腺癌'), ('LUSC','肺鳞癌'),
    ('DLBC', '淋巴肿瘤弥漫大B细胞淋巴瘤'), ('MV','间皮瘤'), ('OV', '卵巢浆液性囊腺癌'), ('PAAD', '胰腺癌'),
    ('PCPG', '嗜铬细胞瘤和副神经节瘤'), ('PRAD', '前列腺癌'), ('READ', '直肠癌'), ('SARC','肉瘤'), ('SKCM','皮肤黑色素瘤'),
    ('STAD', '胃癌'), ('TGCT', '睾丸生殖细胞肿瘤'), ('THYM', '胸腺瘤'), ('THCA', '甲状腺癌'), ('UCS', '子宫癌肉瘤'),
    ('UCEC', '子宫内膜癌'), ('UVM', '葡萄膜黑色素瘤'), ('NA', 'N/A'))

    SMOKER_TYPE_CHOICES = (
        ('NS','Non-smoker'),
        ('SF15','Smoker For <= 15 Years'),
        ('SF16','Smoker For > 15 Years'),
        ('NA', 'N/A')
    )
    GENDER_TYPE_CHOICES = (('M', '男'),('F', '女'),('N', 'N/A'))
    PATHO_TYPE_CHOICES = (('I', 'I 期'),('II', 'II期'),('III', 'III期'),('IV', 'IV期'), ('N', 'N/A'))
    LIFE_STATUS_CHOICES = (('L', '在世'), ('D', '过世'), ('NA', 'N/A'))

    data_name = forms.CharField(label='数据名称', max_length=200)    
    smoke_status = forms.CharField(label='吸烟史', max_length=10, required=False, widget=forms.Select(choices=SMOKER_TYPE_CHOICES))
    gender = forms.CharField(label='性别', max_length=2, required=False, widget=forms.Select(choices=GENDER_TYPE_CHOICES))
    sick_type = forms.CharField(label='癌症类型', max_length=10, required=False, widget=forms.Select(choices=CANCER_TYPE_CHOICES))
    life_status = forms.CharField(label='生存状态', max_length=10, required=False, widget=forms.Select(choices=LIFE_STATUS_CHOICES))
    ICDO3 = forms.IntegerField(label='ICD-O-3')
    patho_status = forms.CharField(label='病理状态', max_length=5, required=False, widget=forms.Select(choices=PATHO_TYPE_CHOICES))
    data_des = forms.CharField(label='描述', max_length=200, required=False)
    #genome_file = forms.FileField(label='基因组序列', required=False)
    #meth_file = forms.FileField(label='DNA甲基化', required=False)
    #micro_file = forms.FileField(label='微小RNA表达量', required=False)
    #mRNA_file = forms.FileField(label='mRNA表达量', required=False)

class UploadFileForm(forms.Form):
    genome_file = forms.FileField(label='基因组序列')

class RequestForm(forms.Form):
    name = forms.CharField(label='姓名', max_length=100)
    email = forms.EmailField(label='电子邮件')    
    title = forms.CharField(label='职务', max_length=50,required=False)
    company = forms.CharField(label='公司', max_length=100,required=False)
    address = forms.CharField(label='地址', max_length=100,required=False)
    city = forms.CharField(label='城市', max_length=50,required=False)
    state = forms.CharField(label='省份', max_length=50,required=False)
    country = forms.CharField(label='国家', max_length=50,required=False)
    phone = forms.CharField(label='电话', max_length=50,required=False)
    description = forms.CharField(label='信息', max_length=500,widget=forms.Textarea, required=False)

class ChangePWForm(forms.Form):
    oldpassword = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'type':'password', 'placeholder':'your old Password',  'class' : 'span'}))
    newpassword1 = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'type':'password', 'placeholder':'New Password',  'class' : 'span'}))
    newpassword2 = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'type':'password', 'placeholder':'Confirm New Password',  'class' : 'span'}))
    
    def clean(self):
        if 'newpassword1' in self.cleaned_data and 'newpassword2' in self.cleaned_data:
            if self.cleaned_data['newpassword1'] != self.cleaned_data['newpassword2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data
