# SubscribeRequestPreviewOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_preview_mode** | **bool** | Specifies whether to create a subscription or preview the invoices that would be generated.  | [optional] 
**number_of_periods** | **int** | The number of invoice periods to show in a preview.  | [optional] 
**preview_through_term_end** | **bool** | Specifies whether to preview the charge through the end of the subscription term. Applicable to termed subscriptions only.  | [optional] 
**preview_type** | **str** | The type of preview to return:   * &#x60;InvoiceItem&#x60; - Return an invoice item preview  * &#x60;ChargeMetrics&#x60; - Return a charge metrics preview  * &#x60;InvoiceItemChargeMetrics&#x60; - Return an invoice item and charge metrics of that item  | [optional] [default to 'InvoiceItem']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


