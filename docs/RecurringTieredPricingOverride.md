# RecurringTieredPricingOverride

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_change_option** | **str** | Specifies how Zuora changes the price of the charge each time the subscription renews.  If the value of this field is &#x60;SpecificPercentageValue&#x60;, use the &#x60;priceIncreasePercentage&#x60; field to specify how much the price of the charge should change.  | [optional] 
**price_increase_percentage** | **float** | Specifies the percentage by which the price of the charge should change each time the subscription renews. Only applicable if the value of the &#x60;priceChangeOption&#x60; field is &#x60;SpecificPercentageValue&#x60;.  | [optional] 
**list_price_base** | **str** | Specifies the duration of each recurring period.  | [optional] 
**quantity** | **float** | Number of units purchased.  | [optional] 
**tiers** | [**list[ChargeTier]**](ChargeTier.md) | List of cumulative pricing tiers in the charge.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


