# POSTPublicNotificationDefinitionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | The status of the notification definition. The default value is true. | [optional] [default to True]
**callout** | [**POSTPublicNotificationDefinitionRequestCallout**](POSTPublicNotificationDefinitionRequestCallout.md) |  | [optional] 
**callout_active** | **bool** | The status of the callout action. Default value is false. | [optional] [default to False]
**communication_profile_id** | **str** | The profile that notification definition belongs to. If you do not pass the communicationProfileId, notification service will be automatically added to the &#39;Default Profile&#39;. | [optional] 
**description** | **str** | The description of the notification definition. | [optional] 
**email_active** | **bool** | The status of the email action. The default value is false. | [optional] [default to False]
**email_template_id** | **str** | The ID of the email template. If emailActive is true, an email template is required. And EventType of the email template MUST be the same as the eventType. | [optional] 
**event_type_name** | **str** | The name of the event type. | 
**filter_rule** | [**POSTPublicNotificationDefinitionRequestFilterRule**](POSTPublicNotificationDefinitionRequestFilterRule.md) |  | [optional] 
**filter_rule_params** | [**FilterRuleParameterValues**](FilterRuleParameterValues.md) |  | [optional] 
**name** | **str** | The name of the notification definition, unique per communication profile. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


