'''
Created on Sep 2, 2013

@author: wzw7yn
'''

from xml.dom import minidom
from xmlutils import XmlUtils


class ConfigReader:
    
    _single = None

    def __init__(self):

        if ConfigReader._single:
            #raise ConfigReader._single
            return
        ConfigReader._single = self


    @staticmethod
    def Instance():
        if ConfigReader._single:
                return ConfigReader._single
        ConfigReader._single = ConfigReader()
        return ConfigReader._single

    def read(self, xmlFile) :
        xmldoc = minidom.parse(xmlFile)
        itemlist = xmldoc.getElementsByTagName("Config")
        if itemlist == None:
            return -1;

        config = XmlUtils.parseElement(itemlist[0], "Database", True)
        self.db_path = XmlUtils.parseString(config, "Path", True)
        self.db_username = XmlUtils.parseString(config, "UserName", False)
        self.db_password = XmlUtils.parseString(config, "PW", False)

    def GetPath(self):
        return self.db_path

    def GetUsername(self):
        return self.db_username

    def GetPassword(self):
        return self.db_password

if __name__ == "__main__":
    _cfg = ConfigReader()
    _cfg.read("config.xml")
    print _cfg.GetPath()
    print _cfg.GetUsername()
    print _cfg.GetPassword()