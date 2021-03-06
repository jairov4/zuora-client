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

from zuora_client.models.account_object_custom_fields import AccountObjectCustomFields  # noqa: F401,E501
from zuora_client.models.account_object_ns_fields import AccountObjectNSFields  # noqa: F401,E501
from zuora_client.models.post_account_type_bill_to_contact import POSTAccountTypeBillToContact  # noqa: F401,E501
from zuora_client.models.post_account_type_credit_card import POSTAccountTypeCreditCard  # noqa: F401,E501
from zuora_client.models.post_account_type_sold_to_contact import POSTAccountTypeSoldToContact  # noqa: F401,E501
from zuora_client.models.post_account_type_subscription import POSTAccountTypeSubscription  # noqa: F401,E501
from zuora_client.models.post_account_type_tax_info import POSTAccountTypeTaxInfo  # noqa: F401,E501


class POSTAccountType(object):
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
        'class__ns': 'str',
        'customer_type__ns': 'str',
        'department__ns': 'str',
        'integration_id__ns': 'str',
        'integration_status__ns': 'str',
        'location__ns': 'str',
        'subsidiary__ns': 'str',
        'sync_date__ns': 'str',
        'syncto_net_suite__ns': 'str',
        'account_number': 'str',
        'additional_email_addresses': 'list[str]',
        'apply_credit_balance': 'bool',
        'auto_pay': 'bool',
        'batch': 'str',
        'bill_cycle_day': 'int',
        'bill_to_contact': 'POSTAccountTypeBillToContact',
        'collect': 'str',
        'communication_profile_id': 'str',
        'credit_card': 'POSTAccountTypeCreditCard',
        'credit_memo_template_id': 'str',
        'crm_id': 'str',
        'currency': 'str',
        'debit_memo_template_id': 'str',
        'hpm_credit_card_payment_method_id': 'str',
        'invoice': 'bool',
        'invoice_collect': 'bool',
        'invoice_delivery_prefs_email': 'bool',
        'invoice_delivery_prefs_print': 'bool',
        'invoice_target_date': 'date',
        'invoice_template_id': 'str',
        'name': 'str',
        'notes': 'str',
        'parent_id': 'str',
        'payment_gateway': 'str',
        'payment_term': 'str',
        'run_billing': 'bool',
        'sales_rep': 'str',
        'sold_to_contact': 'POSTAccountTypeSoldToContact',
        'subscription': 'POSTAccountTypeSubscription',
        'tagging': 'str',
        'target_date': 'date',
        'tax_info': 'POSTAccountTypeTaxInfo'
    }

    attribute_map = {
        'class__ns': 'Class__NS',
        'customer_type__ns': 'CustomerType__NS',
        'department__ns': 'Department__NS',
        'integration_id__ns': 'IntegrationId__NS',
        'integration_status__ns': 'IntegrationStatus__NS',
        'location__ns': 'Location__NS',
        'subsidiary__ns': 'Subsidiary__NS',
        'sync_date__ns': 'SyncDate__NS',
        'syncto_net_suite__ns': 'SynctoNetSuite__NS',
        'account_number': 'accountNumber',
        'additional_email_addresses': 'additionalEmailAddresses',
        'apply_credit_balance': 'applyCreditBalance',
        'auto_pay': 'autoPay',
        'batch': 'batch',
        'bill_cycle_day': 'billCycleDay',
        'bill_to_contact': 'billToContact',
        'collect': 'collect',
        'communication_profile_id': 'communicationProfileId',
        'credit_card': 'creditCard',
        'credit_memo_template_id': 'creditMemoTemplateId',
        'crm_id': 'crmId',
        'currency': 'currency',
        'debit_memo_template_id': 'debitMemoTemplateId',
        'hpm_credit_card_payment_method_id': 'hpmCreditCardPaymentMethodId',
        'invoice': 'invoice',
        'invoice_collect': 'invoiceCollect',
        'invoice_delivery_prefs_email': 'invoiceDeliveryPrefsEmail',
        'invoice_delivery_prefs_print': 'invoiceDeliveryPrefsPrint',
        'invoice_target_date': 'invoiceTargetDate',
        'invoice_template_id': 'invoiceTemplateId',
        'name': 'name',
        'notes': 'notes',
        'parent_id': 'parentId',
        'payment_gateway': 'paymentGateway',
        'payment_term': 'paymentTerm',
        'run_billing': 'runBilling',
        'sales_rep': 'salesRep',
        'sold_to_contact': 'soldToContact',
        'subscription': 'subscription',
        'tagging': 'tagging',
        'target_date': 'targetDate',
        'tax_info': 'taxInfo'
    }

    def __init__(self, class__ns=None, customer_type__ns=None, department__ns=None, integration_id__ns=None, integration_status__ns=None, location__ns=None, subsidiary__ns=None, sync_date__ns=None, syncto_net_suite__ns=None, account_number=None, additional_email_addresses=None, apply_credit_balance=None, auto_pay=None, batch=None, bill_cycle_day=None, bill_to_contact=None, collect=None, communication_profile_id=None, credit_card=None, credit_memo_template_id=None, crm_id=None, currency=None, debit_memo_template_id=None, hpm_credit_card_payment_method_id=None, invoice=None, invoice_collect=None, invoice_delivery_prefs_email=None, invoice_delivery_prefs_print=None, invoice_target_date=None, invoice_template_id=None, name=None, notes=None, parent_id=None, payment_gateway=None, payment_term=None, run_billing=True, sales_rep=None, sold_to_contact=None, subscription=None, tagging=None, target_date=None, tax_info=None):  # noqa: E501
        """POSTAccountType - a model defined in Swagger"""  # noqa: E501

        self._class__ns = None
        self._customer_type__ns = None
        self._department__ns = None
        self._integration_id__ns = None
        self._integration_status__ns = None
        self._location__ns = None
        self._subsidiary__ns = None
        self._sync_date__ns = None
        self._syncto_net_suite__ns = None
        self._account_number = None
        self._additional_email_addresses = None
        self._apply_credit_balance = None
        self._auto_pay = None
        self._batch = None
        self._bill_cycle_day = None
        self._bill_to_contact = None
        self._collect = None
        self._communication_profile_id = None
        self._credit_card = None
        self._credit_memo_template_id = None
        self._crm_id = None
        self._currency = None
        self._debit_memo_template_id = None
        self._hpm_credit_card_payment_method_id = None
        self._invoice = None
        self._invoice_collect = None
        self._invoice_delivery_prefs_email = None
        self._invoice_delivery_prefs_print = None
        self._invoice_target_date = None
        self._invoice_template_id = None
        self._name = None
        self._notes = None
        self._parent_id = None
        self._payment_gateway = None
        self._payment_term = None
        self._run_billing = None
        self._sales_rep = None
        self._sold_to_contact = None
        self._subscription = None
        self._tagging = None
        self._target_date = None
        self._tax_info = None
        self.discriminator = None

        if class__ns is not None:
            self.class__ns = class__ns
        if customer_type__ns is not None:
            self.customer_type__ns = customer_type__ns
        if department__ns is not None:
            self.department__ns = department__ns
        if integration_id__ns is not None:
            self.integration_id__ns = integration_id__ns
        if integration_status__ns is not None:
            self.integration_status__ns = integration_status__ns
        if location__ns is not None:
            self.location__ns = location__ns
        if subsidiary__ns is not None:
            self.subsidiary__ns = subsidiary__ns
        if sync_date__ns is not None:
            self.sync_date__ns = sync_date__ns
        if syncto_net_suite__ns is not None:
            self.syncto_net_suite__ns = syncto_net_suite__ns
        if account_number is not None:
            self.account_number = account_number
        if additional_email_addresses is not None:
            self.additional_email_addresses = additional_email_addresses
        if apply_credit_balance is not None:
            self.apply_credit_balance = apply_credit_balance
        if auto_pay is not None:
            self.auto_pay = auto_pay
        if batch is not None:
            self.batch = batch
        if bill_cycle_day is not None:
            self.bill_cycle_day = bill_cycle_day
        self.bill_to_contact = bill_to_contact
        if collect is not None:
            self.collect = collect
        if communication_profile_id is not None:
            self.communication_profile_id = communication_profile_id
        if credit_card is not None:
            self.credit_card = credit_card
        if credit_memo_template_id is not None:
            self.credit_memo_template_id = credit_memo_template_id
        if crm_id is not None:
            self.crm_id = crm_id
        self.currency = currency
        if debit_memo_template_id is not None:
            self.debit_memo_template_id = debit_memo_template_id
        if hpm_credit_card_payment_method_id is not None:
            self.hpm_credit_card_payment_method_id = hpm_credit_card_payment_method_id
        if invoice is not None:
            self.invoice = invoice
        if invoice_collect is not None:
            self.invoice_collect = invoice_collect
        if invoice_delivery_prefs_email is not None:
            self.invoice_delivery_prefs_email = invoice_delivery_prefs_email
        if invoice_delivery_prefs_print is not None:
            self.invoice_delivery_prefs_print = invoice_delivery_prefs_print
        if invoice_target_date is not None:
            self.invoice_target_date = invoice_target_date
        if invoice_template_id is not None:
            self.invoice_template_id = invoice_template_id
        self.name = name
        if notes is not None:
            self.notes = notes
        if parent_id is not None:
            self.parent_id = parent_id
        if payment_gateway is not None:
            self.payment_gateway = payment_gateway
        if payment_term is not None:
            self.payment_term = payment_term
        if run_billing is not None:
            self.run_billing = run_billing
        if sales_rep is not None:
            self.sales_rep = sales_rep
        if sold_to_contact is not None:
            self.sold_to_contact = sold_to_contact
        if subscription is not None:
            self.subscription = subscription
        if tagging is not None:
            self.tagging = tagging
        if target_date is not None:
            self.target_date = target_date
        if tax_info is not None:
            self.tax_info = tax_info

    @property
    def class__ns(self):
        """Gets the class__ns of this POSTAccountType.  # noqa: E501

        Value of the Class field for the corresponding customer account in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The class__ns of this POSTAccountType.  # noqa: E501
        :rtype: str
        """
        return self._class__ns

    @class__ns.setter
    def class__ns(self, class__ns):
        """Sets the class__ns of this POSTAccountType.

        Value of the Class field for the corresponding customer account in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param class__ns: The class__ns of this POSTAccountType.  # noqa: E501
        :type: str
        """
        if class__ns is not None and len(class__ns) > 255:
            raise ValueError("Invalid value for `class__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._class__ns = class__ns

    @property
    def customer_type__ns(self):
        """Gets the customer_type__ns of this POSTAccountType.  # noqa: E501

        Value of the Customer Type field for the corresponding customer account in NetSuite. The Customer Type field is used when the customer account is created in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The customer_type__ns of this POSTAccountType.  # noqa: E501
        :rtype: str
        """
        return self._customer_type__ns

    @customer_type__ns.setter
    def customer_type__ns(self, customer_type__ns):
        """Sets the customer_type__ns of this POSTAccountType.

        Value of the Customer Type field for the corresponding customer account in NetSuite. The Customer Type field is used when the customer account is created in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param customer_type__ns: The customer_type__ns of this POSTAccountType.  # noqa: E501
        :type: str
        """
        allowed_values = ["Company", "Individual"]  # noqa: E501
        if customer_type__ns not in allowed_values:
            raise ValueError(
                "Invalid value for `customer_type__ns` ({0}), must be one of {1}"  # noqa: E501
                .format(customer_type__ns, allowed_values)
            )

        self._customer_type__ns = customer_type__ns

    @property
    def department__ns(self):
        """Gets the department__ns of this POSTAccountType.  # noqa: E501

        Value of the Department field for the corresponding customer account in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The department__ns of this POSTAccountType.  # noqa: E501
        :rtype: str
        """
        return self._department__ns

    @department__ns.setter
    def department__ns(self, department__ns):
        """Sets the department__ns of this POSTAccountType.

        Value of the Department field for the corresponding customer account in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param department__ns: The department__ns of this POSTAccountType.  # noqa: E501
        :type: str
        """
        if department__ns is not None and len(department__ns) > 255:
            raise ValueError("Invalid value for `department__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._department__ns = department__ns

    @property
    def integration_id__ns(self):
        """Gets the integration_id__ns of this POSTAccountType.  # noqa: E501

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_id__ns of this POSTAccountType.  # noqa: E501
        :rtype: str
        """
        return self._integration_id__ns

    @integration_id__ns.setter
    def integration_id__ns(self, integration_id__ns):
        """Sets the integration_id__ns of this POSTAccountType.

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_id__ns: The integration_id__ns of this POSTAccountType.  # noqa: E501
        :type: str
        """
        if integration_id__ns is not None and len(integration_id__ns) > 255:
            raise ValueError("Invalid value for `integration_id__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_id__ns = integration_id__ns

    @property
    def integration_status__ns(self):
        """Gets the integration_status__ns of this POSTAccountType.  # noqa: E501

        Status of the account's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_status__ns of this POSTAccountType.  # noqa: E501
        :rtype: str
        """
        return self._integration_status__ns

    @integration_status__ns.setter
    def integration_status__ns(self, integration_status__ns):
        """Sets the integration_status__ns of this POSTAccountType.

        Status of the account's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_status__ns: The integration_status__ns of this POSTAccountType.  # noqa: E501
        :type: str
        """
        if integration_status__ns is not None and len(integration_status__ns) > 255:
            raise ValueError("Invalid value for `integration_status__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_status__ns = integration_status__ns

    @property
    def location__ns(self):
        """Gets the location__ns of this POSTAccountType.  # noqa: E501

        Value of the Location field for the corresponding customer account in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The location__ns of this POSTAccountType.  # noqa: E501
        :rtype: str
        """
        return self._location__ns

    @location__ns.setter
    def location__ns(self, location__ns):
        """Sets the location__ns of this POSTAccountType.

        Value of the Location field for the corresponding customer account in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param location__ns: The location__ns of this POSTAccountType.  # noqa: E501
        :type: str
        """
        if location__ns is not None and len(location__ns) > 255:
            raise ValueError("Invalid value for `location__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._location__ns = location__ns

    @property
    def subsidiary__ns(self):
        """Gets the subsidiary__ns of this POSTAccountType.  # noqa: E501

        Value of the Subsidiary field for the corresponding customer account in NetSuite. The Subsidiary field is required if you use NetSuite OneWorld. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The subsidiary__ns of this POSTAccountType.  # noqa: E501
        :rtype: str
        """
        return self._subsidiary__ns

    @subsidiary__ns.setter
    def subsidiary__ns(self, subsidiary__ns):
        """Sets the subsidiary__ns of this POSTAccountType.

        Value of the Subsidiary field for the corresponding customer account in NetSuite. The Subsidiary field is required if you use NetSuite OneWorld. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param subsidiary__ns: The subsidiary__ns of this POSTAccountType.  # noqa: E501
        :type: str
        """
        if subsidiary__ns is not None and len(subsidiary__ns) > 255:
            raise ValueError("Invalid value for `subsidiary__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._subsidiary__ns = subsidiary__ns

    @property
    def sync_date__ns(self):
        """Gets the sync_date__ns of this POSTAccountType.  # noqa: E501

        Date when the account was sychronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The sync_date__ns of this POSTAccountType.  # noqa: E501
        :rtype: str
        """
        return self._sync_date__ns

    @sync_date__ns.setter
    def sync_date__ns(self, sync_date__ns):
        """Sets the sync_date__ns of this POSTAccountType.

        Date when the account was sychronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param sync_date__ns: The sync_date__ns of this POSTAccountType.  # noqa: E501
        :type: str
        """
        if sync_date__ns is not None and len(sync_date__ns) > 255:
            raise ValueError("Invalid value for `sync_date__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._sync_date__ns = sync_date__ns

    @property
    def syncto_net_suite__ns(self):
        """Gets the syncto_net_suite__ns of this POSTAccountType.  # noqa: E501

        Specifies whether the account should be synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The syncto_net_suite__ns of this POSTAccountType.  # noqa: E501
        :rtype: str
        """
        return self._syncto_net_suite__ns

    @syncto_net_suite__ns.setter
    def syncto_net_suite__ns(self, syncto_net_suite__ns):
        """Sets the syncto_net_suite__ns of this POSTAccountType.

        Specifies whether the account should be synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param syncto_net_suite__ns: The syncto_net_suite__ns of this POSTAccountType.  # noqa: E501
        :type: str
        """
        allowed_values = ["Yes", "No"]  # noqa: E501
        if syncto_net_suite__ns not in allowed_values:
            raise ValueError(
                "Invalid value for `syncto_net_suite__ns` ({0}), must be one of {1}"  # noqa: E501
                .format(syncto_net_suite__ns, allowed_values)
            )

        self._syncto_net_suite__ns = syncto_net_suite__ns

    @property
    def account_number(self):
        """Gets the account_number of this POSTAccountType.  # noqa: E501

        A unique account number, up to 50 characters that do not begin with the default account number prefix.  If no account number is specified, one is generated.   # noqa: E501

        :return: The account_number of this POSTAccountType.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this POSTAccountType.

        A unique account number, up to 50 characters that do not begin with the default account number prefix.  If no account number is specified, one is generated.   # noqa: E501

        :param account_number: The account_number of this POSTAccountType.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def additional_email_addresses(self):
        """Gets the additional_email_addresses of this POSTAccountType.  # noqa: E501

        A list of additional email addresses to receive emailed invoices. Use a comma to separate each email address.  **Note:** Invoices are emailed to the email addresses specified in this field only when the `invoiceDeliveryPrefsEmail` field is `true`.   # noqa: E501

        :return: The additional_email_addresses of this POSTAccountType.  # noqa: E501
        :rtype: list[str]
        """
        return self._additional_email_addresses

    @additional_email_addresses.setter
    def additional_email_addresses(self, additional_email_addresses):
        """Sets the additional_email_addresses of this POSTAccountType.

        A list of additional email addresses to receive emailed invoices. Use a comma to separate each email address.  **Note:** Invoices are emailed to the email addresses specified in this field only when the `invoiceDeliveryPrefsEmail` field is `true`.   # noqa: E501

        :param additional_email_addresses: The additional_email_addresses of this POSTAccountType.  # noqa: E501
        :type: list[str]
        """

        self._additional_email_addresses = additional_email_addresses

    @property
    def apply_credit_balance(self):
        """Gets the apply_credit_balance of this POSTAccountType.  # noqa: E501

        Applies a credit balance to an invoice.  If the value is `true`, the credit balance is applied to the invoice. If the value is `false`, no action is taken.  Prerequisite: `invoice` must be `true`.  To view the credit balance adjustment, retrieve the details of the invoice using the Get Invoices method.   **Note:**    - If you are using the field `invoiceCollect` rather than the field `invoice`, the `invoiceCollect` value must be `true`.   - This field is deprecated if you have the Invoice Settlement feature enabled.    # noqa: E501

        :return: The apply_credit_balance of this POSTAccountType.  # noqa: E501
        :rtype: bool
        """
        return self._apply_credit_balance

    @apply_credit_balance.setter
    def apply_credit_balance(self, apply_credit_balance):
        """Sets the apply_credit_balance of this POSTAccountType.

        Applies a credit balance to an invoice.  If the value is `true`, the credit balance is applied to the invoice. If the value is `false`, no action is taken.  Prerequisite: `invoice` must be `true`.  To view the credit balance adjustment, retrieve the details of the invoice using the Get Invoices method.   **Note:**    - If you are using the field `invoiceCollect` rather than the field `invoice`, the `invoiceCollect` value must be `true`.   - This field is deprecated if you have the Invoice Settlement feature enabled.    # noqa: E501

        :param apply_credit_balance: The apply_credit_balance of this POSTAccountType.  # noqa: E501
        :type: bool
        """

        self._apply_credit_balance = apply_credit_balance

    @property
    def auto_pay(self):
        """Gets the auto_pay of this POSTAccountType.  # noqa: E501

        Specifies whether future payments are to be automatically billed when they are due. Possible values are: `true`, `false`.   # noqa: E501

        :return: The auto_pay of this POSTAccountType.  # noqa: E501
        :rtype: bool
        """
        return self._auto_pay

    @auto_pay.setter
    def auto_pay(self, auto_pay):
        """Sets the auto_pay of this POSTAccountType.

        Specifies whether future payments are to be automatically billed when they are due. Possible values are: `true`, `false`.   # noqa: E501

        :param auto_pay: The auto_pay of this POSTAccountType.  # noqa: E501
        :type: bool
        """

        self._auto_pay = auto_pay

    @property
    def batch(self):
        """Gets the batch of this POSTAccountType.  # noqa: E501

        The alias name given to a batch. A string of 50 characters or less.   # noqa: E501

        :return: The batch of this POSTAccountType.  # noqa: E501
        :rtype: str
        """
        return self._batch

    @batch.setter
    def batch(self, batch):
        """Sets the batch of this POSTAccountType.

        The alias name given to a batch. A string of 50 characters or less.   # noqa: E501

        :param batch: The batch of this POSTAccountType.  # noqa: E501
        :type: str
        """

        self._batch = batch

    @property
    def bill_cycle_day(self):
        """Gets the bill_cycle_day of this POSTAccountType.  # noqa: E501

        The account's bill cycle day (BCD), when bill runs generate invoices for the account.  Specify any day of the month (1-31, where 31 = end-of-month), or 0 for auto-set.  Required if no subscription will be created.   Optional if a subscription is created and defaults to the day-of-the-month of the subscription's `contractEffectiveDate`.   # noqa: E501

        :return: The bill_cycle_day of this POSTAccountType.  # noqa: E501
        :rtype: int
        """
        return self._bill_cycle_day

    @bill_cycle_day.setter
    def bill_cycle_day(self, bill_cycle_day):
        """Sets the bill_cycle_day of this POSTAccountType.

        The account's bill cycle day (BCD), when bill runs generate invoices for the account.  Specify any day of the month (1-31, where 31 = end-of-month), or 0 for auto-set.  Required if no subscription will be created.   Optional if a subscription is created and defaults to the day-of-the-month of the subscription's `contractEffectiveDate`.   # noqa: E501

        :param bill_cycle_day: The bill_cycle_day of this POSTAccountType.  # noqa: E501
        :type: int
        """

        self._bill_cycle_day = bill_cycle_day

    @property
    def bill_to_contact(self):
        """Gets the bill_to_contact of this POSTAccountType.  # noqa: E501


        :return: The bill_to_contact of this POSTAccountType.  # noqa: E501
        :rtype: POSTAccountTypeBillToContact
        """
        return self._bill_to_contact

    @bill_to_contact.setter
    def bill_to_contact(self, bill_to_contact):
        """Sets the bill_to_contact of this POSTAccountType.


        :param bill_to_contact: The bill_to_contact of this POSTAccountType.  # noqa: E501
        :type: POSTAccountTypeBillToContact
        """
        if bill_to_contact is None:
            raise ValueError("Invalid value for `bill_to_contact`, must not be `None`")  # noqa: E501

        self._bill_to_contact = bill_to_contact

    @property
    def collect(self):
        """Gets the collect of this POSTAccountType.  # noqa: E501

        Collects an automatic payment for a subscription. The collection generated in this operation is only for this subscription, not for the entire customer account.  If the value is `true`, the automatic payment is collected. If the value is `false`, no action is taken.  The default value is `true`.  Prerequisite: invoice must be `true`.   **Note:** This field is in Zuora REST API version control. Supported minor versions are 196.0 or later. To use this field in the method, you must set the `zuora-version` parameter to the minor version number in the request header.   # noqa: E501

        :return: The collect of this POSTAccountType.  # noqa: E501
        :rtype: str
        """
        return self._collect

    @collect.setter
    def collect(self, collect):
        """Sets the collect of this POSTAccountType.

        Collects an automatic payment for a subscription. The collection generated in this operation is only for this subscription, not for the entire customer account.  If the value is `true`, the automatic payment is collected. If the value is `false`, no action is taken.  The default value is `true`.  Prerequisite: invoice must be `true`.   **Note:** This field is in Zuora REST API version control. Supported minor versions are 196.0 or later. To use this field in the method, you must set the `zuora-version` parameter to the minor version number in the request header.   # noqa: E501

        :param collect: The collect of this POSTAccountType.  # noqa: E501
        :type: str
        """

        self._collect = collect

    @property
    def communication_profile_id(self):
        """Gets the communication_profile_id of this POSTAccountType.  # noqa: E501

        The ID of a communication profile.            # noqa: E501

        :return: The communication_profile_id of this POSTAccountType.  # noqa: E501
        :rtype: str
        """
        return self._communication_profile_id

    @communication_profile_id.setter
    def communication_profile_id(self, communication_profile_id):
        """Sets the communication_profile_id of this POSTAccountType.

        The ID of a communication profile.            # noqa: E501

        :param communication_profile_id: The communication_profile_id of this POSTAccountType.  # noqa: E501
        :type: str
        """

        self._communication_profile_id = communication_profile_id

    @property
    def credit_card(self):
        """Gets the credit_card of this POSTAccountType.  # noqa: E501


        :return: The credit_card of this POSTAccountType.  # noqa: E501
        :rtype: POSTAccountTypeCreditCard
        """
        return self._credit_card

    @credit_card.setter
    def credit_card(self, credit_card):
        """Sets the credit_card of this POSTAccountType.


        :param credit_card: The credit_card of this POSTAccountType.  # noqa: E501
        :type: POSTAccountTypeCreditCard
        """

        self._credit_card = credit_card

    @property
    def credit_memo_template_id(self):
        """Gets the credit_memo_template_id of this POSTAccountType.  # noqa: E501

        **Note**: This field is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  The unique ID of the credit memo template, configured in **Billing Settings** > **Manage Billing Document Configuration** through the Zuora UI. For example, 2c92c08a6246fdf101626b1b3fe0144b.   # noqa: E501

        :return: The credit_memo_template_id of this POSTAccountType.  # noqa: E501
        :rtype: str
        """
        return self._credit_memo_template_id

    @credit_memo_template_id.setter
    def credit_memo_template_id(self, credit_memo_template_id):
        """Sets the credit_memo_template_id of this POSTAccountType.

        **Note**: This field is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  The unique ID of the credit memo template, configured in **Billing Settings** > **Manage Billing Document Configuration** through the Zuora UI. For example, 2c92c08a6246fdf101626b1b3fe0144b.   # noqa: E501

        :param credit_memo_template_id: The credit_memo_template_id of this POSTAccountType.  # noqa: E501
        :type: str
        """

        self._credit_memo_template_id = credit_memo_template_id

    @property
    def crm_id(self):
        """Gets the crm_id of this POSTAccountType.  # noqa: E501

        CRM account ID for the account, up to 100 characters.   # noqa: E501

        :return: The crm_id of this POSTAccountType.  # noqa: E501
        :rtype: str
        """
        return self._crm_id

    @crm_id.setter
    def crm_id(self, crm_id):
        """Sets the crm_id of this POSTAccountType.

        CRM account ID for the account, up to 100 characters.   # noqa: E501

        :param crm_id: The crm_id of this POSTAccountType.  # noqa: E501
        :type: str
        """

        self._crm_id = crm_id

    @property
    def currency(self):
        """Gets the currency of this POSTAccountType.  # noqa: E501

        A currency as defined in Billing Settings in the Zuora UI.   # noqa: E501

        :return: The currency of this POSTAccountType.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this POSTAccountType.

        A currency as defined in Billing Settings in the Zuora UI.   # noqa: E501

        :param currency: The currency of this POSTAccountType.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def debit_memo_template_id(self):
        """Gets the debit_memo_template_id of this POSTAccountType.  # noqa: E501

        **Note**: This field is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  The unique ID of the debit memo template, configured in **Billing Settings** > **Manage Billing Document Configuration** through the Zuora UI. For example, 2c92c08d62470a8501626b19d24f19e2.   # noqa: E501

        :return: The debit_memo_template_id of this POSTAccountType.  # noqa: E501
        :rtype: str
        """
        return self._debit_memo_template_id

    @debit_memo_template_id.setter
    def debit_memo_template_id(self, debit_memo_template_id):
        """Sets the debit_memo_template_id of this POSTAccountType.

        **Note**: This field is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  The unique ID of the debit memo template, configured in **Billing Settings** > **Manage Billing Document Configuration** through the Zuora UI. For example, 2c92c08d62470a8501626b19d24f19e2.   # noqa: E501

        :param debit_memo_template_id: The debit_memo_template_id of this POSTAccountType.  # noqa: E501
        :type: str
        """

        self._debit_memo_template_id = debit_memo_template_id

    @property
    def hpm_credit_card_payment_method_id(self):
        """Gets the hpm_credit_card_payment_method_id of this POSTAccountType.  # noqa: E501

        The ID of the HPM credit card payment method associated with this account. You must provide either this field or the `creditCard` structure, but not both.  **Note:** Non-credit card payment methods are not supported.   # noqa: E501

        :return: The hpm_credit_card_payment_method_id of this POSTAccountType.  # noqa: E501
        :rtype: str
        """
        return self._hpm_credit_card_payment_method_id

    @hpm_credit_card_payment_method_id.setter
    def hpm_credit_card_payment_method_id(self, hpm_credit_card_payment_method_id):
        """Sets the hpm_credit_card_payment_method_id of this POSTAccountType.

        The ID of the HPM credit card payment method associated with this account. You must provide either this field or the `creditCard` structure, but not both.  **Note:** Non-credit card payment methods are not supported.   # noqa: E501

        :param hpm_credit_card_payment_method_id: The hpm_credit_card_payment_method_id of this POSTAccountType.  # noqa: E501
        :type: str
        """

        self._hpm_credit_card_payment_method_id = hpm_credit_card_payment_method_id

    @property
    def invoice(self):
        """Gets the invoice of this POSTAccountType.  # noqa: E501

        **Note:** This field has been replaced by the `runBilling` field. The `invoice` field is only available for backward compatibility.    Creates an invoice for a subscription. The invoice generated in this operation is only for this subscription, not for the entire customer account.   If the value is `true`, an invoice is created. If the value is `false`, no action is taken.   The default value is `true`.    This field is in REST API minor version control. To use this field in the method, you can set the `zuora-version` parameter to the minor version number in the request header. Supported minor versions are `196.0` and `207.0`.   # noqa: E501

        :return: The invoice of this POSTAccountType.  # noqa: E501
        :rtype: bool
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice):
        """Sets the invoice of this POSTAccountType.

        **Note:** This field has been replaced by the `runBilling` field. The `invoice` field is only available for backward compatibility.    Creates an invoice for a subscription. The invoice generated in this operation is only for this subscription, not for the entire customer account.   If the value is `true`, an invoice is created. If the value is `false`, no action is taken.   The default value is `true`.    This field is in REST API minor version control. To use this field in the method, you can set the `zuora-version` parameter to the minor version number in the request header. Supported minor versions are `196.0` and `207.0`.   # noqa: E501

        :param invoice: The invoice of this POSTAccountType.  # noqa: E501
        :type: bool
        """

        self._invoice = invoice

    @property
    def invoice_collect(self):
        """Gets the invoice_collect of this POSTAccountType.  # noqa: E501

        **Note:** This field has been replaced by the `invoice` field and the `collect` field. `invoiceCollect` is available only for backward compatibility.  If `true` (default), and a subscription is created, an invoice is generated at account creation time and payment is immediately collected using the account's default payment method.  This field is in Zuora REST API version control. Supported minor versions are 186.0, 187.0, 188.0, 189.0, and 196.0.   # noqa: E501

        :return: The invoice_collect of this POSTAccountType.  # noqa: E501
        :rtype: bool
        """
        return self._invoice_collect

    @invoice_collect.setter
    def invoice_collect(self, invoice_collect):
        """Sets the invoice_collect of this POSTAccountType.

        **Note:** This field has been replaced by the `invoice` field and the `collect` field. `invoiceCollect` is available only for backward compatibility.  If `true` (default), and a subscription is created, an invoice is generated at account creation time and payment is immediately collected using the account's default payment method.  This field is in Zuora REST API version control. Supported minor versions are 186.0, 187.0, 188.0, 189.0, and 196.0.   # noqa: E501

        :param invoice_collect: The invoice_collect of this POSTAccountType.  # noqa: E501
        :type: bool
        """

        self._invoice_collect = invoice_collect

    @property
    def invoice_delivery_prefs_email(self):
        """Gets the invoice_delivery_prefs_email of this POSTAccountType.  # noqa: E501

        Whether the customer wants to receive invoices through email.   The default value is `false`.   # noqa: E501

        :return: The invoice_delivery_prefs_email of this POSTAccountType.  # noqa: E501
        :rtype: bool
        """
        return self._invoice_delivery_prefs_email

    @invoice_delivery_prefs_email.setter
    def invoice_delivery_prefs_email(self, invoice_delivery_prefs_email):
        """Sets the invoice_delivery_prefs_email of this POSTAccountType.

        Whether the customer wants to receive invoices through email.   The default value is `false`.   # noqa: E501

        :param invoice_delivery_prefs_email: The invoice_delivery_prefs_email of this POSTAccountType.  # noqa: E501
        :type: bool
        """

        self._invoice_delivery_prefs_email = invoice_delivery_prefs_email

    @property
    def invoice_delivery_prefs_print(self):
        """Gets the invoice_delivery_prefs_print of this POSTAccountType.  # noqa: E501

        Whether the customer wants to receive printed invoices, such as through postal mail.  The default value is `false`.   # noqa: E501

        :return: The invoice_delivery_prefs_print of this POSTAccountType.  # noqa: E501
        :rtype: bool
        """
        return self._invoice_delivery_prefs_print

    @invoice_delivery_prefs_print.setter
    def invoice_delivery_prefs_print(self, invoice_delivery_prefs_print):
        """Sets the invoice_delivery_prefs_print of this POSTAccountType.

        Whether the customer wants to receive printed invoices, such as through postal mail.  The default value is `false`.   # noqa: E501

        :param invoice_delivery_prefs_print: The invoice_delivery_prefs_print of this POSTAccountType.  # noqa: E501
        :type: bool
        """

        self._invoice_delivery_prefs_print = invoice_delivery_prefs_print

    @property
    def invoice_target_date(self):
        """Gets the invoice_target_date of this POSTAccountType.  # noqa: E501

        **Note:** This field has been replaced by the `targetDate` field. The `invoiceTargetDate` field is only available for backward compatibility.     Date through which to calculate charges if an invoice is generated, as yyyy-mm-dd. Default is current date.   This field is in REST API minor version control. To use this field in the method, you can set the `zuora-version` parameter to the minor version number in the request header. Supported minor versions are `207.0` and earlier.    # noqa: E501

        :return: The invoice_target_date of this POSTAccountType.  # noqa: E501
        :rtype: date
        """
        return self._invoice_target_date

    @invoice_target_date.setter
    def invoice_target_date(self, invoice_target_date):
        """Sets the invoice_target_date of this POSTAccountType.

        **Note:** This field has been replaced by the `targetDate` field. The `invoiceTargetDate` field is only available for backward compatibility.     Date through which to calculate charges if an invoice is generated, as yyyy-mm-dd. Default is current date.   This field is in REST API minor version control. To use this field in the method, you can set the `zuora-version` parameter to the minor version number in the request header. Supported minor versions are `207.0` and earlier.    # noqa: E501

        :param invoice_target_date: The invoice_target_date of this POSTAccountType.  # noqa: E501
        :type: date
        """

        self._invoice_target_date = invoice_target_date

    @property
    def invoice_template_id(self):
        """Gets the invoice_template_id of this POSTAccountType.  # noqa: E501

        Invoice template ID, configured in Billing Settings in the Zuora UI.   # noqa: E501

        :return: The invoice_template_id of this POSTAccountType.  # noqa: E501
        :rtype: str
        """
        return self._invoice_template_id

    @invoice_template_id.setter
    def invoice_template_id(self, invoice_template_id):
        """Sets the invoice_template_id of this POSTAccountType.

        Invoice template ID, configured in Billing Settings in the Zuora UI.   # noqa: E501

        :param invoice_template_id: The invoice_template_id of this POSTAccountType.  # noqa: E501
        :type: str
        """

        self._invoice_template_id = invoice_template_id

    @property
    def name(self):
        """Gets the name of this POSTAccountType.  # noqa: E501

        Account name, up to 255 characters.   # noqa: E501

        :return: The name of this POSTAccountType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this POSTAccountType.

        Account name, up to 255 characters.   # noqa: E501

        :param name: The name of this POSTAccountType.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this POSTAccountType.  # noqa: E501

        A string of up to 65,535 characters.  # noqa: E501

        :return: The notes of this POSTAccountType.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this POSTAccountType.

        A string of up to 65,535 characters.  # noqa: E501

        :param notes: The notes of this POSTAccountType.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def parent_id(self):
        """Gets the parent_id of this POSTAccountType.  # noqa: E501

        Identifier of the parent customer account for this Account object. The length is 32 characters. Use this field if you have customer hierarchy enabled.  # noqa: E501

        :return: The parent_id of this POSTAccountType.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this POSTAccountType.

        Identifier of the parent customer account for this Account object. The length is 32 characters. Use this field if you have customer hierarchy enabled.  # noqa: E501

        :param parent_id: The parent_id of this POSTAccountType.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def payment_gateway(self):
        """Gets the payment_gateway of this POSTAccountType.  # noqa: E501

        The name of the payment gateway instance. If null or left unassigned, the Account will use the Default Gateway.   # noqa: E501

        :return: The payment_gateway of this POSTAccountType.  # noqa: E501
        :rtype: str
        """
        return self._payment_gateway

    @payment_gateway.setter
    def payment_gateway(self, payment_gateway):
        """Sets the payment_gateway of this POSTAccountType.

        The name of the payment gateway instance. If null or left unassigned, the Account will use the Default Gateway.   # noqa: E501

        :param payment_gateway: The payment_gateway of this POSTAccountType.  # noqa: E501
        :type: str
        """

        self._payment_gateway = payment_gateway

    @property
    def payment_term(self):
        """Gets the payment_term of this POSTAccountType.  # noqa: E501

        Payment terms for this account. Possible values are: `Due Upon Receipt`, `Net 30`, `Net 60`, `Net 90`.   # noqa: E501

        :return: The payment_term of this POSTAccountType.  # noqa: E501
        :rtype: str
        """
        return self._payment_term

    @payment_term.setter
    def payment_term(self, payment_term):
        """Sets the payment_term of this POSTAccountType.

        Payment terms for this account. Possible values are: `Due Upon Receipt`, `Net 30`, `Net 60`, `Net 90`.   # noqa: E501

        :param payment_term: The payment_term of this POSTAccountType.  # noqa: E501
        :type: str
        """

        self._payment_term = payment_term

    @property
    def run_billing(self):
        """Gets the run_billing of this POSTAccountType.  # noqa: E501

        Creates an invoice for a subscription. If you have the Invoice Settlement feature enabled, a credit memo might also be created based on the [invoice and credit memo generation rule.](https://knowledgecenter.zuora.com/CB_Billing/Invoice_Settlement/Credit_and_Debit_Memos/Rules_for_Generating_Invoices_and_Credit_Memos).    The billing documents generated in this operation is only for this subscription, not for the entire customer account.   Possible values:  - `true`: An invoice is created. If you have the Invoice Settlement feature enabled, a credit memo might also be created.   - `false`: No invoice is created.   **Note:** This field is in Zuora REST API version control. Supported minor versions are `211.0` or later. To use this field in the method, you must set the `zuora-version` parameter to the minor version number in the request header.   # noqa: E501

        :return: The run_billing of this POSTAccountType.  # noqa: E501
        :rtype: bool
        """
        return self._run_billing

    @run_billing.setter
    def run_billing(self, run_billing):
        """Sets the run_billing of this POSTAccountType.

        Creates an invoice for a subscription. If you have the Invoice Settlement feature enabled, a credit memo might also be created based on the [invoice and credit memo generation rule.](https://knowledgecenter.zuora.com/CB_Billing/Invoice_Settlement/Credit_and_Debit_Memos/Rules_for_Generating_Invoices_and_Credit_Memos).    The billing documents generated in this operation is only for this subscription, not for the entire customer account.   Possible values:  - `true`: An invoice is created. If you have the Invoice Settlement feature enabled, a credit memo might also be created.   - `false`: No invoice is created.   **Note:** This field is in Zuora REST API version control. Supported minor versions are `211.0` or later. To use this field in the method, you must set the `zuora-version` parameter to the minor version number in the request header.   # noqa: E501

        :param run_billing: The run_billing of this POSTAccountType.  # noqa: E501
        :type: bool
        """

        self._run_billing = run_billing

    @property
    def sales_rep(self):
        """Gets the sales_rep of this POSTAccountType.  # noqa: E501

        The name of the sales representative associated with this account, if applicable. Maximum of 50 characters.  # noqa: E501

        :return: The sales_rep of this POSTAccountType.  # noqa: E501
        :rtype: str
        """
        return self._sales_rep

    @sales_rep.setter
    def sales_rep(self, sales_rep):
        """Sets the sales_rep of this POSTAccountType.

        The name of the sales representative associated with this account, if applicable. Maximum of 50 characters.  # noqa: E501

        :param sales_rep: The sales_rep of this POSTAccountType.  # noqa: E501
        :type: str
        """

        self._sales_rep = sales_rep

    @property
    def sold_to_contact(self):
        """Gets the sold_to_contact of this POSTAccountType.  # noqa: E501


        :return: The sold_to_contact of this POSTAccountType.  # noqa: E501
        :rtype: POSTAccountTypeSoldToContact
        """
        return self._sold_to_contact

    @sold_to_contact.setter
    def sold_to_contact(self, sold_to_contact):
        """Sets the sold_to_contact of this POSTAccountType.


        :param sold_to_contact: The sold_to_contact of this POSTAccountType.  # noqa: E501
        :type: POSTAccountTypeSoldToContact
        """

        self._sold_to_contact = sold_to_contact

    @property
    def subscription(self):
        """Gets the subscription of this POSTAccountType.  # noqa: E501


        :return: The subscription of this POSTAccountType.  # noqa: E501
        :rtype: POSTAccountTypeSubscription
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this POSTAccountType.


        :param subscription: The subscription of this POSTAccountType.  # noqa: E501
        :type: POSTAccountTypeSubscription
        """

        self._subscription = subscription

    @property
    def tagging(self):
        """Gets the tagging of this POSTAccountType.  # noqa: E501

          # noqa: E501

        :return: The tagging of this POSTAccountType.  # noqa: E501
        :rtype: str
        """
        return self._tagging

    @tagging.setter
    def tagging(self, tagging):
        """Sets the tagging of this POSTAccountType.

          # noqa: E501

        :param tagging: The tagging of this POSTAccountType.  # noqa: E501
        :type: str
        """

        self._tagging = tagging

    @property
    def target_date(self):
        """Gets the target_date of this POSTAccountType.  # noqa: E501

        Date through which to calculate charges if an invoice or a credit memo is generated, as yyyy-mm-dd. Default is current date.  **Note:** The credit memo is only available only if you have the Invoice Settlement feature enabled.  This field is in Zuora REST API version control. Supported minor versions are `211.0` and later. To use this field in the method, you must set the  `zuora-version` parameter to the minor version number in the request header.   # noqa: E501

        :return: The target_date of this POSTAccountType.  # noqa: E501
        :rtype: date
        """
        return self._target_date

    @target_date.setter
    def target_date(self, target_date):
        """Sets the target_date of this POSTAccountType.

        Date through which to calculate charges if an invoice or a credit memo is generated, as yyyy-mm-dd. Default is current date.  **Note:** The credit memo is only available only if you have the Invoice Settlement feature enabled.  This field is in Zuora REST API version control. Supported minor versions are `211.0` and later. To use this field in the method, you must set the  `zuora-version` parameter to the minor version number in the request header.   # noqa: E501

        :param target_date: The target_date of this POSTAccountType.  # noqa: E501
        :type: date
        """

        self._target_date = target_date

    @property
    def tax_info(self):
        """Gets the tax_info of this POSTAccountType.  # noqa: E501


        :return: The tax_info of this POSTAccountType.  # noqa: E501
        :rtype: POSTAccountTypeTaxInfo
        """
        return self._tax_info

    @tax_info.setter
    def tax_info(self, tax_info):
        """Sets the tax_info of this POSTAccountType.


        :param tax_info: The tax_info of this POSTAccountType.  # noqa: E501
        :type: POSTAccountTypeTaxInfo
        """

        self._tax_info = tax_info

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
        if not isinstance(other, POSTAccountType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
