from flask_wtf import Form
from wtforms import StringField, PasswordField, SelectMultipleField, RadioField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms import widgets

class DateTimePickerWidget(object):
    datetime_picker = (
        '<label for="datetime_picker">Choose An Appointment Time</label>'
        '<p>The test times available are between June 8th and June 10th, Monday through Wednesday from 10AM to 7PM.</p>'
        '<input name="{0}" type="datetime-local" class="form-control" id="datetimeLocalOptionsRadio" value="datetimeLocal1">'
        '<p>Example: 03/05/2013 11:30 AM (Month/Day/Year Hour/Minute/Period)</p>'
    )

    def __call__(self, **kwargs):
        return self.datetime_picker.format('datetimeLocal1')


class RegisterForm(Form):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=3, max=25)])
    email = StringField('Email',
                        validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField('Verify password',
                            [DataRequired(), EqualTo('password', message='Passwords must match')])

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(username=self.username.data).first()
        if user:
            self.username.errors.append("Username already registered")
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already registered")
            return False
        return True


class DateTimePickerForm(Form):
    # datetime_local = DateTimeField('Test is on 1/16 between 10am and 5pm. These are requests and may not reflect final appointment times.'.format(),
    # validators=[DataRequired()])
    dtpw = DateTimePickerWidget()

    def __init__(self, *args, **kwargs):
        super(DateTimePickerForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        initial_validation = super(DateTimePickerForm, self).validate()
        if not initial_validation:
            return False


class SurveyForm(Form):
    first_name = StringField('First Name',
                             validators=[DataRequired(), Length(min=0, max=40)])
    last_name = StringField('Last Name',
                            validators=[DataRequired(), Length(min=0, max=40)])
    phone_number = StringField('Phone Number',
                               validators=[])
    carriers_list = [
        ( 'Aliant (Canada)', '@chat.wirefree.ca' ),
        ( 'Alltel', '@message.alltel.com' ),
        ( 'Ameritech', '@paging.acswireless.com' ),
        ( 'AT&T', '@txt.att.net' ),
        ( 'Beeline', '@sms.beeline.ua' ),
        ( 'Bell Atlantic', '@message.bam.com' ),
        ( 'Bell Mobility (Canada)', '@txt.bell.ca' ),
        ( 'Bellsouth Mobility', '@blsdcs.net' ),
        ( 'BlueSkyFrog', '@blueskyfrog.com' ),
        ( 'Boost Mobile', '@myboostmobile.com' ),
        ( 'BPL Mobile', '@bplmobile.com' ),
        ( 'Cellular South', '@csouth1.com' ),
        ( 'Claro (Brazil)', '@clarotorpedo.com.br' ),
        ( 'Claro (Nicaragua)', '@ideasclaro-ca.com' ),
        ( 'Comcast PCS', '@comcastpcs.textmsg.com' ),
        ( 'Cricket', '@sms.mycricket.com' ),
        ( 'Du (UAE)', '@email2sms.ae' ),
        ( 'E-Plus (Germany)', '@smsmail.eplus.de' ),
        ( 'Etisalat (UAE)', '@email2sms.ae' ),
        ( 'Fido', '@fido.ca' ),
        ( 'kajeet', '@mobile.kajeet.net' ),
        ( 'Koodoo (Canada)', '@msg.koodomobile.com' ),
        ( 'Manitoba Telecom (Canada)', '@text.mtsmobility.com' ),
        ( 'Metro PCS', '@mymetropcs.com' ),
        ( 'Mobinil', '@mobinil.net' ),
        ( 'Mobistar (Belgium)', '@mobistar.be' ),
        ( 'Mobitel', '@sms.mobitel.lk' ),
        ( 'Movistar (Spain)', '@correo.movistar.net' ),
        ( 'Nextel', '@messaging.nextel.com' ),
        ( 'NorthernTel (Canada)', '@txt.northerntelmobility.com' ),
        ( 'o2 (Germany)', '@o2online.de' ),
        ( 'o2 (UK)', '@mmail.co.uk' ),
        ( 'Orange (Mumbai)', '@orangemail.co.in' ),
        ( 'Orange (Netherlands)', '@sms.orange.nl' ),
        ( 'Orange (UK)', '@orange.net' ),
        ( 'Powertel', '@ptel.net' ),
        ( 'PSC Wireless', '@sms.pscel.com' ),
        ( 'Qwest', '@qwestmp.com' ),
        ( 'Rogers (Canada)', '@pcs.rogers.ca' ),
        ( 'Rogers Wireless', '@pcs.rogers.com' ),
        ( 'SaskTel (canada)', '@sms.sasktel.ca' ),
        ( 'SFR (France)', '@sfr.fr' ),
        ( 'Southern Link', '@page.southernlinc.com' ),
        ( 'Sprint PCS', '@messaging.sprintpcs.com' ),
        ( 'Suncom', '@tms.suncom.com' ),
        ( 'T-Mobile', '@tmomail.net' ),
        ( 'T-Mobile (Austria)', '@sms.t-mobile.at' ),
        ( 'T-Mobile (Netherlands)', '@gin.nl' ),
        ( 'T-Mobile (UK)', '@t-mobile.uk.net' ),
        ( 'Telebec (Canada)', '@txt.telebecmobilite.com' ),
        ( 'Telefonica (Spain)', '@movistar.net' ),
        ( 'Telus (Canada)', '@msg.telus.com' ),
        ( 'Telus Mobility', '@msg.telus.com' ),
        ( 'Tracfone', '@mmst5.tracfone.com' ),
        ( 'US Cellular', '@email.uscc.net' ),
        ( 'Verizon Wireless', '@vtext.com' ),
        ( 'Virgin Mobile', '@vmobl.net' ),
        ( 'Virgin (Canada)', '@vmobile.ca' ),
        ( 'Vodafone (Egypt)', '@vodafone.com.eg' ),
        ( 'Vodafone (Germany)', '@vodafone-sms.de' ),
        ( 'Vodafone (Italy)', '@sms.vodafone.it' ),
        ( 'Vodafone (Japan - Chuugoku)', '@n.vodafone.ne.jp' ),
        ( 'Vodafone (Japan - Hokkaido)', '@d.vodafone.ne.jp' ),
        ( 'Vodafone (Japan - Hokuriko)', '@r.vodafone.ne.jp' ),
        ( 'Vodafone (Japan - Kansai)', '@k.vodafone.ne.jp' ),
        ( 'Vodafone (Japan - Kanto)', '@k.vodafone.ne.jp' ),
        ( 'Vodafone (Japan - Koushin)', '@k.vodafone.ne.jp' ),
        ( 'Vodafone (Japan - Kyuushu)', '@q.vodafone.ne.jp' ),
        ( 'Vodafone (Japan - Niigata)', '@h.vodafone.ne.jp' ),
        ( 'Vodafone (Japan - Okinawa)', '@q.vodafone.ne.jp' ),
        ( 'Vodafone (Japan - Osaka)', '@k.vodafone.ne.jp' ),
        ( 'Vodafone (Japan - Shikoku)', '@s.vodafone.ne.jp' ),
        ( 'Vodafone (Japan - Tokyo)', '@k.vodafone.ne.jp' ),
        ( 'Vodafone (Japan - Touhoku)', '@h.vodafone.ne.jp' ),
        ( 'Vodafone (Japan - Toukai)', '@h.vodafone.ne.jp' ),
        ( 'Vodafone (Japan - Spain)', '@vodafone.es' ),
        ( 'Vodafone (UK)', '@sms.vodafone.net' )
    ]
    carriers_dict = {
        '': '',
        'Vodafone (Italy)': '@sms.vodafone.it', 'Telus Mobility': '@msg.telus.com',
        'Aliant (Canada)': '@chat.wirefree.ca', 'Orange (Mumbai)': '@orangemail.co.in',
        'T-Mobile (Netherlands)': '@gin.nl', 'Boost Mobile': '@myboostmobile.com',
        'Cellular South': '@csouth1.com', 'o2 (Germany)': '@o2online.de',
        'E-Plus (Germany)': '@smsmail.eplus.de', 'Vodafone (Japan - Touhoku)': '@h.vodafone.ne.jp',
        'Fido': '@fido.ca', 'T-Mobile (UK)': '@t-mobile.uk.net', 'Virgin Mobile': '@vmobl.net',
        'Vodafone (Japan - Hokkaido)': '@d.vodafone.ne.jp',
        'Vodafone (Japan - Niigata)': '@h.vodafone.ne.jp',
        'Vodafone (Japan - Hokuriko)': '@r.vodafone.ne.jp', 'Metro PCS': '@mymetropcs.com',
        'Cricket': '@sms.mycricket.com', 'US Cellular': '@email.uscc.net',
        'NorthernTel (Canada)': '@txt.northerntelmobility.com', 'Vodafone (UK)': '@sms.vodafone.net',
        'Vodafone (Japan - Spain)': '@vodafone.es', 'SFR (France)': '@sfr.fr',
        'Vodafone (Egypt)': '@vodafone.com.eg', 'Qwest': '@qwestmp.com', 'Tracfone': '@mmst5.tracfone.com',
        'o2 (UK)': '@mmail.co.uk', 'T-Mobile': '@tmomail.net', 'Claro (Brazil)': '@clarotorpedo.com.br',
        'BlueSkyFrog': '@blueskyfrog.com', 'Koodoo (Canada)': '@msg.koodomobile.com',
        'SaskTel (canada)': '@sms.sasktel.ca', 'Vodafone (Japan - Okinawa)': '@q.vodafone.ne.jp',
        'Verizon Wireless': '@vtext.com', 'AT&T': '@txt.att.net',
        'Vodafone (Japan - Kanto)': '@k.vodafone.ne.jp',
        'Manitoba Telecom (Canada)': '@text.mtsmobility.com', 'Alltel': '@message.alltel.com',
        'Movistar (Spain)': '@correo.movistar.net', 'Claro (Nicaragua)': '@ideasclaro-ca.com',
        'T-Mobile (Austria)': '@sms.t-mobile.at', 'Vodafone (Japan - Tokyo)': '@k.vodafone.ne.jp',
        'Vodafone (Japan - Kyuushu)': '@q.vodafone.ne.jp', 'Comcast PCS': '@comcastpcs.textmsg.com',
        'Telus (Canada)': '@msg.telus.com', 'BPL Mobile': '@bplmobile.com',
        'Bell Mobility (Canada)': '@txt.bell.ca', 'Sprint PCS': '@messaging.sprintpcs.com',
        'PSC Wireless': '@sms.pscel.com', 'kajeet': '@mobile.kajeet.net',
        'Etisalat (UAE)': '@email2sms.ae', 'Orange (Netherlands)': '@sms.orange.nl',
        'Vodafone (Japan - Kansai)': '@k.vodafone.ne.jp', 'Beeline': '@sms.beeline.ua',
        'Rogers Wireless': '@pcs.rogers.com', 'Mobistar (Belgium)': '@mobistar.be',
        'Vodafone (Japan - Chuugoku)': '@n.vodafone.ne.jp', 'Rogers (Canada)': '@pcs.rogers.ca',
        'Ameritech': '@paging.acswireless.com', 'Vodafone (Japan - Shikoku)': '@s.vodafone.ne.jp',
        'Bellsouth Mobility': '@blsdcs.net', 'Telebec (Canada)': '@txt.telebecmobilite.com',
        'Mobinil': '@mobinil.net', 'Nextel': '@messaging.nextel.com', 'Suncom': '@tms.suncom.com',
        'Telefonica (Spain)': '@movistar.net', 'Vodafone (Germany)': '@vodafone-sms.de',
        'Du (UAE)': '@email2sms.ae', 'Virgin (Canada)': '@vmobile.ca',
        'Southern Link': '@page.southernlinc.com', 'Powertel': '@ptel.net',
        'Vodafone (Japan - Koushin)': '@k.vodafone.ne.jp',
        'Vodafone (Japan - Toukai)': '@h.vodafone.ne.jp', 'Orange (UK)': '@orange.net',
        'Mobitel': '@sms.mobitel.lk', 'Bell Atlantic': '@message.bam.com',
        'Vodafone (Japan - Osaka)': '@k.vodafone.ne.jp'
    }
    phone_carrier_selection = {key for key in sorted(carriers_dict)}
    phone_carrier = SelectField('Phone Carrier',
                                choices=[(f, f) for f in sorted(phone_carrier_selection)])
    email = StringField('Email',
                        validators=[DataRequired(), Email(), Length(min=6, max=40)])
    age = StringField('Age',
                      validators=[DataRequired(), Length(min=0, max=2)])
    gender = RadioField('Gender', validators=[DataRequired()],
                        choices=[('Male', 'Male'), ('Female', 'Female'), ('No Answer', 'Choose Not to Answer')])

    platforms = SelectMultipleField('Platforms', validators=[DataRequired()], option_widget=widgets.CheckboxInput(),
                                    widget=widgets.ListWidget(prefix_label=False),
                                    choices=[
                                        ('PC', 'PC/Mac/Linux'),
                                        ('Console', 'Console (such as Xbox One, XBox 360, PS4, PS3, Wii U, Wii)'),
                                        ('Mobile', 'Mobile/Tablet (iOS, WIndows Tablet, or Android Devices)'),
                                        ('Handheld', 'Handheld Console (Vita, PSP, DS, DSi, 3DS, etc.)')])
    genres = SelectMultipleField('Genres', validators=[DataRequired()], option_widget=widgets.CheckboxInput(),
                                 widget=widgets.ListWidget(prefix_label=False),
                                 choices=[
                                     ('Action', 'Action/Adventure'), ('Fighting', 'Fighting'),
                                     ('FPS', 'First-Person Shooter'),
                                     ('MMO', 'Massively Multiplayer Online'),
                                     ('MOBA', 'Massive Online Battle Arena'),
                                     ('Platformers', 'Platformers'), ('Puzzle', 'Puzzle'), ('Racing', 'Racing'),
                                     ('Rogue-Like', 'Rogue-Like'), ('RPG', 'Role-Playing Games'),
                                     ('Sandbox', 'Sandbox'),
                                     ('Simulation', 'Simulation'), ('Social', 'Social/Casual'),
                                     ('Sports', 'Sports'),
                                     ('Strategy', 'Strategy/4X'), ('TPS', 'Third-Person Shooter'),
                                     ('Turn-Based', 'Turn-Based')])
    frequency = RadioField('How often do you buy games?', validators=[DataRequired()],
                           choices=[
                               ('Often', 'Often (about once a week)'),
                               ('Sometimes', 'Sometimes (around once a month)'),
                               ('Rarely', 'Rarely (around once a year)'), ('Never', 'Never')])
    hours = RadioField('On average, how many hours do you play games each week?', validators=[DataRequired()],
                       choices=[
                           ('6', '6 hours or less'), ('13', '7-13 hours'), ('20', '14-20 hours'),
                           ('21', 'More than 20 hours')])
    spending = RadioField('How much do you spend on games each month?', validators=[DataRequired()],
                          choices=[
                              ('15', 'Less than $15'), ('30', '$15 - $30'), ('45', '$30 - $45'),
                              ('60', '$45 - $60'),
                              ('75', '$60 - $75'), ('100', '$75 - $100'), ('125', '$100 - $125'),
                              ('126', 'More than $125')])
    titles_played = SelectMultipleField('Games Played', validators=[DataRequired()],
                                        option_widget=widgets.CheckboxInput(),
                                        widget=widgets.ListWidget(prefix_label=False),
                                        choices=[
                                            ('1', 'Game 1'), ('2', 'Game 2'), ('3', 'Game 3'), ('4', 'Game 4'),
                                            ('5', 'Game 5')])
    household = RadioField(
        'Do you or any member of your household (i.e. roommate, spouse, family member living in household) employed in video game industry?',
        validators=[DataRequired()], choices=[('Yes', 'Yes'), ('No', 'No')])
    datetime_local = DateTimePickerWidget()
    notifications = RadioField(
        'Would you like to receive notifications for future play tests that you could be eligible for?',
        validators=[DataRequired()], choices=[('Yes', 'Yes'), ('No', 'No')])
    verify = RadioField('Do you verify all information is correct?',
                        validators=[DataRequired()], choices=[('Yes', 'Yes'), ('No', 'No')])


    def __init__(self, *args, **kwargs):
        super(SurveyForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        initial_validation = super(SurveyForm, self).validate()
        if not initial_validation:
            return False
