from django.db import models

class LinesManager(models.Manager):
    """
    custom sales model

    title = models.CharField(verbose_name="Title", max_length=500,null=True)
    item_number = models.CharField(verbose_name="Item Number", max_length=500, null=True)
    item_description = models.CharField(verbose_name="Item Description", max_length=500, null=True)
    item_type = models.CharField(verbose_name="Item Type", max_length=1000,null=True)

    item_manufacturer_id = models.CharField(verbose_name="Item Manufacturer ID", max_length=500,null=True)
    item_quantity = models.CharField(verbose_name="Item Quantity", max_length=500, null=True)

    """

    def create_sales_lines(
            self,
            title,
            item_number,
            item_description,
            item_type,
            item_manufacturer_id,
            item_quantity,
            currency,
            
    ):
        line = self.model(
            title=title,
            item_number=item_number,
            item_description=item_description,
            item_type=item_type,
            item_manufacturer_id=item_manufacturer_id,
            item_quantity=item_quantity,
            currency=currency,
        )

        line.save(using=self._db)
        return line
