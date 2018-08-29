# GETDMTaxItemType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied_amount** | **float** | The applied amount of the debit memo taxation item.  | [optional] 
**credit_amount** | **float** | The amount of credit memos applied to the debit memo.   | [optional] 
**exempt_amount** | **float** | The amount of taxes or VAT for which the customer has an exemption.  | [optional] 
**finance_information** | [**GETDMTaxItemTypeFinanceInformation**](GETDMTaxItemTypeFinanceInformation.md) |  | [optional] 
**id** | **str** | The ID of the debit memo taxation item.  | [optional] 
**jurisdiction** | **str** | The jurisdiction that applies the tax or VAT. This value is typically a state, province, county, or city.  | [optional] 
**location_code** | **str** | The identifier for the location based on the value of the &#x60;taxCode&#x60; field.  | [optional] 
**name** | **str** | The name of the debit memo taxation item.  | [optional] 
**payment_amount** | **float** | The amount of payments applied to the debit memo.   | [optional] 
**refund_amount** | **float** | The amount of the refund on the debit memo taxation item.  | [optional] 
**source_tax_item_id** | **str** | The ID of the source taxation item.  | [optional] 
**tax_amount** | **float** | The amount of taxation.  | [optional] 
**tax_code** | **str** | The tax code identifies which tax rules and tax rates to apply to a specific debit memo.  | [optional] 
**tax_code_description** | **str** | The description of the tax code.  | [optional] 
**tax_date** | **date** | The date that the tax is applied to the debit memo, in &#x60;yyyy-mm-dd&#x60; format.  | [optional] 
**tax_rate** | **float** | The tax rate applied to the debit memo.  | [optional] 
**tax_rate_description** | **str** | The description of the tax rate.  | [optional] 
**tax_rate_type** | **str** | The type of the tax rate.  | [optional] 
**unapplied_amount** | **float** | The unapplied amount of the debit memo taxation item.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


