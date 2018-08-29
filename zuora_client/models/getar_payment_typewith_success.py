# coding: utf-8

"""
    Zuora API Reference

      # Introduction Welcome to the reference for the Zuora REST API!  <a href=\"http://en.wikipedia.org/wiki/REST_API\" target=\"_blank\">REST</a> is a web-service protocol that lends itself to rapid development by using everyday HTTP and JSON technology.  The Zuora REST API provides a broad set of operations and resources that:    * Enable Web Storefront integration from your website.   * Support self-service subscriber sign-ups and account management.   * Process revenue schedules through custom revenue rule models.   * Enable manipulation of most objects in the Zuora Object Model.  Want to share your opinion on how our API works for you? <a href=\"https://community.zuora.com/t5/Developers/API-Feedback-Form/gpm-p/21399\" target=\"_blank\">Tell us how you feel </a>about using our API and what we can do to make it better.  ## Access to the API  If you have a Zuora tenant, you can access the Zuora REST API via one of the following endpoints:  | Tenant              | Base URL for REST Endpoints | |-------------------------|-------------------------| |US Production | https://rest.zuora.com   | |US API Sandbox    | https://rest.apisandbox.zuora.com| |US Performance Test | https://rest.pt1.zuora.com | |EU Production | https://rest.eu.zuora.com | |EU Sandbox | https://rest.sandbox.eu.zuora.com |  The Production endpoint provides access to your live user data. API Sandbox tenants are a good place to test code without affecting real-world data. If you would like Zuora to provision an API Sandbox tenant for you, contact your Zuora representative for assistance.  **Note:** If you have a tenant in the Production Copy Environment, submit a request at <a href=\"http://support.zuora.com/\" target=\"_blank\">Zuora Global Support</a> to enable the Zuora REST API in your tenant and obtain the base URL for REST endpoints.  If you do not have a Zuora tenant, go to <a href=\"https://www.zuora.com/resource/zuora-test-drive\" target=\"_blank\">https://www.zuora.com/resource/zuora-test-drive</a> and sign up for a Production Test Drive tenant. The tenant comes with seed data, including a sample product catalog.  # API Changelog You can find the <a href=\"https://community.zuora.com/t5/Developers/API-Changelog/gpm-p/18092\" target=\"_blank\">Changelog</a> of the API Reference in the Zuora Community.  # Authentication  ## OAuth v2.0  Zuora recommends that you use OAuth v2.0 to authenticate to the Zuora REST API. Currently, OAuth is not available in every environment. See [Zuora Testing Environments](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/D_Zuora_Environments) for more information.  Zuora recommends you to create a dedicated API user with API write access on a tenant when authenticating via OAuth, and then create an OAuth client for this user. See <a href=\"https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users/Create_an_API_User\" target=\"_blank\">Create an API User</a> for how to do this. By creating a dedicated API user, you can control permissions of the API user without affecting other non-API users.  If a user is deactivated, all of the user's OAuth clients will be automatically deactivated.  Authenticating via OAuth requires the following steps: 1. Create a Client 2. Generate a Token 3. Make Authenticated Requests  ### Create a Client  You must first [create an OAuth client](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users#Create_an_OAuth_Client_for_a_User) in the Zuora UI. To do this, you must be an administrator of your Zuora tenant. This is a one-time operation. You will be provided with a Client ID and a Client Secret. Please note this information down, as it will be required for the next step.  **Note:** The OAuth client will be owned by a Zuora user account. If you want to perform PUT, POST, or DELETE operations using the OAuth client, the owner of the OAuth client must have a Platform role that includes the \"API Write Access\" permission.  ### Generate a Token  After creating a client, you must make a call to obtain a bearer token using the [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) operation. This operation requires the following parameters: - `client_id` - the Client ID displayed when you created the OAuth client in the previous step - `client_secret` - the Client Secret displayed when you created the OAuth client in the previous step - `grant_type` - must be set to `client_credentials`  **Note**: The Client ID and Client Secret mentioned above were displayed when you created the OAuth Client in the prior step. The [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) response specifies how long the bearer token is valid for. Call [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) again to generate a new bearer token.  ### Make Authenticated Requests  To authenticate subsequent API requests, you must provide a valid bearer token in an HTTP header:  `Authorization: Bearer {bearer_token}`  If you have [Zuora Multi-entity](https://www.zuora.com/developer/api-reference/#tag/Entities) enabled, you need to set an additional header to specify the ID of the entity that you want to access. You can use the `scope` field in the [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) response to determine whether you need to specify an entity ID.  If the `scope` field contains more than one entity ID, you must specify the ID of the entity that you want to access. For example, if the `scope` field contains `entity.1a2b7a37-3e7d-4cb3-b0e2-883de9e766cc` and `entity.c92ed977-510c-4c48-9b51-8d5e848671e9`, specify one of the following headers: - `Zuora-Entity-Ids: 1a2b7a37-3e7d-4cb3-b0e2-883de9e766cc` - `Zuora-Entity-Ids: c92ed977-510c-4c48-9b51-8d5e848671e9`  **Note**: For a limited period of time, Zuora will accept the `entityId` header as an alternative to the `Zuora-Entity-Ids` header. If you choose to set the `entityId` header, you must remove all \"-\" characters from the entity ID in the `scope` field.  If the `scope` field contains a single entity ID, you do not need to specify an entity ID.  ## Other Supported Authentication Schemes  Zuora continues to support the following additional legacy means of authentication:    * Use username and password. Include authentication with each request in the header:         * `apiAccessKeyId`      * `apiSecretAccessKey`          Zuora recommends that you create an API user specifically for making API calls. See <a href=\"https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users/Create_an_API_User\" target=\"_blank\">Create an API User</a> for more information.      * Use an authorization cookie. The cookie authorizes the user to make calls to the REST API for the duration specified in  **Administration > Security Policies > Session timeout**. The cookie expiration time is reset with this duration after every call to the REST API. To obtain a cookie, call the [Connections](https://www.zuora.com/developer/api-reference/#tag/Connections) resource with the following API user information:         *   ID         *   Password        * For CORS-enabled APIs only: Include a 'single-use' token in the request header, which re-authenticates the user with each request. See below for more details.  ### Entity Id and Entity Name  The `entityId` and `entityName` parameters are only used for [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity \"Zuora Multi-entity\"). These are the legacy parameters that Zuora will only continue to support for a period of time. Zuora recommends you to use the `Zuora-Entity-Ids` parameter instead.   The  `entityId` and `entityName` parameters specify the Id and the [name of the entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity/B_Introduction_to_Entity_and_Entity_Hierarchy#Name_and_Display_Name \"Introduction to Entity and Entity Hierarchy\") that you want to access, respectively. Note that you must have permission to access the entity.   You can specify either the `entityId` or `entityName` parameter in the authentication to access and view an entity.    * If both `entityId` and `entityName` are specified in the authentication, an error occurs.    * If neither `entityId` nor `entityName` is specified in the authentication, you will log in to the entity in which your user account is created.      To get the entity Id and entity name, you can use the GET Entities REST call. For more information, see [API User Authentication](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity/A_Overview_of_Multi-entity#API_User_Authentication \"API User Authentication\").      ### Token Authentication for CORS-Enabled APIs      The CORS mechanism enables REST API calls to Zuora to be made directly from your customer's browser, with all credit card and security information transmitted directly to Zuora. This minimizes your PCI compliance burden, allows you to implement advanced validation on your payment forms, and  makes your payment forms look just like any other part of your website.    For security reasons, instead of using cookies, an API request via CORS uses **tokens** for authentication.  The token method of authentication is only designed for use with requests that must originate from your customer's browser; **it should  not be considered a replacement to the existing cookie authentication** mechanism.  See [Zuora CORS REST](https://knowledgecenter.zuora.com/DC_Developers/REST_API/A_REST_basics/G_CORS_REST \"Zuora CORS REST\") for details on how CORS works and how you can begin to implement customer calls to the Zuora REST APIs. See  [HMAC Signatures](https://www.zuora.com/developer/api-reference/#operation/POSTHMACSignature \"HMAC Signatures\") for details on the HMAC method that returns the authentication token.  # Requests and Responses  ## Request IDs  As a general rule, when asked to supply a \"key\" for an account or subscription (accountKey, account-key, subscriptionKey, subscription-key), you can provide either the actual ID or  the number of the entity.  ## HTTP Request Body  Most of the parameters and data accompanying your requests will be contained in the body of the HTTP request.   The Zuora REST API accepts JSON in the HTTP request body. No other data format (e.g., XML) is supported.  ### Data Type  ([Actions](https://www.zuora.com/developer/api-reference/#tag/Actions) and CRUD operations only) We recommend that you do not specify the decimal values with quotation marks, commas, and spaces. Use characters of `+-0-9.eE`, for example, `5`, `1.9`, `-8.469`, and `7.7e2`. Also, Zuora does not convert currencies for decimal values.  ## Testing a Request  Use a third party client, such as [curl](https://curl.haxx.se \"curl\"), [Postman](https://www.getpostman.com \"Postman\"), or [Advanced REST Client](https://advancedrestclient.com \"Advanced REST Client\"), to test the Zuora REST API.  You can test the Zuora REST API from the Zuora API Sandbox or Production tenants. If connecting to Production, bear in mind that you are working with your live production data, not sample data or test data.  ## Testing with Credit Cards  Sooner or later it will probably be necessary to test some transactions that involve credit cards. For suggestions on how to handle this, see [Going Live With Your Payment Gateway](https://knowledgecenter.zuora.com/CB_Billing/M_Payment_Gateways/C_Managing_Payment_Gateways/B_Going_Live_Payment_Gateways#Testing_with_Credit_Cards \"C_Zuora_User_Guides/A_Billing_and_Payments/M_Payment_Gateways/C_Managing_Payment_Gateways/B_Going_Live_Payment_Gateways#Testing_with_Credit_Cards\" ).  ## Concurrent Request Limits  Zuora enforces tenant-level concurrent request limits. See <a href=\"https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits\" target=\"_blank\">Concurrent Request Limits</a> for more information.  ## Timeout Limit  If a request does not complete within 120 seconds, the request times out and Zuora returns a Gateway Timeout error.  ## Error Handling  Responses and error codes are detailed in [Responses and errors](https://knowledgecenter.zuora.com/DC_Developers/REST_API/A_REST_basics/3_Responses_and_errors \"Responses and errors\").  # Pagination  When retrieving information (using GET methods), the optional `pageSize` query parameter sets the maximum number of rows to return in a response. The maximum is `40`; larger values are treated as `40`. If this value is empty or invalid, `pageSize` typically defaults to `10`.  The default value for the maximum number of rows retrieved can be overridden at the method level.  If more rows are available, the response will include a `nextPage` element, which contains a URL for requesting the next page.  If this value is not provided, no more rows are available. No \"previous page\" element is explicitly provided; to support backward paging, use the previous call.  ## Array Size  For data items that are not paginated, the REST API supports arrays of up to 300 rows.  Thus, for instance, repeated pagination can retrieve thousands of customer accounts, but within any account an array of no more than 300 rate plans is returned.  # API Versions  The Zuora REST API are version controlled. Versioning ensures that Zuora REST API changes are backward compatible. Zuora uses a major and minor version nomenclature to manage changes. By specifying a version in a REST request, you can get expected responses regardless of future changes to the API.  ## Major Version  The major version number of the REST API appears in the REST URL. Currently, Zuora only supports the **v1** major version. For example, `POST https://rest.zuora.com/v1/subscriptions`.  ## Minor Version  Zuora uses minor versions for the REST API to control small changes. For example, a field in a REST method is deprecated and a new field is used to replace it.   Some fields in the REST methods are supported as of minor versions. If a field is not noted with a minor version, this field is available for all minor versions. If a field is noted with a minor version, this field is in version control. You must specify the supported minor version in the request header to process without an error.   If a field is in version control, it is either with a minimum minor version or a maximum minor version, or both of them. You can only use this field with the minor version between the minimum and the maximum minor versions. For example, the `invoiceCollect` field in the POST Subscription method is in version control and its maximum minor version is 189.0. You can only use this field with the minor version 189.0 or earlier.  If you specify a version number in the request header that is not supported, Zuora will use the minimum minor version of the REST API. In our REST API documentation, if a field or feature requires a minor version number, we note that in the field description.  You only need to specify the version number when you use the fields require a minor version. To specify the minor version, set the `zuora-version` parameter to the minor version number in the request header for the request call. For example, the `collect` field is in 196.0 minor version. If you want to use this field for the POST Subscription method, set the  `zuora-version` parameter to `196.0` in the request header. The `zuora-version` parameter is case sensitive.  For all the REST API fields, by default, if the minor version is not specified in the request header, Zuora will use the minimum minor version of the REST API to avoid breaking your integration.   ### Minor Version History  The supported minor versions are not serial. This section documents the changes made to each Zuora REST API minor version.  The following table lists the supported versions and the fields that have a Zuora REST API minor version.  | Fields         | Minor Version      | REST Methods    | Description | |:--------|:--------|:--------|:--------| | invoiceCollect | 189.0 and earlier  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice and collects a payment for a subscription. | | collect        | 196.0 and later    | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Collects an automatic payment for a subscription. | | invoice | 196.0 and 207.0| [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice for a subscription. | | invoiceTargetDate | 196.0 and earlier  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") |Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | invoiceTargetDate | 207.0 and earlier  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | targetDate | 207.0 and later | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") |Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | targetDate | 211.0 and later | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | includeExisting DraftInvoiceItems | 196.0 and earlier| [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | Specifies whether to include draft invoice items in subscription previews. Specify it to be `true` (default) to include draft invoice items in the preview result. Specify it to be `false` to excludes draft invoice items in the preview result. | | includeExisting DraftDocItems | 207.0 and later  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | Specifies whether to include draft invoice items in subscription previews. Specify it to be `true` (default) to include draft invoice items in the preview result. Specify it to be `false` to excludes draft invoice items in the preview result. | | previewType | 196.0 and earlier| [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | The type of preview you will receive. The possible values are `InvoiceItem`(default), `ChargeMetrics`, and `InvoiceItemChargeMetrics`. | | previewType | 207.0 and later  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | The type of preview you will receive. The possible values are `LegalDoc`(default), `ChargeMetrics`, and `LegalDocChargeMetrics`. | | runBilling  | 211.0 and later  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice or credit memo for a subscription. **Note:** Credit memos are only available if you have the Invoice Settlement feature enabled. | | invoiceDate | 214.0 and earlier  | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date that should appear on the invoice being generated, as `yyyy-mm-dd`. | | invoiceTargetDate | 214.0 and earlier  | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date through which to calculate charges on this account if an invoice is generated, as `yyyy-mm-dd`. | | documentDate | 215.0 and later | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date that should appear on the invoice and credit memo being generated, as `yyyy-mm-dd`. | | targetDate | 215.0 and later | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date through which to calculate charges on this account if an invoice or a credit memo is generated, as `yyyy-mm-dd`. | | memoItemAmount | 223.0 and earlier | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | Amount of the memo item. | | amount | 224.0 and later | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | Amount of the memo item. | | subscriptionNumbers | 222.4 and earlier | [Create order](https://www.zuora.com/developer/api-reference/#operation/POST_Order \"Create order\") | Container for the subscription numbers of the subscriptions in an order. | | subscriptions | 223.0 and later | [Create order](https://www.zuora.com/developer/api-reference/#operation/POST_Order \"Create order\") | Container for the subscription numbers and statuses in an order. |   #### Version 207.0 and Later  The response structure of the [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") and [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") methods are changed. The following invoice related response fields are moved to the invoice container:    * amount   * amountWithoutTax   * taxAmount   * invoiceItems   * targetDate   * chargeMetrics  # Zuora Object Model  The following diagram presents a high-level view of the key Zuora objects. Click the image to open it in a new tab to resize it.  <a href=\"https://www.zuora.com/wp-content/uploads/2017/01/ZuoraERD.jpeg\" target=\"_blank\"><img src=\"https://www.zuora.com/wp-content/uploads/2017/01/ZuoraERD.jpeg\" alt=\"Zuora Object Model Diagram\"></a>  See the following articles for information about other parts of the Zuora business object model:    * <a href=\"https://knowledgecenter.zuora.com/CB_Billing/Invoice_Settlement/D_Invoice_Settlement_Object_Model\" target=\"_blank\">Invoice Settlement Object Model</a>   * <a href=\"https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/BA_Orders_Object_Model\" target=\"_blank\">Orders Object Model</a>  You can use the [Describe object](https://www.zuora.com/developer/api-reference/#operation/GET_Describe) operation to list the fields of each Zuora object that is available in your tenant. When you call the operation, you must specify the API name of the Zuora object.  The following table provides the API name of each Zuora object:  | Object                                        | API Name                                   | |-----------------------------------------------|--------------------------------------------| | Account                                       | `Account`                                  | | Accounting Code                               | `AccountingCode`                           | | Accounting Period                             | `AccountingPeriod`                         | | Amendment                                     | `Amendment`                                | | Application Group                             | `ApplicationGroup`                         | | Billing Run                                   | <p>`BillingRun`</p><p>**Note:** The API name of this object is `BillingRun` in the [Describe object](https://www.zuora.com/developer/api-reference/#operation/GET_Describe) operation and Export ZOQL queries only. Otherwise, the API name of this object is `BillRun`.</p> | | Contact                                       | `Contact`                                  | | Contact Snapshot                              | `ContactSnapshot`                          | | Credit Balance Adjustment                     | `CreditBalanceAdjustment`                  | | Credit Memo                                   | `CreditMemo`                               | | Credit Memo Application                       | `CreditMemoApplication`                    | | Credit Memo Application Item                  | `CreditMemoApplicationItem`                | | Credit Memo Item                              | `CreditMemoItem`                           | | Credit Memo Part                              | `CreditMemoPart`                           | | Credit Memo Part Item                         | `CreditMemoPartItem`                       | | Credit Taxation Item                          | `CreditTaxationItem`                       | | Custom Exchange Rate                          | `FXCustomRate`                             | | Debit Memo                                    | `DebitMemo`                                | | Debit Memo Item                               | `DebitMemoItem`                            | | Debit Taxation Item                           | `DebitTaxationItem`                        | | Discount Applied Metrics                      | `DiscountAppliedMetrics`                   | | Entity                                        | `Tenant`                                   | | Gateway Reconciliation Event                  | `PaymentGatewayReconciliationEventLog`     | | Gateway Reconciliation Job                    | `PaymentReconciliationJob`                 | | Gateway Reconciliation Log                    | `PaymentReconciliationLog`                 | | Invoice                                       | `Invoice`                                  | | Invoice Adjustment                            | `InvoiceAdjustment`                        | | Invoice Item                                  | `InvoiceItem`                              | | Invoice Item Adjustment                       | `InvoiceItemAdjustment`                    | | Invoice Payment                               | `InvoicePayment`                           | | Journal Entry                                 | `JournalEntry`                             | | Journal Entry Item                            | `JournalEntryItem`                         | | Journal Run                                   | `JournalRun`                               | | Order                                         | `Order`                                    | | Order Action                                  | `OrderAction`                              | | Order ELP                                     | `OrderElp`                                 | | Order Item                                    | `OrderItem`                                | | Order MRR                                     | `OrderMrr`                                 | | Order Quantity                                | `OrderQuantity`                            | | Order TCB                                     | `OrderTcb`                                 | | Order TCV                                     | `OrderTcv`                                 | | Payment                                       | `Payment`                                  | | Payment Application                           | `PaymentApplication`                       | | Payment Application Item                      | `PaymentApplicationItem`                   | | Payment Method                                | `PaymentMethod`                            | | Payment Method Snapshot                       | `PaymentMethodSnapshot`                    | | Payment Method Transaction Log                | `PaymentMethodTransactionLog`              | | Payment Method Update                         | `UpdaterDetail`                            | | Payment Part                                  | `PaymentPart`                              | | Payment Part Item                             | `PaymentPartItem`                          | | Payment Run                                   | `PaymentRun`                               | | Payment Transaction Log                       | `PaymentTransactionLog`                    | | Processed Usage                               | `ProcessedUsage`                           | | Product                                       | `Product`                                  | | Product Rate Plan                             | `ProductRatePlan`                          | | Product Rate Plan Charge                      | `ProductRatePlanCharge`                    | | Product Rate Plan Charge Tier                 | `ProductRatePlanChargeTier`                | | Rate Plan                                     | `RatePlan`                                 | | Rate Plan Charge                              | `RatePlanCharge`                           | | Rate Plan Charge Tier                         | `RatePlanChargeTier`                       | | Refund                                        | `Refund`                                   | | Refund Application                            | `RefundApplication`                        | | Refund Application Item                       | `RefundApplicationItem`                    | | Refund Invoice Payment                        | `RefundInvoicePayment`                     | | Refund Part                                   | `RefundPart`                               | | Refund Part Item                              | `RefundPartItem`                           | | Refund Transaction Log                        | `RefundTransactionLog`                     | | Revenue Charge Summary                        | `RevenueChargeSummary`                     | | Revenue Charge Summary Item                   | `RevenueChargeSummaryItem`                 | | Revenue Event                                 | `RevenueEvent`                             | | Revenue Event Credit Memo Item                | `RevenueEventCreditMemoItem`               | | Revenue Event Debit Memo Item                 | `RevenueEventDebitMemoItem`                | | Revenue Event Invoice Item                    | `RevenueEventInvoiceItem`                  | | Revenue Event Invoice Item Adjustment         | `RevenueEventInvoiceItemAdjustment`        | | Revenue Event Item                            | `RevenueEventItem`                         | | Revenue Event Item Credit Memo Item           | `RevenueEventItemCreditMemoItem`           | | Revenue Event Item Debit Memo Item            | `RevenueEventItemDebitMemoItem`            | | Revenue Event Item Invoice Item               | `RevenueEventItemInvoiceItem`              | | Revenue Event Item Invoice Item Adjustment    | `RevenueEventItemInvoiceItemAdjustment`    | | Revenue Event Type                            | `RevenueEventType`                         | | Revenue Schedule                              | `RevenueSchedule`                          | | Revenue Schedule Credit Memo Item             | `RevenueScheduleCreditMemoItem`            | | Revenue Schedule Debit Memo Item              | `RevenueScheduleDebitMemoItem`             | | Revenue Schedule Invoice Item                 | `RevenueScheduleInvoiceItem`               | | Revenue Schedule Invoice Item Adjustment      | `RevenueScheduleInvoiceItemAdjustment`     | | Revenue Schedule Item                         | `RevenueScheduleItem`                      | | Revenue Schedule Item Credit Memo Item        | `RevenueScheduleItemCreditMemoItem`        | | Revenue Schedule Item Debit Memo Item         | `RevenueScheduleItemDebitMemoItem`         | | Revenue Schedule Item Invoice Item            | `RevenueScheduleItemInvoiceItem`           | | Revenue Schedule Item Invoice Item Adjustment | `RevenueScheduleItemInvoiceItemAdjustment` | | Subscription                                  | `Subscription`                             | | Taxable Item Snapshot                         | `TaxableItemSnapshot`                      | | Taxation Item                                 | `TaxationItem`                             | | Updater Batch                                 | `UpdaterBatch`                             | | Usage                                         | `Usage`                                    |   # noqa: E501

    OpenAPI spec version: 2018-08-23
    Contact: docs@zuora.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from zuora_client.models.getar_payment_type_finance_information import GETARPaymentTypeFinanceInformation  # noqa: F401,E501
from zuora_client.models.payment_object_custom_fields import PaymentObjectCustomFields  # noqa: F401,E501
from zuora_client.models.payment_object_ns_fields import PaymentObjectNSFields  # noqa: F401,E501


class GETARPaymentTypewithSuccess(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'integration_id__ns': 'str',
        'integration_status__ns': 'str',
        'origin__ns': 'str',
        'sync_date__ns': 'str',
        'transaction__ns': 'str',
        'account_id': 'str',
        'amount': 'float',
        'applied_amount': 'float',
        'auth_transaction_id': 'str',
        'bank_identification_number': 'str',
        'cancelled_on': 'datetime',
        'comment': 'str',
        'created_by_id': 'str',
        'created_date': 'datetime',
        'credit_balance_amount': 'float',
        'currency': 'str',
        'effective_date': 'datetime',
        'finance_information': 'GETARPaymentTypeFinanceInformation',
        'gateway_id': 'str',
        'gateway_order_id': 'str',
        'gateway_response': 'str',
        'gateway_response_code': 'str',
        'gateway_state': 'str',
        'id': 'str',
        'marked_for_submission_on': 'datetime',
        'number': 'str',
        'payment_method_id': 'str',
        'payment_method_snapshot_id': 'str',
        'reference_id': 'str',
        'refund_amount': 'float',
        'second_payment_reference_id': 'str',
        'settled_on': 'datetime',
        'soft_descriptor': 'str',
        'soft_descriptor_phone': 'str',
        'status': 'str',
        'submitted_on': 'datetime',
        'type': 'str',
        'unapplied_amount': 'float',
        'updated_by_id': 'str',
        'updated_date': 'datetime'
    }

    attribute_map = {
        'integration_id__ns': 'IntegrationId__NS',
        'integration_status__ns': 'IntegrationStatus__NS',
        'origin__ns': 'Origin__NS',
        'sync_date__ns': 'SyncDate__NS',
        'transaction__ns': 'Transaction__NS',
        'account_id': 'accountId',
        'amount': 'amount',
        'applied_amount': 'appliedAmount',
        'auth_transaction_id': 'authTransactionId',
        'bank_identification_number': 'bankIdentificationNumber',
        'cancelled_on': 'cancelledOn',
        'comment': 'comment',
        'created_by_id': 'createdById',
        'created_date': 'createdDate',
        'credit_balance_amount': 'creditBalanceAmount',
        'currency': 'currency',
        'effective_date': 'effectiveDate',
        'finance_information': 'financeInformation',
        'gateway_id': 'gatewayId',
        'gateway_order_id': 'gatewayOrderId',
        'gateway_response': 'gatewayResponse',
        'gateway_response_code': 'gatewayResponseCode',
        'gateway_state': 'gatewayState',
        'id': 'id',
        'marked_for_submission_on': 'markedForSubmissionOn',
        'number': 'number',
        'payment_method_id': 'paymentMethodId',
        'payment_method_snapshot_id': 'paymentMethodSnapshotId',
        'reference_id': 'referenceId',
        'refund_amount': 'refundAmount',
        'second_payment_reference_id': 'secondPaymentReferenceId',
        'settled_on': 'settledOn',
        'soft_descriptor': 'softDescriptor',
        'soft_descriptor_phone': 'softDescriptorPhone',
        'status': 'status',
        'submitted_on': 'submittedOn',
        'type': 'type',
        'unapplied_amount': 'unappliedAmount',
        'updated_by_id': 'updatedById',
        'updated_date': 'updatedDate'
    }

    def __init__(self, integration_id__ns=None, integration_status__ns=None, origin__ns=None, sync_date__ns=None, transaction__ns=None, account_id=None, amount=None, applied_amount=None, auth_transaction_id=None, bank_identification_number=None, cancelled_on=None, comment=None, created_by_id=None, created_date=None, credit_balance_amount=None, currency=None, effective_date=None, finance_information=None, gateway_id=None, gateway_order_id=None, gateway_response=None, gateway_response_code=None, gateway_state=None, id=None, marked_for_submission_on=None, number=None, payment_method_id=None, payment_method_snapshot_id=None, reference_id=None, refund_amount=None, second_payment_reference_id=None, settled_on=None, soft_descriptor=None, soft_descriptor_phone=None, status=None, submitted_on=None, type=None, unapplied_amount=None, updated_by_id=None, updated_date=None):  # noqa: E501
        """GETARPaymentTypewithSuccess - a model defined in Swagger"""  # noqa: E501

        self._integration_id__ns = None
        self._integration_status__ns = None
        self._origin__ns = None
        self._sync_date__ns = None
        self._transaction__ns = None
        self._account_id = None
        self._amount = None
        self._applied_amount = None
        self._auth_transaction_id = None
        self._bank_identification_number = None
        self._cancelled_on = None
        self._comment = None
        self._created_by_id = None
        self._created_date = None
        self._credit_balance_amount = None
        self._currency = None
        self._effective_date = None
        self._finance_information = None
        self._gateway_id = None
        self._gateway_order_id = None
        self._gateway_response = None
        self._gateway_response_code = None
        self._gateway_state = None
        self._id = None
        self._marked_for_submission_on = None
        self._number = None
        self._payment_method_id = None
        self._payment_method_snapshot_id = None
        self._reference_id = None
        self._refund_amount = None
        self._second_payment_reference_id = None
        self._settled_on = None
        self._soft_descriptor = None
        self._soft_descriptor_phone = None
        self._status = None
        self._submitted_on = None
        self._type = None
        self._unapplied_amount = None
        self._updated_by_id = None
        self._updated_date = None
        self.discriminator = None

        if integration_id__ns is not None:
            self.integration_id__ns = integration_id__ns
        if integration_status__ns is not None:
            self.integration_status__ns = integration_status__ns
        if origin__ns is not None:
            self.origin__ns = origin__ns
        if sync_date__ns is not None:
            self.sync_date__ns = sync_date__ns
        if transaction__ns is not None:
            self.transaction__ns = transaction__ns
        if account_id is not None:
            self.account_id = account_id
        if amount is not None:
            self.amount = amount
        if applied_amount is not None:
            self.applied_amount = applied_amount
        if auth_transaction_id is not None:
            self.auth_transaction_id = auth_transaction_id
        if bank_identification_number is not None:
            self.bank_identification_number = bank_identification_number
        if cancelled_on is not None:
            self.cancelled_on = cancelled_on
        if comment is not None:
            self.comment = comment
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_date is not None:
            self.created_date = created_date
        if credit_balance_amount is not None:
            self.credit_balance_amount = credit_balance_amount
        if currency is not None:
            self.currency = currency
        if effective_date is not None:
            self.effective_date = effective_date
        if finance_information is not None:
            self.finance_information = finance_information
        if gateway_id is not None:
            self.gateway_id = gateway_id
        if gateway_order_id is not None:
            self.gateway_order_id = gateway_order_id
        if gateway_response is not None:
            self.gateway_response = gateway_response
        if gateway_response_code is not None:
            self.gateway_response_code = gateway_response_code
        if gateway_state is not None:
            self.gateway_state = gateway_state
        if id is not None:
            self.id = id
        if marked_for_submission_on is not None:
            self.marked_for_submission_on = marked_for_submission_on
        if number is not None:
            self.number = number
        if payment_method_id is not None:
            self.payment_method_id = payment_method_id
        if payment_method_snapshot_id is not None:
            self.payment_method_snapshot_id = payment_method_snapshot_id
        if reference_id is not None:
            self.reference_id = reference_id
        if refund_amount is not None:
            self.refund_amount = refund_amount
        if second_payment_reference_id is not None:
            self.second_payment_reference_id = second_payment_reference_id
        if settled_on is not None:
            self.settled_on = settled_on
        if soft_descriptor is not None:
            self.soft_descriptor = soft_descriptor
        if soft_descriptor_phone is not None:
            self.soft_descriptor_phone = soft_descriptor_phone
        if status is not None:
            self.status = status
        if submitted_on is not None:
            self.submitted_on = submitted_on
        if type is not None:
            self.type = type
        if unapplied_amount is not None:
            self.unapplied_amount = unapplied_amount
        if updated_by_id is not None:
            self.updated_by_id = updated_by_id
        if updated_date is not None:
            self.updated_date = updated_date

    @property
    def integration_id__ns(self):
        """Gets the integration_id__ns of this GETARPaymentTypewithSuccess.  # noqa: E501

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_id__ns of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._integration_id__ns

    @integration_id__ns.setter
    def integration_id__ns(self, integration_id__ns):
        """Sets the integration_id__ns of this GETARPaymentTypewithSuccess.

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_id__ns: The integration_id__ns of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: str
        """
        if integration_id__ns is not None and len(integration_id__ns) > 255:
            raise ValueError("Invalid value for `integration_id__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_id__ns = integration_id__ns

    @property
    def integration_status__ns(self):
        """Gets the integration_status__ns of this GETARPaymentTypewithSuccess.  # noqa: E501

        Status of the payment's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_status__ns of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._integration_status__ns

    @integration_status__ns.setter
    def integration_status__ns(self, integration_status__ns):
        """Sets the integration_status__ns of this GETARPaymentTypewithSuccess.

        Status of the payment's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_status__ns: The integration_status__ns of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: str
        """
        if integration_status__ns is not None and len(integration_status__ns) > 255:
            raise ValueError("Invalid value for `integration_status__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_status__ns = integration_status__ns

    @property
    def origin__ns(self):
        """Gets the origin__ns of this GETARPaymentTypewithSuccess.  # noqa: E501

        Origin of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The origin__ns of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._origin__ns

    @origin__ns.setter
    def origin__ns(self, origin__ns):
        """Sets the origin__ns of this GETARPaymentTypewithSuccess.

        Origin of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param origin__ns: The origin__ns of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: str
        """
        if origin__ns is not None and len(origin__ns) > 255:
            raise ValueError("Invalid value for `origin__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._origin__ns = origin__ns

    @property
    def sync_date__ns(self):
        """Gets the sync_date__ns of this GETARPaymentTypewithSuccess.  # noqa: E501

        Date when the payment was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The sync_date__ns of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._sync_date__ns

    @sync_date__ns.setter
    def sync_date__ns(self, sync_date__ns):
        """Sets the sync_date__ns of this GETARPaymentTypewithSuccess.

        Date when the payment was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param sync_date__ns: The sync_date__ns of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: str
        """
        if sync_date__ns is not None and len(sync_date__ns) > 255:
            raise ValueError("Invalid value for `sync_date__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._sync_date__ns = sync_date__ns

    @property
    def transaction__ns(self):
        """Gets the transaction__ns of this GETARPaymentTypewithSuccess.  # noqa: E501

        Related transaction in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The transaction__ns of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._transaction__ns

    @transaction__ns.setter
    def transaction__ns(self, transaction__ns):
        """Sets the transaction__ns of this GETARPaymentTypewithSuccess.

        Related transaction in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param transaction__ns: The transaction__ns of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: str
        """
        if transaction__ns is not None and len(transaction__ns) > 255:
            raise ValueError("Invalid value for `transaction__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._transaction__ns = transaction__ns

    @property
    def account_id(self):
        """Gets the account_id of this GETARPaymentTypewithSuccess.  # noqa: E501

        The ID of the customer account that the payment is for.   # noqa: E501

        :return: The account_id of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this GETARPaymentTypewithSuccess.

        The ID of the customer account that the payment is for.   # noqa: E501

        :param account_id: The account_id of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def amount(self):
        """Gets the amount of this GETARPaymentTypewithSuccess.  # noqa: E501

        The total amount of the payment.   # noqa: E501

        :return: The amount of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GETARPaymentTypewithSuccess.

        The total amount of the payment.   # noqa: E501

        :param amount: The amount of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def applied_amount(self):
        """Gets the applied_amount of this GETARPaymentTypewithSuccess.  # noqa: E501

        The applied amount of the payment.   # noqa: E501

        :return: The applied_amount of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: float
        """
        return self._applied_amount

    @applied_amount.setter
    def applied_amount(self, applied_amount):
        """Sets the applied_amount of this GETARPaymentTypewithSuccess.

        The applied amount of the payment.   # noqa: E501

        :param applied_amount: The applied_amount of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: float
        """

        self._applied_amount = applied_amount

    @property
    def auth_transaction_id(self):
        """Gets the auth_transaction_id of this GETARPaymentTypewithSuccess.  # noqa: E501

        The authorization transaction ID from the payment gateway.   # noqa: E501

        :return: The auth_transaction_id of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._auth_transaction_id

    @auth_transaction_id.setter
    def auth_transaction_id(self, auth_transaction_id):
        """Sets the auth_transaction_id of this GETARPaymentTypewithSuccess.

        The authorization transaction ID from the payment gateway.   # noqa: E501

        :param auth_transaction_id: The auth_transaction_id of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._auth_transaction_id = auth_transaction_id

    @property
    def bank_identification_number(self):
        """Gets the bank_identification_number of this GETARPaymentTypewithSuccess.  # noqa: E501

        The first six digits of the credit card or debit card used for the payment, when applicable.   # noqa: E501

        :return: The bank_identification_number of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._bank_identification_number

    @bank_identification_number.setter
    def bank_identification_number(self, bank_identification_number):
        """Sets the bank_identification_number of this GETARPaymentTypewithSuccess.

        The first six digits of the credit card or debit card used for the payment, when applicable.   # noqa: E501

        :param bank_identification_number: The bank_identification_number of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._bank_identification_number = bank_identification_number

    @property
    def cancelled_on(self):
        """Gets the cancelled_on of this GETARPaymentTypewithSuccess.  # noqa: E501

        The date and time when the payment was cancelled, in `yyyy-mm-dd hh:mm:ss` format.   # noqa: E501

        :return: The cancelled_on of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: datetime
        """
        return self._cancelled_on

    @cancelled_on.setter
    def cancelled_on(self, cancelled_on):
        """Sets the cancelled_on of this GETARPaymentTypewithSuccess.

        The date and time when the payment was cancelled, in `yyyy-mm-dd hh:mm:ss` format.   # noqa: E501

        :param cancelled_on: The cancelled_on of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: datetime
        """

        self._cancelled_on = cancelled_on

    @property
    def comment(self):
        """Gets the comment of this GETARPaymentTypewithSuccess.  # noqa: E501

        Comments about the payment.   # noqa: E501

        :return: The comment of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this GETARPaymentTypewithSuccess.

        Comments about the payment.   # noqa: E501

        :param comment: The comment of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def created_by_id(self):
        """Gets the created_by_id of this GETARPaymentTypewithSuccess.  # noqa: E501

        The ID of the Zuora user who created the payment part.   # noqa: E501

        :return: The created_by_id of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this GETARPaymentTypewithSuccess.

        The ID of the Zuora user who created the payment part.   # noqa: E501

        :param created_by_id: The created_by_id of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def created_date(self):
        """Gets the created_date of this GETARPaymentTypewithSuccess.  # noqa: E501

        The date and time when the payment was created, in `yyyy-mm-dd hh:mm:ss` format. For example, 2017-03-01 15:31:10.   # noqa: E501

        :return: The created_date of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this GETARPaymentTypewithSuccess.

        The date and time when the payment was created, in `yyyy-mm-dd hh:mm:ss` format. For example, 2017-03-01 15:31:10.   # noqa: E501

        :param created_date: The created_date of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def credit_balance_amount(self):
        """Gets the credit_balance_amount of this GETARPaymentTypewithSuccess.  # noqa: E501

        The amount that the payment transfers to the credit balance. The value is not `0` only for those payments that come from legacy payment operations performed without the Invoice Settlement feature.   # noqa: E501

        :return: The credit_balance_amount of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: float
        """
        return self._credit_balance_amount

    @credit_balance_amount.setter
    def credit_balance_amount(self, credit_balance_amount):
        """Sets the credit_balance_amount of this GETARPaymentTypewithSuccess.

        The amount that the payment transfers to the credit balance. The value is not `0` only for those payments that come from legacy payment operations performed without the Invoice Settlement feature.   # noqa: E501

        :param credit_balance_amount: The credit_balance_amount of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: float
        """

        self._credit_balance_amount = credit_balance_amount

    @property
    def currency(self):
        """Gets the currency of this GETARPaymentTypewithSuccess.  # noqa: E501

        A currency defined in the web-based UI administrative settings.  For more information about the supported currencies and , see [ISO Currency Codes] (https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/D_Country%2C_State%2C_and_Province_Codes/D_Currencies_and_Their_3-Letter_Codes).   # noqa: E501

        :return: The currency of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this GETARPaymentTypewithSuccess.

        A currency defined in the web-based UI administrative settings.  For more information about the supported currencies and , see [ISO Currency Codes] (https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/D_Country%2C_State%2C_and_Province_Codes/D_Currencies_and_Their_3-Letter_Codes).   # noqa: E501

        :param currency: The currency of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def effective_date(self):
        """Gets the effective_date of this GETARPaymentTypewithSuccess.  # noqa: E501

        The date and time when the payment takes effect, in `yyyy-mm-dd hh:mm:ss` format.   # noqa: E501

        :return: The effective_date of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this GETARPaymentTypewithSuccess.

        The date and time when the payment takes effect, in `yyyy-mm-dd hh:mm:ss` format.   # noqa: E501

        :param effective_date: The effective_date of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: datetime
        """

        self._effective_date = effective_date

    @property
    def finance_information(self):
        """Gets the finance_information of this GETARPaymentTypewithSuccess.  # noqa: E501


        :return: The finance_information of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: GETARPaymentTypeFinanceInformation
        """
        return self._finance_information

    @finance_information.setter
    def finance_information(self, finance_information):
        """Sets the finance_information of this GETARPaymentTypewithSuccess.


        :param finance_information: The finance_information of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: GETARPaymentTypeFinanceInformation
        """

        self._finance_information = finance_information

    @property
    def gateway_id(self):
        """Gets the gateway_id of this GETARPaymentTypewithSuccess.  # noqa: E501

        The ID of the gateway instance that processes the payment.   # noqa: E501

        :return: The gateway_id of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """Sets the gateway_id of this GETARPaymentTypewithSuccess.

        The ID of the gateway instance that processes the payment.   # noqa: E501

        :param gateway_id: The gateway_id of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._gateway_id = gateway_id

    @property
    def gateway_order_id(self):
        """Gets the gateway_order_id of this GETARPaymentTypewithSuccess.  # noqa: E501

        A merchant-specified natural key value that can be passed to the electronic payment gateway when a payment is created.   # noqa: E501

        :return: The gateway_order_id of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._gateway_order_id

    @gateway_order_id.setter
    def gateway_order_id(self, gateway_order_id):
        """Sets the gateway_order_id of this GETARPaymentTypewithSuccess.

        A merchant-specified natural key value that can be passed to the electronic payment gateway when a payment is created.   # noqa: E501

        :param gateway_order_id: The gateway_order_id of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._gateway_order_id = gateway_order_id

    @property
    def gateway_response(self):
        """Gets the gateway_response of this GETARPaymentTypewithSuccess.  # noqa: E501

        The message returned from the payment gateway for the payment. This message is gateway-dependent.   # noqa: E501

        :return: The gateway_response of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._gateway_response

    @gateway_response.setter
    def gateway_response(self, gateway_response):
        """Sets the gateway_response of this GETARPaymentTypewithSuccess.

        The message returned from the payment gateway for the payment. This message is gateway-dependent.   # noqa: E501

        :param gateway_response: The gateway_response of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._gateway_response = gateway_response

    @property
    def gateway_response_code(self):
        """Gets the gateway_response_code of this GETARPaymentTypewithSuccess.  # noqa: E501

        The code returned from the payment gateway for the payment. This code is gateway-dependent.   # noqa: E501

        :return: The gateway_response_code of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._gateway_response_code

    @gateway_response_code.setter
    def gateway_response_code(self, gateway_response_code):
        """Sets the gateway_response_code of this GETARPaymentTypewithSuccess.

        The code returned from the payment gateway for the payment. This code is gateway-dependent.   # noqa: E501

        :param gateway_response_code: The gateway_response_code of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._gateway_response_code = gateway_response_code

    @property
    def gateway_state(self):
        """Gets the gateway_state of this GETARPaymentTypewithSuccess.  # noqa: E501

        The status of the payment in the gateway; use for reconciliation.    # noqa: E501

        :return: The gateway_state of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._gateway_state

    @gateway_state.setter
    def gateway_state(self, gateway_state):
        """Sets the gateway_state of this GETARPaymentTypewithSuccess.

        The status of the payment in the gateway; use for reconciliation.    # noqa: E501

        :param gateway_state: The gateway_state of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: str
        """
        allowed_values = ["MarkedForSubmission", "Submitted", "Settled", "NotSubmitted", "FailedToSettle"]  # noqa: E501
        if gateway_state not in allowed_values:
            raise ValueError(
                "Invalid value for `gateway_state` ({0}), must be one of {1}"  # noqa: E501
                .format(gateway_state, allowed_values)
            )

        self._gateway_state = gateway_state

    @property
    def id(self):
        """Gets the id of this GETARPaymentTypewithSuccess.  # noqa: E501

        The unique ID of the payment. For example, 4028905f5a87c0ff015a87eb6b75007f.   # noqa: E501

        :return: The id of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GETARPaymentTypewithSuccess.

        The unique ID of the payment. For example, 4028905f5a87c0ff015a87eb6b75007f.   # noqa: E501

        :param id: The id of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def marked_for_submission_on(self):
        """Gets the marked_for_submission_on of this GETARPaymentTypewithSuccess.  # noqa: E501

        The date and time when a payment was marked and waiting for batch submission to the payment process, in `yyyy-mm-dd hh:mm:ss` format.   # noqa: E501

        :return: The marked_for_submission_on of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: datetime
        """
        return self._marked_for_submission_on

    @marked_for_submission_on.setter
    def marked_for_submission_on(self, marked_for_submission_on):
        """Sets the marked_for_submission_on of this GETARPaymentTypewithSuccess.

        The date and time when a payment was marked and waiting for batch submission to the payment process, in `yyyy-mm-dd hh:mm:ss` format.   # noqa: E501

        :param marked_for_submission_on: The marked_for_submission_on of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: datetime
        """

        self._marked_for_submission_on = marked_for_submission_on

    @property
    def number(self):
        """Gets the number of this GETARPaymentTypewithSuccess.  # noqa: E501

        The unique identification number of the payment. For example, P-00000001.   # noqa: E501

        :return: The number of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this GETARPaymentTypewithSuccess.

        The unique identification number of the payment. For example, P-00000001.   # noqa: E501

        :param number: The number of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def payment_method_id(self):
        """Gets the payment_method_id of this GETARPaymentTypewithSuccess.  # noqa: E501

        The unique ID of the payment method that the customer used to make the payment.   # noqa: E501

        :return: The payment_method_id of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, payment_method_id):
        """Sets the payment_method_id of this GETARPaymentTypewithSuccess.

        The unique ID of the payment method that the customer used to make the payment.   # noqa: E501

        :param payment_method_id: The payment_method_id of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._payment_method_id = payment_method_id

    @property
    def payment_method_snapshot_id(self):
        """Gets the payment_method_snapshot_id of this GETARPaymentTypewithSuccess.  # noqa: E501

        The unique ID of the payment method snapshot which is a copy of the particular Payment Method used in a transaction.   # noqa: E501

        :return: The payment_method_snapshot_id of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._payment_method_snapshot_id

    @payment_method_snapshot_id.setter
    def payment_method_snapshot_id(self, payment_method_snapshot_id):
        """Sets the payment_method_snapshot_id of this GETARPaymentTypewithSuccess.

        The unique ID of the payment method snapshot which is a copy of the particular Payment Method used in a transaction.   # noqa: E501

        :param payment_method_snapshot_id: The payment_method_snapshot_id of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._payment_method_snapshot_id = payment_method_snapshot_id

    @property
    def reference_id(self):
        """Gets the reference_id of this GETARPaymentTypewithSuccess.  # noqa: E501

        The transaction ID returned by the payment gateway. Use this field to reconcile payments between your gateway and Zuora Payments.   # noqa: E501

        :return: The reference_id of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """Sets the reference_id of this GETARPaymentTypewithSuccess.

        The transaction ID returned by the payment gateway. Use this field to reconcile payments between your gateway and Zuora Payments.   # noqa: E501

        :param reference_id: The reference_id of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._reference_id = reference_id

    @property
    def refund_amount(self):
        """Gets the refund_amount of this GETARPaymentTypewithSuccess.  # noqa: E501

        The amount of the payment that is refunded.   # noqa: E501

        :return: The refund_amount of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: float
        """
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, refund_amount):
        """Sets the refund_amount of this GETARPaymentTypewithSuccess.

        The amount of the payment that is refunded.   # noqa: E501

        :param refund_amount: The refund_amount of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: float
        """

        self._refund_amount = refund_amount

    @property
    def second_payment_reference_id(self):
        """Gets the second_payment_reference_id of this GETARPaymentTypewithSuccess.  # noqa: E501

        The transaction ID returned by the payment gateway if there is an additional transaction for the payment. Use this field to reconcile payments between your gateway and Zuora Payments.   # noqa: E501

        :return: The second_payment_reference_id of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._second_payment_reference_id

    @second_payment_reference_id.setter
    def second_payment_reference_id(self, second_payment_reference_id):
        """Sets the second_payment_reference_id of this GETARPaymentTypewithSuccess.

        The transaction ID returned by the payment gateway if there is an additional transaction for the payment. Use this field to reconcile payments between your gateway and Zuora Payments.   # noqa: E501

        :param second_payment_reference_id: The second_payment_reference_id of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._second_payment_reference_id = second_payment_reference_id

    @property
    def settled_on(self):
        """Gets the settled_on of this GETARPaymentTypewithSuccess.  # noqa: E501

        The date and time when the payment was settled in the payment processor, in `yyyy-mm-dd hh:mm:ss` format. This field is used by the Spectrum gateway only and not applicable to other gateways.   # noqa: E501

        :return: The settled_on of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: datetime
        """
        return self._settled_on

    @settled_on.setter
    def settled_on(self, settled_on):
        """Sets the settled_on of this GETARPaymentTypewithSuccess.

        The date and time when the payment was settled in the payment processor, in `yyyy-mm-dd hh:mm:ss` format. This field is used by the Spectrum gateway only and not applicable to other gateways.   # noqa: E501

        :param settled_on: The settled_on of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: datetime
        """

        self._settled_on = settled_on

    @property
    def soft_descriptor(self):
        """Gets the soft_descriptor of this GETARPaymentTypewithSuccess.  # noqa: E501

        A payment gateway-specific field that maps to Zuora for the gateways, Orbital, Vantiv and Verifi.   # noqa: E501

        :return: The soft_descriptor of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._soft_descriptor

    @soft_descriptor.setter
    def soft_descriptor(self, soft_descriptor):
        """Sets the soft_descriptor of this GETARPaymentTypewithSuccess.

        A payment gateway-specific field that maps to Zuora for the gateways, Orbital, Vantiv and Verifi.   # noqa: E501

        :param soft_descriptor: The soft_descriptor of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._soft_descriptor = soft_descriptor

    @property
    def soft_descriptor_phone(self):
        """Gets the soft_descriptor_phone of this GETARPaymentTypewithSuccess.  # noqa: E501

        A payment gateway-specific field that maps to Zuora for the gateways, Orbital, Vantiv and Verifi.   # noqa: E501

        :return: The soft_descriptor_phone of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._soft_descriptor_phone

    @soft_descriptor_phone.setter
    def soft_descriptor_phone(self, soft_descriptor_phone):
        """Sets the soft_descriptor_phone of this GETARPaymentTypewithSuccess.

        A payment gateway-specific field that maps to Zuora for the gateways, Orbital, Vantiv and Verifi.   # noqa: E501

        :param soft_descriptor_phone: The soft_descriptor_phone of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._soft_descriptor_phone = soft_descriptor_phone

    @property
    def status(self):
        """Gets the status of this GETARPaymentTypewithSuccess.  # noqa: E501

        The status of the payment.   # noqa: E501

        :return: The status of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GETARPaymentTypewithSuccess.

        The status of the payment.   # noqa: E501

        :param status: The status of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: str
        """
        allowed_values = ["Draft", "Processing", "Processed", "Error", "Canceled", "Posted"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def submitted_on(self):
        """Gets the submitted_on of this GETARPaymentTypewithSuccess.  # noqa: E501

        The date and time when the payment was submitted, in `yyyy-mm-dd hh:mm:ss` format.   # noqa: E501

        :return: The submitted_on of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: datetime
        """
        return self._submitted_on

    @submitted_on.setter
    def submitted_on(self, submitted_on):
        """Sets the submitted_on of this GETARPaymentTypewithSuccess.

        The date and time when the payment was submitted, in `yyyy-mm-dd hh:mm:ss` format.   # noqa: E501

        :param submitted_on: The submitted_on of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: datetime
        """

        self._submitted_on = submitted_on

    @property
    def type(self):
        """Gets the type of this GETARPaymentTypewithSuccess.  # noqa: E501

        The type of the payment.   # noqa: E501

        :return: The type of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GETARPaymentTypewithSuccess.

        The type of the payment.   # noqa: E501

        :param type: The type of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: str
        """
        allowed_values = ["External", "Electronic"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def unapplied_amount(self):
        """Gets the unapplied_amount of this GETARPaymentTypewithSuccess.  # noqa: E501

        The unapplied amount of the payment.   # noqa: E501

        :return: The unapplied_amount of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: float
        """
        return self._unapplied_amount

    @unapplied_amount.setter
    def unapplied_amount(self, unapplied_amount):
        """Sets the unapplied_amount of this GETARPaymentTypewithSuccess.

        The unapplied amount of the payment.   # noqa: E501

        :param unapplied_amount: The unapplied_amount of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: float
        """

        self._unapplied_amount = unapplied_amount

    @property
    def updated_by_id(self):
        """Gets the updated_by_id of this GETARPaymentTypewithSuccess.  # noqa: E501

        The ID of the Zuora user who last updated the payment.   # noqa: E501

        :return: The updated_by_id of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """Sets the updated_by_id of this GETARPaymentTypewithSuccess.

        The ID of the Zuora user who last updated the payment.   # noqa: E501

        :param updated_by_id: The updated_by_id of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._updated_by_id = updated_by_id

    @property
    def updated_date(self):
        """Gets the updated_date of this GETARPaymentTypewithSuccess.  # noqa: E501

        The date and time when the payment was last updated, in `yyyy-mm-dd hh:mm:ss` format. For example, 2017-03-02 15:36:10.   # noqa: E501

        :return: The updated_date of this GETARPaymentTypewithSuccess.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this GETARPaymentTypewithSuccess.

        The date and time when the payment was last updated, in `yyyy-mm-dd hh:mm:ss` format. For example, 2017-03-02 15:36:10.   # noqa: E501

        :param updated_date: The updated_date of this GETARPaymentTypewithSuccess.  # noqa: E501
        :type: datetime
        """

        self._updated_date = updated_date

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GETARPaymentTypewithSuccess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
