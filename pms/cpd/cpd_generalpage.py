'''
Created on Jan 8, 2014

@author: wzw7yn
'''
import wx

from wx.adv import PyWizardPage
from wx.adv import Wizard
from wx.adv import DatePickerCtrl
from utils.editoptionsdlg import OptionsDialog
from utils.editoptionsdlg import OptionReader

'''
CPD Types of Activity
Leaning by doing
Case studies
Reflective practice
Clinical audit
Coaching from others
Discussions with colleagues
Peer review
Involvement in wider work of employer
Work shadowing
Secondments
Job rotation
Journal club
In-service Training
Supervising staff or students
Visiting other departments and reporting back
Expanding your role
Analysing significant events
Filling in self-assessment questionnaires
Project work or project managements
'''

class CPD_GeneralPage(PyWizardPage):

    def __init__(self, parent, gpInfo):
        PyWizardPage.__init__(self, parent)
        self.gpInfo = gpInfo
        self.prev = self
        self.next = self
        self.__DoLayout()
        self.SetInitialSize()
        self.Bind(Wizard.EVT_WIZARD_PAGE_CHANGED, self.OnPageChanged)
        #self.gpInfo = GPInfo

    def SetPrev(self, prev):
        self.prev = prev
        return self.prev

    def SetNext(self, nxt):
        self.next = nxt
        return self.next
    def GetNext(self):
        return self.next
    def GetPrev(self):
        return self.prev


    def __DoLayout(self):

        title_lbl= wx.StaticText(self, label="Continuous Professional Development - Details")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        '''
        text = ""
        titleLbl = wx.StaticText(self, -1, "Title:")
        self.title = wx.TextCtrl(self, -1, text, size=(200, 23))

        dateLbl = wx.StaticText(self, -1, "Date:")
        self.date_started = wx.DatePickerCtrl(self, -1, wx.DateTime.Today())

        noOfDaysLbl = wx.StaticText(self, -1, "Number of days taken:")
        self.noOfDays = wx.SpinCtrl(self, -1, text, size=(40,25), min=0, max=23, initial=9)

        atList = [ 'GEC Equipment', 'H&I Services' ]
        activityTypeLbl = wx.StaticText(self, -1, "Activity Type:")
        self.activityType = wx.ComboBox(self, -1, "", (10, 30), (200, 23), atList, wx.CB_DROPDOWN)
        atAddButton = wx.Button(self, -1, "Add", size=(50, 23))

        catList = [ 'GEC Equipment', 'H&I Services' ]
        categoryLbl = wx.StaticText(self, -1, "Category:")
        self.category = wx.ComboBox(self, -1, "", (10, 30), (200, 23), catList, wx.CB_DROPDOWN)
        catAddButton = wx.Button(self, -1, "Add", size=(50, 23))

        catList = [ 'GEC Equipment', 'H&I Services' ]
        coreCPDModuleLbl = wx.StaticText(self, -1, "Core CPD Module:")
        self.coreCPDModule = wx.ComboBox(self, -1, "", (10, 30), (200, 23), catList, wx.CB_DROPDOWN)
        cmAddButton = wx.Button(self, -1, "Add", size=(50, 23))

        text = ""
        descriptionLbl = wx.StaticText(self, -1, "Description:")
        self.description = wx.TextCtrl(self, -1, text, size=(300,70), style=wx.TE_MULTILINE)

        learningObjectivesLbl = wx.StaticText(self, -1, "Learning Objectives:")
        self.learningObjectives = wx.TextCtrl(self, -1, text, size=(300,50), style=wx.TE_MULTILINE)
        '''
        text = ""

        titleLbl = wx.StaticText(self, -1, "Title:")
        self.title = wx.TextCtrl(self, -1, text, size=(200, 23))

        dateLbl = wx.StaticText(self, -1, "Date:")
        self.date_started = DatePickerCtrl(self, -1, wx.DateTime.Today())

        noOfDaysLbl = wx.StaticText(self, -1, "Number of days taken:")
        self.days_taken = wx.SpinCtrl(self, -1, text, size=(40,25), min=0, max=23, initial=9)

        atReader = OptionReader("/home/wzw7yn/workspace/pms/main/cpdatopts.xml");
        self.atList = atReader.read()
        activityTypeLbl = wx.StaticText(self, -1, "Activity Type:")
        self.activity_type = wx.ComboBox(self, -1, text, (10, 30), (200, 23), self.atList, wx.CB_DROPDOWN)
        atAddButton = wx.Button(self, -1, "Add", size=(50, 23))


        catReader = OptionReader("/home/wzw7yn/workspace/pms/main/cpdcatopts.xml");
        catList = catReader.read()
        categoryLbl = wx.StaticText(self, -1, "Category:")
        self.category = wx.ComboBox(self, -1, text, (10, 30), (200, 23), catList, wx.CB_DROPDOWN)
        catAddButton = wx.Button(self, -1, "Add", size=(50, 23))


        cmReader = OptionReader("/home/wzw7yn/workspace/pms/main/cpdcmopts.xml");
        catList = cmReader.read()
        coreCPDModuleLbl = wx.StaticText(self, -1, "Core CPD Module:")
        self.core_cpd_module = wx.ComboBox(self, -1, text, (10, 30), (200, 23), catList, wx.CB_DROPDOWN)
        cmAddButton = wx.Button(self, -1, "Add", size=(50, 23))

        atAddButton.Bind(wx.EVT_BUTTON, self.OnAtButton)
        catAddButton.Bind(wx.EVT_BUTTON, self.OnCatButton)
        cmAddButton.Bind(wx.EVT_BUTTON, self.OnCmButton)


        descriptionLbl = wx.StaticText(self, -1, "Description:")
        self.description = wx.TextCtrl(self, -1, text, size=(300,100), style=wx.TE_MULTILINE)


        learningObjectivesLbl = wx.StaticText(self, -1, "Learning Objectives:")
        self.learning_objectives = wx.TextCtrl(self, -1, text, size=(300,80), style=wx.TE_MULTILINE)

        grpSizer = wx.GridBagSizer(vgap=8, hgap=8)

        grpSizer.Add(titleLbl, (1, 1))
        grpSizer.Add(self.title, (1, 2))

        grpSizer.Add(dateLbl, (2, 1))
        grpSizer.Add(self.date_started, (2, 2))

        grpSizer.Add(noOfDaysLbl, (3, 1))
        grpSizer.Add(self.days_taken, (3, 2))

        grpSizer.Add(activityTypeLbl, (4, 1))
        grpSizer.Add(self.activity_type, (4, 2))
        grpSizer.Add(atAddButton, (4, 3))

        grpSizer.Add(categoryLbl, (5, 1))
        grpSizer.Add(self.category, (5, 2))
        grpSizer.Add(catAddButton, (5, 3))

        grpSizer.Add(coreCPDModuleLbl, (6, 1))
        grpSizer.Add(self.core_cpd_module, (6, 2))
        grpSizer.Add(cmAddButton, (6, 3))

        grpSizer.Add(descriptionLbl, (7, 1))
        grpSizer.Add(self.description, (7, 2)) #wx.FIXED_MINSIZE


        grpSizer.Add(learningObjectivesLbl, (8, 1))
        grpSizer.Add(self.learning_objectives, (8, 2))


        mainSizer.Add(grpSizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)

    def OnAtButton(self, events):
        dialog = OptionsDialog("Add New Activity Type", "/home/wzw7yn/workspace/pms/main/cpdatopts.xml")
        if dialog.ShowModal() == wx.ID_OK:
            dialog.Update()
            opr = OptionReader("/home/wzw7yn/workspace/pms/main/cpdatopts.xml");
            opr.updateComboBox(self.activity_type)

    def OnCatButton(self, events):
        dialog = OptionsDialog("Add New Category", "/home/wzw7yn/workspace/pms/main/cpdcatopts.xml")
        if dialog.ShowModal() == wx.ID_OK:
            dialog.Update()
            opr = OptionReader("/home/wzw7yn/workspace/pms/main/cpdcatopts.xml");
            opr.updateComboBox(self.category)


    def OnCmButton(self, events):
        dialog = OptionsDialog("Add New Core Module Option", "/home/wzw7yn/workspace/pms/main/cpdcmopts.xml")
        if dialog.ShowModal() == wx.ID_OK:
            dialog.Update()
            opr = OptionReader("/home/wzw7yn/workspace/pms/main/cpdcmopts.xml");
            opr.updateComboBox(self.core_cpd_module)


    def OnNew(self, event):
        pass

    def OnPageChanged(self, event):
        '''
        self.gpInfo.title = self.title.GetValue()
        self.gpInfo.first = self.first.GetValue()
        self.gpInfo.surname = self.surname.GetValue()
        self.gpInfo.address = self.address.GetValue()
        self.gpInfo.town = self.town.GetValue()
        self.gpInfo.postcode = self.postcode.GetValue()
        self.gpInfo.homephone = self.homephone.GetValue()
        self.gpInfo.workphone = self.workphone.GetValue()
        self.gpInfo.mobile = self.mobile.GetValue()
        self.gpInfo.preferedPhone = self.preferedPhone.GetValue()
        self.gpInfo.email = self.email.GetValue()
        '''
        pass
    def GetPageInfo(self):
        '''
        return self.gpInfo
        '''
        pass