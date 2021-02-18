# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aaaa(models.Model):
    id = models.AutoField(blank=True, null=True,)
    x = models.TextField(blank=True, null=True)
    y = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aaaa'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bobsource(models.Model):
    sourceid = models.AutoField()
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    muni_municode = models.IntegerField()
    userattributable = models.BooleanField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bobsource'


class Ceactionrequest(models.Model):
    requestid = models.AutoField()
    requestpubliccc = models.IntegerField(blank=True, null=True)
    muni_municode = models.IntegerField()
    property_propertyid = models.IntegerField(blank=True, null=True)
    issuetype_issuetypeid = models.IntegerField()
    actrequestor_requestorid = models.IntegerField()
    cecase_caseid = models.IntegerField(blank=True, null=True)
    submittedtimestamp = models.DateTimeField()
    dateofrecord = models.DateTimeField()
    notataddress = models.BooleanField(blank=True, null=True)
    addressofconcern = models.TextField(blank=True, null=True)
    requestdescription = models.TextField()
    isurgent = models.BooleanField(blank=True, null=True)
    anonymityrequested = models.BooleanField(blank=True, null=True)
    coginternalnotes = models.TextField(blank=True, null=True)
    muniinternalnotes = models.TextField(blank=True, null=True)
    publicexternalnotes = models.TextField(blank=True, null=True)
    status_id = models.IntegerField()
    caseattachmenttimestamp = models.DateTimeField(blank=True, null=True)
    paccenabled = models.BooleanField(blank=True, null=True)
    caseattachment_userid = models.IntegerField(blank=True, null=True)
    usersubmitter_userid = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ceactionrequest'


class Ceactionrequestissuetype(models.Model):
    issuetypeid = models.AutoField()
    typename = models.TextField(blank=True, null=True)
    typedescription = models.TextField(blank=True, null=True)
    muni_municode = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    intensity_classid = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ceactionrequestissuetype'


class Ceactionrequestphotodoc(models.Model):
    photodoc_photodocid = models.IntegerField()
    ceactionrequest_requestid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ceactionrequestphotodoc'


class Ceactionrequeststatus(models.Model):
    statusid = models.IntegerField()
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    icon_iconid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ceactionrequeststatus'


class Cecase(models.Model):
    caseid = models.AutoField()
    cecasepubliccc = models.IntegerField()
    property_propertyid = models.IntegerField()
    propertyunit_unitid = models.IntegerField(blank=True, null=True)
    login_userid = models.IntegerField(blank=True, null=True)
    casename = models.TextField(blank=True, null=True)
    originationdate = models.DateTimeField(blank=True, null=True)
    closingdate = models.DateTimeField(blank=True, null=True)
    creationtimestamp = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    paccenabled = models.BooleanField(blank=True, null=True)
    allowuplinkaccess = models.BooleanField(blank=True, null=True)
    propertyinfocase = models.BooleanField(blank=True, null=True)
    personinfocase_personid = models.IntegerField(blank=True, null=True)
    bobsource_sourceid = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    lastupdatedby_userid = models.IntegerField(blank=True, null=True)
    lastupdatedts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cecase'


class Cecasephasechangerule(models.Model):
    ruleid = models.AutoField()
    title = models.TextField(blank=True, null=True)
    targetcasephase = models.TextField(blank=True, null=True)  # This field type is a guess.
    requiredcurrentcasephase = models.TextField(blank=True, null=True)  # This field type is a guess.
    forbiddencurrentcasephase = models.TextField(blank=True, null=True)  # This field type is a guess.
    requiredextanteventtype = models.TextField(blank=True, null=True)  # This field type is a guess.
    forbiddenextanteventtype = models.TextField(blank=True, null=True)  # This field type is a guess.
    requiredextanteventcat = models.IntegerField(blank=True, null=True)
    forbiddenextanteventcat = models.IntegerField(blank=True, null=True)
    triggeredeventcat = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    mandatory = models.BooleanField(blank=True, null=True)
    treatreqphaseasthreshold = models.BooleanField(blank=True, null=True)
    treatforbidphaseasthreshold = models.BooleanField(blank=True, null=True)
    rejectrulehostifrulefails = models.BooleanField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    triggeredeventcatreqcat = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cecasephasechangerule'


class Cecasestatusicon(models.Model):
    iconid = models.IntegerField()
    status = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'cecasestatusicon'


class Choice(models.Model):
    choiceid = models.AutoField()
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    eventcat_catid = models.IntegerField(blank=True, null=True)
    addeventcat = models.BooleanField(blank=True, null=True)
    eventrule_ruleid = models.IntegerField(blank=True, null=True)
    addeventrule = models.BooleanField(blank=True, null=True)
    relativeorder = models.IntegerField()
    active = models.BooleanField(blank=True, null=True)
    minimumrequireduserranktoview = models.IntegerField(blank=True, null=True)
    minimumrequireduserranktochoose = models.IntegerField(blank=True, null=True)
    icon_iconid = models.IntegerField(blank=True, null=True)
    worflowpagetriggerconstantvar = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'choice'


class Choicedirective(models.Model):
    directiveid = models.AutoField()
    title = models.TextField(blank=True, null=True)
    overalldescription = models.TextField(blank=True, null=True)
    creator_userid = models.IntegerField(blank=True, null=True)
    directtodefaultmuniceo = models.BooleanField(blank=True, null=True)
    directtodefaultmunistaffer = models.BooleanField(blank=True, null=True)
    directtodeveloper = models.BooleanField(blank=True, null=True)
    executechoiceiflonewolf = models.BooleanField(blank=True, null=True)
    applytoclosedentities = models.BooleanField(blank=True, null=True)
    instantiatemultiple = models.BooleanField(blank=True, null=True)
    inactivategeneventoneval = models.BooleanField(blank=True, null=True)
    maintainreldatewindow = models.BooleanField(blank=True, null=True)
    autoinactivateonbobclose = models.BooleanField(blank=True, null=True)
    autoinactiveongeneventinactivation = models.BooleanField(blank=True, null=True)
    minimumrequireduserranktoview = models.IntegerField(blank=True, null=True)
    minimumrequireduserranktoevaluate = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    icon_iconid = models.IntegerField(blank=True, null=True)
    directtomunisysadmin = models.BooleanField(blank=True, null=True)
    requiredevaluationforbobclose = models.BooleanField(blank=True, null=True)
    forcehideprecedingproposals = models.BooleanField(blank=True, null=True)
    forcehidetrailingproposals = models.BooleanField(blank=True, null=True)
    refusetobehidden = models.BooleanField(blank=True, null=True)
    relativeorder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'choicedirective'


class Choicedirectivechoice(models.Model):
    choice_choiceid = models.IntegerField()
    directive_directiveid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'choicedirectivechoice'


class Choicedirectivedirectiveset(models.Model):
    directiveset_setid = models.IntegerField()
    directive_dirid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'choicedirectivedirectiveset'


class Choicedirectiveset(models.Model):
    directivesetid = models.AutoField()
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'choicedirectiveset'


class Choiceproposal(models.Model):
    proposalid = models.AutoField()
    directive_directiveid = models.IntegerField(blank=True, null=True)
    generatingevent_eventid = models.IntegerField(blank=True, null=True)
    initiator_userid = models.IntegerField(blank=True, null=True)
    responderintended_userid = models.IntegerField(blank=True, null=True)
    activateson = models.DateTimeField(blank=True, null=True)
    expireson = models.DateTimeField(blank=True, null=True)
    responderactual_userid = models.IntegerField(blank=True, null=True)
    rejectproposal = models.BooleanField(blank=True, null=True)
    responsetimestamp = models.DateTimeField(blank=True, null=True)
    responseevent_eventid = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    relativeorder = models.IntegerField(blank=True, null=True)
    occperiod_periodid = models.IntegerField(blank=True, null=True)
    cecase_caseid = models.IntegerField(blank=True, null=True)
    chosen_choiceid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'choiceproposal'


class Citation(models.Model):
    citationid = models.AutoField()
    citationno = models.TextField(blank=True, null=True)
    status_statusid = models.IntegerField()
    origin_courtentity_entityid = models.IntegerField()
    login_userid = models.IntegerField()
    dateofrecord = models.DateTimeField()
    transtimestamp = models.DateTimeField()
    isactive = models.BooleanField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    officialtext = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citation'


class Citationperson(models.Model):
    citation_citationid = models.IntegerField()
    person_personid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'citationperson'


class Citationstatus(models.Model):
    statusid = models.AutoField()
    statusname = models.TextField()
    description = models.TextField()
    icon_iconid = models.IntegerField(blank=True, null=True)
    editsforbidden = models.BooleanField(blank=True, null=True)
    eventrule_ruleid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citationstatus'


class Citationviolation(models.Model):
    citationviolationid = models.AutoField()
    citation_citationid = models.IntegerField()
    codeviolation_violationid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'citationviolation'


class Codeelement(models.Model):
    elementid = models.AutoField()
    codesource_sourceid = models.IntegerField()
    ordchapterno = models.IntegerField()
    ordchaptertitle = models.TextField(blank=True, null=True)
    ordsecnum = models.TextField(blank=True, null=True)
    ordsectitle = models.TextField(blank=True, null=True)
    ordsubsecnum = models.TextField(blank=True, null=True)
    ordsubsectitle = models.TextField(blank=True, null=True)
    ordtechnicaltext = models.TextField()
    ordhumanfriendlytext = models.TextField(blank=True, null=True)
    resourceurl = models.TextField(blank=True, null=True)
    guideentryid = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    legacyid = models.IntegerField(blank=True, null=True)
    ordsubsubsecnum = models.TextField(blank=True, null=True)
    useinjectedvalues = models.BooleanField(blank=True, null=True)
    lastupdatedts = models.DateTimeField(blank=True, null=True)
    createdby_userid = models.IntegerField(blank=True, null=True)
    lastupdatedby_userid = models.IntegerField(blank=True, null=True)
    deactivatedts = models.DateTimeField(blank=True, null=True)
    deactivatedby_userid = models.IntegerField(blank=True, null=True)
    createdts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'codeelement'


class Codeelementguide(models.Model):
    guideentryid = models.AutoField()
    category = models.TextField()
    subcategory = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    enforcementguidelines = models.TextField(blank=True, null=True)
    inspectionguidelines = models.TextField(blank=True, null=True)
    priority = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'codeelementguide'


class Codeelementinjectedvalue(models.Model):
    injectedvalueid = models.AutoField()
    value = models.TextField()
    injectionorder = models.IntegerField(blank=True, null=True)
    codelement_eleid = models.IntegerField()
    codeset_codesetid = models.IntegerField()
    creationts = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'codeelementinjectedvalue'


class Codeset(models.Model):
    codesetid = models.AutoField()
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    municipality_municode = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'codeset'


class Codesetelement(models.Model):
    codesetelementid = models.AutoField()
    codeset_codesetid = models.IntegerField()
    codelement_elementid = models.IntegerField()
    elementmaxpenalty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    elementminpenalty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    elementnormpenalty = models.DecimalField(max_digits=65535, decimal_places=65535)
    penaltynotes = models.TextField(blank=True, null=True)
    normdaystocomply = models.IntegerField()
    daystocomplynotes = models.TextField(blank=True, null=True)
    munispecificnotes = models.TextField(blank=True, null=True)
    defaultseverityclass_classid = models.IntegerField(blank=True, null=True)
    fee_feeid = models.IntegerField(blank=True, null=True)
    defaultviolationdescription = models.TextField(blank=True, null=True)
    createdts = models.DateTimeField(blank=True, null=True)
    createdby_userid = models.IntegerField(blank=True, null=True)
    lastupdatedts = models.DateTimeField(blank=True, null=True)
    lastupdatedby_userid = models.IntegerField(blank=True, null=True)
    deactivatedts = models.DateTimeField(blank=True, null=True)
    deactivatedby_userid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'codesetelement'


class Codesource(models.Model):
    sourceid = models.AutoField()
    name = models.TextField()
    year = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    isactive = models.BooleanField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'codesource'


class Codeviolation(models.Model):
    violationid = models.AutoField()
    codesetelement_elementid = models.IntegerField()
    cecase_caseid = models.IntegerField()
    dateofrecord = models.DateTimeField(blank=True, null=True)
    entrytimestamp = models.DateTimeField()
    stipulatedcompliancedate = models.DateTimeField()
    actualcompliancedate = models.DateTimeField(blank=True, null=True)
    penalty = models.DecimalField(max_digits=65535, decimal_places=65535)
    description = models.TextField()
    notes = models.TextField(blank=True, null=True)
    legacyimport = models.BooleanField(blank=True, null=True)
    compliancetimestamp = models.DateTimeField(blank=True, null=True)
    complianceuser = models.IntegerField(blank=True, null=True)
    severity_classid = models.IntegerField(blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    compliancetfexpiry_proposalid = models.IntegerField(blank=True, null=True)
    lastupdatedts = models.DateTimeField(blank=True, null=True)
    lastupdated_userid = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    compliancenote = models.TextField(blank=True, null=True)
    nullifiedts = models.DateTimeField(blank=True, null=True)
    nullifiedby = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'codeviolation'


class Codeviolationphotodoc(models.Model):
    photodoc_photodocid = models.IntegerField()
    codeviolation_violationid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'codeviolationphotodoc'


class Contactemail(models.Model):
    emailid = models.AutoField()
    human_humanid = models.IntegerField()
    emailaddress = models.TextField()
    bouncets = models.DateTimeField(blank=True, null=True)
    createdts = models.DateTimeField(blank=True, null=True)
    createdby_userid = models.IntegerField(blank=True, null=True)
    lastupdatedts = models.DateTimeField(blank=True, null=True)
    lastupdatedby_userid = models.IntegerField(blank=True, null=True)
    deactivatedts = models.DateTimeField(blank=True, null=True)
    deactivatedby_userid = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contactemail'


class Contactphone(models.Model):
    phoneid = models.AutoField()
    human_humanid = models.IntegerField()
    phonenumber = models.TextField()
    phoneext = models.IntegerField(blank=True, null=True)
    phonetype_typeid = models.IntegerField(blank=True, null=True)
    disconnectts = models.DateTimeField(blank=True, null=True)
    disconnect_userid = models.IntegerField(blank=True, null=True)
    createdts = models.DateTimeField(blank=True, null=True)
    createdby_userid = models.IntegerField(blank=True, null=True)
    lastupdatedts = models.DateTimeField(blank=True, null=True)
    lastupdatedby_userid = models.IntegerField(blank=True, null=True)
    deactivatedts = models.DateTimeField(blank=True, null=True)
    deactivatedby_userid = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contactphone'


class Contactphonetype(models.Model):
    phonetypeid = models.AutoField()
    title = models.TextField(blank=True, null=True)
    createdts = models.DateTimeField(blank=True, null=True)
    deactivatedts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contactphonetype'


class Courtentity(models.Model):
    entityid = models.AutoField()
    entityofficialnum = models.TextField(blank=True, null=True)
    jurisdictionlevel = models.TextField()
    name = models.TextField()
    address_street = models.TextField()
    address_city = models.TextField()
    address_zip = models.TextField()
    address_state = models.TextField()
    county = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    judgename = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courtentity'


class Dbpatch(models.Model):
    patchnum = models.IntegerField()
    patchfilename = models.TextField(blank=True, null=True)
    datepublished = models.DateTimeField(blank=True, null=True)
    patchauthor = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbpatch'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Event(models.Model):
    eventid = models.AutoField()
    category_catid = models.IntegerField()
    cecase_caseid = models.IntegerField()
    creationts = models.DateTimeField(blank=True, null=True)
    eventdescription = models.TextField(blank=True, null=True)
    creator_userid = models.IntegerField()
    active = models.BooleanField(blank=True, null=True)
    requiresviewconfirmation = models.BooleanField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    requestedevent_eventid = models.IntegerField(blank=True, null=True)
    directrequesttodefaultmuniceo = models.BooleanField(blank=True, null=True)
    occperiod_periodid = models.IntegerField(blank=True, null=True)
    timestart = models.DateTimeField(blank=True, null=True)
    timeend = models.DateTimeField(blank=True, null=True)
    lastupdatedby_userid = models.IntegerField(blank=True, null=True)
    lastupdatedts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event'


class Eventcategory(models.Model):
    categoryid = models.AutoField()
    categorytype = models.TextField()  # This field type is a guess.
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    notifymonitors = models.BooleanField(blank=True, null=True)
    hidable = models.BooleanField(blank=True, null=True)
    icon_iconid = models.IntegerField(blank=True, null=True)
    requestable = models.BooleanField(blank=True, null=True)
    eventrule_ruleid = models.IntegerField(blank=True, null=True)
    relativeorderwithintype = models.IntegerField(blank=True, null=True)
    relativeorderglobal = models.IntegerField(blank=True, null=True)
    hosteventdescriptionsuggtext = models.TextField(blank=True, null=True)
    directive_directiveid = models.IntegerField(blank=True, null=True)
    defaultdurationmins = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    userrankminimumtoenact = models.IntegerField(blank=True, null=True)
    userrankminimumtoview = models.IntegerField(blank=True, null=True)
    userrankminimumtoupdate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eventcategory'


class Eventperson(models.Model):
    ceevent_eventid = models.IntegerField()
    person_personid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eventperson'


class Eventrule(models.Model):
    ruleid = models.AutoField()
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    requiredeventtype = models.TextField(blank=True, null=True)  # This field type is a guess.
    forbiddeneventtype = models.TextField(blank=True, null=True)  # This field type is a guess.
    requiredeventcat_catid = models.IntegerField(blank=True, null=True)
    requiredeventcatupperboundtypeintorder = models.BooleanField(blank=True, null=True)
    requiredeventcatupperboundglobalorder = models.BooleanField(blank=True, null=True)
    forbiddeneventcat_catid = models.IntegerField(blank=True, null=True)
    forbiddeneventcatupperboundtypeintorder = models.BooleanField(blank=True, null=True)
    forbiddeneventcatupperboundglobalorder = models.BooleanField(blank=True, null=True)
    mandatorypassreqtocloseentity = models.BooleanField(blank=True, null=True)
    autoremoveonentityclose = models.BooleanField(blank=True, null=True)
    triggeredeventcatonpass = models.IntegerField(blank=True, null=True)
    triggeredeventcatonfail = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    requiredeventcatthresholdtypeintorder = models.IntegerField(blank=True, null=True)
    forbiddeneventcatthresholdtypeintorder = models.IntegerField(blank=True, null=True)
    requiredeventcatthresholdglobalorder = models.IntegerField(blank=True, null=True)
    forbiddeneventcatthresholdglobalorder = models.IntegerField(blank=True, null=True)
    promptingdirective_directiveid = models.IntegerField(blank=True, null=True)
    userrankmintoconfigure = models.IntegerField(blank=True, null=True)
    userrankmintoimplement = models.IntegerField(blank=True, null=True)
    userrankmintowaive = models.IntegerField(blank=True, null=True)
    userrankmintooverride = models.IntegerField(blank=True, null=True)
    userrankmintodeactivate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eventrule'


class Eventruleimpl(models.Model):
    erimplid = models.AutoField()
    eventrule_ruleid = models.IntegerField()
    cecase_caseid = models.IntegerField(blank=True, null=True)
    occperiod_periodid = models.IntegerField(blank=True, null=True)
    implts = models.DateTimeField(blank=True, null=True)
    implby_userid = models.IntegerField(blank=True, null=True)
    lastevaluatedts = models.DateTimeField(blank=True, null=True)
    passedrulets = models.DateTimeField(blank=True, null=True)
    triggeredevent_eventid = models.IntegerField(blank=True, null=True)
    waivedts = models.DateTimeField(blank=True, null=True)
    waivedby_userid = models.IntegerField(blank=True, null=True)
    passoverridets = models.DateTimeField(blank=True, null=True)
    passoverrideby_userid = models.IntegerField(blank=True, null=True)
    deacts = models.DateTimeField(blank=True, null=True)
    deacby_userid = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eventruleimpl'


class Eventruleruleset(models.Model):
    ruleset_rulesetid = models.IntegerField()
    eventrule_ruleid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eventruleruleset'


class Eventruleset(models.Model):
    rulesetid = models.AutoField()
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eventruleset'


class Externalrealestateportal(models.Model):
    parcel = models.ForeignKey('Externalwprdc', models.DO_NOTHING, db_column='parcel')
    creationts = models.DateTimeField(blank=True, null=True)
    lastupdatedts = models.DateTimeField(blank=True, null=True)
    parcelid = models.TextField(blank=True, null=True)
    propertyaddress = models.TextField(blank=True, null=True)
    municipality = models.TextField(blank=True, null=True)
    ownername = models.TextField(blank=True, null=True)
    ownermailing = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'externalrealestateportal'


class Externalwprdc(models.Model):
    parcel = models.TextField(unique=True)
    creationts = models.DateTimeField(blank=True, null=True)
    lastupdatedts = models.DateTimeField(blank=True, null=True)
    parid = models.CharField(max_length=30, blank=True, null=True)
    propertyhousenum = models.CharField(max_length=10, blank=True, null=True)
    propertyfraction = models.CharField(max_length=6, blank=True, null=True)
    propertyaddress = models.CharField(max_length=80, blank=True, null=True)
    propertycity = models.CharField(max_length=50, blank=True, null=True)
    propertystate = models.CharField(max_length=50, blank=True, null=True)
    propertyunit = models.CharField(max_length=30, blank=True, null=True)
    propertyzip = models.CharField(max_length=10, blank=True, null=True)
    municode = models.CharField(max_length=5, blank=True, null=True)
    munidesc = models.CharField(max_length=50, blank=True, null=True)
    schoolcode = models.CharField(max_length=30, blank=True, null=True)
    schooldesc = models.CharField(max_length=50, blank=True, null=True)
    legal1 = models.CharField(max_length=60, blank=True, null=True)
    legal2 = models.CharField(max_length=60, blank=True, null=True)
    legal3 = models.CharField(max_length=60, blank=True, null=True)
    neighcode = models.CharField(max_length=8, blank=True, null=True)
    neighdesc = models.CharField(max_length=50, blank=True, null=True)
    taxcode = models.CharField(max_length=1, blank=True, null=True)
    taxdesc = models.CharField(max_length=50, blank=True, null=True)
    taxsubcode = models.CharField(max_length=1, blank=True, null=True)
    taxsubcode_desc = models.CharField(max_length=50, blank=True, null=True)
    ownercode = models.CharField(max_length=3, blank=True, null=True)
    ownerdesc = models.CharField(max_length=50, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=2, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    classdesc = models.CharField(max_length=50, blank=True, null=True)
    usecode = models.CharField(max_length=4, blank=True, null=True)
    usedesc = models.CharField(max_length=50, blank=True, null=True)
    lotarea = models.FloatField(blank=True, null=True)
    homesteadflag = models.CharField(max_length=6, blank=True, null=True)
    cleangreen = models.CharField(max_length=3, blank=True, null=True)
    farmsteadflag = models.CharField(max_length=6, blank=True, null=True)
    abatementflag = models.CharField(max_length=6, blank=True, null=True)
    recorddate = models.CharField(max_length=10, blank=True, null=True)
    saledate = models.CharField(max_length=10, blank=True, null=True)
    saleprice = models.FloatField(blank=True, null=True)
    salecode = models.CharField(max_length=2, blank=True, null=True)
    saledesc = models.CharField(max_length=50, blank=True, null=True)
    deedbook = models.CharField(max_length=8, blank=True, null=True)
    deedpage = models.CharField(max_length=8, blank=True, null=True)
    prevsaledate = models.CharField(max_length=10, blank=True, null=True)
    prevsaleprice = models.FloatField(blank=True, null=True)
    prevsaledate2 = models.CharField(max_length=10, blank=True, null=True)
    prevsaleprice2 = models.FloatField(blank=True, null=True)
    changenoticeaddress1 = models.CharField(max_length=100, blank=True, null=True)
    changenoticeaddress2 = models.CharField(max_length=100, blank=True, null=True)
    changenoticeaddress3 = models.CharField(max_length=100, blank=True, null=True)
    changenoticeaddress4 = models.CharField(max_length=100, blank=True, null=True)
    countybuilding = models.FloatField(blank=True, null=True)
    countyland = models.FloatField(blank=True, null=True)
    countytotal = models.FloatField(blank=True, null=True)
    countyexemptbldg = models.FloatField(blank=True, null=True)
    localbuilding = models.FloatField(blank=True, null=True)
    localland = models.FloatField(blank=True, null=True)
    localtotal = models.FloatField(blank=True, null=True)
    fairmarketbuilding = models.FloatField(blank=True, null=True)
    fairmarketland = models.FloatField(blank=True, null=True)
    fairmarkettotal = models.FloatField(blank=True, null=True)
    style = models.CharField(max_length=2, blank=True, null=True)
    styledesc = models.CharField(max_length=50, blank=True, null=True)
    stories = models.CharField(max_length=3, blank=True, null=True)
    yearblt = models.FloatField(blank=True, null=True)
    exteriorfinish = models.CharField(max_length=2, blank=True, null=True)
    extfinish_desc = models.CharField(max_length=50, blank=True, null=True)
    roof = models.CharField(max_length=20, blank=True, null=True)
    roofdesc = models.CharField(max_length=50, blank=True, null=True)
    basement = models.CharField(max_length=1, blank=True, null=True)
    basementdesc = models.CharField(max_length=50, blank=True, null=True)
    grade = models.CharField(max_length=3, blank=True, null=True)
    gradedesc = models.CharField(max_length=50, blank=True, null=True)
    condition = models.CharField(max_length=2, blank=True, null=True)
    conditiondesc = models.CharField(max_length=50, blank=True, null=True)
    cdu = models.CharField(max_length=2, blank=True, null=True)
    cdudesc = models.CharField(max_length=50, blank=True, null=True)
    totalrooms = models.FloatField(blank=True, null=True)
    bedrooms = models.FloatField(blank=True, null=True)
    fullbaths = models.FloatField(blank=True, null=True)
    halfbaths = models.FloatField(blank=True, null=True)
    heatingcooling = models.CharField(max_length=1, blank=True, null=True)
    heatingcoolingdesc = models.CharField(max_length=50, blank=True, null=True)
    fireplaces = models.FloatField(blank=True, null=True)
    bsmtgarage = models.CharField(max_length=1, blank=True, null=True)
    finishedlivingarea = models.FloatField(blank=True, null=True)
    cardnumber = models.FloatField(blank=True, null=True)
    alt_id = models.CharField(max_length=30, blank=True, null=True)
    taxyear = models.FloatField(blank=True, null=True)
    asofdate = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'externalwprdc'


class Human(models.Model):
    humanid = models.AutoField()
    name = models.TextField()
    dob = models.DateField(blank=True, null=True)
    under18 = models.BooleanField(blank=True, null=True)
    jobtitle = models.TextField(blank=True, null=True)
    businessentity = models.BooleanField(blank=True, null=True)
    multihuman = models.BooleanField(blank=True, null=True)
    source_sourceid = models.IntegerField(blank=True, null=True)
    activationstartdate = models.DateField(blank=True, null=True)
    activationstartnotes = models.TextField(blank=True, null=True)
    activationstopdate = models.DateField(blank=True, null=True)
    activationstopnotes = models.TextField(blank=True, null=True)
    deceaseddate = models.DateField(blank=True, null=True)
    deceasedby_userid = models.IntegerField(blank=True, null=True)
    cloneof_humanid = models.IntegerField(blank=True, null=True)
    createdts = models.DateTimeField(blank=True, null=True)
    createdby_userid = models.IntegerField(blank=True, null=True)
    lastupdatedts = models.DateTimeField(blank=True, null=True)
    lastupdatedby_userid = models.IntegerField(blank=True, null=True)
    deactivatedts = models.DateTimeField(blank=True, null=True)
    deactivatedby_userid = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'human'


class Humanmailingaddress(models.Model):
    humanmailing_humanid = models.IntegerField(blank=True, null=True)
    humanmailing_addressid = models.IntegerField(blank=True, null=True)
    role_humanmailingroleid = models.IntegerField(blank=True, null=True)
    source_sourceid = models.IntegerField(blank=True, null=True)
    createdts = models.DateTimeField(blank=True, null=True)
    createdby_userid = models.IntegerField(blank=True, null=True)
    deactivatedts = models.DateTimeField(blank=True, null=True)
    deactivatedby_userid = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'humanmailingaddress'


class Humanmailingrole(models.Model):
    roleid = models.AutoField()
    title = models.TextField()
    createdts = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    muni_municode = models.IntegerField(blank=True, null=True)
    deactivatedts = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'humanmailingrole'


class Icon(models.Model):
    iconid = models.AutoField()
    name = models.TextField(blank=True, null=True)
    styleclass = models.TextField(blank=True, null=True)
    fontawesome = models.TextField(blank=True, null=True)
    materialicons = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icon'


class Improvementstatus(models.Model):
    statusid = models.IntegerField()
    statustitle = models.TextField(blank=True, null=True)
    statusdescription = models.TextField(blank=True, null=True)
    icon_iconid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'improvementstatus'


class Improvementsuggestion(models.Model):
    improvementid = models.AutoField()
    improvementtypeid = models.IntegerField()
    improvementsuggestiontext = models.TextField()
    improvementreply = models.TextField(blank=True, null=True)
    statusid = models.IntegerField()
    submitterid = models.IntegerField()
    submissiontimestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'improvementsuggestion'


class Improvementtype(models.Model):
    typeid = models.IntegerField()
    typetitle = models.TextField(blank=True, null=True)
    typedescription = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'improvementtype'


class Intensityclass(models.Model):
    classid = models.AutoField()
    title = models.TextField(blank=True, null=True)
    muni_municode = models.IntegerField(blank=True, null=True)
    numericrating = models.IntegerField(blank=True, null=True)
    schemaname = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    icon_iconid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intensityclass'


class Listchangerequest(models.Model):
    changeid = models.AutoField()
    changetext = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'listchangerequest'


class Log(models.Model):
    logentryid = models.AutoField()
    timeofentry = models.DateTimeField(blank=True, null=True)
    user_userid = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    error = models.BooleanField(blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)
    credsig = models.TextField(blank=True, null=True)
    subsys = models.TextField(blank=True, null=True)
    severity = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log'


class Logcategory(models.Model):
    catid = models.IntegerField()
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logcategory'


class Login(models.Model):
    userid = models.AutoField()
    username = models.TextField()
    password = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    personlink = models.IntegerField(blank=True, null=True)
    pswdlastupdated = models.DateTimeField(blank=True, null=True)
    forcepasswordreset = models.DateTimeField(blank=True, null=True)
    createdby = models.IntegerField(blank=True, null=True)
    createdts = models.DateTimeField(blank=True, null=True)
    nologinvirtualonly = models.BooleanField(blank=True, null=True)
    deactivatedts = models.DateTimeField(blank=True, null=True)
    deactivated_userid = models.IntegerField(blank=True, null=True)
    userrole = models.TextField(blank=True, null=True)  # This field type is a guess.
    lastupdatedts = models.DateTimeField(blank=True, null=True)
    homemuni = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login'


class Loginmuniauthperiod(models.Model):
    muniauthperiodid = models.AutoField()
    muni_municode = models.IntegerField()
    authuser_userid = models.IntegerField()
    accessgranteddatestart = models.DateTimeField()
    accessgranteddatestop = models.DateTimeField()
    recorddeactivatedts = models.DateTimeField(blank=True, null=True)
    authorizedrole = models.TextField(blank=True, null=True)  # This field type is a guess.
    createdts = models.DateTimeField(blank=True, null=True)
    createdby_userid = models.IntegerField()
    notes = models.TextField(blank=True, null=True)
    supportassignedby = models.IntegerField(blank=True, null=True)
    assignmentrank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loginmuniauthperiod'


class Loginmuniauthperiodlog(models.Model):
    authperiodlogentryid = models.AutoField()
    authperiod_periodid = models.IntegerField()
    category = models.TextField(blank=True, null=True)
    entryts = models.DateTimeField(blank=True, null=True)
    entrydateofrecord = models.DateTimeField(blank=True, null=True)
    disputedby_userid = models.IntegerField(blank=True, null=True)
    disputedts = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    cookie_jsessionid = models.TextField(blank=True, null=True)
    header_remoteaddr = models.TextField(blank=True, null=True)
    header_useragent = models.TextField(blank=True, null=True)
    header_dateraw = models.TextField(blank=True, null=True)
    header_date = models.DateTimeField(blank=True, null=True)
    header_cachectl = models.TextField(blank=True, null=True)
    audit_usersession_userid = models.IntegerField()
    audit_usercredential_userid = models.IntegerField()
    audit_muni_municode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'loginmuniauthperiodlog'


class Loginobjecthistory(models.Model):
    historyentryid = models.AutoField()
    login_userid = models.IntegerField(blank=True, null=True)
    person_personid = models.IntegerField(blank=True, null=True)
    property_propertyid = models.IntegerField(blank=True, null=True)
    ceactionrequest_requestid = models.IntegerField(blank=True, null=True)
    cecase_caseid = models.IntegerField(blank=True, null=True)
    ceevent_eventid = models.IntegerField(blank=True, null=True)
    occapp_appid = models.IntegerField(blank=True, null=True)
    occpermit_permitid = models.IntegerField(blank=True, null=True)
    entrytimestamp = models.DateTimeField()
    occperiod_periodid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loginobjecthistory'


class Mailingaddress(models.Model):
    addressid = models.AutoField()
    addressnum = models.TextField(blank=True, null=True)
    street = models.TextField(blank=True, null=True)
    unitno = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    zipcode = models.TextField(blank=True, null=True)
    pobox = models.IntegerField(blank=True, null=True)
    verifiedts = models.DateTimeField(blank=True, null=True)
    source_sourceid = models.IntegerField(blank=True, null=True)
    createdts = models.DateTimeField(blank=True, null=True)
    createdby_userid = models.IntegerField(blank=True, null=True)
    lastupdatedts = models.DateTimeField(blank=True, null=True)
    lastupdatedby_userid = models.IntegerField(blank=True, null=True)
    deactivatedts = models.DateTimeField(blank=True, null=True)
    deactivatedby_userid = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    addressfraction = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mailingaddress'


class Moneycecasefeeassigned(models.Model):
    cecaseassignedfeeid = models.AutoField()
    moneyfeeassigned_assignedid = models.IntegerField()
    cecase_caseid = models.IntegerField()
    assignedby_userid = models.IntegerField(blank=True, null=True)
    assignedbyts = models.DateTimeField(blank=True, null=True)
    waivedby_userid = models.IntegerField(blank=True, null=True)
    lastmodifiedts = models.DateTimeField(blank=True, null=True)
    reduceby = models.TextField(blank=True, null=True)  # This field type is a guess.
    reduceby_userid = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    fee_feeid = models.IntegerField()
    codesetelement_elementid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'moneycecasefeeassigned'


class Moneycecasefeepayment(models.Model):
    payment_paymentid = models.IntegerField()
    cecaseassignedfee_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'moneycecasefeepayment'


class Moneycodesetelementfee(models.Model):
    fee_feeid = models.IntegerField()
    codesetelement_elementid = models.IntegerField()
    active = models.BooleanField(blank=True, null=True)
    autoassign = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moneycodesetelementfee'


class Moneyfee(models.Model):
    feeid = models.AutoField()
    muni_municode = models.IntegerField()
    feename = models.TextField()
    feeamount = models.TextField()  # This field type is a guess.
    effectivedate = models.DateTimeField()
    expirydate = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moneyfee'


class Moneyoccperiodfeeassigned(models.Model):
    moneyoccperassignedfeeid = models.AutoField()
    moneyfeeassigned_assignedid = models.IntegerField()
    occperiod_periodid = models.IntegerField()
    assignedby_userid = models.IntegerField(blank=True, null=True)
    assignedbyts = models.DateTimeField(blank=True, null=True)
    waivedby_userid = models.IntegerField(blank=True, null=True)
    lastmodifiedts = models.DateTimeField(blank=True, null=True)
    reduceby = models.TextField(blank=True, null=True)  # This field type is a guess.
    reduceby_userid = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    fee_feeid = models.IntegerField()
    occperiodtype_typeid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'moneyoccperiodfeeassigned'


class Moneyoccperiodfeepayment(models.Model):
    payment_paymentid = models.IntegerField()
    occperiodassignedfee_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'moneyoccperiodfeepayment'


class Moneyoccperiodtypefee(models.Model):
    fee_feeid = models.IntegerField()
    occperiodtype_typeid = models.IntegerField()
    active = models.BooleanField(blank=True, null=True)
    autoassign = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moneyoccperiodtypefee'


class Moneypayment(models.Model):
    paymentid = models.AutoField()
    occinspec_inspectionid = models.IntegerField()
    paymenttype_typeid = models.IntegerField()
    datereceived = models.DateTimeField()
    datedeposited = models.DateTimeField()
    amount = models.TextField()  # This field type is a guess.
    payer_personid = models.IntegerField()
    referencenum = models.TextField(blank=True, null=True)
    checkno = models.IntegerField(blank=True, null=True)
    cleared = models.BooleanField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    recordedby_userid = models.IntegerField(blank=True, null=True)
    entrytimestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'moneypayment'


class Moneypaymenttype(models.Model):
    typeid = models.AutoField()
    pmttypetitle = models.TextField()

    class Meta:
        managed = False
        db_table = 'moneypaymenttype'


class Municipality(models.Model):
    municode = models.IntegerField(unique=True)
    muniname = models.TextField()
    address_street = models.TextField(blank=True, null=True)
    address_city = models.TextField(blank=True, null=True)
    address_state = models.TextField(blank=True, null=True)
    address_zip = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    fax = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)
    activeinprogram = models.BooleanField(blank=True, null=True)
    defaultcodeset = models.IntegerField()
    occpermitissuingsource_sourceid = models.IntegerField()
    novprintstyle_styleid = models.IntegerField(blank=True, null=True)
    enablecodeenforcement = models.BooleanField(blank=True, null=True)
    enableoccupancy = models.BooleanField(blank=True, null=True)
    enablepublicceactionreqsub = models.BooleanField(blank=True, null=True)
    enablepublicceactionreqinfo = models.BooleanField(blank=True, null=True)
    enablepublicoccpermitapp = models.BooleanField(blank=True, null=True)
    enablepublicoccinspectodo = models.BooleanField(blank=True, null=True)
    munimanager_userid = models.IntegerField(blank=True, null=True)
    office_propertyid = models.IntegerField(blank=True, null=True)
    profile_profileid = models.IntegerField(blank=True, null=True)
    primarystaffcontact_userid = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    lastupdatedts = models.DateTimeField(blank=True, null=True)
    lastupdated_userid = models.IntegerField(blank=True, null=True)
    defaultoccperiod = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municipality'


class Municourtentity(models.Model):
    muni_municode = models.IntegerField()
    courtentity_entityid = models.IntegerField()
    relativeorder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municourtentity'


class Munilogin(models.Model):
    muni_municode = models.IntegerField()
    userid = models.IntegerField()
    defaultmuni = models.BooleanField(blank=True, null=True)
    accessgranteddatestart = models.DateTimeField()
    accessgranteddatestop = models.DateTimeField()
    codeofficerstartdate = models.DateTimeField(blank=True, null=True)
    codeofficerstopdate = models.DateTimeField(blank=True, null=True)
    staffstartdate = models.DateTimeField(blank=True, null=True)
    staffstopdate = models.DateTimeField(blank=True, null=True)
    sysadminstartdate = models.DateTimeField(blank=True, null=True)
    sysadminstopdate = models.DateTimeField(blank=True, null=True)
    supportstartdate = models.DateTimeField(blank=True, null=True)
    supportstopdate = models.DateTimeField(blank=True, null=True)
    codeofficerassignmentorder = models.IntegerField(blank=True, null=True)
    staffassignmentorder = models.IntegerField(blank=True, null=True)
    sysadminassignmentorder = models.IntegerField(blank=True, null=True)
    supportassignmentorder = models.IntegerField(blank=True, null=True)
    bypasscodeofficerassignmentorder = models.IntegerField(blank=True, null=True)
    bypassstaffassignmentorder = models.IntegerField(blank=True, null=True)
    bypasssysadminassignmentorder = models.IntegerField(blank=True, null=True)
    bypasssupportassignmentorder = models.IntegerField(blank=True, null=True)
    recorddeactivatedts = models.DateTimeField(blank=True, null=True)
    userrole = models.TextField(blank=True, null=True)  # This field type is a guess.
    muniloginrecordid = models.AutoField()
    recordcreatedts = models.DateTimeField(blank=True, null=True)
    badgenumber = models.TextField(blank=True, null=True)
    orinumber = models.TextField(blank=True, null=True)
    defaultcecase_caseid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'munilogin'


class Muniphotodoc(models.Model):
    photodoc_photodocid = models.IntegerField()
    muni_municode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'muniphotodoc'


class Muniprofile(models.Model):
    profileid = models.AutoField()
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    lastupdatedts = models.DateTimeField(blank=True, null=True)
    lastupdatedby_userid = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    continuousoccupancybufferdays = models.IntegerField(blank=True, null=True)
    minimumuserranktodeclarerentalintent = models.IntegerField(blank=True, null=True)
    minimumuserrankforinspectionoverrides = models.IntegerField(blank=True, null=True)
    novfollowupdefaultdays = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'muniprofile'


class Muniprofileeventruleset(models.Model):
    muniprofile_profileid = models.IntegerField()
    ruleset_setid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'muniprofileeventruleset'


class Muniprofileoccperiodtype(models.Model):
    muniprofile_profileid = models.IntegerField()
    occperiodtype_typeid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'muniprofileoccperiodtype'


class Noticeofviolation(models.Model):
    noticeid = models.AutoField()
    caseid = models.IntegerField()
    lettertextbeforeviolations = models.TextField(blank=True, null=True)
    creationtimestamp = models.DateTimeField()
    dateofrecord = models.DateTimeField()
    sentdate = models.DateTimeField(blank=True, null=True)
    returneddate = models.DateTimeField(blank=True, null=True)
    personid_recipient = models.IntegerField()
    lettertextafterviolations = models.TextField(blank=True, null=True)
    lockedandqueuedformailingdate = models.DateTimeField(blank=True, null=True)
    lockedandqueuedformailingby = models.IntegerField(blank=True, null=True)
    sentby = models.IntegerField(blank=True, null=True)
    returnedby = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    creationby = models.IntegerField(blank=True, null=True)
    printstyle_styleid = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    injectviolations = models.BooleanField(blank=True, null=True)
    followupevent_eventid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'noticeofviolation'


class Noticeofviolationcodeviolation(models.Model):
    noticeofviolation_noticeid = models.IntegerField()
    codeviolation_violationid = models.IntegerField()
    includeordtext = models.BooleanField(blank=True, null=True)
    includehumanfriendlyordtext = models.BooleanField(blank=True, null=True)
    includeviolationphoto = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'noticeofviolationcodeviolation'


class Occchecklist(models.Model):
    checklistid = models.AutoField()
    title = models.TextField()
    description = models.TextField()
    muni_municode = models.IntegerField()
    active = models.BooleanField(blank=True, null=True)
    governingcodesource_sourceid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'occchecklist'


class Occchecklistspacetype(models.Model):
    checklistspacetypeid = models.AutoField()
    checklist_id = models.IntegerField()
    required = models.BooleanField(blank=True, null=True)
    spacetype_typeid = models.IntegerField()
    overridespacetyperequired = models.BooleanField(blank=True, null=True)
    overridespacetyperequiredvalue = models.BooleanField(blank=True, null=True)
    overridespacetyperequireallspaces = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'occchecklistspacetype'


class Occinspectedspace(models.Model):
    inspectedspaceid = models.AutoField()
    occspace_spaceid = models.IntegerField()
    occinspection_inspectionid = models.IntegerField()
    occlocationdescription_descid = models.IntegerField()
    addedtochecklistby_userid = models.IntegerField()
    addedtochecklistts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'occinspectedspace'


class Occinspectedspaceelement(models.Model):
    inspectedspaceelementid = models.AutoField()
    notes = models.TextField(blank=True, null=True)
    locationdescription_id = models.IntegerField(blank=True, null=True)
    lastinspectedby_userid = models.IntegerField(blank=True, null=True)
    lastinspectedts = models.DateTimeField(blank=True, null=True)
    compliancegrantedby_userid = models.IntegerField(blank=True, null=True)
    compliancegrantedts = models.DateTimeField(blank=True, null=True)
    inspectedspace_inspectedspaceid = models.IntegerField()
    overriderequiredflagnotinspected_userid = models.IntegerField(blank=True, null=True)
    spaceelement_elementid = models.IntegerField()
    required = models.BooleanField(blank=True, null=True)
    failureseverity_intensityclassid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'occinspectedspaceelement'


class Occinspectedspaceelementphotodoc(models.Model):
    photodoc_photodocid = models.IntegerField()
    inspectedspaceelement_elementid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'occinspectedspaceelementphotodoc'


class Occinspection(models.Model):
    inspectionid = models.AutoField()
    occperiod_periodid = models.IntegerField()
    inspector_userid = models.IntegerField()
    passedinspection_userid = models.IntegerField(blank=True, null=True)
    maxoccupantsallowed = models.IntegerField()
    publicaccesscc = models.IntegerField(blank=True, null=True)
    enablepacc = models.BooleanField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    thirdpartyinspector_personid = models.IntegerField(blank=True, null=True)
    thirdpartyinspectorapprovalts = models.DateTimeField(blank=True, null=True)
    thirdpartyinspectorapprovalby = models.IntegerField(blank=True, null=True)
    numbedrooms = models.IntegerField(blank=True, null=True)
    numbathrooms = models.IntegerField(blank=True, null=True)
    passedinspectionts = models.DateTimeField(blank=True, null=True)
    occchecklist_checklistlistid = models.IntegerField(blank=True, null=True)
    effectivedate = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    creationts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'occinspection'


class Occlocationdescriptor(models.Model):
    locationdescriptionid = models.AutoField()
    description = models.TextField(blank=True, null=True)
    buildingfloorno = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'occlocationdescriptor'


class Occperiod(models.Model):
    periodid = models.AutoField()
    source_sourceid = models.IntegerField()
    propertyunit_unitid = models.IntegerField(blank=True, null=True)
    createdts = models.DateTimeField(blank=True, null=True)
    type_typeid = models.IntegerField()
    typecertifiedby_userid = models.IntegerField(blank=True, null=True)
    typecertifiedts = models.DateTimeField(blank=True, null=True)
    startdate = models.DateTimeField(blank=True, null=True)
    startdatecertifiedby_userid = models.IntegerField(blank=True, null=True)
    startdatecertifiedts = models.DateTimeField(blank=True, null=True)
    enddate = models.DateTimeField(blank=True, null=True)
    enddatecertifiedby_userid = models.IntegerField(blank=True, null=True)
    enddatecterifiedts = models.DateTimeField(blank=True, null=True)
    manager_userid = models.IntegerField(blank=True, null=True)
    authorizationts = models.DateTimeField(blank=True, null=True)
    authorizedby_userid = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    createdby_userid = models.IntegerField()
    overrideperiodtypeconfig = models.BooleanField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'occperiod'


class Occperiodeventrule(models.Model):
    occperiod_periodid = models.IntegerField()
    eventrule_ruleid = models.IntegerField()
    attachedts = models.DateTimeField(blank=True, null=True)
    attachedby_userid = models.IntegerField(blank=True, null=True)
    lastevaluatedts = models.DateTimeField(blank=True, null=True)
    passedrulets = models.DateTimeField(blank=True, null=True)
    passedrule_eventid = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'occperiodeventrule'


class Occperiodpermitapplication(models.Model):
    occperiod_periodid = models.IntegerField()
    occpermitapp_applicationid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'occperiodpermitapplication'


class Occperiodperson(models.Model):
    period_periodid = models.IntegerField()
    person_personid = models.IntegerField()
    applicant = models.BooleanField(blank=True, null=True)
    preferredcontact = models.BooleanField(blank=True, null=True)
    applicationpersontype = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'occperiodperson'


class Occperiodphotodoc(models.Model):
    photodoc_photodocid = models.IntegerField()
    occperiod_periodid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'occperiodphotodoc'


class Occperiodtype(models.Model):
    typeid = models.AutoField()
    muni_municode = models.IntegerField()
    title = models.TextField()
    authorizeduses = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    userassignable = models.BooleanField(blank=True, null=True)
    permittable = models.BooleanField(blank=True, null=True)
    startdaterequired = models.BooleanField(blank=True, null=True)
    enddaterequired = models.BooleanField(blank=True, null=True)
    passedinspectionrequired = models.BooleanField(blank=True, null=True)
    rentalcompatible = models.BooleanField(blank=True, null=True)
    commercial = models.BooleanField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    allowthirdpartyinspection = models.BooleanField(blank=True, null=True)
    requiredpersontypes = models.TextField(blank=True, null=True)  # This field type is a guess.
    optionalpersontypes = models.TextField(blank=True, null=True)  # This field type is a guess.
    requirepersontypeentrycheck = models.BooleanField(blank=True, null=True)
    defaultpermitvalidityperioddays = models.IntegerField(blank=True, null=True)
    occchecklist_checklistlistid = models.IntegerField(blank=True, null=True)
    asynchronousinspectionvalidityperiod = models.BooleanField(blank=True, null=True)
    defaultinspectionvalidityperiod = models.IntegerField(blank=True, null=True)
    eventruleset_setid = models.IntegerField(blank=True, null=True)
    inspectable = models.BooleanField(blank=True, null=True)
    permittitle = models.TextField(blank=True, null=True)
    permittitlesub = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'occperiodtype'


class Occpermit(models.Model):
    permitid = models.AutoField()
    occperiod_periodid = models.IntegerField()
    referenceno = models.TextField(blank=True, null=True)
    issuedto_personid = models.IntegerField()
    issuedby_userid = models.IntegerField(blank=True, null=True)
    dateissued = models.DateTimeField()
    permitadditionaltext = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'occpermit'


class Occpermitapplication(models.Model):
    applicationid = models.AutoField()
    reason_reasonid = models.IntegerField()
    submissiontimestamp = models.DateTimeField()
    submitternotes = models.TextField(blank=True, null=True)
    internalnotes = models.TextField(blank=True, null=True)
    propertyunitid = models.TextField(blank=True, null=True)
    declaredtotaladults = models.IntegerField(blank=True, null=True)
    declaredtotalyouth = models.IntegerField(blank=True, null=True)
    occperiod_periodid = models.IntegerField(blank=True, null=True)
    rentalintent = models.BooleanField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)  # This field type is a guess.
    externalnotes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'occpermitapplication'


class Occpermitapplicationperson(models.Model):
    occpermitapplication_applicationid = models.IntegerField()
    person_personid = models.IntegerField()
    applicant = models.BooleanField(blank=True, null=True)
    preferredcontact = models.BooleanField(blank=True, null=True)
    applicationpersontype = models.TextField()  # This field type is a guess.
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'occpermitapplicationperson'


class Occpermitapplicationreason(models.Model):
    reasonid = models.AutoField()
    reasontitle = models.TextField()
    reasondescription = models.TextField()
    activereason = models.BooleanField(blank=True, null=True)
    requiredpersontypes = models.TextField(blank=True, null=True)  # This field type is a guess.
    optionalpersontypes = models.TextField(blank=True, null=True)  # This field type is a guess.
    humanfriendlydescription = models.TextField(blank=True, null=True)
    periodtypeproposal_periodid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'occpermitapplicationreason'


class Occspace(models.Model):
    spaceid = models.AutoField()
    name = models.TextField()
    spacetype_id = models.IntegerField()
    required = models.BooleanField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'occspace'


class Occspaceelement(models.Model):
    spaceelementid = models.AutoField()
    space_id = models.IntegerField()
    codeelement_id = models.IntegerField(blank=True, null=True)
    required = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'occspaceelement'


class Occspacetype(models.Model):
    spacetypeid = models.AutoField()
    spacetitle = models.TextField()
    description = models.TextField()
    required = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'occspacetype'


class Parcel(models.Model):
    parcelkey = models.AutoField(unique=True)
    parcelidcnty = models.TextField(blank=True, null=True)
    source_sourceid = models.IntegerField(blank=True, null=True)
    createdts = models.DateTimeField(blank=True, null=True)
    createdby_userid = models.IntegerField(blank=True, null=True)
    lastupdatedts = models.DateTimeField(blank=True, null=True)
    lastupdatedby_userid = models.IntegerField(blank=True, null=True)
    deactivatedts = models.DateTimeField(blank=True, null=True)
    deactivatedby_userid = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    muni_municode = models.ForeignKey(Municipality, models.DO_NOTHING, db_column='muni_municode')

    class Meta:
        managed = False
        db_table = 'parcel'


class Parcelhuman(models.Model):
    human_humanid = models.IntegerField(blank=True, null=True)
    parcel_parcelkey = models.IntegerField(blank=True, null=True)
    source_sourceid = models.IntegerField(blank=True, null=True)
    role_roleid = models.IntegerField(blank=True, null=True)
    createdts = models.DateTimeField(blank=True, null=True)
    createdby_userid = models.IntegerField(blank=True, null=True)
    lastupdatedts = models.DateTimeField(blank=True, null=True)
    lastupdatedby_userid = models.IntegerField(blank=True, null=True)
    deactivatedts = models.DateTimeField(blank=True, null=True)
    deactivatedby_userid = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcelhuman'


class Parcelhumanrole(models.Model):
    roleid = models.AutoField()
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    muni_municode = models.IntegerField(blank=True, null=True)
    deactivatedts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcelhumanrole'


class Parcelmailingaddress(models.Model):
    mailingparcel_parcelid = models.IntegerField(blank=True, null=True)
    mailingparcel_mailingid = models.IntegerField(blank=True, null=True)
    source_sourceid = models.IntegerField(blank=True, null=True)
    createdts = models.DateTimeField(blank=True, null=True)
    deactivatedts = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcelmailingaddress'


class Parcelunit(models.Model):
    unitid = models.AutoField()
    unitnumber = models.TextField()
    parcel_parcelkey = models.IntegerField()
    rentalintentdatestart = models.DateTimeField(blank=True, null=True)
    rentalintentdatestop = models.DateTimeField(blank=True, null=True)
    rentalnotes = models.TextField(blank=True, null=True)
    condition_intensityclassid = models.IntegerField(blank=True, null=True)
    source_sourceid = models.IntegerField(blank=True, null=True)
    createdts = models.DateTimeField(blank=True, null=True)
    createdby_userid = models.IntegerField(blank=True, null=True)
    lastupdatedts = models.DateTimeField(blank=True, null=True)
    lastupdatedby_userid = models.IntegerField(blank=True, null=True)
    deactivatedts = models.DateTimeField(blank=True, null=True)
    deactivatedby_userid = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcelunit'


class Person(models.Model):
    personid = models.AutoField()
    persontype = models.TextField(blank=True, null=True)  # This field type is a guess.
    muni_municode = models.IntegerField()
    fname = models.TextField(blank=True, null=True)
    lname = models.TextField()
    jobtitle = models.TextField(blank=True, null=True)
    phonecell = models.TextField(blank=True, null=True)
    phonehome = models.TextField(blank=True, null=True)
    phonework = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    address_street = models.TextField(blank=True, null=True)
    address_city = models.TextField(blank=True, null=True)
    address_state = models.TextField(blank=True, null=True)
    address_zip = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    lastupdated = models.DateTimeField(blank=True, null=True)
    expirydate = models.DateTimeField(blank=True, null=True)
    isactive = models.BooleanField(blank=True, null=True)
    isunder18 = models.BooleanField(blank=True, null=True)
    humanverifiedby = models.IntegerField(blank=True, null=True)
    compositelname = models.BooleanField(blank=True, null=True)
    sourceid = models.IntegerField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    businessentity = models.BooleanField(blank=True, null=True)
    mailing_address_street = models.TextField(blank=True, null=True)
    mailing_address_city = models.TextField(blank=True, null=True)
    mailing_address_zip = models.TextField(blank=True, null=True)
    mailing_address_state = models.TextField(blank=True, null=True)
    useseparatemailingaddr = models.BooleanField(blank=True, null=True)
    expirynotes = models.TextField(blank=True, null=True)
    creationtimestamp = models.DateTimeField(blank=True, null=True)
    canexpire = models.BooleanField(blank=True, null=True)
    userlink = models.IntegerField(blank=True, null=True)
    mailing_address_thirdline = models.TextField(blank=True, null=True)
    ghostof = models.IntegerField(blank=True, null=True)
    ghostby = models.IntegerField(blank=True, null=True)
    ghosttimestamp = models.DateTimeField(blank=True, null=True)
    cloneof = models.IntegerField(blank=True, null=True)
    clonedby = models.IntegerField(blank=True, null=True)
    clonetimestamp = models.DateTimeField(blank=True, null=True)
    referenceperson = models.BooleanField(blank=True, null=True)
    rawname = models.TextField(blank=True, null=True)
    cleanname = models.TextField(blank=True, null=True)
    multientity = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'


class Personchange(models.Model):
    personchangeid = models.AutoField()
    person_personid = models.IntegerField(blank=True, null=True)
    firstname = models.TextField(blank=True, null=True)
    lastname = models.TextField(blank=True, null=True)
    compositelastname = models.BooleanField(blank=True, null=True)
    phonecell = models.TextField(blank=True, null=True)
    phonehome = models.TextField(blank=True, null=True)
    phonework = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    addressstreet = models.TextField(blank=True, null=True)
    addresscity = models.TextField(blank=True, null=True)
    addresszip = models.TextField(blank=True, null=True)
    addressstate = models.TextField(blank=True, null=True)
    useseparatemailingaddress = models.BooleanField(blank=True, null=True)
    mailingaddressstreet = models.TextField(blank=True, null=True)
    mailingaddresthirdline = models.TextField(blank=True, null=True)
    mailingaddresscity = models.TextField(blank=True, null=True)
    mailingaddresszip = models.TextField(blank=True, null=True)
    mailingaddressstate = models.TextField(blank=True, null=True)
    removed = models.BooleanField(blank=True, null=True)
    added = models.BooleanField(blank=True, null=True)
    entryts = models.DateTimeField(blank=True, null=True)
    approvedondate = models.DateTimeField(blank=True, null=True)
    approvedby_userid = models.IntegerField(blank=True, null=True)
    changedby_userid = models.IntegerField(blank=True, null=True)
    changedby_personid = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personchange'


class Personmergehistory(models.Model):
    mergeid = models.AutoField()
    mergetarget_personid = models.IntegerField(blank=True, null=True)
    mergesource_personid = models.IntegerField(blank=True, null=True)
    mergby_userid = models.IntegerField(blank=True, null=True)
    mergetimestamp = models.DateTimeField(blank=True, null=True)
    mergenotes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personmergehistory'


class Personmunilink(models.Model):
    muni_municode = models.IntegerField()
    person_personid = models.IntegerField()
    defaultmuni = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personmunilink'


class Photodoc(models.Model):
    photodocid = models.AutoField()
    photodocdescription = models.CharField(max_length=100, blank=True, null=True)
    photodocdate = models.DateTimeField(blank=True, null=True)
    photodoctype_typeid = models.IntegerField()
    photodocblob = models.BinaryField(blank=True, null=True)
    photodoccommitted = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'photodoc'


class Photodoctype(models.Model):
    typeid = models.IntegerField()
    typetitle = models.TextField(blank=True, null=True)
    icon_iconid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'photodoctype'


class Printstyle(models.Model):
    styleid = models.AutoField()
    description = models.TextField(blank=True, null=True)
    headerimage_photodocid = models.IntegerField(blank=True, null=True)
    headerheight = models.IntegerField(blank=True, null=True)
    novtopmargin = models.IntegerField(blank=True, null=True)
    novaddresseleftmargin = models.IntegerField(blank=True, null=True)
    novaddressetopmargin = models.IntegerField(blank=True, null=True)
    browserheadfootenabled = models.BooleanField(blank=True, null=True)
    novtexttopmargin = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'printstyle'


class Property(models.Model):
    propertyid = models.AutoField()
    municipality_municode = models.IntegerField(blank=True, null=True)
    parid = models.TextField()
    lotandblock = models.TextField(blank=True, null=True)
    address = models.TextField()
    usegroup = models.TextField(blank=True, null=True)
    constructiontype = models.TextField(blank=True, null=True)
    countycode = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    addr_city = models.TextField(blank=True, null=True)
    addr_state = models.TextField(blank=True, null=True)
    addr_zip = models.TextField(blank=True, null=True)
    ownercode = models.TextField(blank=True, null=True)
    propclass = models.TextField(blank=True, null=True)
    lastupdated = models.DateTimeField(blank=True, null=True)
    lastupdatedby = models.IntegerField(blank=True, null=True)
    locationdescription = models.TextField(blank=True, null=True)
    multiunit = models.BooleanField(blank=True, null=True)
    bobsource_sourceid = models.IntegerField(blank=True, null=True)
    unfitdatestart = models.DateTimeField(blank=True, null=True)
    unfitdatestop = models.DateTimeField(blank=True, null=True)
    unfitby_userid = models.IntegerField(blank=True, null=True)
    abandoneddatestart = models.DateTimeField(blank=True, null=True)
    abandoneddatestop = models.DateTimeField(blank=True, null=True)
    abandonedby_userid = models.IntegerField(blank=True, null=True)
    vacantdatestart = models.DateTimeField(blank=True, null=True)
    vacantdatestop = models.DateTimeField(blank=True, null=True)
    vacantby_userid = models.IntegerField(blank=True, null=True)
    condition_intensityclassid = models.IntegerField(blank=True, null=True)
    landbankprospect_intensityclassid = models.IntegerField(blank=True, null=True)
    landbankheld = models.BooleanField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    nonaddressable = models.BooleanField(blank=True, null=True)
    usetype_typeid = models.IntegerField(blank=True, null=True)
    creationts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'property'


class Propertyotherid(models.Model):
    otheridid = models.AutoField()
    property_propid = models.IntegerField()
    otheraddress = models.TextField(blank=True, null=True)
    otheraddressnotes = models.TextField(blank=True, null=True)
    otheraddresslastupdated = models.DateTimeField(blank=True, null=True)
    otherlotandblock = models.TextField(blank=True, null=True)
    otherlotandblocknotes = models.TextField(blank=True, null=True)
    otherlotandblocklastupdated = models.DateTimeField(blank=True, null=True)
    otherparcelid = models.TextField(blank=True, null=True)
    otherparcelidnotes = models.TextField(blank=True, null=True)
    otherparceladdresslastupdated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'propertyotherid'


class Propertyperson(models.Model):
    property_propertyid = models.IntegerField()
    person_personid = models.IntegerField()
    creationts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'propertyperson'


class Propertyphotodoc(models.Model):
    photodoc_photodocid = models.IntegerField()
    property_propertyid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'propertyphotodoc'


class Propertystatus(models.Model):
    statusid = models.AutoField()
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    userdeployable = models.BooleanField(blank=True, null=True)
    minimumuserranktoassign = models.IntegerField(blank=True, null=True)
    minimumuserranktoremove = models.IntegerField(blank=True, null=True)
    muni_municode = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'propertystatus'


class Propertyunit(models.Model):
    unitid = models.AutoField()
    unitnumber = models.TextField(blank=True, null=True)
    property_propertyid = models.IntegerField()
    otherknownaddress = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    rentalintentdatestart = models.DateTimeField(blank=True, null=True)
    rentalintentdatestop = models.DateTimeField(blank=True, null=True)
    rentalintentlastupdatedby_userid = models.IntegerField(blank=True, null=True)
    rentalnotes = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    condition_intensityclassid = models.IntegerField(blank=True, null=True)
    lastupdatedts = models.DateTimeField(blank=True, null=True)
    rental = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'propertyunit'


class Propertyunitchange(models.Model):
    unitchangeid = models.AutoField()
    propertyunit_unitid = models.IntegerField(blank=True, null=True)
    unitnumber = models.TextField(blank=True, null=True)
    otherknownaddress = models.TextField(blank=True, null=True)
    removed = models.BooleanField(blank=True, null=True)
    added = models.BooleanField(blank=True, null=True)
    entryts = models.DateTimeField(blank=True, null=True)
    approvedondate = models.DateTimeField(blank=True, null=True)
    approvedby_userid = models.IntegerField(blank=True, null=True)
    changedby_userid = models.IntegerField(blank=True, null=True)
    changedby_personid = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    rentalnotes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'propertyunitchange'


class Propertyusetype(models.Model):
    propertyusetypeid = models.AutoField()
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True, null=True)
    icon_iconid = models.IntegerField(blank=True, null=True)
    zoneclass = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'propertyusetype'


class Taxstatus(models.Model):
    taxstatusid = models.AutoField()
    year = models.IntegerField(blank=True, null=True)
    paidstatus = models.TextField(blank=True, null=True)
    tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    penalty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    interest = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    datepaid = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taxstatus'


class Textblock(models.Model):
    blockid = models.AutoField()
    blockcategory_catid = models.IntegerField()
    muni_municode = models.IntegerField()
    blockname = models.TextField()
    blocktext = models.TextField()
    placementorderdefault = models.IntegerField(blank=True, null=True)
    injectabletemplate = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'textblock'


class Textblockcategory(models.Model):
    categoryid = models.AutoField()
    categorytitle = models.TextField()
    icon_iconid = models.IntegerField(blank=True, null=True)
    muni_municode = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'textblockcategory'
