from django.db import models

# Create your models here.

class peptide(models.Model):
	pdb_id = models.CharField(max_length=10, primary_key=True)
	is_amp = models.BooleanField()
	hfobic_area = models.CharField(max_length=96)
	hfobic_avg = models.FloatField()
	hairpin = models.BooleanField()
	beta_sheet = models.BooleanField()
	alpha_helix = models.BooleanField()
	alpha_helix_beta_sheet = models.BooleanField()
	alpha_helix_beta_sheet_hairpin = models.BooleanField()
	charge = models.FloatField()
	m_dipol = models.FloatField()
	charge_amt_atm = models.FloatField()
	m_dipol_amt_atm = models.FloatField()
	sequence = models.TextField(blank = True, null= True)
	organism = models.CharField(max_length=100, blank = True, null= True)

	def __str__(self):
		return self.pdb_id
