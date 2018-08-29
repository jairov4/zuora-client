# CreditMemoFromChargeDetailType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount of the credit memo item.  This field is in Zuora REST API version control. Supported minor versions are &#x60;224.0&#x60; and later. To use this field in the method, you must set the &#x60;zuora-version&#x60; parameter to the request header.  | [optional] 
**charge_id** | **str** | The ID of the product rate plan charge that the credit memo is created from.  | 
**comment** | **str** | Comments about the product rate plan charge.  | [optional] 
**finance_information** | [**CreditMemoFromChargeDetailTypeFinanceInformation**](CreditMemoFromChargeDetailTypeFinanceInformation.md) |  | [optional] 
**memo_item_amount** | **float** | The amount of the credit memo item.  This field is in Zuora REST API version control. Supported minor versions are &#x60;223.0&#x60; and earlier.  | [optional] 
**service_end_date** | **date** | The service end date of the credit memo item. If not specified, the effective end date of the corresponding product rate plan will be used.  | [optional] 
**service_start_date** | **date** | The service start date of the credit memo item. If not specified, the effective start date of the corresponding product rate plan will be used.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


