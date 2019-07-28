'''
Created on Jan 8, 2014

@author: wzw7yn
'''
import wx

from wx.wizard import PyWizardPage
import wx.wizard
#from newinfo import GPInfo


class Eqp_OtherPage(PyWizardPage):

    def __init__(self, parent, gpInfo):
        PyWizardPage.__init__(self, parent)
        self.prev = self
        self.next = self
        self.__DoLayout()
        self.SetInitialSize()
        self.Bind(wx.wizard.EVT_WIZARD_PAGE_CHANGED, self.OnPageChanged)
        self.gpInfo = gpInfo
        self.Done = False;

    def SetPrev(self, prev):
        self.prev = prev
        return self.prev

    def SetNext(self, next):
        self.next = next
        return self.next
    def GetNext(self):
        return self.next
    def GetPrev(self):
        return self.prev


    def __DoLayout(self):
        title_lbl= wx.StaticText(self, label="Equipment - Other")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)


        serviceHistoryLbl = wx.StaticText(self, -1, "Service History:")
        #self.appointments = wx.TextCtrl(self, style=wx.TE_MULTILINE, size=(300,100))
        self.rows = [
                ("2013 12 23", "PNA"),
                ("2013 06 02", "Check-up"),
                ]

        self.serviceHistory = ServiceHistoryListCtrl(self)
        self.serviceHistory.populateList(self.rows)

        text = ""
        noteLbl = wx.StaticText(self, -1, "Notes:")
        self.other = wx.TextCtrl(self, -1, text, size=(300,100), style=wx.TE_MULTILINE)
        #td.Set(GPTable.IDX_TITLE, text, title)
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        addrSizer = wx.GridBagSizer(vgap=8, hgap=8)
        
        addrSizer.Add(serviceHistoryLbl, (1, 1))
        addrSizer.Add(self.serviceHistory, (1, 2)) #wx.FIXED_MINSIZE
        
        addrSizer.Add(noteLbl, (2, 1))
        addrSizer.Add(self.other, (2, 2)) #wx.FIXED_MINSIZE

        mainSizer.Add(addrSizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)

    def IsDone(self):
        return self.Done


    def OnPageChanged(self, event):
        print "EVT_WIZARD_PAGE_CHANGED"
        self.gpInfo.other = self.other.GetValue()
        self.Done = True

    def GetPageInfo(self):
        pass
        #return self.gpInfo
        
        
class ServiceHistoryListCtrl(wx.ListCtrl):

    def __init__(self, parent):
        super(ServiceHistoryListCtrl, self).__init__(parent, style=wx.LC_REPORT, size=(300,100))

        self.InsertColumn(0, "Date")
        self.InsertColumn(1, "Title")
        self.InsertColumn(2, "Cost")

        self.SetColumnWidth(0, 120)
        self.SetColumnWidth(1, 180)
        self.SetColumnWidth(2, 180)
        #self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        #self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)

    def populateList(self, data):
        for row in data:
            list = row[0], row[1]
            self.Append(list)