/api/v1/auth/Login
req: email , password
res: accessToken, refreshToken
		↓
/api/v1/accountinfo
req: Authorization: Bearer {jwt}
res: id, email, fullName, organizations, twoFactorEnabled, pendingInvitations, emailConfirmed, createdAt, celloJwtToken, isManagedByUserProvisioning
		↓
/api/v1/organization/CheckOrganizationName
req: req: Authorization: Bearer {jwt}
res: conflict, existingOrganizationName, alternativeOrganizationName
		↓
/api/v1/organization/CreateInitial
req: Authorization: Bearer {jwt}, evaluationVersion:1(in json)
res: organizationId, name, forced2FA etc false on all
		↓
Bunche of reapeted request and login success