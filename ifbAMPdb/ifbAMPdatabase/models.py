from django.db import models

# Create your models here.

class peptide(models.Model):
    pdb_id = models.CharField(max_length=10, primary_key=True)
    is_amp = models.BooleanField()
    hfobic_area = models.CharField(max_length=96)
    hfobic_avg = models.FloatField()
    hdl = models.IntegerField()
    beta_hdl = models.IntegerField()
    alpha_hdl = models.IntegerField()
    alpha_beta = models.IntegerField()
    alpha_beta_hdl = models.IntegerField()
    charge = models.FloatField()
    m_dipol = models.FloatField()
    charge_amt_atm = models.FloatField()
    m_dipol_amt_atm = models.FloatField()
    sequence = models.TextField()
    def __str__(self):
        return self.id

