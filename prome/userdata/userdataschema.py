from zope.interface import Interface, implements
from zope import schema
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone import api
from Products.CMFPlone.utils import safe_unicode

from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.component import queryUtility
from plone.registry.interfaces import IRegistry

from prome.userdata import MessageFactory as _
from plone.app.users.userdataschema import IUserDataSchemaProvider
from plone.app.users.userdataschema import IUserDataSchema


@grok.provider(IContextSourceBinder)
def availableClass(context):
    registry = queryUtility(IRegistry)
    terms = []
    if registry is not None:
        for className in registry.get('prome.userdata.userdataschema.IPromeClassSetting.classSetup', ()).split('\n'):
            className_uni = safe_unicode(className)
            terms.append(SimpleVocabulary.createTerm(className_uni.split(':')[0],
                                                     className_uni.split(':')[0],
                                                     className_uni.split(':')[1]))
    return SimpleVocabulary(terms)

def validateAccept(value):
    if not value == True:
        return False
    return True

class UserDataSchemaProvider(object):
    implements(IUserDataSchemaProvider)

    def getSchema(self):
        """
        """
        return IEnhancedUserDataSchema

checkGender = SimpleVocabulary(
    [SimpleTerm(value=u'Male', title=_(u'Male')),
     SimpleTerm(value=u'Female', title=_(u'Female')),]
    )

highestDegree = SimpleVocabulary(
    [SimpleTerm(value=u'Primary', title=_(u'Primary')),
     SimpleTerm(value=u'Junior', title=_(u'Junior')),
     SimpleTerm(value=u'Senior', title=_(u'Senior')),
     SimpleTerm(value=u'College', title=_(u'College')),
     SimpleTerm(value=u'University', title=_(u'University')),
     SimpleTerm(value=u'Master', title=_(u'Master')),
     SimpleTerm(value=u'Doctor', title=_(u'Doctor')),]
    )




class IEnhancedUserDataSchema(IUserDataSchema):


    """ Use all the fields from the default user data schema, and add various
    extra fields.
    """

    classSetting = schema.Choice(
        title=_(u'label_classSetting', default=u'ClassSetting'),
        description=_(u'help_classSetting',
                      default=u"Class Setting"),
#        vocabulary=availableClass,
        source=availableClass,
        required=True,
        )





    gender = schema.Choice(
        title=_(u'label_gender', default=u'Gender'),
        description=_(u'help_gender',
                      default=u"Are you a girl or a boy?"),
        vocabulary=checkGender,
        required=True,
        )
    birthdate = schema.Date(
        title=_(u'label_birthdate', default=u'birthdate'),
        description=_(u'help_birthdate', 
            default=u'Your date of birth, in the format yyyy-mm-dd'),
        required=False,
        )
    phone = schema.TextLine(
        title=_(u'label_phone', default=u'Telephone number'),
        description=_(u'help_phone',
                      default=u"Leave your phone number so we can reach you."),
        required=False,
        )
    mobile = schema.TextLine(
        title=_(u'label_mobile', default=u'Mobile phone number'),
        description=_(u'help_mobile',
                      default=u"Leave your mobile phone number so we can reach you."),
        required=False,
        )
    address = schema.TextLine(
        title=_(u'label_address', default=u'input address'),
        description=_(u'help_address',
                      default=u"Please input address in here."),
        required=False,
        )
    idCardNumber = schema.TextLine(
        title=_(u'label_idcardnumber', default=u'input id card number'),
        description=_(u'help_idcardnumber',
                      default=u"Please input ID card number in here."),
        required=False,
        )
    degree = schema.Choice(
        title=_(u'label_degree', default=u'Degree'),
        description=_(u'help_degree',
                      default=u"Please select a degree by your highest degree"),
        vocabulary=highestDegree,
        required=False,
        )
    schoolName = schema.TextLine(
        title=_(u'label_schoolname', default=u"input your highest's degree school name."),
        description=_(u'help_schoolname',
                      default=u"Please input your highest degree's school name."),
        required=False,
        )
    schoolDep = schema.TextLine(
        title=_(u'label_schooldep', default=u"input your school department, if you have."),
        description=_(u'help_schooldep',
                      default=u"Please input your school department, if you have."),
        required=False,
        )



from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from plone.z3cform import layout
from z3c.form import form
from plone.directives import form as Form

class IPromeClassSetting(Form.Schema):
    classSetup = schema.Text(
        title=_(u"Class setup"),
        required=False,
    )


class PromeClassSettingControlPanelForm(RegistryEditForm):
    form.extends(RegistryEditForm)
    schema = IPromeClassSetting

PromeClassSettingControlPanelView = layout.wrap_form(PromeClassSettingControlPanelForm, ControlPanelFormWrapper)
PromeClassSettingControlPanelView.label = _(u"Prome class setting")
