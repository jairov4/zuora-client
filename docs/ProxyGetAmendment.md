# ProxyGetAmendment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_renew** | **bool** |  Determines whether the subscription is automatically renewed, or whether it expires at the end of the term and needs to be manually renewed. **Required:** For amendment of type TermsAndConditions when changing the automatic renewal status of a subscription. **Values**: true, false  | [optional] 
**code** | **str** |  A unique alphanumeric string that identifies the amendment. **Character limit**: 50 **Values**: one of the following:  - &#x60;null&#x60; generates a value automatically - A string  | [optional] 
**contract_effective_date** | **date** |  The date when the amendment&#39;s changes become effective for billing purposes. **Version notes**: --  | [optional] 
**created_by_id** | **str** |  The user ID of the person who created the amendment. **Character limit**: 32 **Values**: automatically generated  | [optional] 
**created_date** | **datetime** |  The date when the amendment was created. **Values**: automatically generated  | [optional] 
**current_term** | **int** |  The length of the period for the current subscription term. This field can be updated when Status is &#x60;Draft&#x60;. **Required**: Only if the value of the Type field is set to &#x60;TermsAndConditions&#x60; and TermType is set to &#x60;TERMED&#x60;. This field is not required if TermType is set to &#x60;EVERGREEN&#x60;. **Character limit**: **Values**: a valid number  | [optional] 
**current_term_period_type** | **str** |  The period type for the current subscription term. **Values**:  - &#x60;Month&#x60; (default) - &#x60;Year&#x60; - &#x60;Day&#x60; - &#x60;Week&#x60; **Note**:  - This field can be updated when Status is &#x60;Draft&#x60;. - This field is used with the CurrentTerm field to specify the current subscription term.  | [optional] 
**customer_acceptance_date** | **date** |  The date when the customer accepts the amendment&#39;s changes to the subscription. **Required**: Only if the value of the Status field is set to PendingAcceptance. **Version notes**: --  | [optional] 
**description** | **str** |  A description of the amendment. **Character limit**: 500 **Values**: maximum 500 characters  | [optional] 
**effective_date** | **date** |  The date when the amendment&#39;s changes take effective. This field validates that the amendment&#39;s changes are within valid ranges of products and product rate plans. **Required**: For the cancellation amendments. Optional for other types of amendments. **Version notes**: --  | [optional] 
**id** | **str** | Object identifier. | [optional] 
**name** | **str** |  The name of the amendment. **Character limit**: 100 **Values**: a string of 100 characters or fewer  | [optional] 
**renewal_setting** | **str** |  Specifies whether a termed subscription will remain termed or change to evergreen when it is renewed. **Required**: If TermType is Termed **Values**: RENEW_WITH_SPECIFIC_TERM (default), RENEW_TO_EVERGREEN  | [optional] 
**renewal_term** | **int** |  The term of renewal for the amended subscription. This field can be updated when Status is &#x60;Draft&#x60;. **Required**: Only if the value of the Type field is set to &#x60;TermsAndConditions&#x60;. **Character limit**: **Values:** a valid number  | [optional] 
**renewal_term_period_type** | **str** |  The period type for the subscription renewal term. This field can be updated when Status is &#x60;Draft&#x60;. **Required**: Only if the value of the Type field is set to &#x60;TermsAndConditions&#x60;. This field is used with the RenewalTerm field to specify the subscription renewal term. **Values**:  - &#x60;Month&#x60; (default) - &#x60;Year&#x60; - &#x60;Day&#x60; - &#x60;Week&#x60;  | [optional] 
**service_activation_date** | **date** |  The date when service is activated. **Required**: Only if the value of the Status field is set to PendingActivation. **Version notes**: --  | [optional] 
**specific_update_date** | **date** |  The date when the UpdateProduct amendment takes effect. This field is only applicable if there is already a future-dated UpdateProduct amendment on the subscription. **Required**: Only for the UpdateProduct amendments if there is already a future-dated UpdateProduct amendment on the subscription. **Version notes**: --  | [optional] 
**status** | **str** |  The status of the amendment. Type: string (enum) **Character limit**: 17 **Values**: one of the following:  - Draft (default, if left null) - Pending Activation - Pending Acceptance - Completed  | [optional] 
**subscription_id** | **str** |  The ID of the subscription that the amendment changes. **Character limit**: 32 **Values**: a valid subscription ID  | [optional] 
**term_start_date** | **date** |  The date when the new terms and conditions take effect.   **Version notes**: --  | [optional] 
**term_type** | **str** |  Indicates if the subscription isTERMED or EVERGREEN.  - A TERMED subscription has an expiration date, and must be manually renewed. - An EVERGREEN subscription doesn&#39;t have an expiration date, and must be manually ended.  **Required**: Only when as part of an amendment of type TermsAndConditions &amp;#65279;to change the term type of a subscription. Type: string **Character limit**: 9 **Values**: TERMED, EVERGREEN  | [optional] 
**type** | **str** |  The type of amendment. **Character limit**: 18 **Values**: one of the following:  - Cancellation - NewProduct - OwnerTransfer - RemoveProduct - Renewal - UpdateProduct - TermsAndConditions - SuspendSubscription (This value is in **Limited Availability**.) - ResumeSubscription (This value is in **Limited Availability**.)  | [optional] 
**updated_by_id** | **str** |  The ID of the user who last updated the amendment. **Character limit**: 32 **Values**: automatically generated  | [optional] 
**updated_date** | **datetime** |  The date when the amendment was last updated. **Values**: automatically generated  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


