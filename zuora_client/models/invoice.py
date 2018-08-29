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


class Invoice(object):
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
        'account_id': 'str',
        'adjustment_amount': 'float',
        'amount': 'float',
        'amount_without_tax': 'float',
        'balance': 'float',
        'bill_run_id': 'str',
        'body': 'str',
        'comments': 'str',
        'created_by_id': 'str',
        'created_date': 'datetime',
        'credit_balance_adjustment_amount': 'float',
        'due_date': 'date',
        'includes_one_time': 'bool',
        'includes_recurring': 'bool',
        'includes_usage': 'bool',
        'invoice_date': 'date',
        'invoice_number': 'str',
        'last_email_sent_date': 'datetime',
        'payment_amount': 'float',
        'posted_by': 'str',
        'posted_date': 'datetime',
        'refund_amount': 'float',
        'regenerate_invoice_pdf': 'bool',
        'status': 'str',
        'target_date': 'date',
        'tax_amount': 'float',
        'tax_exempt_amount': 'float',
        'transferred_to_accounting': 'str',
        'updated_by_id': 'str',
        'updated_date': 'datetime'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'adjustment_amount': 'AdjustmentAmount',
        'amount': 'Amount',
        'amount_without_tax': 'AmountWithoutTax',
        'balance': 'Balance',
        'bill_run_id': 'BillRunId',
        'body': 'Body',
        'comments': 'Comments',
        'created_by_id': 'CreatedById',
        'created_date': 'CreatedDate',
        'credit_balance_adjustment_amount': 'CreditBalanceAdjustmentAmount',
        'due_date': 'DueDate',
        'includes_one_time': 'IncludesOneTime',
        'includes_recurring': 'IncludesRecurring',
        'includes_usage': 'IncludesUsage',
        'invoice_date': 'InvoiceDate',
        'invoice_number': 'InvoiceNumber',
        'last_email_sent_date': 'LastEmailSentDate',
        'payment_amount': 'PaymentAmount',
        'posted_by': 'PostedBy',
        'posted_date': 'PostedDate',
        'refund_amount': 'RefundAmount',
        'regenerate_invoice_pdf': 'RegenerateInvoicePDF',
        'status': 'Status',
        'target_date': 'TargetDate',
        'tax_amount': 'TaxAmount',
        'tax_exempt_amount': 'TaxExemptAmount',
        'transferred_to_accounting': 'TransferredToAccounting',
        'updated_by_id': 'UpdatedById',
        'updated_date': 'UpdatedDate'
    }

    def __init__(self, account_id=None, adjustment_amount=None, amount=None, amount_without_tax=None, balance=None, bill_run_id=None, body=None, comments=None, created_by_id=None, created_date=None, credit_balance_adjustment_amount=None, due_date=None, includes_one_time=None, includes_recurring=None, includes_usage=None, invoice_date=None, invoice_number=None, last_email_sent_date=None, payment_amount=None, posted_by=None, posted_date=None, refund_amount=None, regenerate_invoice_pdf=None, status=None, target_date=None, tax_amount=None, tax_exempt_amount=None, transferred_to_accounting=None, updated_by_id=None, updated_date=None):  # noqa: E501
        """Invoice - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._adjustment_amount = None
        self._amount = None
        self._amount_without_tax = None
        self._balance = None
        self._bill_run_id = None
        self._body = None
        self._comments = None
        self._created_by_id = None
        self._created_date = None
        self._credit_balance_adjustment_amount = None
        self._due_date = None
        self._includes_one_time = None
        self._includes_recurring = None
        self._includes_usage = None
        self._invoice_date = None
        self._invoice_number = None
        self._last_email_sent_date = None
        self._payment_amount = None
        self._posted_by = None
        self._posted_date = None
        self._refund_amount = None
        self._regenerate_invoice_pdf = None
        self._status = None
        self._target_date = None
        self._tax_amount = None
        self._tax_exempt_amount = None
        self._transferred_to_accounting = None
        self._updated_by_id = None
        self._updated_date = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if adjustment_amount is not None:
            self.adjustment_amount = adjustment_amount
        if amount is not None:
            self.amount = amount
        if amount_without_tax is not None:
            self.amount_without_tax = amount_without_tax
        if balance is not None:
            self.balance = balance
        if bill_run_id is not None:
            self.bill_run_id = bill_run_id
        if body is not None:
            self.body = body
        if comments is not None:
            self.comments = comments
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_date is not None:
            self.created_date = created_date
        if credit_balance_adjustment_amount is not None:
            self.credit_balance_adjustment_amount = credit_balance_adjustment_amount
        if due_date is not None:
            self.due_date = due_date
        if includes_one_time is not None:
            self.includes_one_time = includes_one_time
        if includes_recurring is not None:
            self.includes_recurring = includes_recurring
        if includes_usage is not None:
            self.includes_usage = includes_usage
        if invoice_date is not None:
            self.invoice_date = invoice_date
        if invoice_number is not None:
            self.invoice_number = invoice_number
        if last_email_sent_date is not None:
            self.last_email_sent_date = last_email_sent_date
        if payment_amount is not None:
            self.payment_amount = payment_amount
        if posted_by is not None:
            self.posted_by = posted_by
        if posted_date is not None:
            self.posted_date = posted_date
        if refund_amount is not None:
            self.refund_amount = refund_amount
        if regenerate_invoice_pdf is not None:
            self.regenerate_invoice_pdf = regenerate_invoice_pdf
        if status is not None:
            self.status = status
        if target_date is not None:
            self.target_date = target_date
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if tax_exempt_amount is not None:
            self.tax_exempt_amount = tax_exempt_amount
        if transferred_to_accounting is not None:
            self.transferred_to_accounting = transferred_to_accounting
        if updated_by_id is not None:
            self.updated_by_id = updated_by_id
        if updated_date is not None:
            self.updated_date = updated_date

    @property
    def account_id(self):
        """Gets the account_id of this Invoice.  # noqa: E501

          # noqa: E501

        :return: The account_id of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Invoice.

          # noqa: E501

        :param account_id: The account_id of this Invoice.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def adjustment_amount(self):
        """Gets the adjustment_amount of this Invoice.  # noqa: E501

         The amount of the invoice adjustments associated with the invoice. **Character limi**t: 16  **Values**: a valid currency amount   # noqa: E501

        :return: The adjustment_amount of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._adjustment_amount

    @adjustment_amount.setter
    def adjustment_amount(self, adjustment_amount):
        """Sets the adjustment_amount of this Invoice.

         The amount of the invoice adjustments associated with the invoice. **Character limi**t: 16  **Values**: a valid currency amount   # noqa: E501

        :param adjustment_amount: The adjustment_amount of this Invoice.  # noqa: E501
        :type: float
        """

        self._adjustment_amount = adjustment_amount

    @property
    def amount(self):
        """Gets the amount of this Invoice.  # noqa: E501

         The sum of all charges and taxes associated with the invoice.   **Character limit**: 16  **Values**: automatically generated   # noqa: E501

        :return: The amount of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Invoice.

         The sum of all charges and taxes associated with the invoice.   **Character limit**: 16  **Values**: automatically generated   # noqa: E501

        :param amount: The amount of this Invoice.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def amount_without_tax(self):
        """Gets the amount_without_tax of this Invoice.  # noqa: E501

         The sum of all charges associated with the invoice. Taxes are excluded from this value.   **Character limit**: 16  **Values**: automatically generated   # noqa: E501

        :return: The amount_without_tax of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._amount_without_tax

    @amount_without_tax.setter
    def amount_without_tax(self, amount_without_tax):
        """Sets the amount_without_tax of this Invoice.

         The sum of all charges associated with the invoice. Taxes are excluded from this value.   **Character limit**: 16  **Values**: automatically generated   # noqa: E501

        :param amount_without_tax: The amount_without_tax of this Invoice.  # noqa: E501
        :type: float
        """

        self._amount_without_tax = amount_without_tax

    @property
    def balance(self):
        """Gets the balance of this Invoice.  # noqa: E501

         The remaining balance of the invoice after all payments, adjustments, and refunds are applied.   **Character limit**: 16  **Values**: automatically generated   # noqa: E501

        :return: The balance of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this Invoice.

         The remaining balance of the invoice after all payments, adjustments, and refunds are applied.   **Character limit**: 16  **Values**: automatically generated   # noqa: E501

        :param balance: The balance of this Invoice.  # noqa: E501
        :type: float
        """

        self._balance = balance

    @property
    def bill_run_id(self):
        """Gets the bill_run_id of this Invoice.  # noqa: E501

         The ID of a Bill Run.   **Character limit**: 32  **Values**: a BillRun ID   # noqa: E501

        :return: The bill_run_id of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._bill_run_id

    @bill_run_id.setter
    def bill_run_id(self, bill_run_id):
        """Sets the bill_run_id of this Invoice.

         The ID of a Bill Run.   **Character limit**: 32  **Values**: a BillRun ID   # noqa: E501

        :param bill_run_id: The bill_run_id of this Invoice.  # noqa: E501
        :type: str
        """

        self._bill_run_id = bill_run_id

    @property
    def body(self):
        """Gets the body of this Invoice.  # noqa: E501

         Required   # noqa: E501

        :return: The body of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this Invoice.

         Required   # noqa: E501

        :param body: The body of this Invoice.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def comments(self):
        """Gets the comments of this Invoice.  # noqa: E501

         Additional information related to the invoice that a Zuora user added to the invoice.   **Character limit**: 255  **Values:** a string of 255 characters or fewer   # noqa: E501

        :return: The comments of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this Invoice.

         Additional information related to the invoice that a Zuora user added to the invoice.   **Character limit**: 255  **Values:** a string of 255 characters or fewer   # noqa: E501

        :param comments: The comments of this Invoice.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def created_by_id(self):
        """Gets the created_by_id of this Invoice.  # noqa: E501

         The user ID of the person who created the invoice. If a bill run generated the invoice, then the value is the user ID of person who created the bill run.   **Character limit**: 32  **Values**: automatically generated   # noqa: E501

        :return: The created_by_id of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this Invoice.

         The user ID of the person who created the invoice. If a bill run generated the invoice, then the value is the user ID of person who created the bill run.   **Character limit**: 32  **Values**: automatically generated   # noqa: E501

        :param created_by_id: The created_by_id of this Invoice.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def created_date(self):
        """Gets the created_date of this Invoice.  # noqa: E501

         The date when the invoice was generated.   **Character limit**: 29  **Values**: automatically generated   # noqa: E501

        :return: The created_date of this Invoice.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this Invoice.

         The date when the invoice was generated.   **Character limit**: 29  **Values**: automatically generated   # noqa: E501

        :param created_date: The created_date of this Invoice.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def credit_balance_adjustment_amount(self):
        """Gets the credit_balance_adjustment_amount of this Invoice.  # noqa: E501

         The currency amount of the adjustment applied to the customer's credit balance.   **Character limit**: 16  **Values**: a valid currency amount This field is only available if the [Zuora Global Support](http://support.zuora.com/) to enable this feature.     # noqa: E501

        :return: The credit_balance_adjustment_amount of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._credit_balance_adjustment_amount

    @credit_balance_adjustment_amount.setter
    def credit_balance_adjustment_amount(self, credit_balance_adjustment_amount):
        """Sets the credit_balance_adjustment_amount of this Invoice.

         The currency amount of the adjustment applied to the customer's credit balance.   **Character limit**: 16  **Values**: a valid currency amount This field is only available if the [Zuora Global Support](http://support.zuora.com/) to enable this feature.     # noqa: E501

        :param credit_balance_adjustment_amount: The credit_balance_adjustment_amount of this Invoice.  # noqa: E501
        :type: float
        """

        self._credit_balance_adjustment_amount = credit_balance_adjustment_amount

    @property
    def due_date(self):
        """Gets the due_date of this Invoice.  # noqa: E501

         The date by which the payment for this invoice is due.   **Character limit**: 29   # noqa: E501

        :return: The due_date of this Invoice.  # noqa: E501
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this Invoice.

         The date by which the payment for this invoice is due.   **Character limit**: 29   # noqa: E501

        :param due_date: The due_date of this Invoice.  # noqa: E501
        :type: date
        """

        self._due_date = due_date

    @property
    def includes_one_time(self):
        """Gets the includes_one_time of this Invoice.  # noqa: E501

         Specifies whether the invoice includes one-time charges.   **Character limit**: 5  **Values**: automatically generated from one of the following: `True` (default), `False`   # noqa: E501

        :return: The includes_one_time of this Invoice.  # noqa: E501
        :rtype: bool
        """
        return self._includes_one_time

    @includes_one_time.setter
    def includes_one_time(self, includes_one_time):
        """Sets the includes_one_time of this Invoice.

         Specifies whether the invoice includes one-time charges.   **Character limit**: 5  **Values**: automatically generated from one of the following: `True` (default), `False`   # noqa: E501

        :param includes_one_time: The includes_one_time of this Invoice.  # noqa: E501
        :type: bool
        """

        self._includes_one_time = includes_one_time

    @property
    def includes_recurring(self):
        """Gets the includes_recurring of this Invoice.  # noqa: E501

         Specifies whether the invoice includes recurring charges.   **Character limit**: 5  **Values**: automatically generated from one of the following: `True` (default), `False`   # noqa: E501

        :return: The includes_recurring of this Invoice.  # noqa: E501
        :rtype: bool
        """
        return self._includes_recurring

    @includes_recurring.setter
    def includes_recurring(self, includes_recurring):
        """Sets the includes_recurring of this Invoice.

         Specifies whether the invoice includes recurring charges.   **Character limit**: 5  **Values**: automatically generated from one of the following: `True` (default), `False`   # noqa: E501

        :param includes_recurring: The includes_recurring of this Invoice.  # noqa: E501
        :type: bool
        """

        self._includes_recurring = includes_recurring

    @property
    def includes_usage(self):
        """Gets the includes_usage of this Invoice.  # noqa: E501

         Specifies whether the invoice includes usage charges.   **Character limit**: 5  **Values**: automatically generated from one of the following: `True `(default), `False`   # noqa: E501

        :return: The includes_usage of this Invoice.  # noqa: E501
        :rtype: bool
        """
        return self._includes_usage

    @includes_usage.setter
    def includes_usage(self, includes_usage):
        """Sets the includes_usage of this Invoice.

         Specifies whether the invoice includes usage charges.   **Character limit**: 5  **Values**: automatically generated from one of the following: `True `(default), `False`   # noqa: E501

        :param includes_usage: The includes_usage of this Invoice.  # noqa: E501
        :type: bool
        """

        self._includes_usage = includes_usage

    @property
    def invoice_date(self):
        """Gets the invoice_date of this Invoice.  # noqa: E501

         Specifies the date on which to generate the invoice.   **Character limit**: 29   # noqa: E501

        :return: The invoice_date of this Invoice.  # noqa: E501
        :rtype: date
        """
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, invoice_date):
        """Sets the invoice_date of this Invoice.

         Specifies the date on which to generate the invoice.   **Character limit**: 29   # noqa: E501

        :param invoice_date: The invoice_date of this Invoice.  # noqa: E501
        :type: date
        """

        self._invoice_date = invoice_date

    @property
    def invoice_number(self):
        """Gets the invoice_number of this Invoice.  # noqa: E501

         The unique identification number for the invoice. This number is returned as a string.   **Character limit**: 32  **Values**: automatically generated   # noqa: E501

        :return: The invoice_number of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """Sets the invoice_number of this Invoice.

         The unique identification number for the invoice. This number is returned as a string.   **Character limit**: 32  **Values**: automatically generated   # noqa: E501

        :param invoice_number: The invoice_number of this Invoice.  # noqa: E501
        :type: str
        """

        self._invoice_number = invoice_number

    @property
    def last_email_sent_date(self):
        """Gets the last_email_sent_date of this Invoice.  # noqa: E501

         The date when the invoice was last emailed.   **Character limit**: 29  **Values**: automatically generated   # noqa: E501

        :return: The last_email_sent_date of this Invoice.  # noqa: E501
        :rtype: datetime
        """
        return self._last_email_sent_date

    @last_email_sent_date.setter
    def last_email_sent_date(self, last_email_sent_date):
        """Sets the last_email_sent_date of this Invoice.

         The date when the invoice was last emailed.   **Character limit**: 29  **Values**: automatically generated   # noqa: E501

        :param last_email_sent_date: The last_email_sent_date of this Invoice.  # noqa: E501
        :type: datetime
        """

        self._last_email_sent_date = last_email_sent_date

    @property
    def payment_amount(self):
        """Gets the payment_amount of this Invoice.  # noqa: E501

         The amount of payments applied to the invoice.   **Character limit**: 16 **Value**s: automatically generated   # noqa: E501

        :return: The payment_amount of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, payment_amount):
        """Sets the payment_amount of this Invoice.

         The amount of payments applied to the invoice.   **Character limit**: 16 **Value**s: automatically generated   # noqa: E501

        :param payment_amount: The payment_amount of this Invoice.  # noqa: E501
        :type: float
        """

        self._payment_amount = payment_amount

    @property
    def posted_by(self):
        """Gets the posted_by of this Invoice.  # noqa: E501

         The user ID of the person who moved the invoice to Posted status.   **Character limit**: 32  **Values**: automatically generated   # noqa: E501

        :return: The posted_by of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._posted_by

    @posted_by.setter
    def posted_by(self, posted_by):
        """Sets the posted_by of this Invoice.

         The user ID of the person who moved the invoice to Posted status.   **Character limit**: 32  **Values**: automatically generated   # noqa: E501

        :param posted_by: The posted_by of this Invoice.  # noqa: E501
        :type: str
        """

        self._posted_by = posted_by

    @property
    def posted_date(self):
        """Gets the posted_date of this Invoice.  # noqa: E501

         The date when the invoice was posted.   **Character limit:** 29  **Values**: automatically generated   # noqa: E501

        :return: The posted_date of this Invoice.  # noqa: E501
        :rtype: datetime
        """
        return self._posted_date

    @posted_date.setter
    def posted_date(self, posted_date):
        """Sets the posted_date of this Invoice.

         The date when the invoice was posted.   **Character limit:** 29  **Values**: automatically generated   # noqa: E501

        :param posted_date: The posted_date of this Invoice.  # noqa: E501
        :type: datetime
        """

        self._posted_date = posted_date

    @property
    def refund_amount(self):
        """Gets the refund_amount of this Invoice.  # noqa: E501

         Specifies the amount of a refund that was applied against an earlier payment on the invoice.   **Character limit**: 16  **Values**: automatically generated   # noqa: E501

        :return: The refund_amount of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, refund_amount):
        """Sets the refund_amount of this Invoice.

         Specifies the amount of a refund that was applied against an earlier payment on the invoice.   **Character limit**: 16  **Values**: automatically generated   # noqa: E501

        :param refund_amount: The refund_amount of this Invoice.  # noqa: E501
        :type: float
        """

        self._refund_amount = refund_amount

    @property
    def regenerate_invoice_pdf(self):
        """Gets the regenerate_invoice_pdf of this Invoice.  # noqa: E501

         Regenerates a PDF of an invoice that was already generated.  **Character limit**: 5  **Values**: `True`, `False`   # noqa: E501

        :return: The regenerate_invoice_pdf of this Invoice.  # noqa: E501
        :rtype: bool
        """
        return self._regenerate_invoice_pdf

    @regenerate_invoice_pdf.setter
    def regenerate_invoice_pdf(self, regenerate_invoice_pdf):
        """Sets the regenerate_invoice_pdf of this Invoice.

         Regenerates a PDF of an invoice that was already generated.  **Character limit**: 5  **Values**: `True`, `False`   # noqa: E501

        :param regenerate_invoice_pdf: The regenerate_invoice_pdf of this Invoice.  # noqa: E501
        :type: bool
        """

        self._regenerate_invoice_pdf = regenerate_invoice_pdf

    @property
    def status(self):
        """Gets the status of this Invoice.  # noqa: E501

         The status of the invoice in the system. This status is not the status of the payment of the invoice, just the status of the invoice itself.   **Character limit**: 8  **Values**: one of the following:  -  Draft (default, automatically set upon invoice creation)  -  Posted  -  Canceled    # noqa: E501

        :return: The status of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Invoice.

         The status of the invoice in the system. This status is not the status of the payment of the invoice, just the status of the invoice itself.   **Character limit**: 8  **Values**: one of the following:  -  Draft (default, automatically set upon invoice creation)  -  Posted  -  Canceled    # noqa: E501

        :param status: The status of this Invoice.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def target_date(self):
        """Gets the target_date of this Invoice.  # noqa: E501

         This date is used to determine which charges are to be billed. All charges that are to be billed on this date or prior will be included in this bill run.   **Character limit**: 29   # noqa: E501

        :return: The target_date of this Invoice.  # noqa: E501
        :rtype: date
        """
        return self._target_date

    @target_date.setter
    def target_date(self, target_date):
        """Sets the target_date of this Invoice.

         This date is used to determine which charges are to be billed. All charges that are to be billed on this date or prior will be included in this bill run.   **Character limit**: 29   # noqa: E501

        :param target_date: The target_date of this Invoice.  # noqa: E501
        :type: date
        """

        self._target_date = target_date

    @property
    def tax_amount(self):
        """Gets the tax_amount of this Invoice.  # noqa: E501

         The total amount of the taxes applied to the invoice.   **Character limit**: 16  **Values**: automatically generated   # noqa: E501

        :return: The tax_amount of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this Invoice.

         The total amount of the taxes applied to the invoice.   **Character limit**: 16  **Values**: automatically generated   # noqa: E501

        :param tax_amount: The tax_amount of this Invoice.  # noqa: E501
        :type: float
        """

        self._tax_amount = tax_amount

    @property
    def tax_exempt_amount(self):
        """Gets the tax_exempt_amount of this Invoice.  # noqa: E501

         The total amount of the invoice that is exempt from taxation.   **Character limit**: 16  **Values**: automatically generated   # noqa: E501

        :return: The tax_exempt_amount of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._tax_exempt_amount

    @tax_exempt_amount.setter
    def tax_exempt_amount(self, tax_exempt_amount):
        """Sets the tax_exempt_amount of this Invoice.

         The total amount of the invoice that is exempt from taxation.   **Character limit**: 16  **Values**: automatically generated   # noqa: E501

        :param tax_exempt_amount: The tax_exempt_amount of this Invoice.  # noqa: E501
        :type: float
        """

        self._tax_exempt_amount = tax_exempt_amount

    @property
    def transferred_to_accounting(self):
        """Gets the transferred_to_accounting of this Invoice.  # noqa: E501

         Specifies whether or not the invoice was transferred to an external accounting system, such as NetSuite.   **Character limit**: 10  **Values**: Processing, Yes, Error, Ignore   # noqa: E501

        :return: The transferred_to_accounting of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._transferred_to_accounting

    @transferred_to_accounting.setter
    def transferred_to_accounting(self, transferred_to_accounting):
        """Sets the transferred_to_accounting of this Invoice.

         Specifies whether or not the invoice was transferred to an external accounting system, such as NetSuite.   **Character limit**: 10  **Values**: Processing, Yes, Error, Ignore   # noqa: E501

        :param transferred_to_accounting: The transferred_to_accounting of this Invoice.  # noqa: E501
        :type: str
        """

        self._transferred_to_accounting = transferred_to_accounting

    @property
    def updated_by_id(self):
        """Gets the updated_by_id of this Invoice.  # noqa: E501

          # noqa: E501

        :return: The updated_by_id of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """Sets the updated_by_id of this Invoice.

          # noqa: E501

        :param updated_by_id: The updated_by_id of this Invoice.  # noqa: E501
        :type: str
        """

        self._updated_by_id = updated_by_id

    @property
    def updated_date(self):
        """Gets the updated_date of this Invoice.  # noqa: E501

         The date when the invoice was last updated.   **Character limit**: 29  **Values**: automatically generated   # noqa: E501

        :return: The updated_date of this Invoice.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this Invoice.

         The date when the invoice was last updated.   **Character limit**: 29  **Values**: automatically generated   # noqa: E501

        :param updated_date: The updated_date of this Invoice.  # noqa: E501
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
        if not isinstance(other, Invoice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
