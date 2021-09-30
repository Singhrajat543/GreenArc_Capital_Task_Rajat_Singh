from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db.models.enums import Choices

# Create your models here.

STATE_CHOICES = (
('UP','UP'),
('MP','MP'),
('Keral','Keral'),
('Goa','Goa'),
('Maharastra','Maharastra'),
('Haryana','Haryana'),
('Bengal','Bengal'),
('Tamilnadu','Tamilnadu'),
('JK','JK'),
('Tripura','Tripura'),
('Bihar','Bihar'),
('karnatka','karnatka'),
('Andman','Andman'),

)

class Customer(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    name = models.CharField(max_length=400)
    locality = models.CharField( max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

  
    def __str__(self):         
                                 
        return str(self.id)   
                          
        
          
CATOGARY_CHOICES = (
('Mobile','Mobile'),
('Laptop','Laptop'),
('Top Wear','Top Wear'),
('Bottom wear','Bottom wear'),

)

class Product(models.Model):
    title = models.CharField(max_length=200)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    discription = models.TextField()
    brand =  models.CharField(max_length=100)
    Comment= models.CharField(max_length=200,default="")
    catogary = models.CharField(choices= CATOGARY_CHOICES, max_length=200)
    product_image = models.ImageField(upload_to='productimg',default="")



    def __str__(self):
        return str(self.id)



class Cart(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    Product = models.ForeignKey( Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return str(self.id)

    @property 
    def totalCost_Of_Item(self):
        return self.quantity * self.Product.discounted_price  
                          


STATE_CHOICES= (

('Accepted','Accepted'),
('Packed','Packed'),
('On The way','On The way'),
('Deliverd','Deliverd'),
('Cancel','Cancel'),

)        

class OrderdPlace(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField( max_length=50, choices= STATE_CHOICES, default= 'Pending')
    
    def __str__(self):
        return str(self.id)

    
    @property # so here we are Creatingon for checkout.html page
    def totalCost_Of_Item(self):
        return self.quantity * self.product.discounted_price  



    






