# zuora_client.PaymentRunsApi

All URIs are relative to *https://rest.zuora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_elete_payment_run**](PaymentRunsApi.md#d_elete_payment_run) | **DELETE** /v1/payment-runs/{paymentRunId} | Delete payment run
[**g_et_payment_run**](PaymentRunsApi.md#g_et_payment_run) | **GET** /v1/payment-runs/{paymentRunId} | Get payment run
[**g_et_payment_run_summary**](PaymentRunsApi.md#g_et_payment_run_summary) | **GET** /v1/payment-runs/{paymentRunId}/summary | Get payment run summary
[**g_et_payment_runs**](PaymentRunsApi.md#g_et_payment_runs) | **GET** /v1/payment-runs | Get payment runs
[**p_ost_payment_run**](PaymentRunsApi.md#p_ost_payment_run) | **POST** /v1/payment-runs | Create payment run
[**p_ut_payment_run**](PaymentRunsApi.md#p_ut_payment_run) | **PUT** /v1/payment-runs/{paymentRunId} | Update payment run


# **d_elete_payment_run**
> CommonResponseType d_elete_payment_run(payment_run_id)

Delete payment run

Deletes a payment run. Only payment runs with the Canceled or Error status can be deleted. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentRunsApi()
payment_run_id = 'payment_run_id_example' # str | The unique ID of a payment run. For example, 402890245f097f39015f0f074a2e0566. 

try:
    # Delete payment run
    api_response = api_instance.d_elete_payment_run(payment_run_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentRunsApi->d_elete_payment_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_run_id** | [**str**](.md)| The unique ID of a payment run. For example, 402890245f097f39015f0f074a2e0566.  | 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_payment_run**
> GETPaymentRunType g_et_payment_run(payment_run_id, zuora_entity_ids=zuora_entity_ids)

Get payment run

Retrives the information about a specific payment run. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentRunsApi()
payment_run_id = 'payment_run_id_example' # str | The unique ID of a payment run. For example, 402890245f097f39015f0f074a2e0566. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get payment run
    api_response = api_instance.g_et_payment_run(payment_run_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentRunsApi->g_et_payment_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_run_id** | [**str**](.md)| The unique ID of a payment run. For example, 402890245f097f39015f0f074a2e0566.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETPaymentRunType**](GETPaymentRunType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_payment_run_summary**
> GETPaymentRunSummaryResponse g_et_payment_run_summary(payment_run_id)

Get payment run summary

Retrives the summary of a payment run. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentRunsApi()
payment_run_id = 'payment_run_id_example' # str | The unique ID of a payment run. For example, 402890245f097f39015f0f074a2e0566. 

try:
    # Get payment run summary
    api_response = api_instance.g_et_payment_run_summary(payment_run_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentRunsApi->g_et_payment_run_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_run_id** | [**str**](.md)| The unique ID of a payment run. For example, 402890245f097f39015f0f074a2e0566.  | 

### Return type

[**GETPaymentRunSummaryResponse**](GETPaymentRunSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_payment_runs**
> GETPaymentRunCollectionType g_et_payment_runs(zuora_entity_ids=zuora_entity_ids, page_size=page_size, fields_filterable=fields_filterable, sort=sort)

Get payment runs

Retrieves the information about all payment runs. You can define filterable fields to restrict the data returned in the response. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentRunsApi()
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 20 # int | Number of rows returned per page.  (optional) (default to 20)
fields_filterable = 'fields_filterable_example' # str | This parameter restricts the data returned in the response. You can use this parameter to supply a dimension you want to filter on.  A single filter uses the following form:   *fieldsFilterable* `=` *field_value*              Filters can be combined by using `&`. For example: *fieldsFilterable* `=` *field_value* `&` *fieldsFilterable* `=` *field_value*  *fieldsFilterable* indicates the name of a supported field that you can use to filter the response data. The supported filterable fields of this operation are as below:    - targetDate   - status   - createdDate   - createdById   - updatedDate   - updatedById   *field_value* indicates a valid value of the filterable field. If the type of the field value is string, you can set the field to `null` value for filtering. Then, you can get the response data with this field value being `null`. For more information about these fields, see the field descriptions in the **Responses** section.     Examples:  - /v1/payment-runs?status=Processed  - /v1/payment-runs?targetDate=2017-10-10&status=Pending  - /v1/payment-runs?status=Completed&sort=+updatedDate  (optional)
sort = 'sort_example' # str | This parameter restricts the order of the data returned in the response. You can use this parameter to supply a dimension you want to sort on.  A sortable field uses the following form:   *operator* *field_name*  You can use at most two sortable fields in one URL path. Use a comma to separate sortable fields. For example:  *operator* *field_name*, *operator* *field_name*    *operator* is used to mark the order of sequencing. The operator is optional. If you only specify the sortable field without any operator, the response data is sorted in descending order by this field.    - The `-` operator indicates an ascending order.   - The `+` operator indicates a descending order.  By default, the response data is displayed in descending order by payment run number.  *field_name* indicates the name of a sortable field. The supported sortable fields of this operation are as below:    - targetDate   - status   - createdDate   - createdById   - updatedDate   - updatedById  Examples:  - /v1/payment-runs?sort=+createdDate  - /v1/payment-runs?status=Processing&sort=-createdById,+targetDate  (optional)

try:
    # Get payment runs
    api_response = api_instance.g_et_payment_runs(zuora_entity_ids=zuora_entity_ids, page_size=page_size, fields_filterable=fields_filterable, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentRunsApi->g_et_payment_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] [default to 20]
 **fields_filterable** | **str**| This parameter restricts the data returned in the response. You can use this parameter to supply a dimension you want to filter on.  A single filter uses the following form:   *fieldsFilterable* &#x60;&#x3D;&#x60; *field_value*              Filters can be combined by using &#x60;&amp;&#x60;. For example: *fieldsFilterable* &#x60;&#x3D;&#x60; *field_value* &#x60;&amp;&#x60; *fieldsFilterable* &#x60;&#x3D;&#x60; *field_value*  *fieldsFilterable* indicates the name of a supported field that you can use to filter the response data. The supported filterable fields of this operation are as below:    - targetDate   - status   - createdDate   - createdById   - updatedDate   - updatedById   *field_value* indicates a valid value of the filterable field. If the type of the field value is string, you can set the field to &#x60;null&#x60; value for filtering. Then, you can get the response data with this field value being &#x60;null&#x60;. For more information about these fields, see the field descriptions in the **Responses** section.     Examples:  - /v1/payment-runs?status&#x3D;Processed  - /v1/payment-runs?targetDate&#x3D;2017-10-10&amp;status&#x3D;Pending  - /v1/payment-runs?status&#x3D;Completed&amp;sort&#x3D;+updatedDate  | [optional] 
 **sort** | **str**| This parameter restricts the order of the data returned in the response. You can use this parameter to supply a dimension you want to sort on.  A sortable field uses the following form:   *operator* *field_name*  You can use at most two sortable fields in one URL path. Use a comma to separate sortable fields. For example:  *operator* *field_name*, *operator* *field_name*    *operator* is used to mark the order of sequencing. The operator is optional. If you only specify the sortable field without any operator, the response data is sorted in descending order by this field.    - The &#x60;-&#x60; operator indicates an ascending order.   - The &#x60;+&#x60; operator indicates a descending order.  By default, the response data is displayed in descending order by payment run number.  *field_name* indicates the name of a sortable field. The supported sortable fields of this operation are as below:    - targetDate   - status   - createdDate   - createdById   - updatedDate   - updatedById  Examples:  - /v1/payment-runs?sort&#x3D;+createdDate  - /v1/payment-runs?status&#x3D;Processing&amp;sort&#x3D;-createdById,+targetDate  | [optional] 

### Return type

[**GETPaymentRunCollectionType**](GETPaymentRunCollectionType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_payment_run**
> GETPaymentRunType p_ost_payment_run(body, zuora_entity_ids=zuora_entity_ids)

Create payment run

Creates a payment run. You can create a payment run to be executed immediately after it is created, or a scheduced payment run to be executed in future.  The `accountId`, `batch`, `billCycleDay`, `currency`, `paymentGatewayId`, and `billingRunId` fields are used to determine which receivables to be paid in the payment run. If none of these fields is specified in the request body, the corresponding payment run collects payments for all accounts. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentRunsApi()
body = zuora_client.POSTPaymentRunRequest() # POSTPaymentRunRequest | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Create payment run
    api_response = api_instance.p_ost_payment_run(body, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentRunsApi->p_ost_payment_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**POSTPaymentRunRequest**](POSTPaymentRunRequest.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETPaymentRunType**](GETPaymentRunType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_payment_run**
> GETPaymentRunType p_ut_payment_run(payment_run_id, body, zuora_entity_ids=zuora_entity_ids)

Update payment run

Updates the information about an unexecuted payment run. Only pending payment runs can be updated.  If none of the **accountId**, **batch**, **billCycleDay**, **currency**, **paymentGatewayId**, and **billingRunId** fields is specified in the request body, the corresponding payment run collects payments for all accounts. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentRunsApi()
payment_run_id = 'payment_run_id_example' # str | The unique ID of a payment run. For example, 402890245f097f39015f0f074a2e0566. 
body = zuora_client.PUTPaymentRunRequest() # PUTPaymentRunRequest | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Update payment run
    api_response = api_instance.p_ut_payment_run(payment_run_id, body, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentRunsApi->p_ut_payment_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_run_id** | [**str**](.md)| The unique ID of a payment run. For example, 402890245f097f39015f0f074a2e0566.  | 
 **body** | [**PUTPaymentRunRequest**](PUTPaymentRunRequest.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETPaymentRunType**](GETPaymentRunType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

