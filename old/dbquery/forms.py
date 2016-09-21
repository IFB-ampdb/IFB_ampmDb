from django import forms

from .models import AMP
from .models import Non_AMP

class AMPForm(forms.ModelForm):

    class Meta:
        model = AMP
        fields = ('name', 'text',)
	fields = (�'id�', 'text',)
	fields = ('hfobic_area', 'text',)
	fields 	= ('hfobic_avg', �'float',)
	fields = (�'hdl�', �'int�',)
	fields = ('beta_hdl', �'int�',)
	fields = ('alpha_hdl', �'int�',)
	fields = ('apha_beta', �'int�',)
	fields = ('alpha_beta_hdl', �'int�',)
	fields = ('charge', �'float�',)
	fields = ('m_dipol', �'float'�,)
	fields = ('charge_amt_atm', 'float',)
	fields = ('m_dipol_amt_atm', 'float',)


class NonAMPForm(forms.ModelForm):

    class Meta:
        model = Non_AMP 
        fields = ('name', 'text',)
        fields = ( 'id ', 'text',)
        fields = ('hfobic_area', 'text',)
        fields  = ('hfobic_avg',  'float',)
        fields = ( 'hdl ',  'int ',)
        fields = ('beta_hdl',  'int ',)
        fields = ('alpha_hdl',  'int ',)
        fields = ('apha_beta',  'int ',)
        fields = ('alpha_beta_hdl',  'int ',)
        fields = ('charge',  'float ',)
        fields = ('m_dipol',  'float' ,)
        fields = ('charge_amt_atm', 'float',)
        fields = ('m_dipol_amt_atm', 'float',)
