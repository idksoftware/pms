'''
Created on Jul 11, 2013

@author: wzw7yn
'''
import wx

from patent.patentspage import PatentsCtrl
from gps.gpspage import GPCtrl
from appointment.appointmentspage import AppointmentsCtrl
from equipment.equipmentpage import EquipmentCtrl
from patent.currentpatentpage import CurrentPatentCtrl
from finance.financepage import FinanceCtrl
from treatment.treatmentpage import TreatmentsCtrl
from cpd.cpdpage import CPDCtrl

class MainPane(wx.Notebook):

    def __init__(self, parent):
        super(MainPane, self).__init__(parent, style=wx.NB_TOP)


        self.currentPatentCtrl = CurrentPatentCtrl(self)
        self.patentsCtrl = PatentsCtrl(self)
        self.appointmentsCtrl = AppointmentsCtrl(self)
        self.treatmentsCtrl = TreatmentsCtrl(self)
        self.gpCtrl = GPCtrl(self)
        self.equipmentCtrl = EquipmentCtrl(self)
        self.financeCtrl = FinanceCtrl(self)
        self.cpdCtrl = CPDCtrl(self)
        
        self.AddPage(self.currentPatentCtrl, "Patent")
        self.AddPage(self.appointmentsCtrl, "Appointments")
        self.AddPage(self.patentsCtrl, "Patents List")
        self.AddPage(self.treatmentsCtrl, "Treatments")
        self.AddPage(self.gpCtrl, "GPs")
        self.AddPage(self.equipmentCtrl, "Equipment")
        self.AddPage(self.financeCtrl, "Finance")
        self.AddPage(self.cpdCtrl, "C.P.D.")
