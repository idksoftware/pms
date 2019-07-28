'''
Created on Jan 27, 2014

@author: wzw7yn
'''
import wx
import wx.lib.scrolledpanel as scrolledpanel

class PaymentEditDialog(wx.Dialog):
    '''
    classdocs
    '''


    def __init__(self):
        wx.Dialog.__init__(self, None, -1, "Payment Details", size=(700, 600))
        '''
        Constructor
        '''
        self.panel = PaymentEditPanel(self)

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

class PaymentEditPanel(wx.Notebook):
    def __init__(self, parent):
        super(PaymentEditPanel, self).__init__(parent, style=wx.LB_BOTTOM)

        self.pgCtrl = PaymentCtrl(self)
        self.AddPage(self.pgCtrl, "Payment")
        self.historyCtrl = HistoryCtrl(self)
        self.AddPage(self.historyCtrl, "History")
        self.billingCtrl = BillingAddressCtrl(self)
        self.AddPage(self.billingCtrl, "Billing")
        
class PaymentCtrl(scrolledpanel.ScrolledPanel):

    def __init__(self, parent, style=wx.TAB_TRAVERSAL):
        super(PaymentCtrl, self).__init__(parent, style=style)
        
        # Layout
        self.__DoLayout()
        self.SetInitialSize()

    def __DoLayout(self):
        title_lbl= wx.StaticText(self, label="Payment")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)
        
        paymentTypeList = "Cash", "Cheque", "Inter-Bank", "Defered", 
        
        firstLbl = wx.StaticText(self, -1, "Amount:")
        first = wx.TextCtrl(self, -1, "")

        surnameLbl = wx.StaticText(self, -1, "Type:")
        surname = wx.ComboBox(self, -1, "Cash", (15, 30), wx.DefaultSize, paymentTypeList, wx.CB_DROPDOWN)
        
        payedTodayLbl = wx.StaticText(self, -1, "Payed today:")
        self.payedTodayRadio = wx.CheckBox(self, -1, "yes/no");

        invoiceRequiredLbl = wx.StaticText(self, -1, "Invoice Required:")
        self.invoiceRadio = wx.CheckBox(self, -1, "yes/no");

        townLbl = wx.StaticText(self, -1, "Paid by:")
        town = wx.TextCtrl(self, -1, "Patent")

      
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)
        
        addrSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        addrSizer.AddGrowableCol(1)
        
        addrSizer.Add(firstLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(first, 0, wx.EXPAND)
        
        addrSizer.Add(surnameLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(surname, 0, wx.EXPAND)
        
        addrSizer.Add(payedTodayLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.payedTodayRadio, 0, wx.EXPAND)
        
        addrSizer.Add(invoiceRequiredLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.invoiceRadio, 0, wx.EXPAND)
        
        
        addrSizer.Add(townLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(town, 0, wx.EXPAND)
        
       
        
        mainSizer.Add(addrSizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)
  
class HistoryCtrl(scrolledpanel.ScrolledPanel):

    def __init__(self, parent, style=wx.TAB_TRAVERSAL):
        super(HistoryCtrl, self).__init__(parent, style=style)
        
        self.historyListCtrl = HistoryListCtrl(self)
        data = [
                ("2013 12 23", "28.50", "Yes"),
                ("2013 06 02", "28.50", "Yes"),
                ("2013 01 22", "29.50", "Yes"),
                ("2012 11 10", "38.50", "Yes")
                ]
        self.historyListCtrl.populateList(data)
        # Layout
        self.__DoLayout()
        self.SetInitialSize()

    def __DoLayout(self):
        
        
        title_lbl= wx.StaticText(self, label="History")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)
        
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)
        
        sizer = wx.GridBagSizer(vgap=8, hgap=8)
    
        current_lbl= wx.StaticText(self, label="History:")
        sizer.Add(current_lbl, (1, 1))
        sizer.Add(self.historyListCtrl, (1, 2))

        mainSizer.Add(sizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)
        
        
class HistoryListCtrl(wx.ListCtrl):

    def __init__(self, parent):
        super(HistoryListCtrl, self).__init__(parent, style=wx.LC_REPORT, size=(250,300))

        self.InsertColumn(0, "Date")
        self.InsertColumn(1, "Amount")
        self.InsertColumn(2, "Paid")
       
        self.SetColumnWidth(0, 120)
        self.SetColumnWidth(1, 70)
        self.SetColumnWidth(2, wx.LIST_AUTOSIZE_USEHEADER)
        #self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        #self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)

    def populateList(self, data):
        self.DeleteAllItems()
        for row in data:
            list = row[0], row[1], row[2]
            self.Append(list)

class BillingAddressCtrl(scrolledpanel.ScrolledPanel):

    def __init__(self, parent, style=wx.TAB_TRAVERSAL):
        super(BillingAddressCtrl, self).__init__(parent, style=style)
         
    
        # Layout
        self.__DoLayout()
        self.SetInitialSize()

    def __DoLayout(self):
        title_lbl= wx.StaticText(self, label="Optional Billing Address")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)
        
        firstLbl = wx.StaticText(self, -1, "First Names:")
        first = wx.TextCtrl(self, -1, "")

        surnameLbl = wx.StaticText(self, -1, "Surname:")
        surname = wx.TextCtrl(self, -1, "")

        addressLbl = wx.StaticText(self, -1, "Address:")
        address1 = wx.TextCtrl(self, -1, "")
        address2 = wx.TextCtrl(self, -1, "")

        townLbl = wx.StaticText(self, -1, "Town/City:")
        town = wx.TextCtrl(self, -1, "")

        postcodeLbl = wx.StaticText(self, -1, "Postcode:")
        self.postcode = wx.TextCtrl(self, -1, "")
        
        homephoneLbl = wx.StaticText(self, -1, "Home Phone:")
        self.homephone = wx.TextCtrl(self, -1, "", size=(100, 23))
         
        workphoneLbl = wx.StaticText(self, -1, "Work Phone:")
        self.workphone = wx.TextCtrl(self, -1, "", size=(100, 23))
        
        mobileLbl = wx.StaticText(self, -1, "Mobile:")
        self.mobile = wx.TextCtrl(self, -1, "", size=(100, 23))
        
        preferedPhoneLbl = wx.StaticText(self, -1, "Prefered Phone:")
        self.preferedPhone = wx.TextCtrl(self, -1, "", size=(100, 23))
        
        emailLbl = wx.StaticText(self, -1, "Email:")
        self.email = wx.TextCtrl(self, -1, "", size=(200, 23))

      
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)
        
        addrSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        addrSizer.AddGrowableCol(1)
        
        addrSizer.Add(firstLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(first, 0, wx.EXPAND)
        
        addrSizer.Add(surnameLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(surname, 0, wx.EXPAND)
        
        addrSizer.Add(addressLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(address1, 0, wx.EXPAND)
        addrSizer.Add((10,10))
        addrSizer.Add(address2, 0, wx.EXPAND)
        
        addrSizer.Add(townLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(town, 0, wx.EXPAND)
        
        addrSizer.Add(postcodeLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.postcode, 0, wx.FIXED_MINSIZE)
        
        addrSizer.Add(homephoneLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.homephone, 0, wx.FIXED_MINSIZE)
        
        addrSizer.Add(workphoneLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.workphone, 0, wx.FIXED_MINSIZE)
        
        addrSizer.Add(mobileLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.mobile, 0, wx.FIXED_MINSIZE)
        
        addrSizer.Add(preferedPhoneLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.preferedPhone, 0, wx.FIXED_MINSIZE)
        
        addrSizer.Add(emailLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.email, 0, wx.FIXED_MINSIZE)
        
        mainSizer.Add(addrSizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)
    
class TestApp(wx.App):
    def OnInit(self):
        paymentEditDialog = PaymentEditDialog()
        paymentEditDialog.ShowModal()
        return True

if __name__=="__main__":

    app = TestApp(False)
    app.MainLoop()