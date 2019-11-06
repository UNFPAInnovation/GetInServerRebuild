# user's gender
GENDER_MALE = 0
GENDER_FEMALE = 1
GENDER_NOT_SPECIFIED = 2

PRIMARY_LEVEL = "Primary level"
O_LEVEL = "O level"
A_LEVEL = "A level"
TERTIARY_LEVEL = "Tertiary"


SINGLE = "Single"
MARRIED = "Married"
DIVORCED = "Divorced"


HOME = "Home"
HEALTH_FACILITY = "Health facility"

USER_TYPE_DEVELOPER = 1
USER_TYPE_DHO = 2
# Also known as VHT
USER_TYPE_CHEW = 3
USER_TYPE_MIDWIFE = 4
USER_TYPE_AMBULANCE = 5
USER_TYPE_MANAGER = 6

MISSED = "Missed"
ATTENDED = "Attended"
EXPECTED = "Expected"

#####################################
# NOTE: The form ids must be the same in odk central, android app, xslm forms and django backend
# When you change a form and generate the xml, odk central will require you to upload one with a different id
# from those that are already there
#####################################
APPOINTMENT_FORM_CHEW_NAME = "GetINAppointment6_chew"
APPOINTMENT_FORM_MIDWIFE_NAME = "GetINAppointment6_midwife"
# each district has its own form.
MAP_GIRL_BUNDIBUGYO_CHEW_FORM_NAME = "GetInMapGirlBundibugyo6_chew"
MAP_GIRL_BUNDIBUGYO_MIDWIFE_FORM_NAME = "GetInMapGirlBundibugyo6_midwife"
FOLLOW_UP_FORM_CHEW_NAME = "GetInFollowup14_chew"
FOLLOW_UP_FORM_MIDWIFE_NAME = "GetInFollowup13_midwife"
POSTNATAL_FORM_CHEW_NAME = "GetINPostnatalForm3_chew"
POSTNATAL_FORM_MIDWIFE_NAME = "GetINPostnatalForm3_midwife"
