from twilio.rest import Client 
 
account_sid = 'AC0248566a593e434463b53c3aa3c6fe95' 
auth_token = '9c7dd57c323119bd199ec586e3ad8158' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+12058393771',  
                              body = 'I feel so coooooooool!!!!!!!!!!!!!',     
                              to='+85256047550' 
                          ) 
 
print(message.sid)