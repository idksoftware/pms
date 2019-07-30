'''
Created on Jan 8, 2014

@author: wzw7yn
'''
import wx
import os
import wx.lib.scrolledpanel as scrolledpanel
from wx.adv import DatePickerCtrl
from wx import FileDialog


from access.cpd import CPDTable
from cpdlists import FilesListCtrl
from utils.copyattachments import Attachments
from cpdlists import WebLinksCtrl
from utils.editoptionsdlg import OptionsDialog
from utils.editoptionsdlg import OptionReader

class EditValidator(wx.PyValidator):
    def __init__(self): #, data, key)
        wx.PyValidator.__init__(self)
        #self.data = data
        #self.key = key

    def Clone(self):
        return EditValidator(self) #.data, self.key)

    def TransferFromWindow(self, *args, **kwargs):
        print "got here"
        return wx.PyValidator.TransferFromWindow(self, *args, **kwargs)


class GeneralCtrl(scrolledpanel.ScrolledPanel):

    def __init__(self, parent, dbRow, style=wx.TAB_TRAVERSAL):
        super(GeneralCtrl, self).__init__(parent, style=style)

        # Layout
        self.__DoLayout(dbRow)
        self.SetInitialSize()

    def __DoLayout(self, dbRow):

        title_lbl= wx.StaticText(self, label="Continuous Professional Development - Details")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)



        text = ""
        title = dbRow.GetAttr('title')
        titleLbl = wx.StaticText(self, -1, "Title:")
        title.SetCtrl(wx.TextCtrl(self, -1, title.GetText(), size=(200, 23)))

        dateLbl = wx.StaticText(self, -1, "Date:")
        date = wx.DateTime()
        date_started = dbRow.GetAttr('date_started')
        date.ParseDate(date_started.GetText())
        date_started.SetCtrl(DatePickerCtrl(self, -1, date))

        days_taken = dbRow.GetAttr('days_taken')
        noOfDaysLbl = wx.StaticText(self, -1, "Number of days taken:")
        text = days_taken.GetText()
        # validator=EditValidator(text, 'days_taken')
        days_taken.SetCtrl(wx.SpinCtrl(self, -1, "", size=(40,25), min=0, max=23, initial=9))

        self.activity_type = dbRow.GetAttr('activity_type')

        atReader = OptionReader("/home/wzw7yn/workspace/pms/main/cpdatopts.xml");
        self.atList = atReader.read()
        activityTypeLbl = wx.StaticText(self, -1, "Activity Type:")
        self.activity_type.SetCtrl(wx.ComboBox(self, -1, self.activity_type.GetText(), (10, 30), (200, 23), self.atList, wx.CB_DROPDOWN))
        atAddButton = wx.Button(self, -1, "Add", size=(50, 23))

        self.category = dbRow.GetAttr('category')
        catReader = OptionReader("/home/wzw7yn/workspace/pms/main/cpdcatopts.xml");
        catList = catReader.read()
        categoryLbl = wx.StaticText(self, -1, "Category:")
        self.category.SetCtrl(wx.ComboBox(self, -1, self.category.GetText(), (10, 30), (200, 23), catList, wx.CB_DROPDOWN))
        catAddButton = wx.Button(self, -1, "Add", size=(50, 23))

        self.core_cpd_module = dbRow.GetAttr('core_cpd_module')
        cmReader = OptionReader("/home/wzw7yn/workspace/pms/main/cpdcmopts.xml");
        catList = cmReader.read()
        coreCPDModuleLbl = wx.StaticText(self, -1, "Core CPD Module:")
        self.core_cpd_module.SetCtrl(wx.ComboBox(self, -1, self.core_cpd_module.GetText(), (10, 30), (200, 23), catList, wx.CB_DROPDOWN))
        cmAddButton = wx.Button(self, -1, "Add", size=(50, 23))

        atAddButton.Bind(wx.EVT_BUTTON, self.OnAtButton)
        catAddButton.Bind(wx.EVT_BUTTON, self.OnCatButton)
        cmAddButton.Bind(wx.EVT_BUTTON, self.OnCmButton)

        description = dbRow.GetAttr('description')
        descriptionLbl = wx.StaticText(self, -1, "Description:")
        description.SetCtrl(wx.TextCtrl(self, -1, description.GetText(), size=(300,100), style=wx.TE_MULTILINE))

        learning_objectives = dbRow.GetAttr('learning_objectives')
        learningObjectivesLbl = wx.StaticText(self, -1, "Learning Objectives:")
        learning_objectives.SetCtrl(wx.TextCtrl(self, -1, learning_objectives.GetText(), size=(300,80), style=wx.TE_MULTILINE))



        grpSizer = wx.GridBagSizer(vgap=8, hgap=8)

        grpSizer.Add(titleLbl, (1, 1))
        grpSizer.Add(title.GetCtrl(), (1, 2))

        grpSizer.Add(dateLbl, (2, 1))
        grpSizer.Add(date_started.GetCtrl(), (2, 2))

        grpSizer.Add(noOfDaysLbl, (3, 1))
        grpSizer.Add(days_taken.GetCtrl(), (3, 2))

        grpSizer.Add(activityTypeLbl, (4, 1))
        grpSizer.Add(self.activity_type.GetCtrl(), (4, 2))
        grpSizer.Add(atAddButton, (4, 3))

        grpSizer.Add(categoryLbl, (5, 1))
        grpSizer.Add(self.category.GetCtrl(), (5, 2))
        grpSizer.Add(catAddButton, (5, 3))

        grpSizer.Add(coreCPDModuleLbl, (6, 1))
        grpSizer.Add(self.core_cpd_module.GetCtrl(), (6, 2))
        grpSizer.Add(cmAddButton, (6, 3))

        grpSizer.Add(descriptionLbl, (7, 1))
        grpSizer.Add(description.GetCtrl(), (7, 2)) #wx.FIXED_MINSIZE

        grpSizer.Add(learningObjectivesLbl, (8, 1))
        grpSizer.Add(learning_objectives.GetCtrl(), (8, 2))

        mainSizer.Add(grpSizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)

    def Close(self, *args, **kwargs):
        print "closing GeneralCtrl"
        return scrolledpanel.ScrolledPanel.Close(self, *args, **kwargs)

    def OnAtButton(self, events):
        dialog = OptionsDialog("Add New Activity Type", "/home/wzw7yn/workspace/pms/main/cpdatopts.xml")
        if dialog.ShowModal() == wx.ID_OK:
            dialog.Update()
            opr = OptionReader("/home/wzw7yn/workspace/pms/main/cpdatopts.xml");
            opr.updateComboBox(self.activity_type.GetCtrl())

    def OnCatButton(self, events):
        dialog = OptionsDialog("Add New Category", "/home/wzw7yn/workspace/pms/main/cpdcatopts.xml")
        if dialog.ShowModal() == wx.ID_OK:
            dialog.Update()
            opr = OptionReader("/home/wzw7yn/workspace/pms/main/cpdcatopts.xml");
            opr.updateComboBox(self.category.GetCtrl())


    def OnCmButton(self, events):
        dialog = OptionsDialog("Add New Core Module Option", "/home/wzw7yn/workspace/pms/main/cpdcmopts.xml")
        if dialog.ShowModal() == wx.ID_OK:
            dialog.Update()
            opr = OptionReader("/home/wzw7yn/workspace/pms/main/cpdcmopts.xml");
            opr.updateComboBox(self.core_cpd_module.GetCtrl())

class OtherCtrl(scrolledpanel.ScrolledPanel):

    def __init__(self, parent, dbRow, style=wx.TAB_TRAVERSAL):
        super(OtherCtrl, self).__init__(parent, style=style)

        # Layout
        self.__DoLayout(dbRow)
        self.SetInitialSize()

    def __DoLayout(self, dbRow):
        
        title_lbl= wx.StaticText(self, label="Continuous Professional Development - Other")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        self.rows = [
                ("2013 12 23", "PNA"),
                ("2013 06 02", "Check-up"),
                ]
        self.attachments = Attachments("/home/wzw7yn/pms/repos")
        afList = list() 
        newOptionLbl = wx.StaticText(self, -1, "Attached Files:")
        self.listCtrl = wx.ListBox(self, -1, (10, 30), (300,80), afList, wx.LB_SINGLE | wx.LB_SORT)
        self.addButton = wx.Button(self, -1, "Add", size=(50, 23))
        self.deleteButton = wx.Button(self, -1, "Delete", size=(50, 23))

        btnSizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer.Add(self.addButton)
        btnSizer.Add(self.deleteButton)

        self.listCtrl.Bind(wx.EVT_LISTBOX_DCLICK , self.OnItemSelected)
        self.listCtrl.Bind(wx.EVT_LISTBOX , self.OnClicked)
        self.addButton.Bind(wx.EVT_BUTTON , self.OnAdd)
        self.deleteButton.Bind(wx.EVT_BUTTON , self.OnDelete)

        webLinksLbl = wx.StaticText(self, -1, "Web Links:")
        self.webLinksCtrl = WebLinksCtrl(self)
        self.webLinksCtrl.populateList(self.rows)

        text = ""

        reflectiveCommentsLbl = wx.StaticText(self, -1, "Reflective Comments:")
        self.reflective_comments = wx.TextCtrl(self, -1, text, size=(300,80), style=wx.TE_MULTILINE)

        grpSizer = wx.GridBagSizer(vgap=8, hgap=8)



        grpSizer.Add(reflectiveCommentsLbl, (1, 1))
        grpSizer.Add(self.reflective_comments, (1, 2))

        grpSizer.Add(newOptionLbl, (2, 1))
        grpSizer.Add(self.listCtrl, (2, 2))
        grpSizer.Add(btnSizer, (2, 3))


        grpSizer.Add(webLinksLbl, (3, 1))
        grpSizer.Add(self.webLinksCtrl, (3, 2)) #wx.FIXED_MINSIZE

        mainSizer.Add(grpSizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)

    def OnItemSelected(self, event):
        print "Here 1"

    def OnClicked(self, event):
        self.selection = self.listCtrl.GetSelection()

    def OnAdd(self, event):
        '''
        dialog = AddDialog("Add Option", None)
        if dialog.ShowModal() == wx.ID_OK:
            print dialog.GetOption()
            self.listCtrl.AppendAndEnsureVisible(dialog.GetOption())
        '''
        wildcard = "All Files (*.*) | *.* |" \
                   "source (*.py) | *.py |" \
                   "Doc Files (*.doc) | *.doc"
        dialog = FileDialog(self, "Attach files", os.getcwd(), "", "*.*", FileDialog.OPEN | FileDialog.MULTIPLE)
        if dialog.ShowModal() == wx.ID_OK:
            
            fullList = dialog.GetPaths()
            self.attachments.copy(fullList)
            for item in self.attachments.GetFilenames():
                self.listCtrl.Append(item)
                
        dialog.Destroy()
   
    def OnDelete(self, event):
        fstr = self.listCtrl.GetString(self.selection)
        print fstr
        self.attachments.Delete(fstr)
        self.listCtrl.Delete(self.selection)

class HistoryCtrl(scrolledpanel.ScrolledPanel):

    def __init__(self, parent, style=wx.TAB_TRAVERSAL):
        super(HistoryCtrl, self).__init__(parent, style=style)
        #self.current = "Default"
        # Layout
        self.__DoLayout()
        self.SetInitialSize()

    def __DoLayout(self):

        title_lbl= wx.StaticText(self, label="History")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        AppointmentsLbl = wx.StaticText(self, -1, "Appointment History:")
        #self.appointments = wx.TextCtrl(self, style=wx.TE_MULTILINE, size=(300,100))
        self.rows = [
                ("2013 12 23", "PNA"),
                ("2013 06 02", "Check-up"),
                ]

        self.appointments = AppointmentListCtrl(self)
        self.appointments.populateList(self.rows)

        otherLbl = wx.StaticText(self, -1, "Other Notes:")
        self.other = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE, size=(300,100))

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        grp1Sizer = wx.GridBagSizer(vgap=8, hgap=8)



        grp1Sizer.Add(AppointmentsLbl, (1, 1))
        grp1Sizer.Add(self.appointments, (1, 2))

        grp1Sizer.Add(otherLbl, (2, 1))
        grp1Sizer.Add(self.other, (2, 2))

        mainSizer.Add(grp1Sizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)

class AppointmentListCtrl(wx.ListCtrl):

    def __init__(self, parent):
        super(AppointmentListCtrl, self).__init__(parent, style=wx.LC_REPORT, size=(300,100))

        self.InsertColumn(0, "Date")
        self.InsertColumn(1, "Title")

        self.SetColumnWidth(0, 120)
        self.SetColumnWidth(1, 180)
        #self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        #self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)

    def populateList(self, data):
        for row in data:
            list = row[0], row[1]
            self.Append(list)




class CPDEditDialog(wx.Dialog):
    '''
    classdocs
    '''


    def __init__(self, idx):
        wx.Dialog.__init__(self, None, -1, "Continuous Professional Development", size=(600, 600))
        '''
        Constructor
        '''
        self.selection = idx
        self.cpdTable = CPDTable()
        rows = self.cpdTable.showAll()
        if len(rows) == 0:
            # no row to edit
            return
        row = rows[self.selection]
        print row

        from cpdtableitem import CPDTableDef
        from access.database import DBTable

        cpdTableBind = DBTable(CPDTableDef())

        self.dbRow = cpdTableBind.GetRow(row)


        self.panel = PatentEditPanel(self, self.dbRow)

        sizer = wx.BoxSizer(wx.VERTICAL)
        #btnSizer = wx.StdDialogButtonSizer()
        btnSizer = self.CreateButtonSizer(wx.OK | wx.CANCEL)

        sizer.Add(self.panel, 1, wx.EXPAND)
        #okButton = wx.Button(self, wx.ID_OK, "Ok", pos=(15, 15))
        #okButton.SetDefault()
        #btnSizer.Add(okButton)
        #cancelButton = wx.Button(self, wx.ID_CANCEL, "Cancel", pos=(15, 15))
        #btnSizer.Add(cancelButton)
        sizer.Add(btnSizer, 0, wx.ALIGN_RIGHT | wx.ALL, 2)


        #sizer.Add(btnSizer)
        self.SetSizer(sizer)
        self.SetInitialSize()

        #okButton.Bind(wx.EVT_BUTTON, self.OnButton)

    def OnButton(self, event):
        print "Close"
        #pos = self.panel.generalCtrl.preferedPhone.Value()
        #self.EndModal(event)
        return event


    def Update(self):


        self.cpdTable.update(
                self.dbRow.GetAttr("cpd_id").GetCurText(),
                title=self.dbRow.GetAttr("title").GetCurText(),
                date_started=self.dbRow.GetAttr("date_started").GetCurText(),
                days_taken=self.dbRow.GetAttr("days_taken").GetCurText(),
                activity_type=self.dbRow.GetAttr("activity_type").GetCurText(),
                category=self.dbRow.GetAttr("category").GetCurText(),
                core_cpd_module=self.dbRow.GetAttr("core_cpd_module").GetCurText(),
                description=self.dbRow.GetAttr("description").GetCurText(),
                learning_objectives=self.dbRow.GetAttr("learning_objectives").GetCurText(),
                reflective_comments=self.dbRow.GetAttr("reflective_comments").GetCurText(),
                attached_files=self.dbRow.GetAttr("attached_files").GetCurText(),
                web_links=self.dbRow.GetAttr("web_links").GetCurText()
                )


class AddOptionDialog(wx.Dialog):
    '''
    classdocs
    '''


    def __init__(self, title):
        wx.Dialog.__init__(self, None, -1, "Add Option", size=(600, 600))
        '''
        Constructor
        '''
        self.panel = AddOptionPanel(self, title)
        sizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer = self.CreateButtonSizer(wx.OK | wx.CANCEL)

        sizer.Add(self.panel, 1, wx.EXPAND)
        sizer.Add(btnSizer, 0, wx.ALIGN_RIGHT | wx.ALL, 2)

        self.SetSizer(sizer)
        self.SetInitialSize()

class AddOptionPanel(wx.Panel):
    def __init__(self, parent, title):
        super(AddOptionPanel, self).__init__(parent, style=wx.LB_BOTTOM)

        title_lbl= wx.StaticText(self, label=title)
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        text = ""
        newOptionLbl = wx.StaticText(self, -1, "New Option:")
        self.newOption = wx.TextCtrl(self, -1, text, size=(200, 23))

        grpSizer = wx.GridBagSizer(vgap=8, hgap=8)

        grpSizer.Add(newOptionLbl, (1, 1))
        grpSizer.Add(self.newOption, (1, 2))

        mainSizer.Add(grpSizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)



class PatentEditPanel(wx.Notebook):
    def __init__(self, parent, dbRow):
        super(PatentEditPanel, self).__init__(parent, style=wx.LB_BOTTOM)


        self.generalCtrl = GeneralCtrl(self, dbRow)
        self.AddPage(self.generalCtrl, "General")
        self.otherCtrl = OtherCtrl(self, dbRow)
        self.AddPage(self.otherCtrl, "Other")
        self.historyCtrl = HistoryCtrl(self)
        self.AddPage(self.historyCtrl, "history")

class TestApp(wx.App):
    def OnInit(self):
        cpdEditDialog = CPDEditDialog(0)

        print "Opening CPDEditDialog"
        if cpdEditDialog.ShowModal() == wx.ID_OK:
            cpdEditDialog.Update()
        print "Closing CPDEditDialog"
        return True

from access.database import Database
from utils.configreader import ConfigReader

if __name__=="__main__":
    cfg = ConfigReader()
    cfg.read("/home/wzw7yn/workspace/pms/main/config.xml")
    Database.Open(cfg.GetPath(), cfg.GetUsername(), cfg.GetPassword())
    app = TestApp(False)
    app.MainLoop()