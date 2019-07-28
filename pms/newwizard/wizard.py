'''
Created on Jan 8, 2014

@author: wzw7yn
'''
import wx

from mainpage import MainPage
from patent.pat_generalpage import GeneralPage
from patent.pat_medicalpage import MedicalPage
from patent.pat_otherpage import OtherPage
from patent.pat_historypage import HistoryPage
from appointment.app_patentpage import App_PatentPage
from appointment.app_timepage import App_TimePage
from gps.gp_generalpage import GP_GeneralPage
from gps.gp_otherpage import  GP_OtherPage
from cpd.cpd_generalpage import CPD_GeneralPage
from cpd.cpd_otherpage import  CPD_OtherPage
from access.cpd import CPDTable

from equipment.equ_generalpage import Eqp_GeneralPage
from equipment.equ_otherpage import  Eqp_OtherPage
from gps.newinfo import GPInfo

from access.gp import GPTable

from wx.wizard import Wizard





class NewWizard(Wizard):
    def __init__(self, parent):
        Wizard.__init__(self, parent, -1, "Mirror Wizard")

        #self.Bind(Wizard.EVT_WIZARD_FINISHED, self.OnWizardFinished)
        self.Ok = False

    def Create(self):
        self.gpInfo = GPInfo()
        self.wizard = NewWizard(self)

        self.mainPage = MainPage(self.wizard)

        # patent rerord
        self.prGeneralPage = GeneralPage(self.wizard)
        self.prMedicalPage = MedicalPage(self.wizard)
        self.prOtherPage = OtherPage(self.wizard)
        self.prHistoryPage = HistoryPage(self.wizard)

        self.mainPage.SetPrev(None)


        self.prGeneralPage.SetPrev(self.mainPage)
        self.prGeneralPage.SetNext(self.prMedicalPage)

        self.prMedicalPage.SetPrev(self.prMedicalPage)
        self.prMedicalPage.SetNext(self.prOtherPage)

        self.prOtherPage.SetNext(self.prHistoryPage)
        self.prOtherPage.SetPrev(self.prMedicalPage)

        self.prHistoryPage.SetNext(None)
        self.prHistoryPage.SetPrev(self.prOtherPage)

        # appointment
        self.apPatentPage = App_PatentPage(self.wizard)
        self.apTimePage = App_TimePage(self.wizard)

        self.apPatentPage.SetNext(self.apTimePage)
        self.apPatentPage.SetPrev(self.mainPage)

        self.apTimePage.SetNext(None)
        self.apTimePage.SetPrev(self.apPatentPage)

        # gps
        self.gpGeneralPage = GP_GeneralPage(self.wizard, self.gpInfo)
        self.gpOtherPage = GP_OtherPage(self.wizard, self.gpInfo)

        self.gpGeneralPage.SetNext(self.gpOtherPage)
        self.gpGeneralPage.SetPrev(self.mainPage)

        self.gpOtherPage.SetNext(None)
        self.gpOtherPage.SetPrev(self.gpGeneralPage)
        
        #cpd
        self.cpdGeneralPage = CPD_GeneralPage(self.wizard, self.gpInfo)
        self.cpdOtherPage = CPD_OtherPage(self.wizard, self.gpInfo)

        self.cpdGeneralPage.SetNext(self.cpdOtherPage)
        self.cpdGeneralPage.SetPrev(self.mainPage)

        self.cpdOtherPage.SetNext(None)
        self.cpdOtherPage.SetPrev(self.cpdGeneralPage)

        
        #equ
        self.eqpGeneralPage = Eqp_GeneralPage(self.wizard, self.gpInfo)
        self.eqpOtherPage = Eqp_OtherPage(self.wizard, self.gpInfo)

        self.eqpGeneralPage.SetNext(self.eqpOtherPage)
        self.eqpGeneralPage.SetPrev(self.mainPage)

        self.eqpOtherPage.SetNext(None)
        self.eqpOtherPage.SetPrev(self.eqpGeneralPage)

        self.mainPage.SetOptions([self.apPatentPage, self.prGeneralPage, self.gpGeneralPage, self.cpdGeneralPage, self.eqpGeneralPage])

        self.wizard.SetPageSize((600,400))
        #self.Bind(self.EVT_WIZARD_FINISHED, self.OnWizardFinished)

    def Run(self):
        if self.wizard.RunWizard(self.mainPage):
            if self.prHistoryPage.IsDone():
                print "New PR"
            if self.apTimePage.IsDone():
                print "New AP"
            if self.gpOtherPage.IsDone():
                self.NewGP()
                print self.gpInfo
                print "New GP"
            if self.cpdOtherPage.IsDone():
                self.NewCPD()
                print "Success"
        else:
            print "Canceled"

    def NewGP(self):
        gpTable = GPTable()
        gpTable.add(
                    self.gpGeneralPage.first.GetValue(),
                    self.gpGeneralPage.surname.GetValue(),
                    address=self.gpGeneralPage.address.GetValue(),
                    town=self.gpGeneralPage.town.GetValue(),
                    post_code=self.gpGeneralPage.postcode.GetValue(),
                    home_phone=self.gpGeneralPage.homephone.GetValue(),
                    work_phone=self.gpGeneralPage.workphone.GetValue(),
                    mobile=self.gpGeneralPage.mobile.GetValue(),
                    prefered_phone=self.gpGeneralPage.preferedPhone.GetValue(),
                    email=self.gpGeneralPage.email.GetValue())
        #self.gpGeneralPage.title.GetValue()
        '''
        address=None,
                                town=None,
                                post_code=None,
                                home_phone=None,
                                work_phone=None,
                                mobile=None,
                                prefered_phone=None,
                                email=None):
        self.gpInfo.first = self.gpGeneralPage.first.GetValue()
        self.gpInfo.surname = self.gpGeneralPage.surname.GetValue()
        self.gpInfo.address = self.gpGeneralPage.address.GetValue()
        self.gpInfo.town = self.gpGeneralPage.town.GetValue()
        self.gpInfo.postcode = self.gpGeneralPage.postcode.GetValue()
        self.gpInfo.homephone = self.gpGeneralPage.homephone.GetValue()
        self.gpInfo.workphone = self.gpGeneralPage.workphone.GetValue()
        self.gpInfo.mobile = self.gpGeneralPage.mobile.GetValue()
        self.gpInfo.preferedPhone = self.gpGeneralPage.preferedPhone.GetValue()
        self.gpInfo.email = self.gpGeneralPage.email.GetValue()
        self.gpInfo.other = self.gpOtherPage.other.GetValue()
        '''

    def NewCPD(self):
        cpdTable = CPDTable()
        
        cpdTable.add(
                title = self.cpdGeneralPage.title.GetValue(),
                date_started=self.cpdGeneralPage.date_started.GetValue(),
                days_taken=self.cpdGeneralPage.days_taken.GetValue(),
                activity_type=self.cpdGeneralPage.activity_type.GetValue(),
                category=self.cpdGeneralPage.category.GetValue(),
                core_cpd_module=self.cpdGeneralPage.core_cpd_module.GetValue(),
                description=self.cpdGeneralPage.description.GetValue(),
                learning_objectives=self.cpdGeneralPage.learning_objectives.GetValue(),
                reflective_comments=self.cpdOtherPage.reflective_comments.GetValue(),
                attached_files=None,
                web_links=None,
                  )

    def OnWizardFinished(self, event):
        #self.cpdGeneralPage.category
        self.Ok = True
        print "EVT_WIZARD_FINISHED"

class PatentEditDialog(wx.Dialog):
    '''
    classdocs
    '''


    def __init__(self):
        wx.Dialog.__init__(self, None, -1, "Patent Details", size=(700, 600))
        '''
        Constructor
        '''
        self.panel = PatentEditPanel(self)

        sizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        okButton = wx.Button(self, wx.ID_OK, "Ok", pos=(15, 15))
        okButton.SetDefault()
        btnSizer.Add(okButton)
        
        openFileDlgBtn = wx.Button(self, label="Show Dialog")
        btnSizer.Add(openFileDlgBtn)
        openFileDlgBtn.Bind(wx.EVT_BUTTON, self.OnOpenDlg)
        
    
        sizer.Add(btnSizer)
        self.SetSizer(sizer)
        self.SetInitialSize()
        
    def OnOpenDlg(self, event):
        wizard = NewWizard(self)
        wizard.Create()
        wizard.Run()

class PatentEditPanel(wx.Panel):
    def __init__(self, parent):
        super(PatentEditPanel, self).__init__(parent, style=wx.LB_BOTTOM)




class TestApp(wx.App):
    def OnInit(self):
        patentEditDialog = PatentEditDialog()
        patentEditDialog.ShowModal()
        return True

from access.database import Database
from utils.configreader import ConfigReader

if __name__=="__main__":
    cfg = ConfigReader()
    cfg.read("/home/wzw7yn/workspace/pms/main/config.xml")
    Database.Open(cfg.GetPath(), cfg.GetUsername(), cfg.GetPassword())
    app = TestApp(False)
    app.MainLoop()