from django.db import models

from users.models import User


class Item(models.Model):
    """
    Model Ref.
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """

    # sales stage/dropdown
    sales_stage_choice = (
        (1, 'Lead Received'),
        (2, 'Preparation for Initial Meeting'),
        (3, 'Qualification/Needs Analysis'),
        (4, 'Proposal/​Price Quote'),
        (5, 'Implementation​  (Closed Won)​'),
        (6, 'Closed Lost'),
    )

    sales_stage = models.IntegerField(
        verbose_name='Sales Stage',
        choices=sales_stage_choice,
        blank=True,
        null=True,
    )
    
    # contact name/text
    contact_name = models.CharField(
        verbose_name='Contact Name',
        max_length=20,
        blank=True,
        null=True,
    )

    # email/text
    email = models.CharField(
        verbose_name='E-mail',
        max_length=20,
        blank=True,
        null=True,
    )

    # company name/text
    company_name = models.CharField(
        verbose_name='Company Name',
        max_length=20,
        blank=True,
        null=True,
    )

    # lead from/dropdown
    lead_from_choice = (
        (1, 'Cold call/e-mail'),
        (2, 'Web to lead'),
        (3, 'Referral')
    )

    lead_from = models.IntegerField(
        verbose_name='Lead From',
        choices=lead_from_choice,
        blank=True,
        null=True,
    )

    # lead received date/date
    lead_received_date = models.DateField(
        verbose_name='Lead Received Date',
        blank=True,
        null=True,
    )

    # initial meeting date/date
    initial_meeting_date = models.DateField(
        verbose_name='Initial Meeting Date',
        blank=True,
        null=True,
    )

    # estimated closed date/date
    estimated_closed_date = models.DateField(
        verbose_name='Estimated Closed Date',
        blank=True,
        null=True,
    )
    
    # sales rep/User tied
    sales_rep = models.ForeignKey(
        User,
        verbose_name='Sales Rep.',
        blank=True,
        null=True,
        related_name='sales_rep',
        on_delete=models.SET_NULL,
    )

    # deal size/float number
    deal_size = models.FloatField(
        verbose_name='Deal Size [USD]',
        blank=True,
        null=True,
    )
    
    # prob. of deal/int number
    probability_of_deal = models.IntegerField(
        verbose_name='Probability of Deal [%]',
        blank=True,
        null=True,
    )

    # forecast/float number
    forecast = models.FloatField(
        verbose_name='Forecast [USD]',
        blank=True,
        null=True,
    )

    # creator
    created_by = models.ForeignKey(
        User,
        verbose_name='Creator',
        blank=True,
        null=True,
        related_name='CreatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # created datetime
    created_at = models.DateTimeField(
        verbose_name='Created datetime',
        blank=True,
        null=True,
        editable=False,
    )

    # updater
    updated_by = models.ForeignKey(
        User,
        verbose_name='Updater',
        blank=True,
        null=True,
        related_name='UpdatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # updated datetime
    updated_at = models.DateTimeField(
        verbose_name='Updated datetime',
        blank=True,
        null=True,
        editable=False,
    )

    def __str__(self):
        """
        display on the settings view and so on
        """
        return self.contact_name

    class Meta:
        """
        display on the settings view
        """
        verbose_name = 'Sales Pipeline'
        verbose_name_plural = 'Sales Pipeline'
