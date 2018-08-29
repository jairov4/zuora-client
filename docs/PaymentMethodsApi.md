# zuora_client.PaymentMethodsApi

All URIs are relative to *https://rest.zuora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_elete_payment_methods**](PaymentMethodsApi.md#d_elete_payment_methods) | **DELETE** /v1/payment-methods/{payment-method-id} | Delete payment method
[**g_et_payment_methods_credit_card**](PaymentMethodsApi.md#g_et_payment_methods_credit_card) | **GET** /v1/payment-methods/credit-cards/accounts/{account-key} | Get credit card payment methods for account
[**object_delete_payment_method**](PaymentMethodsApi.md#object_delete_payment_method) | **DELETE** /v1/object/payment-method/{id} | CRUD: Delete payment method
[**object_get_payment_method**](PaymentMethodsApi.md#object_get_payment_method) | **GET** /v1/object/payment-method/{id} | CRUD: Get payment method
[**object_post_payment_method**](PaymentMethodsApi.md#object_post_payment_method) | **POST** /v1/object/payment-method | CRUD: Create payment method
[**object_put_payment_method**](PaymentMethodsApi.md#object_put_payment_method) | **PUT** /v1/object/payment-method/{id} | CRUD: Update payment method
[**p_ost_cancel_authorization**](PaymentMethodsApi.md#p_ost_cancel_authorization) | **POST** /v1/payment-methods/{payment-method-id}/voidAuthorize | Cancel authorization
[**p_ost_create_authorization**](PaymentMethodsApi.md#p_ost_create_authorization) | **POST** /v1/payment-methods/{payment-method-id}/authorize | Create authorization
[**p_ost_payment_methods**](PaymentMethodsApi.md#p_ost_payment_methods) | **POST** /v1/payment-methods | Create payment method
[**p_ost_payment_methods_credit_card**](PaymentMethodsApi.md#p_ost_payment_methods_credit_card) | **POST** /v1/payment-methods/credit-cards | Create credit card payment method
[**p_ost_payment_methods_decryption**](PaymentMethodsApi.md#p_ost_payment_methods_decryption) | **POST** /v1/payment-methods/decryption | Create Apple Pay payment method
[**p_ut_payment_methods_credit_card**](PaymentMethodsApi.md#p_ut_payment_methods_credit_card) | **PUT** /v1/payment-methods/credit-cards/{payment-method-id} | Update credit card payment method
[**p_ut_scrub_payment_methods**](PaymentMethodsApi.md#p_ut_scrub_payment_methods) | **PUT** /v1/payment-methods/{payment-method-id}/scrub | Scrub payment method
[**p_ut_verify_payment_methods**](PaymentMethodsApi.md#p_ut_verify_payment_methods) | **PUT** /v1/payment-methods/{payment-method-id}/verify | Verify payment method


# **d_elete_payment_methods**
> CommonResponseType d_elete_payment_methods(payment_method_id, zuora_entity_ids=zuora_entity_ids)

Delete payment method

Deletes a credit card payment method from the specified customer account.  If the specified payment method is the account's default payment method, the request will fail.  In that case, you must first designate a different payment method for that customer to be the default. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
payment_method_id = 'payment_method_id_example' # str | Unique identifier of a payment method. (Since this ID is unique, and linked to a customer account in the system, no customer identifier is needed.)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Delete payment method
    api_response = api_instance.d_elete_payment_methods(payment_method_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->d_elete_payment_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**| Unique identifier of a payment method. (Since this ID is unique, and linked to a customer account in the system, no customer identifier is needed.) | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_payment_methods_credit_card**
> GETPaymentMethodsType g_et_payment_methods_credit_card(account_key, zuora_entity_ids=zuora_entity_ids, page_size=page_size)

Get credit card payment methods for account

This REST API reference describes how to retrieve all credit card information for the specified customer account.   ## Notes The response includes details credit or debit cards for the specified customer account. Card numbers are masked, e.g., \"************1234\". Cards are returned in reverse chronological order of last update.  You can send requests for bank transfer payment methods types. The response will not include bank transfer details.  The response only includes payment details on payment methods that are credit or debit cards. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
account_key = 'account_key_example' # str | Account number or account ID.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 20 # int | Number of rows returned per page.  (optional) (default to 20)

try:
    # Get credit card payment methods for account
    api_response = api_instance.g_et_payment_methods_credit_card(account_key, zuora_entity_ids=zuora_entity_ids, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->g_et_payment_methods_credit_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_key** | **str**| Account number or account ID. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] [default to 20]

### Return type

[**GETPaymentMethodsType**](GETPaymentMethodsType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **object_delete_payment_method**
> ProxyDeleteResponse object_delete_payment_method(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

CRUD: Delete payment method



### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
id = 'id_example' # str | Object id
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # CRUD: Delete payment method
    api_response = api_instance.object_delete_payment_method(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->object_delete_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 

### Return type

[**ProxyDeleteResponse**](ProxyDeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **object_get_payment_method**
> ProxyGetPaymentMethod object_get_payment_method(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, fields=fields)

CRUD: Get payment method



### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
id = 'id_example' # str | Object id
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
fields = 'fields_example' # str | Object fields to return (optional)

try:
    # CRUD: Get payment method
    api_response = api_instance.object_get_payment_method(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->object_get_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **fields** | **str**| Object fields to return | [optional] 

### Return type

[**ProxyGetPaymentMethod**](ProxyGetPaymentMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **object_post_payment_method**
> ProxyCreateOrModifyResponse object_post_payment_method(create_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

CRUD: Create payment method



### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
create_request = zuora_client.ProxyCreatePaymentMethod() # ProxyCreatePaymentMethod | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # CRUD: Create payment method
    api_response = api_instance.object_post_payment_method(create_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->object_post_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_request** | [**ProxyCreatePaymentMethod**](ProxyCreatePaymentMethod.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 

### Return type

[**ProxyCreateOrModifyResponse**](ProxyCreateOrModifyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **object_put_payment_method**
> ProxyCreateOrModifyResponse object_put_payment_method(id, modify_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

CRUD: Update payment method



### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
id = 'id_example' # str | Object id
modify_request = zuora_client.ProxyModifyPaymentMethod() # ProxyModifyPaymentMethod | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # CRUD: Update payment method
    api_response = api_instance.object_put_payment_method(id, modify_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->object_put_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id | 
 **modify_request** | [**ProxyModifyPaymentMethod**](ProxyModifyPaymentMethod.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 

### Return type

[**ProxyCreateOrModifyResponse**](ProxyCreateOrModifyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_cancel_authorization**
> POSTVoidAuthorizeResponse p_ost_cancel_authorization(payment_method_id, request, zuora_entity_ids=zuora_entity_ids)

Cancel authorization

**Note:** If you wish to enable this feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Allows you to cancel an authorization. The payment gateways that support this operation include Verifi, CyberSource 1.28, and CyberSource 1.97. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
payment_method_id = 'payment_method_id_example' # str | The unique ID of the payment method where the authorization is cancelled. 
request = zuora_client.POSTVoidAuthorize() # POSTVoidAuthorize | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Cancel authorization
    api_response = api_instance.p_ost_cancel_authorization(payment_method_id, request, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->p_ost_cancel_authorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**| The unique ID of the payment method where the authorization is cancelled.  | 
 **request** | [**POSTVoidAuthorize**](POSTVoidAuthorize.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**POSTVoidAuthorizeResponse**](POSTVoidAuthorizeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_create_authorization**
> POSTAuthorizeResponse p_ost_create_authorization(payment_method_id, request, zuora_entity_ids=zuora_entity_ids)

Create authorization

**Note:** If you wish to enable this feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Enables you to authorize the availability of funds for a transaction but delay the capture of funds until a later time. The payment gateways that support this operation include Verifi, CyberSource 1.28, and CyberSource 1.97. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
payment_method_id = 'payment_method_id_example' # str | The unique ID of the payment method where the authorization is created. 
request = zuora_client.POSTDelayAuthorizeCapture() # POSTDelayAuthorizeCapture | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Create authorization
    api_response = api_instance.p_ost_create_authorization(payment_method_id, request, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->p_ost_create_authorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**| The unique ID of the payment method where the authorization is created.  | 
 **request** | [**POSTDelayAuthorizeCapture**](POSTDelayAuthorizeCapture.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**POSTAuthorizeResponse**](POSTAuthorizeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_payment_methods**
> POSTPaymentMethodResponse p_ost_payment_methods(request, zuora_entity_ids=zuora_entity_ids)

Create payment method

You can use this operation to create a payment method for a customer account. This operation supports the payment methods listed below.  ### PayPal Express Checkout The following request body fields are specific to this payment method: * `BAID` (required) * `email` (required)  ### PayPal Native Express Checkout The following request body fields are specific to this payment method: * `BAID` (required) * `email` (optional)  ### PayPal Adaptive The following request body fields are specific to this payment method: * `preapprovalKey` (required) * `email` (required) 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
request = zuora_client.POSTPaymentMethodRequest() # POSTPaymentMethodRequest | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Create payment method
    api_response = api_instance.p_ost_payment_methods(request, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->p_ost_payment_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**POSTPaymentMethodRequest**](POSTPaymentMethodRequest.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**POSTPaymentMethodResponse**](POSTPaymentMethodResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_payment_methods_credit_card**
> POSTPaymentMethodResponseType p_ost_payment_methods_credit_card(request, zuora_entity_ids=zuora_entity_ids)

Create credit card payment method

This REST API reference describes how to create a new credit card payment method for a customer account.  This API call is CORS Enabled. Use client-side JavaScript to invoke the call.   **Note**: If you use this operation to create credit card payment methods instead of using the [iFrame of Hosted Payment Pages](https://knowledgecenter.zuora.com/CB_Billing/LA_Hosted_Payment_Pages/C_Hosted_Payment_Pages/B_Implementing_Hosted_Payment_Pages_on_Your_Website/C_Embed_and_Submit_the_iFrame), you are subject to PCI-compliance audit requirements. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
request = zuora_client.POSTPaymentMethodType() # POSTPaymentMethodType | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Create credit card payment method
    api_response = api_instance.p_ost_payment_methods_credit_card(request, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->p_ost_payment_methods_credit_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**POSTPaymentMethodType**](POSTPaymentMethodType.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**POSTPaymentMethodResponseType**](POSTPaymentMethodResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_payment_methods_decryption**
> POSTPaymentMethodResponseDecryption p_ost_payment_methods_decryption(request, zuora_entity_ids=zuora_entity_ids)

Create Apple Pay payment method

The decryption API endpoint can conditionally perform 3 tasks in one atomic call:   * Decrypt Apple Pay Payment token   * Create Credit Card Payment Method in Zuora with decrypted Apple Pay information   * Process Payment on a specified Invoice (optional) 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
request = zuora_client.POSTPaymentMethodDecryption() # POSTPaymentMethodDecryption | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Create Apple Pay payment method
    api_response = api_instance.p_ost_payment_methods_decryption(request, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->p_ost_payment_methods_decryption: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**POSTPaymentMethodDecryption**](POSTPaymentMethodDecryption.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**POSTPaymentMethodResponseDecryption**](POSTPaymentMethodResponseDecryption.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_payment_methods_credit_card**
> PUTPaymentMethodResponseType p_ut_payment_methods_credit_card(payment_method_id, request, zuora_entity_ids=zuora_entity_ids)

Update credit card payment method

Updates an existing credit card payment method for the specified customer account. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
payment_method_id = 'payment_method_id_example' # str | Unique ID of the payment method to update.
request = zuora_client.PUTPaymentMethodType() # PUTPaymentMethodType | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Update credit card payment method
    api_response = api_instance.p_ut_payment_methods_credit_card(payment_method_id, request, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->p_ut_payment_methods_credit_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**| Unique ID of the payment method to update. | 
 **request** | [**PUTPaymentMethodType**](PUTPaymentMethodType.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**PUTPaymentMethodResponseType**](PUTPaymentMethodResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_scrub_payment_methods**
> CommonResponseType p_ut_scrub_payment_methods(payment_method_id, zuora_entity_ids=zuora_entity_ids)

Scrub payment method

**Note:** If you wish to enable this feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   This operation enables you to replace all sensitive data in a payment method, related payment method snapshot table, and four related log tables with dummy values that will be stored in Zuora databases.   This operation will scrub the sensitive data and soft-delete the specified payment method at the same time.  

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
payment_method_id = 'payment_method_id_example' # str | The ID of the payment method where you want to scrub the sensitive data. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Scrub payment method
    api_response = api_instance.p_ut_scrub_payment_methods(payment_method_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->p_ut_scrub_payment_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**| The ID of the payment method where you want to scrub the sensitive data.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_verify_payment_methods**
> PUTVerifyPaymentMethodResponseType p_ut_verify_payment_methods(payment_method_id, body)

Verify payment method

Sends an authorization request to the corresponding payment gateway to verify the payment method, even though no changes are made for the payment method. Supported payment methods are Credit Cards and Paypal.  Zuora now supports performing a standalone zero dollar verification or one dollar authorization for credit cards. It also supports a billing agreement status check on PayPal payment methods.  If a payment method is created by Hosted Payment Pages and is not assigned to any billing account, the payment method cannot be verified through this operation. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
payment_method_id = 'payment_method_id_example' # str | The ID of the payment method to be verified. 
body = zuora_client.PUTVerifyPaymentMethodType() # PUTVerifyPaymentMethodType | 

try:
    # Verify payment method
    api_response = api_instance.p_ut_verify_payment_methods(payment_method_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->p_ut_verify_payment_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**| The ID of the payment method to be verified.  | 
 **body** | [**PUTVerifyPaymentMethodType**](PUTVerifyPaymentMethodType.md)|  | 

### Return type

[**PUTVerifyPaymentMethodResponseType**](PUTVerifyPaymentMethodResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

