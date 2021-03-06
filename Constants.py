'''
Created on Aug 26, 2014

@author: abhinav2
'''
import datetime


####################config variables 
HTTP_PORT=8085
# status codes for web requests  , from server to user
NOT_ACTIVATED = 104
ACTIVATED = 105
NOT_AUTHORIZED = 106
OK =200
OK_AUTH=202
USER_EXISTS=203
USER_NOT_EXISTS = 204
USER_SAVED = 205
OK_IMMUTABLE = 206
OK_INIT = 208
FAILED=300
DUPLICATE_USER = 301
CAN_UPGRADE=212
ALLOWED=211
CAN_UPGRADE_RECHARGE = 213
REG_SAVED = 214
OK_USER_INFO =215
OK_NAME=216
NO_NAME_FOUND = 217
RATING_OK = 220;

OK_DETAILS = 501
NOT_FOUND=404   
OK_QUESTIONS = 502
OK_QUESTION = 503
OK_SERVER_DETAILS = 504
OK_UPDATES = 505
FACEBOOK_USER_SAVED = 506
GPLUS_USER_SAVED = 507
OK_MESSAGES = 508
OK_FEED = 509
OK_CHALLENGES= 510
NO_REPLY_FROM_OTHER_USERS=512
OK_SEND_MESSAGE = 513
OK_USERS_INFO = 514
OK_SCORE_BOARD = 515

################################# dict values/commands for payload type definition , from user to server
USER_ANSWERED_QUESTION = 1
GET_NEXT_QUESTION = 2
STARTING_QUESTIONS = 3
ANNOUNCING_WINNER = 4
USER_DISCONNECTED = 5
NEXT_QUESTION =6
STATUS_WHAT_USER_GOT = 8
ACTIVATE_BOT = 9
REMATCH_REQUEST = 10
LOAD_CHALLENGE_FROM_OFFLINE =11
OK_START_REMATCH = 12
START_CHALLENGE_NOW  = 14
OK_CHALLENGE_WITHOUT_OPPONENT = 15
OK_ACTIVATING_BOT = 16
USER_HAS_LEFT_POOL = 17
USER_READY = 18
LOAD_QUESTIONS=19
#################################dict keys in socket connections on server sent from user to server
MESSAGE_TYPE = '3'
QUESTIONS = '1'
CURRENT_QUESTION = '2'
QUESTION_ID = '4'
WHAT_USER_HAS_GOT = '5'
N_CURRENT_QUESTION_ANSWERED = '6'
USER_ANSWER = '7'
USERS='8'
CREATED_AT='9'
ELAPSED_TIME='10'
POINTS ='11'
N_CURRENT_REMATCH_REQUEST='12'
UID_2 = '13'
N_CURRENT_USERS_READY='14'

#preference strigns
PREF_IMMUTABLES_COUNT = "immutables_count"
###########Notification types
CHALLENGE_QUIZ_TYPE = 2;
RANDOM_USER_TYPE = 1; 
#############################33
WIN_TYPE="w"
LOOSE_TYPE="l"
CHALLENGE_TYPE = "c"


##########################33333
DONT_KNOW = 0
NOTIFICATION_USER_CHALLENGED_YOU = 1
NOTIFICATION_USER_PRIVATE_MESSAGE = 2
NOTIFICATION_USER_PLAY_REQUEST =3
NOTIFICATION_GCM_INBOX_MESSAGE = 4
NOTIFICATION_SERVER_MESSAGE =5
NOTIFICATION_SERVER_COMMAND = 6
NOTIFICATION_GCM_CHALLENGE_NOTIFICATION = 7
NOTIFICATION_GCM_OFFLINE_CHALLENGE_NOTIFICATION = 8

#############################feed types################
FEED_GENERAL = 0  
FEED_USER_WON = 1 
FEED_USER_TOOK_PART = 2 
FEED_USER_ADDED_FRIEND = 3
FEED_USER_WON_BADGES = 4
FEED_CHALLENGE = 5
FEED_USER_JOINED = 6

####################################
 
IS_TEST_BUILD = True
ONE_DAY= datetime.timedelta(days = 1)
EPOCH_DATETIME = datetime.datetime(1970,1,1)

secret_auth="helloworldabhinavreddyletsstart"





##### db server
DEFAULT_SERVER_ALIAS ="0000"
