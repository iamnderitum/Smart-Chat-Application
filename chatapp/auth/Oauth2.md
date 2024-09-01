### OAuth Or Oauth 2.0

###### "When I say ''Oauth, '' I mean Oauth 2.0 "

### HTTP redirects
###### Securely storing information in the browser.

### An Oauth Server
###### "PHP-based from the league of Extraordinary Packages"

##### OAUTH & OPENID CONNECTORS
###### "Most people think they understand OAuth. They Dont"

#### Authentication(AuthN) Vs. Authorization(AuthN)

    - Authentication is "Who are you?"
    - Authorization is "What can you do?"

###### Authorization depend on Authentication, But they are not Interchangeable
     auth 2.0 Framework
     Loose Operating agreement,not a
     contract

### OAuth 2.0 Extensions
#### JWT
    - Oauth does not require JWTs, but it's common
    - JWT are encoded, not encrypted
    - JSON Web Encryption (JWE)
    - Includes iss (issuer), iat(issued at), sub(subject),
     aud(audience), and exp(expiration)

###### RFC 7009 Token Revocation
    - Revokes(cancel) a token via API
    - Technically Optional
    - In practice, required

###### RFC 7662 Token Introspection
    - Examines a token to descrine it's contents
    - Userful  for opaqe tokens
    - Describes if the token is active or not
    - Mandatory if you have token revocation.

###### RFC 7591 Dynamic Client Registration
    - Defines a consistent API for creating OAuth clients
    - Useful in self-service API developer portals
    - Followed by RFC 7592 Dynamic client management