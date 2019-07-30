'''
Created on Jan 23, 2014

@author: wzw7yn
'''
import wx

from appointmentbookctrl import AppointmentBookCtrl
from appointmentdetailsctrl import AppointmentDetailsCtrl
 



class ClinicAddDialog(wx.Dialog):
    '''
    classdocs
    '''


    def __init__(self):
        wx.Dialog.__init__(self, None, -1, "Clinic Details", size=(1000, 600))
        '''
        Constructor
        '''
        self.panel = ClinicAddPanel(self)

        sizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        okButton = wx.Button(self, wx.ID_OK, "Ok", pos=(15, 15))
        okButton.SetDefault()
        btnSizer.Add(okButton)
        cancelButton = wx.Button(self, wx.ID_CANCEL, "Cancel", pos=(15, 15))
        btnSizer.Add(cancelButton)
        sizer.Add(btnSizer)
        self.SetSizer(sizer)
        self.SetInitialSize()

   

class ClinicAddPanel(wx.Panel):
    def __init__(self, parent):
        super(ClinicAddPanel, self).__init__(parent, style=wx.LB_BOTTOM, size=(1000, 600))
        
        # Layout
        self.__DoLayout()
        self.SetInitialSize()


    def __DoLayout(self):
       
        title_lbl= wx.StaticText(self, label="Contact Details")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)
        
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)
        
        text = ""
        serviceProviderLbl = wx.StaticText(self, -1, "Clinic:")
        self.serviceProvider = wx.TextCtrl(self, -1, text, size=(170, 23))
        
        contactNameLbl = wx.StaticText(self, -1, "Contact Name:")
        self.contactName = wx.TextCtrl(self, -1, text, size=(170, 23))

        addressLbl = wx.StaticText(self, -1, "Address:")
        self.address = wx.TextCtrl(self, -1, text, style=wx.TE_MULTILINE, size=(170,50))

        townLbl = wx.StaticText(self, -1, "Town/City:")
        self.town = wx.TextCtrl(self, -1, text, size=(75, 23))

        postcodeLbl = wx.StaticText(self, -1, "Postcode:")
        self.postcode = wx.TextCtrl(self, -1, text)

        workphoneLbl = wx.StaticText(self, -1, "Work Phone:")
        self.workphone = wx.TextCtrl(self, -1, text, size=(100, 23))

        mobileLbl = wx.StaticText(self, -1, "Mobile:")
        self.mobile = wx.TextCtrl(self, -1, text, size=(100, 23))


        emailLbl = wx.StaticText(self, -1, "Email:")
        self.email = wx.TextCtrl(self, -1, text, size=(170, 23))

        grpSizer = wx.GridBagSizer(vgap=8, hgap=8)

       

        grpSizer.Add(serviceProviderLbl, (1, 1))
        grpSizer.Add(self.serviceProvider, (1, 2))
        
        grpSizer.Add(contactNameLbl, (2, 1))
        grpSizer.Add(self.contactName, (2, 2))
        
        grpSizer.Add(addressLbl, (3, 1))
        grpSizer.Add(self.address, (3, 2))

        grpSizer.Add(townLbl, (4, 1))
        grpSizer.Add(self.town, (4, 2))

        grpSizer.Add(postcodeLbl, (4, 3))
        grpSizer.Add(self.postcode, (4, 4))
        
        
        grpSizer.Add(workphoneLbl, (5, 1))
        grpSizer.Add(self.workphone, (5, 2))

        grpSizer.Add(mobileLbl, (5, 3))
        grpSizer.Add(self.mobile, (5, 4))

        grpSizer.Add(emailLbl, (6, 1))
        grpSizer.Add(self.email, (6, 2))
        
        btnszr = wx.StdDialogButtonSizer()
        editbtn = wx.Button(self, wx.ID_EDIT)
        #openbtn = wx.Button(self, wx.ID_OPEN)
        
        
        editbtn.SetDefault()
        btnszr.Add(editbtn)
        #btnszr.Add(openbtn)
       
        btnszr.Realize()

        listSizer = wx.GridBagSizer(vgap=2, hgap=2)
       
        mainSizer.Add(grpSizer, 0, wx.EXPAND | wx.ALL, 10)
        
        mainSizer.Add(listSizer, 0, wx.EXPAND | wx.ALL, 10)
        mainSizer.Add(btnszr, 0, wx.ALIGN_RIGHT, 12)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)
        self.SetSizer(mainSizer)
        
        self.Bind(wx.EVT_BUTTON, self.OnEdit, editbtn)
        #self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        #self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)
    
    def OnEdit(self, event):
        page = self.appointmentDetailsCtrl.GetSelection()
        if page == 0:
            print "Appointments page"
        elif page == 1:
            print "Patents page"
            #from main.patenteditdlg import PatentEditDialog
            #patentEditDialog = PatentEditDialog()
            #patentEditDialog.ShowModal()
        elif page == 2:
            print "Payment page"
        elif page == 3: 
            print "History page"
        print "Edit button"
     
        
class TestApp(wx.App):
    def OnInit(self):
        clinicAddDialog = ClinicAddDialog()
        
        print "Opening ClinicAddDialog"
        clinicAddDialog.ShowModal()
        print "Closing ClinicAddDialog"
        return True

if __name__=="__main__":

    app = TestApp(False)
    app.MainLoop()