# coding: utf-8

"""
    Zuora API Reference

      # Introduction Welcome to the reference for the Zuora REST API!  <a href=\"http://en.wikipedia.org/wiki/REST_API\" target=\"_blank\">REST</a> is a web-service protocol that lends itself to rapid development by using everyday HTTP and JSON technology.  The Zuora REST API provides a broad set of operations and resources that:    * Enable Web Storefront integration from your website.   * Support self-service subscriber sign-ups and account management.   * Process revenue schedules through custom revenue rule models.   * Enable manipulation of most objects in the Zuora Object Model.  Want to share your opinion on how our API works for you? <a href=\"https://community.zuora.com/t5/Developers/API-Feedback-Form/gpm-p/21399\" target=\"_blank\">Tell us how you feel </a>about using our API and what we can do to make it better.  ## Access to the API  If you have a Zuora tenant, you can access the Zuora REST API via one of the following endpoints:  | Tenant              | Base URL for REST Endpoints | |-------------------------|-------------------------| |US Production | https://rest.zuora.com   | |US API Sandbox    | https://rest.apisandbox.zuora.com| |US Performance Test | https://rest.pt1.zuora.com | |EU Production | https://rest.eu.zuora.com | |EU Sandbox | https://rest.sandbox.eu.zuora.com |  The Production endpoint provides access to your live user data. API Sandbox tenants are a good place to test code without affecting real-world data. If you would like Zuora to provision an API Sandbox tenant for you, contact your Zuora representative for assistance.  **Note:** If you have a tenant in the Production Copy Environment, submit a request at <a href=\"http://support.zuora.com/\" target=\"_blank\">Zuora Global Support</a> to enable the Zuora REST API in your tenant and obtain the base URL for REST endpoints.  If you do not have a Zuora tenant, go to <a href=\"https://www.zuora.com/resource/zuora-test-drive\" target=\"_blank\">https://www.zuora.com/resource/zuora-test-drive</a> and sign up for a Production Test Drive tenant. The tenant comes with seed data, including a sample product catalog.  # API Changelog You can find the <a href=\"https://community.zuora.com/t5/Developers/API-Changelog/gpm-p/18092\" target=\"_blank\">Changelog</a> of the API Reference in the Zuora Community.  # Authentication  ## OAuth v2.0  Zuora recommends that you use OAuth v2.0 to authenticate to the Zuora REST API. Currently, OAuth is not available in every environment. See [Zuora Testing Environments](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/D_Zuora_Environments) for more information.  Zuora recommends you to create a dedicated API user with API write access on a tenant when authenticating via OAuth, and then create an OAuth client for this user. See <a href=\"https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users/Create_an_API_User\" target=\"_blank\">Create an API User</a> for how to do this. By creating a dedicated API user, you can control permissions of the API user without affecting other non-API users.  If a user is deactivated, all of the user's OAuth clients will be automatically deactivated.  Authenticating via OAuth requires the following steps: 1. Create a Client 2. Generate a Token 3. Make Authenticated Requests  ### Create a Client  You must first [create an OAuth client](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users#Create_an_OAuth_Client_for_a_User) in the Zuora UI. To do this, you must be an administrator of your Zuora tenant. This is a one-time operation. You will be provided with a Client ID and a Client Secret. Please note this information down, as it will be required for the next step.  **Note:** The OAuth client will be owned by a Zuora user account. If you want to perform PUT, POST, or DELETE operations using the OAuth client, the owner of the OAuth client must have a Platform role that includes the \"API Write Access\" permission.  ### Generate a Token  After creating a client, you must make a call to obtain a bearer token using the [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) operation. This operation requires the following parameters: - `client_id` - the Client ID displayed when you created the OAuth client in the previous step - `client_secret` - the Client Secret displayed when you created the OAuth client in the previous step - `grant_type` - must be set to `client_credentials`  **Note**: The Client ID and Client Secret mentioned above were displayed when you created the OAuth Client in the prior step. The [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) response specifies how long the bearer token is valid for. Call [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) again to generate a new bearer token.  ### Make Authenticated Requests  To authenticate subsequent API requests, you must provide a valid bearer token in an HTTP header:  `Authorization: Bearer {bearer_token}`  If you have [Zuora Multi-entity](https://www.zuora.com/developer/api-reference/#tag/Entities) enabled, you need to set an additional header to specify the ID of the entity that you want to access. You can use the `scope` field in the [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) response to determine whether you need to specify an entity ID.  If the `scope` field contains more than one entity ID, you must specify the ID of the entity that you want to access. For example, if the `scope` field contains `entity.1a2b7a37-3e7d-4cb3-b0e2-883de9e766cc` and `entity.c92ed977-510c-4c48-9b51-8d5e848671e9`, specify one of the following headers: - `Zuora-Entity-Ids: 1a2b7a37-3e7d-4cb3-b0e2-883de9e766cc` - `Zuora-Entity-Ids: c92ed977-510c-4c48-9b51-8d5e848671e9`  **Note**: For a limited period of time, Zuora will accept the `entityId` header as an alternative to the `Zuora-Entity-Ids` header. If you choose to set the `entityId` header, you must remove all \"-\" characters from the entity ID in the `scope` field.  If the `scope` field contains a single entity ID, you do not need to specify an entity ID.  ## Other Supported Authentication Schemes  Zuora continues to support the following additional legacy means of authentication:    * Use username and password. Include authentication with each request in the header:         * `apiAccessKeyId`      * `apiSecretAccessKey`          Zuora recommends that you create an API user specifically for making API calls. See <a href=\"https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users/Create_an_API_User\" target=\"_blank\">Create an API User</a> for more information.      * Use an authorization cookie. The cookie authorizes the user to make calls to the REST API for the duration specified in  **Administration > Security Policies > Session timeout**. The cookie expiration time is reset with this duration after every call to the REST API. To obtain a cookie, call the [Connections](https://www.zuora.com/developer/api-reference/#tag/Connections) resource with the following API user information:         *   ID         *   Password        * For CORS-enabled APIs only: Include a 'single-use' token in the request header, which re-authenticates the user with each request. See below for more details.  ### Entity Id and Entity Name  The `entityId` and `entityName` parameters are only used for [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity \"Zuora Multi-entity\"). These are the legacy parameters that Zuora will only continue to support for a period of time. Zuora recommends you to use the `Zuora-Entity-Ids` parameter instead.   The  `entityId` and `entityName` parameters specify the Id and the [name of the entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity/B_Introduction_to_Entity_and_Entity_Hierarchy#Name_and_Display_Name \"Introduction to Entity and Entity Hierarchy\") that you want to access, respectively. Note that you must have permission to access the entity.   You can specify either the `entityId` or `entityName` parameter in the authentication to access and view an entity.    * If both `entityId` and `entityName` are specified in the authentication, an error occurs.    * If neither `entityId` nor `entityName` is specified in the authentication, you will log in to the entity in which your user account is created.      To get the entity Id and entity name, you can use the GET Entities REST call. For more information, see [API User Authentication](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity/A_Overview_of_Multi-entity#API_User_Authentication \"API User Authentication\").      ### Token Authentication for CORS-Enabled APIs      The CORS mechanism enables REST API calls to Zuora to be made directly from your customer's browser, with all credit card and security information transmitted directly to Zuora. This minimizes your PCI compliance burden, allows you to implement advanced validation on your payment forms, and  makes your payment forms look just like any other part of your website.    For security reasons, instead of using cookies, an API request via CORS uses **tokens** for authentication.  The token method of authentication is only designed for use with requests that must originate from your customer's browser; **it should  not be considered a replacement to the existing cookie authentication** mechanism.  See [Zuora CORS REST](https://knowledgecenter.zuora.com/DC_Developers/REST_API/A_REST_basics/G_CORS_REST \"Zuora CORS REST\") for details on how CORS works and how you can begin to implement customer calls to the Zuora REST APIs. See  [HMAC Signatures](https://www.zuora.com/developer/api-reference/#operation/POSTHMACSignature \"HMAC Signatures\") for details on the HMAC method that returns the authentication token.  # Requests and Responses  ## Request IDs  As a general rule, when asked to supply a \"key\" for an account or subscription (accountKey, account-key, subscriptionKey, subscription-key), you can provide either the actual ID or  the number of the entity.  ## HTTP Request Body  Most of the parameters and data accompanying your requests will be contained in the body of the HTTP request.   The Zuora REST API accepts JSON in the HTTP request body. No other data format (e.g., XML) is supported.  ### Data Type  ([Actions](https://www.zuora.com/developer/api-reference/#tag/Actions) and CRUD operations only) We recommend that you do not specify the decimal values with quotation marks, commas, and spaces. Use characters of `+-0-9.eE`, for example, `5`, `1.9`, `-8.469`, and `7.7e2`. Also, Zuora does not convert currencies for decimal values.  ## Testing a Request  Use a third party client, such as [curl](https://curl.haxx.se \"curl\"), [Postman](https://www.getpostman.com \"Postman\"), or [Advanced REST Client](https://advancedrestclient.com \"Advanced REST Client\"), to test the Zuora REST API.  You can test the Zuora REST API from the Zuora API Sandbox or Production tenants. If connecting to Production, bear in mind that you are working with your live production data, not sample data or test data.  ## Testing with Credit Cards  Sooner or later it will probably be necessary to test some transactions that involve credit cards. For suggestions on how to handle this, see [Going Live With Your Payment Gateway](https://knowledgecenter.zuora.com/CB_Billing/M_Payment_Gateways/C_Managing_Payment_Gateways/B_Going_Live_Payment_Gateways#Testing_with_Credit_Cards \"C_Zuora_User_Guides/A_Billing_and_Payments/M_Payment_Gateways/C_Managing_Payment_Gateways/B_Going_Live_Payment_Gateways#Testing_with_Credit_Cards\" ).  ## Concurrent Request Limits  Zuora enforces tenant-level concurrent request limits. See <a href=\"https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits\" target=\"_blank\">Concurrent Request Limits</a> for more information.  ## Timeout Limit  If a request does not complete within 120 seconds, the request times out and Zuora returns a Gateway Timeout error.  ## Error Handling  Responses and error codes are detailed in [Responses and errors](https://knowledgecenter.zuora.com/DC_Developers/REST_API/A_REST_basics/3_Responses_and_errors \"Responses and errors\").  # Pagination  When retrieving information (using GET methods), the optional `pageSize` query parameter sets the maximum number of rows to return in a response. The maximum is `40`; larger values are treated as `40`. If this value is empty or invalid, `pageSize` typically defaults to `10`.  The default value for the maximum number of rows retrieved can be overridden at the method level.  If more rows are available, the response will include a `nextPage` element, which contains a URL for requesting the next page.  If this value is not provided, no more rows are available. No \"previous page\" element is explicitly provided; to support backward paging, use the previous call.  ## Array Size  For data items that are not paginated, the REST API supports arrays of up to 300 rows.  Thus, for instance, repeated pagination can retrieve thousands of customer accounts, but within any account an array of no more than 300 rate plans is returned.  # API Versions  The Zuora REST API are version controlled. Versioning ensures that Zuora REST API changes are backward compatible. Zuora uses a major and minor version nomenclature to manage changes. By specifying a version in a REST request, you can get expected responses regardless of future changes to the API.  ## Major Version  The major version number of the REST API appears in the REST URL. Currently, Zuora only supports the **v1** major version. For example, `POST https://rest.zuora.com/v1/subscriptions`.  ## Minor Version  Zuora uses minor versions for the REST API to control small changes. For example, a field in a REST method is deprecated and a new field is used to replace it.   Some fields in the REST methods are supported as of minor versions. If a field is not noted with a minor version, this field is available for all minor versions. If a field is noted with a minor version, this field is in version control. You must specify the supported minor version in the request header to process without an error.   If a field is in version control, it is either with a minimum minor version or a maximum minor version, or both of them. You can only use this field with the minor version between the minimum and the maximum minor versions. For example, the `invoiceCollect` field in the POST Subscription method is in version control and its maximum minor version is 189.0. You can only use this field with the minor version 189.0 or earlier.  If you specify a version number in the request header that is not supported, Zuora will use the minimum minor version of the REST API. In our REST API documentation, if a field or feature requires a minor version number, we note that in the field description.  You only need to specify the version number when you use the fields require a minor version. To specify the minor version, set the `zuora-version` parameter to the minor version number in the request header for the request call. For example, the `collect` field is in 196.0 minor version. If you want to use this field for the POST Subscription method, set the  `zuora-version` parameter to `196.0` in the request header. The `zuora-version` parameter is case sensitive.  For all the REST API fields, by default, if the minor version is not specified in the request header, Zuora will use the minimum minor version of the REST API to avoid breaking your integration.   ### Minor Version History  The supported minor versions are not serial. This section documents the changes made to each Zuora REST API minor version.  The following table lists the supported versions and the fields that have a Zuora REST API minor version.  | Fields         | Minor Version      | REST Methods    | Description | |:--------|:--------|:--------|:--------| | invoiceCollect | 189.0 and earlier  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice and collects a payment for a subscription. | | collect        | 196.0 and later    | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Collects an automatic payment for a subscription. | | invoice | 196.0 and 207.0| [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice for a subscription. | | invoiceTargetDate | 196.0 and earlier  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") |Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | invoiceTargetDate | 207.0 and earlier  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | targetDate | 207.0 and later | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") |Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | targetDate | 211.0 and later | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | includeExisting DraftInvoiceItems | 196.0 and earlier| [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | Specifies whether to include draft invoice items in subscription previews. Specify it to be `true` (default) to include draft invoice items in the preview result. Specify it to be `false` to excludes draft invoice items in the preview result. | | includeExisting DraftDocItems | 207.0 and later  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | Specifies whether to include draft invoice items in subscription previews. Specify it to be `true` (default) to include draft invoice items in the preview result. Specify it to be `false` to excludes draft invoice items in the preview result. | | previewType | 196.0 and earlier| [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | The type of preview you will receive. The possible values are `InvoiceItem`(default), `ChargeMetrics`, and `InvoiceItemChargeMetrics`. | | previewType | 207.0 and later  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | The type of preview you will receive. The possible values are `LegalDoc`(default), `ChargeMetrics`, and `LegalDocChargeMetrics`. | | runBilling  | 211.0 and later  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice or credit memo for a subscription. **Note:** Credit memos are only available if you have the Invoice Settlement feature enabled. | | invoiceDate | 214.0 and earlier  | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date that should appear on the invoice being generated, as `yyyy-mm-dd`. | | invoiceTargetDate | 214.0 and earlier  | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date through which to calculate charges on this account if an invoice is generated, as `yyyy-mm-dd`. | | documentDate | 215.0 and later | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date that should appear on the invoice and credit memo being generated, as `yyyy-mm-dd`. | | targetDate | 215.0 and later | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date through which to calculate charges on this account if an invoice or a credit memo is generated, as `yyyy-mm-dd`. | | memoItemAmount | 223.0 and earlier | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | Amount of the memo item. | | amount | 224.0 and later | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | Amount of the memo item. | | subscriptionNumbers | 222.4 and earlier | [Create order](https://www.zuora.com/developer/api-reference/#operation/POST_Order \"Create order\") | Container for the subscription numbers of the subscriptions in an order. | | subscriptions | 223.0 and later | [Create order](https://www.zuora.com/developer/api-reference/#operation/POST_Order \"Create order\") | Container for the subscription numbers and statuses in an order. |   #### Version 207.0 and Later  The response structure of the [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") and [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") methods are changed. The following invoice related response fields are moved to the invoice container:    * amount   * amountWithoutTax   * taxAmount   * invoiceItems   * targetDate   * chargeMetrics  # Zuora Object Model  The following diagram presents a high-level view of the key Zuora objects. Click the image to open it in a new tab to resize it.  <a href=\"https://www.zuora.com/wp-content/uploads/2017/01/ZuoraERD.jpeg\" target=\"_blank\"><img src=\"https://www.zuora.com/wp-content/uploads/2017/01/ZuoraERD.jpeg\" alt=\"Zuora Object Model Diagram\"></a>  See the following articles for information about other parts of the Zuora business object model:    * <a href=\"https://knowledgecenter.zuora.com/CB_Billing/Invoice_Settlement/D_Invoice_Settlement_Object_Model\" target=\"_blank\">Invoice Settlement Object Model</a>   * <a href=\"https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/BA_Orders_Object_Model\" target=\"_blank\">Orders Object Model</a>  You can use the [Describe object](https://www.zuora.com/developer/api-reference/#operation/GET_Describe) operation to list the fields of each Zuora object that is available in your tenant. When you call the operation, you must specify the API name of the Zuora object.  The following table provides the API name of each Zuora object:  | Object                                        | API Name                                   | |-----------------------------------------------|--------------------------------------------| | Account                                       | `Account`                                  | | Accounting Code                               | `AccountingCode`                           | | Accounting Period                             | `AccountingPeriod`                         | | Amendment                                     | `Amendment`                                | | Application Group                             | `ApplicationGroup`                         | | Billing Run                                   | <p>`BillingRun`</p><p>**Note:** The API name of this object is `BillingRun` in the [Describe object](https://www.zuora.com/developer/api-reference/#operation/GET_Describe) operation and Export ZOQL queries only. Otherwise, the API name of this object is `BillRun`.</p> | | Contact                                       | `Contact`                                  | | Contact Snapshot                              | `ContactSnapshot`                          | | Credit Balance Adjustment                     | `CreditBalanceAdjustment`                  | | Credit Memo                                   | `CreditMemo`                               | | Credit Memo Application                       | `CreditMemoApplication`                    | | Credit Memo Application Item                  | `CreditMemoApplicationItem`                | | Credit Memo Item                              | `CreditMemoItem`                           | | Credit Memo Part                              | `CreditMemoPart`                           | | Credit Memo Part Item                         | `CreditMemoPartItem`                       | | Credit Taxation Item                          | `CreditTaxationItem`                       | | Custom Exchange Rate                          | `FXCustomRate`                             | | Debit Memo                                    | `DebitMemo`                                | | Debit Memo Item                               | `DebitMemoItem`                            | | Debit Taxation Item                           | `DebitTaxationItem`                        | | Discount Applied Metrics                      | `DiscountAppliedMetrics`                   | | Entity                                        | `Tenant`                                   | | Gateway Reconciliation Event                  | `PaymentGatewayReconciliationEventLog`     | | Gateway Reconciliation Job                    | `PaymentReconciliationJob`                 | | Gateway Reconciliation Log                    | `PaymentReconciliationLog`                 | | Invoice                                       | `Invoice`                                  | | Invoice Adjustment                            | `InvoiceAdjustment`                        | | Invoice Item                                  | `InvoiceItem`                              | | Invoice Item Adjustment                       | `InvoiceItemAdjustment`                    | | Invoice Payment                               | `InvoicePayment`                           | | Journal Entry                                 | `JournalEntry`                             | | Journal Entry Item                            | `JournalEntryItem`                         | | Journal Run                                   | `JournalRun`                               | | Order                                         | `Order`                                    | | Order Action                                  | `OrderAction`                              | | Order ELP                                     | `OrderElp`                                 | | Order Item                                    | `OrderItem`                                | | Order MRR                                     | `OrderMrr`                                 | | Order Quantity                                | `OrderQuantity`                            | | Order TCB                                     | `OrderTcb`                                 | | Order TCV                                     | `OrderTcv`                                 | | Payment                                       | `Payment`                                  | | Payment Application                           | `PaymentApplication`                       | | Payment Application Item                      | `PaymentApplicationItem`                   | | Payment Method                                | `PaymentMethod`                            | | Payment Method Snapshot                       | `PaymentMethodSnapshot`                    | | Payment Method Transaction Log                | `PaymentMethodTransactionLog`              | | Payment Method Update                         | `UpdaterDetail`                            | | Payment Part                                  | `PaymentPart`                              | | Payment Part Item                             | `PaymentPartItem`                          | | Payment Run                                   | `PaymentRun`                               | | Payment Transaction Log                       | `PaymentTransactionLog`                    | | Processed Usage                               | `ProcessedUsage`                           | | Product                                       | `Product`                                  | | Product Rate Plan                             | `ProductRatePlan`                          | | Product Rate Plan Charge                      | `ProductRatePlanCharge`                    | | Product Rate Plan Charge Tier                 | `ProductRatePlanChargeTier`                | | Rate Plan                                     | `RatePlan`                                 | | Rate Plan Charge                              | `RatePlanCharge`                           | | Rate Plan Charge Tier                         | `RatePlanChargeTier`                       | | Refund                                        | `Refund`                                   | | Refund Application                            | `RefundApplication`                        | | Refund Application Item                       | `RefundApplicationItem`                    | | Refund Invoice Payment                        | `RefundInvoicePayment`                     | | Refund Part                                   | `RefundPart`                               | | Refund Part Item                              | `RefundPartItem`                           | | Refund Transaction Log                        | `RefundTransactionLog`                     | | Revenue Charge Summary                        | `RevenueChargeSummary`                     | | Revenue Charge Summary Item                   | `RevenueChargeSummaryItem`                 | | Revenue Event                                 | `RevenueEvent`                             | | Revenue Event Credit Memo Item                | `RevenueEventCreditMemoItem`               | | Revenue Event Debit Memo Item                 | `RevenueEventDebitMemoItem`                | | Revenue Event Invoice Item                    | `RevenueEventInvoiceItem`                  | | Revenue Event Invoice Item Adjustment         | `RevenueEventInvoiceItemAdjustment`        | | Revenue Event Item                            | `RevenueEventItem`                         | | Revenue Event Item Credit Memo Item           | `RevenueEventItemCreditMemoItem`           | | Revenue Event Item Debit Memo Item            | `RevenueEventItemDebitMemoItem`            | | Revenue Event Item Invoice Item               | `RevenueEventItemInvoiceItem`              | | Revenue Event Item Invoice Item Adjustment    | `RevenueEventItemInvoiceItemAdjustment`    | | Revenue Event Type                            | `RevenueEventType`                         | | Revenue Schedule                              | `RevenueSchedule`                          | | Revenue Schedule Credit Memo Item             | `RevenueScheduleCreditMemoItem`            | | Revenue Schedule Debit Memo Item              | `RevenueScheduleDebitMemoItem`             | | Revenue Schedule Invoice Item                 | `RevenueScheduleInvoiceItem`               | | Revenue Schedule Invoice Item Adjustment      | `RevenueScheduleInvoiceItemAdjustment`     | | Revenue Schedule Item                         | `RevenueScheduleItem`                      | | Revenue Schedule Item Credit Memo Item        | `RevenueScheduleItemCreditMemoItem`        | | Revenue Schedule Item Debit Memo Item         | `RevenueScheduleItemDebitMemoItem`         | | Revenue Schedule Item Invoice Item            | `RevenueScheduleItemInvoiceItem`           | | Revenue Schedule Item Invoice Item Adjustment | `RevenueScheduleItemInvoiceItemAdjustment` | | Subscription                                  | `Subscription`                             | | Taxable Item Snapshot                         | `TaxableItemSnapshot`                      | | Taxation Item                                 | `TaxationItem`                             | | Updater Batch                                 | `UpdaterBatch`                             | | Usage                                         | `Usage`                                    |   # noqa: E501

    OpenAPI spec version: 2018-08-23
    Contact: docs@zuora.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from zuora_client.api_client import ApiClient


class RevenueSchedulesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def d_eleters(self, rs_number, **kwargs):  # noqa: E501
        """Delete revenue schedule  # noqa: E501

        Deletes a revenue schedule by specifying its revenue schedule number ## Prerequisites You must have the Delete Custom Revenue Schedule permissions in Zuora Finance.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.d_eleters(rs_number, async=True)
        >>> result = thread.get()

        :param async bool
        :param str rs_number:  Revenue schedule number of the revenue schedule you want to delete, for example, RS-00000256. To be deleted, the revenue schedule: * Must be using a custom unlimited recognition rule. * Cannot have any revenue in a closed accounting period. * Cannot be included in a summary journal entry. * Cannot have a revenue schedule date in a closed accounting period.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: CommonResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.d_eleters_with_http_info(rs_number, **kwargs)  # noqa: E501
        else:
            (data) = self.d_eleters_with_http_info(rs_number, **kwargs)  # noqa: E501
            return data

    def d_eleters_with_http_info(self, rs_number, **kwargs):  # noqa: E501
        """Delete revenue schedule  # noqa: E501

        Deletes a revenue schedule by specifying its revenue schedule number ## Prerequisites You must have the Delete Custom Revenue Schedule permissions in Zuora Finance.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.d_eleters_with_http_info(rs_number, async=True)
        >>> result = thread.get()

        :param async bool
        :param str rs_number:  Revenue schedule number of the revenue schedule you want to delete, for example, RS-00000256. To be deleted, the revenue schedule: * Must be using a custom unlimited recognition rule. * Cannot have any revenue in a closed accounting period. * Cannot be included in a summary journal entry. * Cannot have a revenue schedule date in a closed accounting period.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: CommonResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rs_number', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method d_eleters" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rs_number' is set
        if ('rs_number' not in params or
                params['rs_number'] is None):
            raise ValueError("Missing the required parameter `rs_number` when calling `d_eleters`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rs_number' in params:
            path_params['rs-number'] = params['rs_number']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/revenue-schedules/{rs-number}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CommonResponseType',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def g_etr_sby_credit_memo_item(self, cmi_id, **kwargs):  # noqa: E501
        """Get revenue schedule by credit memo item ID   # noqa: E501

        **Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves the details about a revenue schedule by specifying a valid credit memo item ID.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.g_etr_sby_credit_memo_item(cmi_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cmi_id: The unique ID of a credit memo item. You can get the credit memo item ID from the response of [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems).  (required)
        :return: GETRSDetailType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.g_etr_sby_credit_memo_item_with_http_info(cmi_id, **kwargs)  # noqa: E501
        else:
            (data) = self.g_etr_sby_credit_memo_item_with_http_info(cmi_id, **kwargs)  # noqa: E501
            return data

    def g_etr_sby_credit_memo_item_with_http_info(self, cmi_id, **kwargs):  # noqa: E501
        """Get revenue schedule by credit memo item ID   # noqa: E501

        **Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves the details about a revenue schedule by specifying a valid credit memo item ID.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.g_etr_sby_credit_memo_item_with_http_info(cmi_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cmi_id: The unique ID of a credit memo item. You can get the credit memo item ID from the response of [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems).  (required)
        :return: GETRSDetailType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cmi_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method g_etr_sby_credit_memo_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cmi_id' is set
        if ('cmi_id' not in params or
                params['cmi_id'] is None):
            raise ValueError("Missing the required parameter `cmi_id` when calling `g_etr_sby_credit_memo_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cmi_id' in params:
            path_params['cmi-id'] = params['cmi_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/revenue-schedules/credit-memo-items/{cmi-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETRSDetailType',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def g_etr_sby_debit_memo_item(self, dmi_id, **kwargs):  # noqa: E501
        """Get revenue schedule by debit memo item ID   # noqa: E501

        **Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves the details about a revenue schedule by specifying a valid debit memo item ID.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.g_etr_sby_debit_memo_item(dmi_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dmi_id: The unique ID of a debit memo item. You can get the debit memo item ID from the response of [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems).  (required)
        :return: GETRSDetailType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.g_etr_sby_debit_memo_item_with_http_info(dmi_id, **kwargs)  # noqa: E501
        else:
            (data) = self.g_etr_sby_debit_memo_item_with_http_info(dmi_id, **kwargs)  # noqa: E501
            return data

    def g_etr_sby_debit_memo_item_with_http_info(self, dmi_id, **kwargs):  # noqa: E501
        """Get revenue schedule by debit memo item ID   # noqa: E501

        **Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves the details about a revenue schedule by specifying a valid debit memo item ID.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.g_etr_sby_debit_memo_item_with_http_info(dmi_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dmi_id: The unique ID of a debit memo item. You can get the debit memo item ID from the response of [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems).  (required)
        :return: GETRSDetailType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dmi_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method g_etr_sby_debit_memo_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dmi_id' is set
        if ('dmi_id' not in params or
                params['dmi_id'] is None):
            raise ValueError("Missing the required parameter `dmi_id` when calling `g_etr_sby_debit_memo_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dmi_id' in params:
            path_params['dmi-id'] = params['dmi_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/revenue-schedules/debit-memo-items/{dmi-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETRSDetailType',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def g_etr_sby_invoice_item(self, invoice_item_id, **kwargs):  # noqa: E501
        """Get revenue schedule by invoice item ID  # noqa: E501

        Retrieves the details of a revenue schedule by specifying the invoice item ID.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.g_etr_sby_invoice_item(invoice_item_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str invoice_item_id: A valid Invoice Item ID. (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETRSDetailType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.g_etr_sby_invoice_item_with_http_info(invoice_item_id, **kwargs)  # noqa: E501
        else:
            (data) = self.g_etr_sby_invoice_item_with_http_info(invoice_item_id, **kwargs)  # noqa: E501
            return data

    def g_etr_sby_invoice_item_with_http_info(self, invoice_item_id, **kwargs):  # noqa: E501
        """Get revenue schedule by invoice item ID  # noqa: E501

        Retrieves the details of a revenue schedule by specifying the invoice item ID.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.g_etr_sby_invoice_item_with_http_info(invoice_item_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str invoice_item_id: A valid Invoice Item ID. (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETRSDetailType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['invoice_item_id', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method g_etr_sby_invoice_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'invoice_item_id' is set
        if ('invoice_item_id' not in params or
                params['invoice_item_id'] is None):
            raise ValueError("Missing the required parameter `invoice_item_id` when calling `g_etr_sby_invoice_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'invoice_item_id' in params:
            path_params['invoice-item-id'] = params['invoice_item_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/revenue-schedules/invoice-items/{invoice-item-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETRSDetailType',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def g_etr_sby_invoice_item_adjustment(self, invoice_item_adj_key, **kwargs):  # noqa: E501
        """Get revenue schedule by invoice item adjustment  # noqa: E501

        Retrieves the details of a revenue schedule by specifying a valid invoice item adjustment identifier. Request and response field descriptions and sample code are provided.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.g_etr_sby_invoice_item_adjustment(invoice_item_adj_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str invoice_item_adj_key: ID or number of the Invoice Item Adjustment, for example, e20b07fd416dcfcf0141c81164fd0a72. (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETRSDetailType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.g_etr_sby_invoice_item_adjustment_with_http_info(invoice_item_adj_key, **kwargs)  # noqa: E501
        else:
            (data) = self.g_etr_sby_invoice_item_adjustment_with_http_info(invoice_item_adj_key, **kwargs)  # noqa: E501
            return data

    def g_etr_sby_invoice_item_adjustment_with_http_info(self, invoice_item_adj_key, **kwargs):  # noqa: E501
        """Get revenue schedule by invoice item adjustment  # noqa: E501

        Retrieves the details of a revenue schedule by specifying a valid invoice item adjustment identifier. Request and response field descriptions and sample code are provided.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.g_etr_sby_invoice_item_adjustment_with_http_info(invoice_item_adj_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str invoice_item_adj_key: ID or number of the Invoice Item Adjustment, for example, e20b07fd416dcfcf0141c81164fd0a72. (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETRSDetailType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['invoice_item_adj_key', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method g_etr_sby_invoice_item_adjustment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'invoice_item_adj_key' is set
        if ('invoice_item_adj_key' not in params or
                params['invoice_item_adj_key'] is None):
            raise ValueError("Missing the required parameter `invoice_item_adj_key` when calling `g_etr_sby_invoice_item_adjustment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'invoice_item_adj_key' in params:
            path_params['invoice-item-adj-key'] = params['invoice_item_adj_key']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/revenue-schedules/invoice-item-adjustments/{invoice-item-adj-key}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETRSDetailType',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def g_etr_sby_product_charge_and_billing_account(self, account_key, charge_key, **kwargs):  # noqa: E501
        """Get all revenue schedules of product charge by charge ID and billing account ID   # noqa: E501

        **Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves the details about all revenue schedules of a product rate plan charge by specifying the charge ID and billing account ID.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.g_etr_sby_product_charge_and_billing_account(account_key, charge_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str account_key: The account number or account ID.  (required)
        :param str charge_key: The unique ID of a product rate plan charge. For example, 8a8082e65ba86084015bb323d3c61d82.  (required)
        :param int page_size: Number of rows returned per page. 
        :return: GETRSDetailsByProductChargeType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.g_etr_sby_product_charge_and_billing_account_with_http_info(account_key, charge_key, **kwargs)  # noqa: E501
        else:
            (data) = self.g_etr_sby_product_charge_and_billing_account_with_http_info(account_key, charge_key, **kwargs)  # noqa: E501
            return data

    def g_etr_sby_product_charge_and_billing_account_with_http_info(self, account_key, charge_key, **kwargs):  # noqa: E501
        """Get all revenue schedules of product charge by charge ID and billing account ID   # noqa: E501

        **Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves the details about all revenue schedules of a product rate plan charge by specifying the charge ID and billing account ID.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.g_etr_sby_product_charge_and_billing_account_with_http_info(account_key, charge_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str account_key: The account number or account ID.  (required)
        :param str charge_key: The unique ID of a product rate plan charge. For example, 8a8082e65ba86084015bb323d3c61d82.  (required)
        :param int page_size: Number of rows returned per page. 
        :return: GETRSDetailsByProductChargeType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_key', 'charge_key', 'page_size']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method g_etr_sby_product_charge_and_billing_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_key' is set
        if ('account_key' not in params or
                params['account_key'] is None):
            raise ValueError("Missing the required parameter `account_key` when calling `g_etr_sby_product_charge_and_billing_account`")  # noqa: E501
        # verify the required parameter 'charge_key' is set
        if ('charge_key' not in params or
                params['charge_key'] is None):
            raise ValueError("Missing the required parameter `charge_key` when calling `g_etr_sby_product_charge_and_billing_account`")  # noqa: E501

        if 'page_size' in params and params['page_size'] > 300:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `g_etr_sby_product_charge_and_billing_account`, must be a value less than or equal to `300`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'account_key' in params:
            path_params['account-key'] = params['account_key']  # noqa: E501
        if 'charge_key' in params:
            path_params['charge-key'] = params['charge_key']  # noqa: E501

        query_params = []
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/revenue-schedules/product-charges/{charge-key}/{account-key}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETRSDetailsByProductChargeType',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def g_etr_sfor_subsc_charge(self, charge_key, **kwargs):  # noqa: E501
        """Get revenue schedule by subscription charge  # noqa: E501

        Retrieves the revenue schedule details by specifying subscription charge ID. Request and response field descriptions and sample code are provided   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.g_etr_sfor_subsc_charge(charge_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str charge_key: ID of the subscription rate plan charge; for example, 402892793e173340013e173b81000012. (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param int page_size: Number of rows returned per page. 
        :return: GETRSDetailsByChargeType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.g_etr_sfor_subsc_charge_with_http_info(charge_key, **kwargs)  # noqa: E501
        else:
            (data) = self.g_etr_sfor_subsc_charge_with_http_info(charge_key, **kwargs)  # noqa: E501
            return data

    def g_etr_sfor_subsc_charge_with_http_info(self, charge_key, **kwargs):  # noqa: E501
        """Get revenue schedule by subscription charge  # noqa: E501

        Retrieves the revenue schedule details by specifying subscription charge ID. Request and response field descriptions and sample code are provided   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.g_etr_sfor_subsc_charge_with_http_info(charge_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str charge_key: ID of the subscription rate plan charge; for example, 402892793e173340013e173b81000012. (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param int page_size: Number of rows returned per page. 
        :return: GETRSDetailsByChargeType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['charge_key', 'zuora_entity_ids', 'page_size']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method g_etr_sfor_subsc_charge" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'charge_key' is set
        if ('charge_key' not in params or
                params['charge_key'] is None):
            raise ValueError("Missing the required parameter `charge_key` when calling `g_etr_sfor_subsc_charge`")  # noqa: E501

        if 'page_size' in params and params['page_size'] > 300:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `g_etr_sfor_subsc_charge`, must be a value less than or equal to `300`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'charge_key' in params:
            path_params['charge-key'] = params['charge_key']  # noqa: E501

        query_params = []
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/revenue-schedules/subscription-charges/{charge-key}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETRSDetailsByChargeType',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def g_etrs(self, rs_number, **kwargs):  # noqa: E501
        """Get revenue schedule details  # noqa: E501

        Retrieves the details of a revenue schedule by specifying the revenue schedule number. Request and response field descriptions and sample code are provided.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.g_etrs(rs_number, async=True)
        >>> result = thread.get()

        :param async bool
        :param str rs_number: Revenue schedule number. The revenue schedule number is always prefixed with \"RS\", for example, \"RS-00000001\".  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETRSDetailType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.g_etrs_with_http_info(rs_number, **kwargs)  # noqa: E501
        else:
            (data) = self.g_etrs_with_http_info(rs_number, **kwargs)  # noqa: E501
            return data

    def g_etrs_with_http_info(self, rs_number, **kwargs):  # noqa: E501
        """Get revenue schedule details  # noqa: E501

        Retrieves the details of a revenue schedule by specifying the revenue schedule number. Request and response field descriptions and sample code are provided.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.g_etrs_with_http_info(rs_number, async=True)
        >>> result = thread.get()

        :param async bool
        :param str rs_number: Revenue schedule number. The revenue schedule number is always prefixed with \"RS\", for example, \"RS-00000001\".  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETRSDetailType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rs_number', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method g_etrs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rs_number' is set
        if ('rs_number' not in params or
                params['rs_number'] is None):
            raise ValueError("Missing the required parameter `rs_number` when calling `g_etrs`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rs_number' in params:
            path_params['rs-number'] = params['rs_number']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/revenue-schedules/{rs-number}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETRSDetailType',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ostr_sfor_credit_memo_item_distribute_by_date_range(self, cmi_id, body, **kwargs):  # noqa: E501
        """Create revenue schedule for credit memo item (distribute by date range)   # noqa: E501

        **Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Creates a revenue schedule for a credit memo item, and automatically distribute the revenue by specifying the recognition start and end dates.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.p_ostr_sfor_credit_memo_item_distribute_by_date_range(cmi_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cmi_id: The unique ID of a credit memo item. You can get the credit memo item ID from the response of [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems).  (required)
        :param POSTRevenueScheduleByTransactionRatablyType body:  (required)
        :return: POSTRevenueScheduleByTransactionResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.p_ostr_sfor_credit_memo_item_distribute_by_date_range_with_http_info(cmi_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ostr_sfor_credit_memo_item_distribute_by_date_range_with_http_info(cmi_id, body, **kwargs)  # noqa: E501
            return data

    def p_ostr_sfor_credit_memo_item_distribute_by_date_range_with_http_info(self, cmi_id, body, **kwargs):  # noqa: E501
        """Create revenue schedule for credit memo item (distribute by date range)   # noqa: E501

        **Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Creates a revenue schedule for a credit memo item, and automatically distribute the revenue by specifying the recognition start and end dates.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.p_ostr_sfor_credit_memo_item_distribute_by_date_range_with_http_info(cmi_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cmi_id: The unique ID of a credit memo item. You can get the credit memo item ID from the response of [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems).  (required)
        :param POSTRevenueScheduleByTransactionRatablyType body:  (required)
        :return: POSTRevenueScheduleByTransactionResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cmi_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ostr_sfor_credit_memo_item_distribute_by_date_range" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cmi_id' is set
        if ('cmi_id' not in params or
                params['cmi_id'] is None):
            raise ValueError("Missing the required parameter `cmi_id` when calling `p_ostr_sfor_credit_memo_item_distribute_by_date_range`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `p_ostr_sfor_credit_memo_item_distribute_by_date_range`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cmi_id' in params:
            path_params['cmi-id'] = params['cmi_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/revenue-schedules/credit-memo-items/{cmi-id}/distribute-revenue-with-date-range', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='POSTRevenueScheduleByTransactionResponseType',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ostr_sfor_credit_memo_item_manual_distribution(self, cmi_id, body, **kwargs):  # noqa: E501
        """Create revenue schedule for credit memo item (manual distribution)   # noqa: E501

        **Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Creates a revenue schedule for a credit memo item, and manually distribute the revenue.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.p_ostr_sfor_credit_memo_item_manual_distribution(cmi_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cmi_id: The unique ID of a credit memo item. You can get the credit memo item ID from the response of [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems).  (required)
        :param POSTRevenueScheduleByTransactionType body:  (required)
        :return: POSTRevenueScheduleByTransactionResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.p_ostr_sfor_credit_memo_item_manual_distribution_with_http_info(cmi_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ostr_sfor_credit_memo_item_manual_distribution_with_http_info(cmi_id, body, **kwargs)  # noqa: E501
            return data

    def p_ostr_sfor_credit_memo_item_manual_distribution_with_http_info(self, cmi_id, body, **kwargs):  # noqa: E501
        """Create revenue schedule for credit memo item (manual distribution)   # noqa: E501

        **Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Creates a revenue schedule for a credit memo item, and manually distribute the revenue.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.p_ostr_sfor_credit_memo_item_manual_distribution_with_http_info(cmi_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cmi_id: The unique ID of a credit memo item. You can get the credit memo item ID from the response of [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems).  (required)
        :param POSTRevenueScheduleByTransactionType body:  (required)
        :return: POSTRevenueScheduleByTransactionResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cmi_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ostr_sfor_credit_memo_item_manual_distribution" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cmi_id' is set
        if ('cmi_id' not in params or
                params['cmi_id'] is None):
            raise ValueError("Missing the required parameter `cmi_id` when calling `p_ostr_sfor_credit_memo_item_manual_distribution`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `p_ostr_sfor_credit_memo_item_manual_distribution`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cmi_id' in params:
            path_params['cmi-id'] = params['cmi_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/revenue-schedules/credit-memo-items/{cmi-id}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='POSTRevenueScheduleByTransactionResponseType',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ostr_sfor_debit_memo_item_distribute_by_date_range(self, dmi_id, body, **kwargs):  # noqa: E501
        """Create revenue schedule for debit memo item (distribute by date range)   # noqa: E501

        **Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Creates a revenue schedule for a debit memo item, and automatically distribute the revenue by specifying the recognition start and end dates.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.p_ostr_sfor_debit_memo_item_distribute_by_date_range(dmi_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dmi_id: The unique ID of a debit memo item. You can get the debit memo item ID from the response of [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems).  (required)
        :param POSTRevenueScheduleByTransactionRatablyType body:  (required)
        :return: POSTRevenueScheduleByTransactionResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.p_ostr_sfor_debit_memo_item_distribute_by_date_range_with_http_info(dmi_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ostr_sfor_debit_memo_item_distribute_by_date_range_with_http_info(dmi_id, body, **kwargs)  # noqa: E501
            return data

    def p_ostr_sfor_debit_memo_item_distribute_by_date_range_with_http_info(self, dmi_id, body, **kwargs):  # noqa: E501
        """Create revenue schedule for debit memo item (distribute by date range)   # noqa: E501

        **Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Creates a revenue schedule for a debit memo item, and automatically distribute the revenue by specifying the recognition start and end dates.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.p_ostr_sfor_debit_memo_item_distribute_by_date_range_with_http_info(dmi_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dmi_id: The unique ID of a debit memo item. You can get the debit memo item ID from the response of [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems).  (required)
        :param POSTRevenueScheduleByTransactionRatablyType body:  (required)
        :return: POSTRevenueScheduleByTransactionResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dmi_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ostr_sfor_debit_memo_item_distribute_by_date_range" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dmi_id' is set
        if ('dmi_id' not in params or
                params['dmi_id'] is None):
            raise ValueError("Missing the required parameter `dmi_id` when calling `p_ostr_sfor_debit_memo_item_distribute_by_date_range`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `p_ostr_sfor_debit_memo_item_distribute_by_date_range`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dmi_id' in params:
            path_params['dmi-id'] = params['dmi_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/revenue-schedules/debit-memo-items/{dmi-id}/distribute-revenue-with-date-range', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='POSTRevenueScheduleByTransactionResponseType',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ostr_sfor_debit_memo_item_manual_distribution(self, dmi_id, body, **kwargs):  # noqa: E501
        """Create revenue schedule for debit memo item (manual distribution)   # noqa: E501

        **Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Creates a revenue schedule for a debit memo item, and manually distribute the revenue.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.p_ostr_sfor_debit_memo_item_manual_distribution(dmi_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dmi_id: The unique ID of a debit memo item. You can get the debit memo item ID from the response of [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems).  (required)
        :param POSTRevenueScheduleByTransactionType body:  (required)
        :return: POSTRevenueScheduleByTransactionResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.p_ostr_sfor_debit_memo_item_manual_distribution_with_http_info(dmi_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ostr_sfor_debit_memo_item_manual_distribution_with_http_info(dmi_id, body, **kwargs)  # noqa: E501
            return data

    def p_ostr_sfor_debit_memo_item_manual_distribution_with_http_info(self, dmi_id, body, **kwargs):  # noqa: E501
        """Create revenue schedule for debit memo item (manual distribution)   # noqa: E501

        **Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Creates a revenue schedule for a debit memo item, and manually distribute the revenue.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.p_ostr_sfor_debit_memo_item_manual_distribution_with_http_info(dmi_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dmi_id: The unique ID of a debit memo item. You can get the debit memo item ID from the response of [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems).  (required)
        :param POSTRevenueScheduleByTransactionType body:  (required)
        :return: POSTRevenueScheduleByTransactionResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dmi_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ostr_sfor_debit_memo_item_manual_distribution" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dmi_id' is set
        if ('dmi_id' not in params or
                params['dmi_id'] is None):
            raise ValueError("Missing the required parameter `dmi_id` when calling `p_ostr_sfor_debit_memo_item_manual_distribution`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `p_ostr_sfor_debit_memo_item_manual_distribution`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dmi_id' in params:
            path_params['dmi-id'] = params['dmi_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/revenue-schedules/debit-memo-items/{dmi-id}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='POSTRevenueScheduleByTransactionResponseType',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ostr_sfor_invoice_item_adjustment_distribute_by_date_range(self, invoice_item_adj_key, request, **kwargs):  # noqa: E501
        """Create revenue schedule for Invoice Item Adjustment (distribute by date range)  # noqa: E501

        Creates a revenue schedule for an Invoice Item Adjustment and distribute the revenue by specifying the recognition start and end dates.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.p_ostr_sfor_invoice_item_adjustment_distribute_by_date_range(invoice_item_adj_key, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str invoice_item_adj_key: ID or number of the Invoice Item Adjustment, for example, e20b07fd416dcfcf0141c81164fd0a72. If the specified Invoice Item Adjustment is already associated with a revenue schedule, the call will fail.  (required)
        :param POSTRevenueScheduleByDateRangeType request:  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: POSTRevenueScheduleByTransactionResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.p_ostr_sfor_invoice_item_adjustment_distribute_by_date_range_with_http_info(invoice_item_adj_key, request, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ostr_sfor_invoice_item_adjustment_distribute_by_date_range_with_http_info(invoice_item_adj_key, request, **kwargs)  # noqa: E501
            return data

    def p_ostr_sfor_invoice_item_adjustment_distribute_by_date_range_with_http_info(self, invoice_item_adj_key, request, **kwargs):  # noqa: E501
        """Create revenue schedule for Invoice Item Adjustment (distribute by date range)  # noqa: E501

        Creates a revenue schedule for an Invoice Item Adjustment and distribute the revenue by specifying the recognition start and end dates.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.p_ostr_sfor_invoice_item_adjustment_distribute_by_date_range_with_http_info(invoice_item_adj_key, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str invoice_item_adj_key: ID or number of the Invoice Item Adjustment, for example, e20b07fd416dcfcf0141c81164fd0a72. If the specified Invoice Item Adjustment is already associated with a revenue schedule, the call will fail.  (required)
        :param POSTRevenueScheduleByDateRangeType request:  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: POSTRevenueScheduleByTransactionResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['invoice_item_adj_key', 'request', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ostr_sfor_invoice_item_adjustment_distribute_by_date_range" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'invoice_item_adj_key' is set
        if ('invoice_item_adj_key' not in params or
                params['invoice_item_adj_key'] is None):
            raise ValueError("Missing the required parameter `invoice_item_adj_key` when calling `p_ostr_sfor_invoice_item_adjustment_distribute_by_date_range`")  # noqa: E501
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `p_ostr_sfor_invoice_item_adjustment_distribute_by_date_range`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'invoice_item_adj_key' in params:
            path_params['invoice-item-adj-key'] = params['invoice_item_adj_key']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/revenue-schedules/invoice-item-adjustments/{invoice-item-adj-key}/distribute-revenue-with-date-range', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='POSTRevenueScheduleByTransactionResponseType',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ostr_sfor_invoice_item_adjustment_manual_distribution(self, invoice_item_adj_key, request, **kwargs):  # noqa: E501
        """Create revenue schedule for Invoice Item Adjustment (manual distribution)  # noqa: E501

        Creates a revenue schedule for an Invoice Item Adjustment and manually distribute the revenue.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.p_ostr_sfor_invoice_item_adjustment_manual_distribution(invoice_item_adj_key, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str invoice_item_adj_key: ID or number of the Invoice Item Adjustment, for example, e20b07fd416dcfcf0141c81164fd0a72. If the specified Invoice Item Adjustment is already associated with a revenue schedule, the call will fail.  (required)
        :param POSTRevenueScheduleByTransactionType request:  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: POSTRevenueScheduleByTransactionResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.p_ostr_sfor_invoice_item_adjustment_manual_distribution_with_http_info(invoice_item_adj_key, request, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ostr_sfor_invoice_item_adjustment_manual_distribution_with_http_info(invoice_item_adj_key, request, **kwargs)  # noqa: E501
            return data

    def p_ostr_sfor_invoice_item_adjustment_manual_distribution_with_http_info(self, invoice_item_adj_key, request, **kwargs):  # noqa: E501
        """Create revenue schedule for Invoice Item Adjustment (manual distribution)  # noqa: E501

        Creates a revenue schedule for an Invoice Item Adjustment and manually distribute the revenue.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.p_ostr_sfor_invoice_item_adjustment_manual_distribution_with_http_info(invoice_item_adj_key, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str invoice_item_adj_key: ID or number of the Invoice Item Adjustment, for example, e20b07fd416dcfcf0141c81164fd0a72. If the specified Invoice Item Adjustment is already associated with a revenue schedule, the call will fail.  (required)
        :param POSTRevenueScheduleByTransactionType request:  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: POSTRevenueScheduleByTransactionResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['invoice_item_adj_key', 'request', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ostr_sfor_invoice_item_adjustment_manual_distribution" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'invoice_item_adj_key' is set
        if ('invoice_item_adj_key' not in params or
                params['invoice_item_adj_key'] is None):
            raise ValueError("Missing the required parameter `invoice_item_adj_key` when calling `p_ostr_sfor_invoice_item_adjustment_manual_distribution`")  # noqa: E501
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `p_ostr_sfor_invoice_item_adjustment_manual_distribution`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'invoice_item_adj_key' in params:
            path_params['invoice-item-adj-key'] = params['invoice_item_adj_key']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/revenue-schedules/invoice-item-adjustments/{invoice-item-adj-key}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='POSTRevenueScheduleByTransactionResponseType',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ostr_sfor_invoice_item_distribute_by_date_range(self, invoice_item_id, request, **kwargs):  # noqa: E501
        """Create revenue schedule for Invoice Item (distribute by date range)  # noqa: E501

        Creates a revenue schedule for an Invoice Item and distribute the revenue by specifying the recognition start and end dates.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.p_ostr_sfor_invoice_item_distribute_by_date_range(invoice_item_id, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str invoice_item_id: ID of the Invoice Item, for example, e20b07fd416dcfcf0141c81164fd0a75. If the specified Invoice Item is already associated with a revenue schedule, the call will fail.  (required)
        :param POSTRevenueScheduleByDateRangeType request:  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: POSTRevenueScheduleByTransactionResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.p_ostr_sfor_invoice_item_distribute_by_date_range_with_http_info(invoice_item_id, request, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ostr_sfor_invoice_item_distribute_by_date_range_with_http_info(invoice_item_id, request, **kwargs)  # noqa: E501
            return data

    def p_ostr_sfor_invoice_item_distribute_by_date_range_with_http_info(self, invoice_item_id, request, **kwargs):  # noqa: E501
        """Create revenue schedule for Invoice Item (distribute by date range)  # noqa: E501

        Creates a revenue schedule for an Invoice Item and distribute the revenue by specifying the recognition start and end dates.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.p_ostr_sfor_invoice_item_distribute_by_date_range_with_http_info(invoice_item_id, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str invoice_item_id: ID of the Invoice Item, for example, e20b07fd416dcfcf0141c81164fd0a75. If the specified Invoice Item is already associated with a revenue schedule, the call will fail.  (required)
        :param POSTRevenueScheduleByDateRangeType request:  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: POSTRevenueScheduleByTransactionResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['invoice_item_id', 'request', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ostr_sfor_invoice_item_distribute_by_date_range" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'invoice_item_id' is set
        if ('invoice_item_id' not in params or
                params['invoice_item_id'] is None):
            raise ValueError("Missing the required parameter `invoice_item_id` when calling `p_ostr_sfor_invoice_item_distribute_by_date_range`")  # noqa: E501
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `p_ostr_sfor_invoice_item_distribute_by_date_range`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'invoice_item_id' in params:
            path_params['invoice-item-id'] = params['invoice_item_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/revenue-schedules/invoice-items/{invoice-item-id}/distribute-revenue-with-date-range', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='POSTRevenueScheduleByTransactionResponseType',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ostr_sfor_invoice_item_manual_distribution(self, invoice_item_id, request, **kwargs):  # noqa: E501
        """Create revenue schedule for Invoice Item (manual distribution)  # noqa: E501

        Creates a revenue schedule for an Invoice Item and manually distribute the revenue.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.p_ostr_sfor_invoice_item_manual_distribution(invoice_item_id, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str invoice_item_id: ID of the Invoice Item, for example, e20b07fd416dcfcf0141c81164fd0a75. If the specified Invoice Item is already associated with a revenue schedule, the call will fail.  (required)
        :param POSTRevenueScheduleByTransactionType request:  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: POSTRevenueScheduleByTransactionResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.p_ostr_sfor_invoice_item_manual_distribution_with_http_info(invoice_item_id, request, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ostr_sfor_invoice_item_manual_distribution_with_http_info(invoice_item_id, request, **kwargs)  # noqa: E501
            return data

    def p_ostr_sfor_invoice_item_manual_distribution_with_http_info(self, invoice_item_id, request, **kwargs):  # noqa: E501
        """Create revenue schedule for Invoice Item (manual distribution)  # noqa: E501

        Creates a revenue schedule for an Invoice Item and manually distribute the revenue.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.p_ostr_sfor_invoice_item_manual_distribution_with_http_info(invoice_item_id, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str invoice_item_id: ID of the Invoice Item, for example, e20b07fd416dcfcf0141c81164fd0a75. If the specified Invoice Item is already associated with a revenue schedule, the call will fail.  (required)
        :param POSTRevenueScheduleByTransactionType request:  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: POSTRevenueScheduleByTransactionResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['invoice_item_id', 'request', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ostr_sfor_invoice_item_manual_distribution" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'invoice_item_id' is set
        if ('invoice_item_id' not in params or
                params['invoice_item_id'] is None):
            raise ValueError("Missing the required parameter `invoice_item_id` when calling `p_ostr_sfor_invoice_item_manual_distribution`")  # noqa: E501
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `p_ostr_sfor_invoice_item_manual_distribution`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'invoice_item_id' in params:
            path_params['invoice-item-id'] = params['invoice_item_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/revenue-schedules/invoice-items/{invoice-item-id}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='POSTRevenueScheduleByTransactionResponseType',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ostr_sfor_subsc_charge(self, charge_key, request, **kwargs):  # noqa: E501
        """Create revenue schedule on subscription charge  # noqa: E501

        Creates a revenue schedule by specifying the subscription charge. This method is for custom unlimited revenue recognition only.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.p_ostr_sfor_subsc_charge(charge_key, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str charge_key: ID of the subscription rate plan charge; for example, 402892793e173340013e173b81000012. (required)
        :param POSTRevenueScheduleByChargeType request:  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: POSTRevenueScheduleByChargeResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.p_ostr_sfor_subsc_charge_with_http_info(charge_key, request, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ostr_sfor_subsc_charge_with_http_info(charge_key, request, **kwargs)  # noqa: E501
            return data

    def p_ostr_sfor_subsc_charge_with_http_info(self, charge_key, request, **kwargs):  # noqa: E501
        """Create revenue schedule on subscription charge  # noqa: E501

        Creates a revenue schedule by specifying the subscription charge. This method is for custom unlimited revenue recognition only.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.p_ostr_sfor_subsc_charge_with_http_info(charge_key, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str charge_key: ID of the subscription rate plan charge; for example, 402892793e173340013e173b81000012. (required)
        :param POSTRevenueScheduleByChargeType request:  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: POSTRevenueScheduleByChargeResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['charge_key', 'request', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ostr_sfor_subsc_charge" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'charge_key' is set
        if ('charge_key' not in params or
                params['charge_key'] is None):
            raise ValueError("Missing the required parameter `charge_key` when calling `p_ostr_sfor_subsc_charge`")  # noqa: E501
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `p_ostr_sfor_subsc_charge`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'charge_key' in params:
            path_params['charge-key'] = params['charge_key']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/revenue-schedules/subscription-charges/{charge-key}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='POSTRevenueScheduleByChargeResponseType',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ut_revenue_across_ap(self, rs_number, request, **kwargs):  # noqa: E501
        """Distribute revenue across accounting periods  # noqa: E501

        Distributes revenue by specifying the revenue schedule number. Request and response field descriptions and sample code are provided.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.p_ut_revenue_across_ap(rs_number, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str rs_number: Revenue schedule number. The revenue schedule number is always prefixed with \"RS\", for example, \"RS-00000001\".  (required)
        :param PUTAllocateManuallyType request:  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: PUTRevenueScheduleResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.p_ut_revenue_across_ap_with_http_info(rs_number, request, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ut_revenue_across_ap_with_http_info(rs_number, request, **kwargs)  # noqa: E501
            return data

    def p_ut_revenue_across_ap_with_http_info(self, rs_number, request, **kwargs):  # noqa: E501
        """Distribute revenue across accounting periods  # noqa: E501

        Distributes revenue by specifying the revenue schedule number. Request and response field descriptions and sample code are provided.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.p_ut_revenue_across_ap_with_http_info(rs_number, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str rs_number: Revenue schedule number. The revenue schedule number is always prefixed with \"RS\", for example, \"RS-00000001\".  (required)
        :param PUTAllocateManuallyType request:  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: PUTRevenueScheduleResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rs_number', 'request', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ut_revenue_across_ap" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rs_number' is set
        if ('rs_number' not in params or
                params['rs_number'] is None):
            raise ValueError("Missing the required parameter `rs_number` when calling `p_ut_revenue_across_ap`")  # noqa: E501
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `p_ut_revenue_across_ap`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rs_number' in params:
            path_params['rs-number'] = params['rs_number']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/revenue-schedules/{rs-number}/distribute-revenue-across-accounting-periods', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PUTRevenueScheduleResponseType',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ut_revenue_by_recognition_startand_end_dates(self, rs_number, request, **kwargs):  # noqa: E501
        """Distribute revenue by recognition start and end dates  # noqa: E501

        Distributes revenue by specifying the recognition start and end dates. Request and response field descriptions and sample code are provided.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.p_ut_revenue_by_recognition_startand_end_dates(rs_number, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str rs_number: Revenue schedule number. Specify the revenue schedule whose revenue you want to distribute.    The revenue schedule number is always prefixed with \"RS\", for example, \"RS-00000001\".  (required)
        :param PUTRSTermType request:  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: PUTRevenueScheduleResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.p_ut_revenue_by_recognition_startand_end_dates_with_http_info(rs_number, request, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ut_revenue_by_recognition_startand_end_dates_with_http_info(rs_number, request, **kwargs)  # noqa: E501
            return data

    def p_ut_revenue_by_recognition_startand_end_dates_with_http_info(self, rs_number, request, **kwargs):  # noqa: E501
        """Distribute revenue by recognition start and end dates  # noqa: E501

        Distributes revenue by specifying the recognition start and end dates. Request and response field descriptions and sample code are provided.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.p_ut_revenue_by_recognition_startand_end_dates_with_http_info(rs_number, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str rs_number: Revenue schedule number. Specify the revenue schedule whose revenue you want to distribute.    The revenue schedule number is always prefixed with \"RS\", for example, \"RS-00000001\".  (required)
        :param PUTRSTermType request:  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: PUTRevenueScheduleResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rs_number', 'request', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ut_revenue_by_recognition_startand_end_dates" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rs_number' is set
        if ('rs_number' not in params or
                params['rs_number'] is None):
            raise ValueError("Missing the required parameter `rs_number` when calling `p_ut_revenue_by_recognition_startand_end_dates`")  # noqa: E501
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `p_ut_revenue_by_recognition_startand_end_dates`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rs_number' in params:
            path_params['rs-number'] = params['rs_number']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/revenue-schedules/{rs-number}/distribute-revenue-with-date-range', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PUTRevenueScheduleResponseType',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ut_revenue_specific_date(self, rs_number, request, **kwargs):  # noqa: E501
        """Distribute revenue on specific date  # noqa: E501

        Distributes revenue on a specific recognition date. Request and response field descriptions and sample code are provided.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.p_ut_revenue_specific_date(rs_number, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str rs_number: Revenue schedule number. The revenue schedule number is always prefixed with \"RS\", for example, \"RS-00000001\".  (required)
        :param PUTSpecificDateAllocationType request:  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: PUTRevenueScheduleResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.p_ut_revenue_specific_date_with_http_info(rs_number, request, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ut_revenue_specific_date_with_http_info(rs_number, request, **kwargs)  # noqa: E501
            return data

    def p_ut_revenue_specific_date_with_http_info(self, rs_number, request, **kwargs):  # noqa: E501
        """Distribute revenue on specific date  # noqa: E501

        Distributes revenue on a specific recognition date. Request and response field descriptions and sample code are provided.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.p_ut_revenue_specific_date_with_http_info(rs_number, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str rs_number: Revenue schedule number. The revenue schedule number is always prefixed with \"RS\", for example, \"RS-00000001\".  (required)
        :param PUTSpecificDateAllocationType request:  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: PUTRevenueScheduleResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rs_number', 'request', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ut_revenue_specific_date" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rs_number' is set
        if ('rs_number' not in params or
                params['rs_number'] is None):
            raise ValueError("Missing the required parameter `rs_number` when calling `p_ut_revenue_specific_date`")  # noqa: E501
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `p_ut_revenue_specific_date`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rs_number' in params:
            path_params['rs-number'] = params['rs_number']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/revenue-schedules/{rs-number}/distribute-revenue-on-specific-date', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PUTRevenueScheduleResponseType',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_utrs_basic_info(self, rs_number, request, **kwargs):  # noqa: E501
        """Update revenue schedule basic information  # noqa: E501

        Retrieves basic information of a revenue schedule by specifying the revenue schedule number. Request and response field descriptions and sample code are provided.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.p_utrs_basic_info(rs_number, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str rs_number: Revenue schedule number. The revenue schedule number is always prefixed with \"RS\", for example, \"RS-00000001\".  (required)
        :param PUTRSBasicInfoType request:  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: CommonResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.p_utrs_basic_info_with_http_info(rs_number, request, **kwargs)  # noqa: E501
        else:
            (data) = self.p_utrs_basic_info_with_http_info(rs_number, request, **kwargs)  # noqa: E501
            return data

    def p_utrs_basic_info_with_http_info(self, rs_number, request, **kwargs):  # noqa: E501
        """Update revenue schedule basic information  # noqa: E501

        Retrieves basic information of a revenue schedule by specifying the revenue schedule number. Request and response field descriptions and sample code are provided.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.p_utrs_basic_info_with_http_info(rs_number, request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str rs_number: Revenue schedule number. The revenue schedule number is always prefixed with \"RS\", for example, \"RS-00000001\".  (required)
        :param PUTRSBasicInfoType request:  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: CommonResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rs_number', 'request', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_utrs_basic_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rs_number' is set
        if ('rs_number' not in params or
                params['rs_number'] is None):
            raise ValueError("Missing the required parameter `rs_number` when calling `p_utrs_basic_info`")  # noqa: E501
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `p_utrs_basic_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rs_number' in params:
            path_params['rs-number'] = params['rs_number']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/revenue-schedules/{rs-number}/basic-information', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CommonResponseType',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
