# Account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**auto_pay** | **bool** | Specifies whether future payments are to be automatically billed when they are due. Possible values are &#x60;true&#x60;, &#x60;false&#x60;. | [optional] 
**batch** | **str** |  | [optional] 
**bill_cycle_day** | **int** | Day of the month that the account prefers billing periods to begin on. If set to 0, the bill cycle day will be set as \&quot;AutoSet\&quot;. | 
**bill_to_contact** | [**BillToContact**](BillToContact.md) |  | 
**communication_profile_id** | **str** |  | [optional] 
**credit_card** | [**CreditCard**](CreditCard.md) |  | [optional] 
**crm_id** | **str** |  | [optional] 
**currency** | **str** | 3 uppercase character currency code | 
**custom_fields** | [**AccountObjectCustomFields**](AccountObjectCustomFields.md) |  | [optional] 
**hpm_credit_card_payment_method_id** | **str** |  | [optional] 
**invoice_delivery_prefs_email** | **bool** | Specifies whether to turn on the invoice delivery method &#39;Email&#39; for the new account.  Values are:   * &#x60;true&#x60; (default). Turn on the invoice delivery method &#39;Email&#39; for the new account. * &#x60;false&#x60;. Turn off the invoice delivery method &#39;Email&#39; for the new account.  | [optional] 
**invoice_delivery_prefs_print** | **bool** | Specifies whether to turn on the invoice delivery method &#39;Print&#39; for the new account. Values are:   * &#x60;true&#x60;. Turn on the invoice delivery method &#39;Print&#39; for the new account. * &#x60;false&#x60; (default). Turn off the invoice delivery method &#39;Print&#39; for the new account.  | [optional] 
**invoice_template_id** | **str** |  | [optional] 
**name** | **str** |  | 
**notes** | **str** |  | [optional] 
**parent_id** | **str** | Identifier of the parent customer account for this Account object. Use this field if you have customer hierarchy enabled. | [optional] 
**payment_gateway** | **str** |  | [optional] 
**payment_term** | **str** |  | [optional] 
**sold_to_contact** | [**SoldToContact**](SoldToContact.md) |  | [optional] 
**tax_info** | [**TaxInfo**](TaxInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


