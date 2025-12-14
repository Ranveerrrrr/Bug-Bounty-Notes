Configcat signup page
		↓
POST /api/v1/account
res: integrityToken
email cofirmation email
         ↓
OPTIONS /api/v1/account/confirmEmail
req: token, turnstileToken, integrityToken
res: {"oneTimeLoginToken":null,"isNewUser":true}
		↓
Account creation Successfull