# PostGenerateBillingDocumentType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_post** | **bool** | Determines whether to auto post the billing documents once the draft billing documents are generated.   If an error occurred during posting billing documents, the draft billing documents are not generated too.  | [optional] [default to False]
**effective_date** | **date** | The date on which to generate the billing documents, in &#x60;yyyy-mm-dd&#x60; format.  | [optional] 
**subscription_ids** | **list[str]** | The IDs of the subscriptions that you want to create the billing documents for.   | [optional] 
**target_date** | **date** | The date used to determine which charges are to be billed, in &#x60;yyyy-mm-dd&#x60; format.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


