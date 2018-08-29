# OrderActionUpdateProduct

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_updates** | [**list[ChargeUpdate]**](ChargeUpdate.md) |  | [optional] 
**custom_fields** | [**RatePlanObjectCustomFields**](RatePlanObjectCustomFields.md) |  | [optional] 
**rate_plan_id** | **str** | The id of the rate plan to be updated. It can be the latest version or any history version id.  | [optional] 
**specific_update_date** | **date** | Used for the &#39;update before update&#39; and &#39;update before remove&#39; cases. | [optional] 
**unique_token** | **str** | A unique string to represent the rate plan charge in the order. The unique token is used to perform multiple actions against a newly added rate plan. For example, if you want to add and update a product in the same order, you would assign a unique token to the product rate plan when added and use that token in future order actions.  | [optional] 
**origin_rate_plan_id** | **str** | The original rate plan id. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


