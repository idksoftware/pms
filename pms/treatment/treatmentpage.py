'''
Created on Feb 5, 2014

@author: wzw7yn

This will contain the treatment page
this will include a list of treatment with times, costs etc.
'''
import wx

import wx.lib.scrolledpanel as scrolledpanel

class TreatmentsCtrl(scrolledpanel.ScrolledPanel):
    pageName = "TreatmentsPage"
    def __init__(self, parent, style=wx.TAB_TRAVERSAL):
        super(TreatmentsCtrl, self).__init__(parent, style=style)
        self.backupsListCtrl = BackupListCtrl(self)
        ##self.gpTable = GPTable()
        #rows = self.gpTable.showAll()
        ##self.rowManager = RowManager(rows)
        #self.backupsListCtrl.populateList(self.rowManager.Get())
        # Layout


        # Layout
        self.__DoLayout()
        self.SetInitialSize()


    def __DoLayout(self):

        title_lbl= wx.StaticText(self, label="Treatments")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)


        sizer = wx.GridBagSizer(vgap=2, hgap=2)
        nameLbl = wx.StaticText(self, -1, "Name:")

        nameStr = 'Prelimary Assessment'
        self.name = wx.StaticText(self, -1, nameStr)

        sizer.Add(nameLbl, (1, 1))
        sizer.Add(self.name, (1, 2))

        discriptionLbl = wx.StaticText(self, -1, "Discription:")
        
        discriptionStr = 'Inital assessment of the patent'
        self.discription = wx.StaticText(self, -1, discriptionStr)

        sizer.Add(discriptionLbl, (2, 1))
        sizer.Add(self.discription, (2, 2))
        
        amountLbl = wx.StaticText(self, -1, "Amount:")
        amountStr = '38.50'
        sizer.Add(amountLbl, (5, 1))
        self.amount = wx.StaticText(self, -1, amountStr)
        sizer.Add(self.amount, (5, 2))
        



        btnszr = wx.StdDialogButtonSizer()
        editbtn = wx.Button(self, wx.ID_EDIT)
        openbtn = wx.Button(self, wx.ID_OPEN)
        editbtn.SetDefault()
        sizer.Add(editbtn, (8, 3))
        sizer.Add(openbtn, (8, 4))

        btnszr.Realize()

        listSizer = wx.GridBagSizer(vgap=2, hgap=2)
        listSizer.Add(self.backupsListCtrl, (1, 1))
        mainSizer.Add(sizer, 0, wx.EXPAND | wx.ALL, 10)
        #mainSizer.Add(btnszr, 0, wx.ALIGN_LEFT, 12)
        mainSizer.Add(listSizer, 0, wx.EXPAND | wx.ALL, 10)

        self.SetSizer(mainSizer)

        #self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        #self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)

   

    def DBStr(self,data):
        if data == None:
            return ""
        return data


    def AddressUpdate(self, row):
        pass
        '''
        title = self.DBStr(row[PatentTable.IDX_TITLE])
        first = self.DBStr(row[PatentTable.IDX_FIRST_NAME])
        surname = self.DBStr(row[PatentTable.IDX_SURNAME])
        nameStr = ""
        if title == "":
            nameStr = first + " " + surname
        else:
            nameStr = title + " " + first + " " + surname
        self.name.SetLabel(nameStr)

        address = self.DBStr(row[PatentTable.IDX_ADDRESS])
        town = self.DBStr(row[PatentTable.IDX_TOWN])

        address1Str = address + " " + town
        self.address.SetLabel(address1Str)

        county = "West Sussex"
        postcode = self.DBStr(row[PatentTable.IDX_POST_CODE])

        self.county.SetLabel(county)
        self.post.SetLabel(postcode)

        Home = self.DBStr(row[PatentTable.IDX_HOME_PHONE])
        Work = self.DBStr(row[PatentTable.IDX_WORK_PHONE])
        Mobile = self.DBStr(row[PatentTable.IDX_MOBILE])

        phoneStr = "Home " + Home + " Work " + Work

        if Mobile == None:
            mobileStr = "Mobile " + Mobile
        else:
            mobileStr = ""

        self.phone.SetLabel(phoneStr)
        self.mobile.SetLabel(mobileStr)

        email = self.DBStr(row[PatentTable.IDX_EMAIL])
        if email != None:
            self.email.SetLabel(email)
        else:
            self.email.SetLabel("")
        '''

class BackupListCtrl(wx.ListCtrl):

    def __init__(self, parent):
        super(BackupListCtrl, self).__init__(parent, style=wx.LC_REPORT, size=(500,300))

        self.InsertColumn(0, "Period")
        self.InsertColumn(1, "Type")
        self.InsertColumn(2, "Volume Set Label")
        self.InsertColumn(3, "Location")

        self.SetColumnWidth(0, 120)
        self.SetColumnWidth(1, 50)
        self.SetColumnWidth(1, 100)
        self.SetColumnWidth(2, wx.LIST_AUTOSIZE_USEHEADER)
        #self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        #self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)

    def populateList(self, data):
        for row in data:
            list = row[1], row[2], row[3], row[4]
            self.Append(list)

    
class MainFrame(wx.Frame):
    
    def __init__(self, parent, id=wx.ID_ANY, title="",pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, name ="myFrame"):
        super(MainFrame, self).__init__(parent, id, title, pos, size, style, name)

        self.panel = MainPane(self)
    
class MainPane(wx.Notebook):

    def __init__(self, parent):
        super(MainPane, self).__init__(parent, style=wx.NB_LEFT)

        #self.gpCtrl = GPCtrl(self)
        #self.AddPage(self.gpCtrl, "Patents")


class TestApp(wx.App):
    
    def OnInit(self):
        frame = MainFrame(None, title="The Main Frame")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

if __name__=="__main__":

    app = TestApp(False)
    app.MainLoop()
