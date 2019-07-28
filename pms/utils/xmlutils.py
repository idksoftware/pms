'''
Created on Aug 27, 2013

@author: wzw7yn
'''
from datetime import datetime

class XmlUtils:
    @staticmethod
    def parseElement(parent, tag, required):
        nodelist = parent.getElementsByTagName(tag)
        if nodelist == None:
            if required:
                raise SyntaxError("Error parsing: " + tag)
            else:
                return None
        return nodelist[0]
    @staticmethod
    def parseLong(parent, tag, required, isHex):
        nodelist = parent.getElementsByTagName(tag)
        if nodelist == None:
            return None
        text = XmlUtils.handleText(nodelist)
        if text == None:
            if required == False:
                return 0;
            raise SyntaxError("Error parsing: " + tag)
        if isHex == True:
            return long(text, 16)
        return long(text, 10)
    @staticmethod
    def parseString(parent, tag, required):
        nodelist = parent.getElementsByTagName(tag)
        if nodelist == None:
            return None
        text = XmlUtils.handleText(nodelist)
        if text == None:
            if required == False:
                return 0;
            raise SyntaxError("Error parsing: " + tag)

        return text
    @staticmethod
    def parseDate(parent, tag, required):
        nodelist = parent.getElementsByTagName(tag)
        text = XmlUtils.handleText(nodelist)
        if text == None:
            if required == False:
                return 0;
            raise SyntaxError("Error parsing: " + tag)
        try:
            ascText = text.encode("ascii", 'ignore')
            #ascText = " 2008 02 12"
            date = datetime.strptime(ascText, "%Y %m %d")
        except ValueError, e:
            print str(e)

        return date
    @staticmethod
    def handleText(nodelist):
        text = ""
        for node in nodelist:
            text += XmlUtils.getText(node.childNodes)
        return text
    @staticmethod
    def getText(nodelist):
        rc = []
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                rc.append(node.data)
                return ''.join(rc)