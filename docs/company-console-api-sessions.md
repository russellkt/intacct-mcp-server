Title: API Sessions

URL Source: https://developer.intacct.com/api/company-console/api-sessions/

Markdown Content:
*   [Get API Session](https://developer.intacct.com/api/company-console/api-sessions/#get-api-session)

* * *

An API session is a temporary unique identifier tied to a company ID, user ID, possibly an entity (via location ID), and an endpoint URL.

An API session is used as an alternative authentication method to avoid effectively logging in with company credentials for each API call.

You use the `getAPISession` function to get a session ID. You should always isolate `getAPISession` in a single request—do not mix `getAPISession` with other functions.

You can initiate a new entity-level session by issuing a call to `getAPISession` and supplying the location ID of the entity you want. From an entity-level session, you can provide an empty location ID to get a new top-level session (assuming you are not restricted to entity-level access).

### Session Lifespan / Timeout

The response for each API call includes the projected session timeout in the authentication element:

![Image 1: Session timeout XML tag](https://developer.intacct.com/images/api/company-console/api-sessions/sessionTimeout.png)

The session timeout is calculated based on the [session duration](https://www.intacct.com/ia/docs/en_US/help_action/Default.htm#cshid=Company_sign_in_settings) specified for the user or company plus the current time. A timeout occurs if the session timeout is reached before any subsequent API calls are made. If a call occurs before the projected timeout, it is reset to the current time plus the session duration.

* * *

Get API Session
---------------

[History](https://developer.intacct.com/api/company-console/api-sessions/#history-get-api-session)

| Release | Changes |
| --- | --- |
| 2019 Release 2 | Allow use of empty locationid to get top-level session |
| 2018 Release 4 | Added locationid |

You should not mix `getAPISession` with other functions in one request.

#### `getAPISession`

> Gets an API session for a company:

```
<getAPISession/>
```

> Gets an API session for the given entity:

```
<getAPISession>
    <locationid>California</locationid>
</getAPISession>
```

> Gets an API session for the top level:

```
<getAPISession>
    <locationid/>
</getAPISession>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| locationid | Optional | string | Location ID for an entity. From a top-level, you can provide the location ID of an entity. From an entity-level, you can provide the location ID of a different entity, or provide an empty location ID for the top level. |

#### `Response`

> The above function returns data structured like this. The location ID is empty when at the top level of a company:

```
<api>
    <sessionid>nOTaReAlSesSIonId..</sessionid>
    <endpoint>https://na12.intacct.com/ia/xml/xmlgw.phtml</endpoint>
    <locationid></locationid>
</api>
```

#### Parameters

`api`

| Name | Type | Description |
| --- | --- | --- |
| sessionid | string | Unique identifier for an API session |
| endpoint | string | Endpoint URL the sessionid is tied to. Use this and the sessionid for subsequent API requests |
| locationid | string | Location ID for an entity or empty if at the top level/only level of a company |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

