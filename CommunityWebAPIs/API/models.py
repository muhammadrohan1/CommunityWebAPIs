from django.db import models

class Community(models.Model):
    #CommunityNumber INTEGER, " + "Name TEXT," + "Address TEXT," + "Logo TEXT," + "Regin TEXT," + " PRIMARY KEY(CommunityNumber))
    communityNumber = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='communityNumber')
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    logo = models.CharField(max_length=100)
    regin = models.CharField(max_length=100)
    def __str__(self):
        return self.name


# ResidentInfo(Email TEXT, " + " Password TEXT, " + " CommunityNumber INTEGER, " + " Name TEXT, " + " Address TEXT, " + " Phone INTEGER, " + " Status INTEGER, " + " PRIMARY KEY(Email))"
class ResidentInfo(models.Model):
    email = models.CharField(max_length=40,primary_key=True)
    password = models.CharField(max_length=50)
    comunityNumber= models.ForeignKey(Community,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=40)
    phone = models.IntegerField()
    accountStatus= models.BooleanField(default=False)
    def __str__(self):
        return self.name



#"CREATE TABLE BusinessInfo (Email TEXT, " + "Password TEXT," + "CommunityNumber INTEGER," + "Name TEXT," + "Address TEXT," + "Legal_Number TEXT,"+ "Status INTEGER," + "Type TEXT," + "Premium INTEGER," + " PRIMARY KEY(Email))";
class BusinessInfo(models.Model):
    businessEmail = models.CharField(max_length=40,primary_key=True)
    password = models.CharField(max_length=50)
    comunityNumber= models.ForeignKey(Community,on_delete=models.CASCADE)
    businessName = models.CharField(max_length=30)
    businessAddress = models.CharField(max_length=30)
    legalNumber = models.CharField(max_length=30, blank=True ,default='')
    phone = models.IntegerField()
    businessType = models.CharField(max_length=30)
    accountStatus = models.BooleanField(default=False)
    premium = models.BooleanField(default=False)
    def __str__(self):
        return self.businessName


class Categories(models.Model):
    category= models.CharField(max_length=50)
    def __str__(self):
        return self.category


#"CREATE TABLE Categories (CommunityNumber INTEGER, " + "Category TEXT," + " PRIMARY KEY(CommunityNumber,Category))";
class ComunityCategories(models.Model):
    comunity = models.ForeignKey(Community, on_delete=models.CASCADE)
    category = models.ManyToManyField(Categories)
    def __str__(self):
        return str(self.id)


class Bussiness_Categories(models.Model):
    business = models.ForeignKey(BusinessInfo, on_delete=models.CASCADE)
    category = models.ManyToManyField(Categories)
    def __str__(self):
        return str(self.id)


class Resident_Categories(models.Model):
    resident = models.ForeignKey(ResidentInfo, on_delete=models.CASCADE)
    category = models.ManyToManyField(Categories)
    def __str__(self):
        return str(self.id)





   #"CREATE TABLE Bussiness_Categories (Email TEXT, " + "Category TEXT," + " PRIMARY KEY(Email,Category))";
   #"CREATE TABLE Resident_Categories (Email TEXT, " + "Category TEXT," + " PRIMARY KEY(Email,Category))";





