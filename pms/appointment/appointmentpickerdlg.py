'''
Created on Jan 8, 2014

@author: wzw7yn
'''
import wx
import wx.lib.scrolledpanel as scrolledpanel
from access.gp import GPTable
from appointmentbookctrl import AppointmentBookCtrl
from wx.adv import DatePickerCtrl



class AppointmentPickerDialog(wx.Dialog):
    '''
    classdocs
    '''


    def __init__(self):
        wx.Dialog.__init__(self, None, -1, "Appointment Details", size=(1000, 600))
        '''
        Constructor
        '''
        self.panel = AppointmentPickerPanel(self)

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

    def OnButton(self, event):
        if event == wx.ID_OK:
            self.Save()

    def Save(self):
        cl = self.tableData.updateList()
        if len(cl):
            self.gpTable.updatelist(1, cl)
            return True
        return False

    def GetUsername(self):
        self.panel.GetUsername()

    def GetPassword(self):
        self.panel.GetPasswd()

class AppointmentPickerPanel(wx.Panel):
    def __init__(self, parent):
        super(AppointmentPickerPanel, self).__init__(parent, style=wx.LB_BOTTOM, size=(1000, 600))
        self.appointmentBookCtrl = AppointmentBookCtrl(self)
        title_lbl= wx.StaticText(self, label="Appointment date")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        text = ""
        makeModelLbl = wx.StaticText(self, -1, "Date:")
        self.date = DatePickerCtrl(self, size=(100, -1), style=DatePickerCtrl.DP_DROPDOWN | DatePickerCtrl.DP_SHOWCENTURY)

        serialNoLbl = wx.StaticText(self, -1, "Time:")

        timeSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.hour = wx.SpinCtrl(self, -1, "", size=(40,23), min=0, max=23, initial=9)
        hourLbl = wx.StaticText(self, -1, " hour ")
        self.min = wx.SpinCtrl(self, -1, "", size=(40,23), min=0, max=59, initial=30)
        minLbl = wx.StaticText(self, -1, " min")
        self.amRadio = wx.RadioButton(self, -1, "am");
        self.pmRadio = wx.RadioButton(self, -1, "pm");
        timeSizer.Add(self.hour)
        timeSizer.Add(hourLbl)
        timeSizer.Add(self.min)
        timeSizer.Add(minLbl)
        timeSizer.Add(self.amRadio)
        timeSizer.Add(self.pmRadio)

        grpSizer = wx.GridBagSizer(vgap=8, hgap=8)
        grpSizer.Add(makeModelLbl, (1, 1))
        grpSizer.Add(self.date, (1, 2))

        grpSizer.Add(serialNoLbl, (2, 1))
        grpSizer.Add(timeSizer, (2, 2))


        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        listSizer = wx.GridBagSizer(vgap=2, hgap=2)
        listSizer.Add(self.appointmentBookCtrl, (1, 1))
        mainSizer.Add(grpSizer, 0, wx.EXPAND | wx.ALL, 10)
        mainSizer.Add(listSizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)

        self.hour.Bind(wx.EVT_TEXT, self.OnText)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)

    def OnText(self, event):
        print self.hour.Value
        #if self.hour.Value > 12:
        #    pass
            #self.amRadio.Enabled(False)
            #self.pmRadio.Enabled

    def OnClicked(self, event):
        self.selected_row = event.GetIndex()
        #row = self.rows[self.selected_row]
        print self.selected_row

        rows = self.appointmentBookCtrl.GetRows()
        row = rows[self.selected_row]
        date = row[0]
        print date
        dateTime = wx.DateTime()
        dateTime.ParseDateTime(date)
        self.date.Value = dateTime
        self.hour.Value = dateTime.Hour
        self.min.Value = dateTime.Minute
        #appointmentDialog.ShowModal()

class TestApp(wx.App):
    def OnInit(self):
        appointmentPickerDialog = AppointmentPickerDialog()
        
        print "Opening AppointmentPickerDialog"
        appointmentPickerDialog.ShowModal()
        print "Closing AppointmentPickerDialog"
       
        return True

from access.database import Database
from utils.configreader import ConfigReader

if __name__=="__main__":
    cfg = ConfigReader()
    cfg.read("config.xml")
    Database.Open(cfg.GetPath(), cfg.GetUsername(), cfg.GetPassword())
    app = TestApp(False)
    app.MainLoop()