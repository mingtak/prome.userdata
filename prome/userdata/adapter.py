from plone.app.users.browser.personalpreferences import UserDataPanelAdapter
from Products.CMFPlone.utils import safe_unicode

class EnhancedUserDataPanelAdapter(UserDataPanelAdapter):
    """
    """
    def get_videoPermission(self):
        return self.context.getProperty('videoPermission', '')
    def set_videoPermission(self, value):
        return self.context.setMemberProperties({'videoPermission': value})
    videoPermission = property(get_videoPermission, set_videoPermission)

    def get_teachingMethod(self):
        return self.context.getProperty('teachingMethod', '')
    def set_teachingMethod(self, value):
        return self.context.setMemberProperties({'teachingMethod': str(value)})
    teachingMethod = property(get_teachingMethod, set_teachingMethod)

    def get_courses(self):
        return self.context.getProperty('courses', '')
    def set_courses(self, value):
        return self.context.setMemberProperties({'courses': str(value)})
    courses = property(get_courses, set_courses)

    def get_studentStatus(self):
        return self.context.getProperty('studentStatus', '')
    def set_studentStatus(self, value):
        return self.context.setMemberProperties({'studentStatus': str(value)})
    studentStatus = property(get_studentStatus, set_studentStatus)

    def get_howToGetInfo(self):
        return self.context.getProperty('howToGetInfo', '')
    def set_howToGetInfo(self, value):
        return self.context.setMemberProperties({'howToGetInfo': str(value)})
    howToGetInfo = property(get_howToGetInfo, set_howToGetInfo)

    def get_paymentState(self):
        return self.context.getProperty('paymentState', '')
    def set_paymentState(self, value):
        return self.context.setMemberProperties({'paymentState': str(value)})
    paymentState = property(get_paymentState, set_paymentState)

    def get_note(self):
        return self.context.getProperty('note', '')
    def set_note(self, value):
        return self.context.setMemberProperties({'note': str(value)})
    note = property(get_note, set_note)

    def get_classSetting(self):
        return self.context.getProperty('classSetting', '')
    def set_classSetting(self, value):
        return self.context.setMemberProperties({'classSetting': value})
    classSetting = property(get_classSetting, set_classSetting)

    def get_gender(self):
        return self.context.getProperty('gender', '')
    def set_gender(self, value):
        return self.context.setMemberProperties({'gender': str(value)})
    gender = property(get_gender, set_gender)

    def get_mobile(self):
        return self.context.getProperty('mobile', '')
    def set_mobile(self, value):
        return self.context.setMemberProperties({'mobile': value})
    mobile = property(get_mobile, set_mobile)

    def get_address(self):
        return self.context.getProperty('address', '')
    def set_address(self, value):
        return self.context.setMemberProperties({'address': value})
    address = property(get_address, set_address)

    def get_idCardNumber(self):
        return self.context.getProperty('idCardNumber', '')
    def set_idCardNumber(self, value):
        return self.context.setMemberProperties({'idCardNumber': value})
    idCardNumber = property(get_idCardNumber, set_idCardNumber)

    def get_birthdate(self):
        return self.context.getProperty('birthdate', '')
    def set_birthdate(self, value):
        return self.context.setMemberProperties({'birthdate': value})
    birthdate = property(get_birthdate, set_birthdate)

    def get_degree(self):
        return self.context.getProperty('degree', '')
    def set_degree(self, value):
        return self.context.setMemberProperties({'degree': str(value)})
    degree = property(get_degree, set_degree)

    def get_schoolName(self):
        return self.context.getProperty('schoolName', '')
    def set_schoolName(self, value):
        return self.context.setMemberProperties({'schoolName': value})
    schoolName = property(get_schoolName, set_schoolName)

    def get_phone(self):
        return self.context.getProperty('phone', '')
    def set_phone(self, value):
        return self.context.setMemberProperties({'phone': value})
    phone = property(get_phone, set_phone)

    def get_schoolDep(self):
        return self.context.getProperty('schoolDep', '')
    def set_schoolDep(self, value):
        return self.context.setMemberProperties({'schoolDep': value})
    schoolDep = property(get_schoolDep, set_schoolDep)
