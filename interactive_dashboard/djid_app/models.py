from django.db import models
from django.utils import timezone

# Create your models here.




class DashboardData(models.Model):

    _id = models.AutoField(primary_key=True)
    end_year = models.CharField(max_length=255, blank=True, default="")
    intensity = models.IntegerField(default=0)
    sector = models.CharField(max_length=255, default="")
    topic = models.CharField(max_length=255, default="")
    insight = models.CharField(max_length=255, default="")
    url = models.URLField(default='')
    region = models.CharField(max_length=255, default="")
    start_year = models.CharField(max_length=255, default="")
    impact = models.CharField(max_length=255, default="")
    
    added = models.CharField(max_length=255, default="")
    published = models.CharField(max_length=255, default="")
    # added = models.DateTimeField(default=timezone.now)
    # published = models.DateTimeField(default=timezone.now)
    
    country = models.CharField(max_length=255, default="")
    relevance = models.IntegerField(default=0)
    pestle = models.CharField(max_length=255, default="")
    source = models.CharField(max_length=255, default="")
    title = models.CharField(max_length=255, default="")
    likelihood = models.IntegerField(default=0)

    def __str__(self):
        return f"{self._id} | {self.source} | {self.title}"



# class Product(models.Model):
#     Product_id = models.AutoField(primary_key=True)
#     product_name = models.CharField(max_length=50)
#     category = models.CharField(max_length=50, default="")
#     slug = models.CharField(max_length=100, default="")
#     price = models.IntegerField(default=0)
#     desc = models.CharField(max_length=300)
#     image = models.ImageField(upload_to="tze/images", default="")
#     testimoniallink = models.CharField(max_length=300, default="")
#     ytlink = models.CharField(max_length=300, default="")
#     benifits = models.CharField(max_length=300, default="")
#     how_to_use = models.CharField(max_length=400, default="")
#     doc_link = models.CharField(max_length=300, default="")
#     net_Qty = models.CharField(max_length=100, default="")
#     pack_of = models.CharField(max_length=50, default="")
#     # pub_date = models.DateField()
#     # subcategory = models.CharField(max_length=30, default="")

#     def __str__(self):
#         return self.product_name
    
# # mem: member
# class Contact(models.Model):
#     mem_id = models.AutoField(primary_key=True)

#     mem_name = models.CharField(max_length=60, default="")
#     mem_image = models.ImageField(upload_to="tze/contactImages", default="")
#     mem_desc = models.CharField(max_length=300, default="")
#     mem_email = models.CharField(max_length=100, default="")
#     mem_phone = models.IntegerField(default=0)
#     mem_fb_link = models.CharField(max_length=100, default="")
#     mem_IG_link = models.CharField(max_length=100, default="")
#     mem_status = models.CharField(max_length=100, default="")
#     mem_tag = models.CharField(max_length=20, default="")

#     def __str__(self):
#         return self.mem_name
    
# class Contact(models.Model):
#     msg_id = models.AutoField(primary_key=True)

#     name = models.CharField(max_length=50, default="")
#     email = models.CharField(max_length=70, default="")
#     phone = models.IntegerField(default=0)
#     msg = models.CharField(max_length=500, default="")


#     def __str__(self):
#         return self.name