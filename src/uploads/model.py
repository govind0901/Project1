class User(AbstractUser):#transactions
	loct_of_interest = models.CharField(blank=True,null=True,max_length=100)#$$input$$text$$Location of interest
	reward_points = models.IntegerField(blank=True,null=True)#$$input$$text$$reard points
	email = models.CharField(max_length=100,blank=True,null=True)#$$input$$email$$email address
	name = models.CharField(max_length=100,blank=True,null=True)#$$input$$text$$username
class UrlLink(models.Model):#urllink
	url = models.CharField(max_length=500,blank=True, null=True)#$$input$$text$$Enter URL
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True,related_name="url_links")#$$input$$text$$USERNAME

class PhoneNumber(models.Model):#phonenumber
	phone_number = models.CharField(max_length=500,blank=True, null=True) #$$input$$number$$10 digit phone no
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True,related_name="mobile_numbers")#$$select.EntityA.A_propertyName1$$number$$property one of EntityA

class Category(models.Model):#category
	name = models.CharField(max_length=100, default="")#$$input$$text$$Category name

class Keyword(models.Model):#keyword
	name = models.CharField(max_length=100, unique=True)#$$input$$text$$keyword name
	category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True)#$$select.category.name$$text$$category
	strength = models.FloatField(max_length=100, default=0)#$$input$$number$$strength

class News(models.Model):#news
	title = models.CharField(max_length=100)#$$input$$text$$news title
	slug = models.SlugField(max_length=100, blank=True, null=True)#$$input$$text$$new slug
	image = models.FileField(upload_to='images/', null=True, verbose_name="")#$$input$$file$$news image
	body = models.TextField(max_length=100, blank=True, null=True)#$$input$$text$$image body
	author = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)#$$select.User.username$$author name
	keywords = models.ManyToManyField(Keyword, blank=True)#$$input$$text$$keywords
	title = models.CharField(max_length=100, blank=True, null=True)#$$input$$text$$news title
	by = models.CharField(max_length=100, blank=True, null=True)#$$input$$text$$News by
		
class Balance(models.Model):#transactions
	timestamp = models.DateTimeField(max_length=100, unique=True)#$$input$$datetime$$timestamp
	username = models.CharField(max_length=100, blank=True, null=True)#$$input$$text$$username 
