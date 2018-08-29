# POSTPublicEmailTemplateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | The status of the email template. The default value is true. | [optional] [default to True]
**bcc_email_address** | **str** | The email bcc address. | [optional] 
**cc_email_address** | **str** | The email CC address. | [optional] 
**cc_email_type** | **str** | Email CC type: * When EventType is CDC/External and &#39;ReferenceObjectType&#39; in EventType is associated to Account, ccEmailType can be ALL values in enum.  * When EventType is CDC/External and &#39;ReferenceObjectType&#39; in EventType is not associated to Account, ccEmailType MUST be TenantAdmin, RunOwner or SpecificEmail.  * When EventType is CDC/External and &#39;ReferenceObjectType&#39; in EventType is EMPTY, ccEmailType MUST be TenantAdmin, RunOwner or SpecificEmail. | [optional] [default to 'SpecificEmails']
**description** | **str** | The description of the email template. | [optional] 
**email_body** | **str** | The email body. You can add merge fields in the email object using angle brackets.  You can also embed HTML tags if &#39;isHtml&#39; is true. | 
**email_subject** | **str** | The email subject. Users can add merge fields in the email subject using angle brackets. | 
**encoding_type** | **str** | The endcode type of the email body. | [optional] [default to 'UTF8']
**event_type_name** | **str** | The name of event type | 
**from_email_address** | **str** | If fromEmailType is SpecificEmail, this field is required. | [optional] 
**from_email_type** | **str** | The type of the email. | 
**from_name** | **str** | The name of the email sender. | [optional] 
**is_html** | **bool** | Specifies whether the style of email body is HTML. The default value is false. | [optional] [default to False]
**name** | **str** | The name of the email template, a unique name in a tenant. | 
**reply_to_email_address** | **str** | If replyToEmailType is SpecificEmail, this field is required. | [optional] 
**reply_to_email_type** | **str** | Type of the replyTo email. | [optional] 
**to_email_address** | **str** | If toEmailType is SpecificEmail, this field is required. | [optional] 
**to_email_type** | **str** | Email receive type. * When EventType is CDC/External and &#39;ReferenceObjectType&#39; in EventType is associated to Account, toEmailType can be ALL values in enum.  * When EventType is CDC/External and &#39;ReferenceObjectType&#39; in EventType is not associated to Account, toEmailType MUST be TenantAdmin, RunOwner or SpecificEmail. * When EventType is CDC/External and &#39;ReferenceObjectType&#39; in EventType is EMPTY, toEmailType MUST be TenantAdmin, RunOwner or SpecificEmail. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


