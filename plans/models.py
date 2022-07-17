from django.db import models
from enum import Enum
from multiselectfield import MultiSelectField
from django.db.models.signals import post_save, post_init
from django.dispatch import receiver
from datetime import datetime, timedelta
futuredate = datetime.now() + timedelta(days=10)


# Create your models here.

class MyTortoiseUser(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField(max_length=30)

  def __str__(self):
    return self.first_name + ' ' + self.last_name 

class  Plan(models.Model):
  AMOUNTCHOICE = {
    (0, 'Debit cards'),
    (1, 'Credit cards'),
    (2, 'Mobile payments'),
    (3, 'Electronic bank transfers'),
  }
  TENTURECHOICE = (
    (0, 'weekly'),
    (1, 'fortnightly'),
    (2, 'quarterly'),
)
  BENIFITCHOICE = (
    (0, 'cashback'),
    (1, 'extraVoucher'),
)
  planName = models.CharField('Plan Name', max_length=200)
  amountOptions = MultiSelectField(choices=AMOUNTCHOICE, max_choices=3, max_length=3)
  tenureOptions = MultiSelectField(choices=TENTURECHOICE, max_choices=3, max_length=3)
  benefitPercentage = models.IntegerField()
  benefitType = MultiSelectField(choices=BENIFITCHOICE, max_choices=3, max_length=3)

  def __str__(self):
    return self.planName 

class Promotion(models.Model):
  promotionName =  models.CharField('Promotion Name', max_length=200)
  planName = models.ForeignKey(Plan, on_delete=models.CASCADE)
  benefitPercentage = models.IntegerField()
  userCount = models.IntegerField(default=10)
  duration = models.IntegerField(default=20)


  def __str__(self):
    return self.promotionName

class CustomerGoal(models.Model):
  user = models.ManyToManyField(MyTortoiseUser, blank=True)
  plans = models.ManyToManyField(Plan, blank=True)
  benefitPercentage = models.IntegerField(default=2)

  #post_save callback on CustomerGoal to update benefitPercentage,

  def post_save(sender, instance, created, **kwargs):
        if created:
            plan_promotions = instance.plans.promotion
            lowestbenefitPercentage = 999999

            for promotion in plan_promotions:
              if promotion.user_count<500 and promotion.duration < 30:
                lowestbenefitPercentage = min(promotion.benefitPercentage)

            benefitPercentage = lowestbenefitPercentage

  def __str__(self):
    return str(self.user)