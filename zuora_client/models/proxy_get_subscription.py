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

from zuora_client.models.subscription_object_custom_fields import SubscriptionObjectCustomFields  # noqa: F401,E501
from zuora_client.models.subscription_object_ns_fields import SubscriptionObjectNSFields  # noqa: F401,E501
from zuora_client.models.subscription_object_qt_fields import SubscriptionObjectQTFields  # noqa: F401,E501


class ProxyGetSubscription(object):
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
        'cpq_bundle_json_id__qt': 'str',
        'opportunity_close_date__qt': 'date',
        'opportunity_name__qt': 'str',
        'quote_business_type__qt': 'str',
        'quote_number__qt': 'str',
        'quote_type__qt': 'str',
        'integration_id__ns': 'str',
        'integration_status__ns': 'str',
        'project__ns': 'str',
        'sales_order__ns': 'str',
        'sync_date__ns': 'str',
        'account_id': 'str',
        'auto_renew': 'bool',
        'cancelled_date': 'date',
        'contract_acceptance_date': 'date',
        'contract_effective_date': 'date',
        'created_by_id': 'str',
        'created_date': 'datetime',
        'creator_account_id': 'str',
        'creator_invoice_owner_id': 'str',
        'current_term': 'int',
        'current_term_period_type': 'str',
        'id': 'str',
        'initial_term': 'int',
        'initial_term_period_type': 'str',
        'invoice_owner_id': 'str',
        'is_invoice_separate': 'bool',
        'name': 'str',
        'notes': 'str',
        'original_created_date': 'datetime',
        'original_id': 'str',
        'previous_subscription_id': 'str',
        'renewal_setting': 'str',
        'renewal_term': 'int',
        'renewal_term_period_type': 'str',
        'service_activation_date': 'date',
        'status': 'str',
        'subscription_end_date': 'date',
        'subscription_start_date': 'date',
        'term_end_date': 'date',
        'term_start_date': 'date',
        'term_type': 'str',
        'updated_by_id': 'str',
        'updated_date': 'datetime',
        'version': 'int'
    }

    attribute_map = {
        'cpq_bundle_json_id__qt': 'CpqBundleJsonId__QT',
        'opportunity_close_date__qt': 'OpportunityCloseDate__QT',
        'opportunity_name__qt': 'OpportunityName__QT',
        'quote_business_type__qt': 'QuoteBusinessType__QT',
        'quote_number__qt': 'QuoteNumber__QT',
        'quote_type__qt': 'QuoteType__QT',
        'integration_id__ns': 'IntegrationId__NS',
        'integration_status__ns': 'IntegrationStatus__NS',
        'project__ns': 'Project__NS',
        'sales_order__ns': 'SalesOrder__NS',
        'sync_date__ns': 'SyncDate__NS',
        'account_id': 'AccountId',
        'auto_renew': 'AutoRenew',
        'cancelled_date': 'CancelledDate',
        'contract_acceptance_date': 'ContractAcceptanceDate',
        'contract_effective_date': 'ContractEffectiveDate',
        'created_by_id': 'CreatedById',
        'created_date': 'CreatedDate',
        'creator_account_id': 'CreatorAccountId',
        'creator_invoice_owner_id': 'CreatorInvoiceOwnerId',
        'current_term': 'CurrentTerm',
        'current_term_period_type': 'CurrentTermPeriodType',
        'id': 'Id',
        'initial_term': 'InitialTerm',
        'initial_term_period_type': 'InitialTermPeriodType',
        'invoice_owner_id': 'InvoiceOwnerId',
        'is_invoice_separate': 'IsInvoiceSeparate',
        'name': 'Name',
        'notes': 'Notes',
        'original_created_date': 'OriginalCreatedDate',
        'original_id': 'OriginalId',
        'previous_subscription_id': 'PreviousSubscriptionId',
        'renewal_setting': 'RenewalSetting',
        'renewal_term': 'RenewalTerm',
        'renewal_term_period_type': 'RenewalTermPeriodType',
        'service_activation_date': 'ServiceActivationDate',
        'status': 'Status',
        'subscription_end_date': 'SubscriptionEndDate',
        'subscription_start_date': 'SubscriptionStartDate',
        'term_end_date': 'TermEndDate',
        'term_start_date': 'TermStartDate',
        'term_type': 'TermType',
        'updated_by_id': 'UpdatedById',
        'updated_date': 'UpdatedDate',
        'version': 'Version'
    }

    def __init__(self, cpq_bundle_json_id__qt=None, opportunity_close_date__qt=None, opportunity_name__qt=None, quote_business_type__qt=None, quote_number__qt=None, quote_type__qt=None, integration_id__ns=None, integration_status__ns=None, project__ns=None, sales_order__ns=None, sync_date__ns=None, account_id=None, auto_renew=None, cancelled_date=None, contract_acceptance_date=None, contract_effective_date=None, created_by_id=None, created_date=None, creator_account_id=None, creator_invoice_owner_id=None, current_term=None, current_term_period_type=None, id=None, initial_term=None, initial_term_period_type=None, invoice_owner_id=None, is_invoice_separate=None, name=None, notes=None, original_created_date=None, original_id=None, previous_subscription_id=None, renewal_setting=None, renewal_term=None, renewal_term_period_type=None, service_activation_date=None, status=None, subscription_end_date=None, subscription_start_date=None, term_end_date=None, term_start_date=None, term_type=None, updated_by_id=None, updated_date=None, version=None):  # noqa: E501
        """ProxyGetSubscription - a model defined in Swagger"""  # noqa: E501

        self._cpq_bundle_json_id__qt = None
        self._opportunity_close_date__qt = None
        self._opportunity_name__qt = None
        self._quote_business_type__qt = None
        self._quote_number__qt = None
        self._quote_type__qt = None
        self._integration_id__ns = None
        self._integration_status__ns = None
        self._project__ns = None
        self._sales_order__ns = None
        self._sync_date__ns = None
        self._account_id = None
        self._auto_renew = None
        self._cancelled_date = None
        self._contract_acceptance_date = None
        self._contract_effective_date = None
        self._created_by_id = None
        self._created_date = None
        self._creator_account_id = None
        self._creator_invoice_owner_id = None
        self._current_term = None
        self._current_term_period_type = None
        self._id = None
        self._initial_term = None
        self._initial_term_period_type = None
        self._invoice_owner_id = None
        self._is_invoice_separate = None
        self._name = None
        self._notes = None
        self._original_created_date = None
        self._original_id = None
        self._previous_subscription_id = None
        self._renewal_setting = None
        self._renewal_term = None
        self._renewal_term_period_type = None
        self._service_activation_date = None
        self._status = None
        self._subscription_end_date = None
        self._subscription_start_date = None
        self._term_end_date = None
        self._term_start_date = None
        self._term_type = None
        self._updated_by_id = None
        self._updated_date = None
        self._version = None
        self.discriminator = None

        if cpq_bundle_json_id__qt is not None:
            self.cpq_bundle_json_id__qt = cpq_bundle_json_id__qt
        if opportunity_close_date__qt is not None:
            self.opportunity_close_date__qt = opportunity_close_date__qt
        if opportunity_name__qt is not None:
            self.opportunity_name__qt = opportunity_name__qt
        if quote_business_type__qt is not None:
            self.quote_business_type__qt = quote_business_type__qt
        if quote_number__qt is not None:
            self.quote_number__qt = quote_number__qt
        if quote_type__qt is not None:
            self.quote_type__qt = quote_type__qt
        if integration_id__ns is not None:
            self.integration_id__ns = integration_id__ns
        if integration_status__ns is not None:
            self.integration_status__ns = integration_status__ns
        if project__ns is not None:
            self.project__ns = project__ns
        if sales_order__ns is not None:
            self.sales_order__ns = sales_order__ns
        if sync_date__ns is not None:
            self.sync_date__ns = sync_date__ns
        if account_id is not None:
            self.account_id = account_id
        if auto_renew is not None:
            self.auto_renew = auto_renew
        if cancelled_date is not None:
            self.cancelled_date = cancelled_date
        if contract_acceptance_date is not None:
            self.contract_acceptance_date = contract_acceptance_date
        if contract_effective_date is not None:
            self.contract_effective_date = contract_effective_date
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_date is not None:
            self.created_date = created_date
        if creator_account_id is not None:
            self.creator_account_id = creator_account_id
        if creator_invoice_owner_id is not None:
            self.creator_invoice_owner_id = creator_invoice_owner_id
        if current_term is not None:
            self.current_term = current_term
        if current_term_period_type is not None:
            self.current_term_period_type = current_term_period_type
        if id is not None:
            self.id = id
        if initial_term is not None:
            self.initial_term = initial_term
        if initial_term_period_type is not None:
            self.initial_term_period_type = initial_term_period_type
        if invoice_owner_id is not None:
            self.invoice_owner_id = invoice_owner_id
        if is_invoice_separate is not None:
            self.is_invoice_separate = is_invoice_separate
        if name is not None:
            self.name = name
        if notes is not None:
            self.notes = notes
        if original_created_date is not None:
            self.original_created_date = original_created_date
        if original_id is not None:
            self.original_id = original_id
        if previous_subscription_id is not None:
            self.previous_subscription_id = previous_subscription_id
        if renewal_setting is not None:
            self.renewal_setting = renewal_setting
        if renewal_term is not None:
            self.renewal_term = renewal_term
        if renewal_term_period_type is not None:
            self.renewal_term_period_type = renewal_term_period_type
        if service_activation_date is not None:
            self.service_activation_date = service_activation_date
        if status is not None:
            self.status = status
        if subscription_end_date is not None:
            self.subscription_end_date = subscription_end_date
        if subscription_start_date is not None:
            self.subscription_start_date = subscription_start_date
        if term_end_date is not None:
            self.term_end_date = term_end_date
        if term_start_date is not None:
            self.term_start_date = term_start_date
        if term_type is not None:
            self.term_type = term_type
        if updated_by_id is not None:
            self.updated_by_id = updated_by_id
        if updated_date is not None:
            self.updated_date = updated_date
        if version is not None:
            self.version = version

    @property
    def cpq_bundle_json_id__qt(self):
        """Gets the cpq_bundle_json_id__qt of this ProxyGetSubscription.  # noqa: E501

        The Bundle product structures from Zuora Quotes if you utilize Bundling in Salesforce. Do not change the value in this field.   # noqa: E501

        :return: The cpq_bundle_json_id__qt of this ProxyGetSubscription.  # noqa: E501
        :rtype: str
        """
        return self._cpq_bundle_json_id__qt

    @cpq_bundle_json_id__qt.setter
    def cpq_bundle_json_id__qt(self, cpq_bundle_json_id__qt):
        """Sets the cpq_bundle_json_id__qt of this ProxyGetSubscription.

        The Bundle product structures from Zuora Quotes if you utilize Bundling in Salesforce. Do not change the value in this field.   # noqa: E501

        :param cpq_bundle_json_id__qt: The cpq_bundle_json_id__qt of this ProxyGetSubscription.  # noqa: E501
        :type: str
        """
        if cpq_bundle_json_id__qt is not None and len(cpq_bundle_json_id__qt) > 32:
            raise ValueError("Invalid value for `cpq_bundle_json_id__qt`, length must be less than or equal to `32`")  # noqa: E501

        self._cpq_bundle_json_id__qt = cpq_bundle_json_id__qt

    @property
    def opportunity_close_date__qt(self):
        """Gets the opportunity_close_date__qt of this ProxyGetSubscription.  # noqa: E501

        The closing date of the Opportunity. This field is used in Zuora data sources to report on Subscription metrics. If the subscription originated from Zuora Quotes, the value is populated with the value from Zuora Quotes.   # noqa: E501

        :return: The opportunity_close_date__qt of this ProxyGetSubscription.  # noqa: E501
        :rtype: date
        """
        return self._opportunity_close_date__qt

    @opportunity_close_date__qt.setter
    def opportunity_close_date__qt(self, opportunity_close_date__qt):
        """Sets the opportunity_close_date__qt of this ProxyGetSubscription.

        The closing date of the Opportunity. This field is used in Zuora data sources to report on Subscription metrics. If the subscription originated from Zuora Quotes, the value is populated with the value from Zuora Quotes.   # noqa: E501

        :param opportunity_close_date__qt: The opportunity_close_date__qt of this ProxyGetSubscription.  # noqa: E501
        :type: date
        """

        self._opportunity_close_date__qt = opportunity_close_date__qt

    @property
    def opportunity_name__qt(self):
        """Gets the opportunity_name__qt of this ProxyGetSubscription.  # noqa: E501

        The unique identifier of the Opportunity. This field is used in Zuora data sources to report on Subscription metrics. If the subscription originated from Zuora Quotes, the value is populated with the value from Zuora Quotes.   # noqa: E501

        :return: The opportunity_name__qt of this ProxyGetSubscription.  # noqa: E501
        :rtype: str
        """
        return self._opportunity_name__qt

    @opportunity_name__qt.setter
    def opportunity_name__qt(self, opportunity_name__qt):
        """Sets the opportunity_name__qt of this ProxyGetSubscription.

        The unique identifier of the Opportunity. This field is used in Zuora data sources to report on Subscription metrics. If the subscription originated from Zuora Quotes, the value is populated with the value from Zuora Quotes.   # noqa: E501

        :param opportunity_name__qt: The opportunity_name__qt of this ProxyGetSubscription.  # noqa: E501
        :type: str
        """
        if opportunity_name__qt is not None and len(opportunity_name__qt) > 100:
            raise ValueError("Invalid value for `opportunity_name__qt`, length must be less than or equal to `100`")  # noqa: E501

        self._opportunity_name__qt = opportunity_name__qt

    @property
    def quote_business_type__qt(self):
        """Gets the quote_business_type__qt of this ProxyGetSubscription.  # noqa: E501

        The specific identifier for the type of business transaction the Quote represents such as New, Upsell, Downsell, Renewal or Churn. This field is used in Zuora data sources to report on Subscription metrics. If the subscription originated from Zuora Quotes, the value is populated with the value from Zuora Quotes.   # noqa: E501

        :return: The quote_business_type__qt of this ProxyGetSubscription.  # noqa: E501
        :rtype: str
        """
        return self._quote_business_type__qt

    @quote_business_type__qt.setter
    def quote_business_type__qt(self, quote_business_type__qt):
        """Sets the quote_business_type__qt of this ProxyGetSubscription.

        The specific identifier for the type of business transaction the Quote represents such as New, Upsell, Downsell, Renewal or Churn. This field is used in Zuora data sources to report on Subscription metrics. If the subscription originated from Zuora Quotes, the value is populated with the value from Zuora Quotes.   # noqa: E501

        :param quote_business_type__qt: The quote_business_type__qt of this ProxyGetSubscription.  # noqa: E501
        :type: str
        """
        if quote_business_type__qt is not None and len(quote_business_type__qt) > 32:
            raise ValueError("Invalid value for `quote_business_type__qt`, length must be less than or equal to `32`")  # noqa: E501

        self._quote_business_type__qt = quote_business_type__qt

    @property
    def quote_number__qt(self):
        """Gets the quote_number__qt of this ProxyGetSubscription.  # noqa: E501

        The unique identifier of the Quote. This field is used in Zuora data sources to report on Subscription metrics. If the subscription originated from Zuora Quotes, the value is populated with the value from Zuora Quotes.   # noqa: E501

        :return: The quote_number__qt of this ProxyGetSubscription.  # noqa: E501
        :rtype: str
        """
        return self._quote_number__qt

    @quote_number__qt.setter
    def quote_number__qt(self, quote_number__qt):
        """Sets the quote_number__qt of this ProxyGetSubscription.

        The unique identifier of the Quote. This field is used in Zuora data sources to report on Subscription metrics. If the subscription originated from Zuora Quotes, the value is populated with the value from Zuora Quotes.   # noqa: E501

        :param quote_number__qt: The quote_number__qt of this ProxyGetSubscription.  # noqa: E501
        :type: str
        """
        if quote_number__qt is not None and len(quote_number__qt) > 32:
            raise ValueError("Invalid value for `quote_number__qt`, length must be less than or equal to `32`")  # noqa: E501

        self._quote_number__qt = quote_number__qt

    @property
    def quote_type__qt(self):
        """Gets the quote_type__qt of this ProxyGetSubscription.  # noqa: E501

        The Quote type that represents the subscription lifecycle stage such as New, Amendment, Renew or Cancel. This field is used in Zuora data sources to report on Subscription metrics. If the subscription originated from Zuora Quotes, the value is populated with the value from Zuora Quotes.   # noqa: E501

        :return: The quote_type__qt of this ProxyGetSubscription.  # noqa: E501
        :rtype: str
        """
        return self._quote_type__qt

    @quote_type__qt.setter
    def quote_type__qt(self, quote_type__qt):
        """Sets the quote_type__qt of this ProxyGetSubscription.

        The Quote type that represents the subscription lifecycle stage such as New, Amendment, Renew or Cancel. This field is used in Zuora data sources to report on Subscription metrics. If the subscription originated from Zuora Quotes, the value is populated with the value from Zuora Quotes.   # noqa: E501

        :param quote_type__qt: The quote_type__qt of this ProxyGetSubscription.  # noqa: E501
        :type: str
        """
        if quote_type__qt is not None and len(quote_type__qt) > 32:
            raise ValueError("Invalid value for `quote_type__qt`, length must be less than or equal to `32`")  # noqa: E501

        self._quote_type__qt = quote_type__qt

    @property
    def integration_id__ns(self):
        """Gets the integration_id__ns of this ProxyGetSubscription.  # noqa: E501

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_id__ns of this ProxyGetSubscription.  # noqa: E501
        :rtype: str
        """
        return self._integration_id__ns

    @integration_id__ns.setter
    def integration_id__ns(self, integration_id__ns):
        """Sets the integration_id__ns of this ProxyGetSubscription.

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_id__ns: The integration_id__ns of this ProxyGetSubscription.  # noqa: E501
        :type: str
        """
        if integration_id__ns is not None and len(integration_id__ns) > 255:
            raise ValueError("Invalid value for `integration_id__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_id__ns = integration_id__ns

    @property
    def integration_status__ns(self):
        """Gets the integration_status__ns of this ProxyGetSubscription.  # noqa: E501

        Status of the subscription's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_status__ns of this ProxyGetSubscription.  # noqa: E501
        :rtype: str
        """
        return self._integration_status__ns

    @integration_status__ns.setter
    def integration_status__ns(self, integration_status__ns):
        """Sets the integration_status__ns of this ProxyGetSubscription.

        Status of the subscription's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_status__ns: The integration_status__ns of this ProxyGetSubscription.  # noqa: E501
        :type: str
        """
        if integration_status__ns is not None and len(integration_status__ns) > 255:
            raise ValueError("Invalid value for `integration_status__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_status__ns = integration_status__ns

    @property
    def project__ns(self):
        """Gets the project__ns of this ProxyGetSubscription.  # noqa: E501

        The NetSuite project that the subscription was created from. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The project__ns of this ProxyGetSubscription.  # noqa: E501
        :rtype: str
        """
        return self._project__ns

    @project__ns.setter
    def project__ns(self, project__ns):
        """Sets the project__ns of this ProxyGetSubscription.

        The NetSuite project that the subscription was created from. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param project__ns: The project__ns of this ProxyGetSubscription.  # noqa: E501
        :type: str
        """
        if project__ns is not None and len(project__ns) > 255:
            raise ValueError("Invalid value for `project__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._project__ns = project__ns

    @property
    def sales_order__ns(self):
        """Gets the sales_order__ns of this ProxyGetSubscription.  # noqa: E501

        The NetSuite sales order than the subscription was created from. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The sales_order__ns of this ProxyGetSubscription.  # noqa: E501
        :rtype: str
        """
        return self._sales_order__ns

    @sales_order__ns.setter
    def sales_order__ns(self, sales_order__ns):
        """Sets the sales_order__ns of this ProxyGetSubscription.

        The NetSuite sales order than the subscription was created from. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param sales_order__ns: The sales_order__ns of this ProxyGetSubscription.  # noqa: E501
        :type: str
        """
        if sales_order__ns is not None and len(sales_order__ns) > 255:
            raise ValueError("Invalid value for `sales_order__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._sales_order__ns = sales_order__ns

    @property
    def sync_date__ns(self):
        """Gets the sync_date__ns of this ProxyGetSubscription.  # noqa: E501

        Date when the subscription was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The sync_date__ns of this ProxyGetSubscription.  # noqa: E501
        :rtype: str
        """
        return self._sync_date__ns

    @sync_date__ns.setter
    def sync_date__ns(self, sync_date__ns):
        """Sets the sync_date__ns of this ProxyGetSubscription.

        Date when the subscription was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param sync_date__ns: The sync_date__ns of this ProxyGetSubscription.  # noqa: E501
        :type: str
        """
        if sync_date__ns is not None and len(sync_date__ns) > 255:
            raise ValueError("Invalid value for `sync_date__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._sync_date__ns = sync_date__ns

    @property
    def account_id(self):
        """Gets the account_id of this ProxyGetSubscription.  # noqa: E501

         This field can be updated when **Status** is `Draft`. The ID of a valid account ID.   # noqa: E501

        :return: The account_id of this ProxyGetSubscription.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ProxyGetSubscription.

         This field can be updated when **Status** is `Draft`. The ID of a valid account ID.   # noqa: E501

        :param account_id: The account_id of this ProxyGetSubscription.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def auto_renew(self):
        """Gets the auto_renew of this ProxyGetSubscription.  # noqa: E501

         This field can be updated when **Status** is `Draft`. Indicates if the subscription automatically renews at the end of the term. **Values**: `true`, `false`   # noqa: E501

        :return: The auto_renew of this ProxyGetSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, auto_renew):
        """Sets the auto_renew of this ProxyGetSubscription.

         This field can be updated when **Status** is `Draft`. Indicates if the subscription automatically renews at the end of the term. **Values**: `true`, `false`   # noqa: E501

        :param auto_renew: The auto_renew of this ProxyGetSubscription.  # noqa: E501
        :type: bool
        """

        self._auto_renew = auto_renew

    @property
    def cancelled_date(self):
        """Gets the cancelled_date of this ProxyGetSubscription.  # noqa: E501

         The date on which the subscription was canceled.   # noqa: E501

        :return: The cancelled_date of this ProxyGetSubscription.  # noqa: E501
        :rtype: date
        """
        return self._cancelled_date

    @cancelled_date.setter
    def cancelled_date(self, cancelled_date):
        """Sets the cancelled_date of this ProxyGetSubscription.

         The date on which the subscription was canceled.   # noqa: E501

        :param cancelled_date: The cancelled_date of this ProxyGetSubscription.  # noqa: E501
        :type: date
        """

        self._cancelled_date = cancelled_date

    @property
    def contract_acceptance_date(self):
        """Gets the contract_acceptance_date of this ProxyGetSubscription.  # noqa: E501

         The date when the customer accepts the contract. This field can be updated when **Status** is `Draft`.   # noqa: E501

        :return: The contract_acceptance_date of this ProxyGetSubscription.  # noqa: E501
        :rtype: date
        """
        return self._contract_acceptance_date

    @contract_acceptance_date.setter
    def contract_acceptance_date(self, contract_acceptance_date):
        """Sets the contract_acceptance_date of this ProxyGetSubscription.

         The date when the customer accepts the contract. This field can be updated when **Status** is `Draft`.   # noqa: E501

        :param contract_acceptance_date: The contract_acceptance_date of this ProxyGetSubscription.  # noqa: E501
        :type: date
        """

        self._contract_acceptance_date = contract_acceptance_date

    @property
    def contract_effective_date(self):
        """Gets the contract_effective_date of this ProxyGetSubscription.  # noqa: E501

         The date when the contract takes effect. This field can be updated when **Status** is `Draft`. **Note**: This field is required in the subscribe call. If you set the value of this field to null and both the ServiceActivationDate and ContractAcceptanceDate fields are not required, the subscribe call still returns success, but the new subscription is in `DRAFT` status. To activate the subscription, you must set a valid date to this field.   # noqa: E501

        :return: The contract_effective_date of this ProxyGetSubscription.  # noqa: E501
        :rtype: date
        """
        return self._contract_effective_date

    @contract_effective_date.setter
    def contract_effective_date(self, contract_effective_date):
        """Sets the contract_effective_date of this ProxyGetSubscription.

         The date when the contract takes effect. This field can be updated when **Status** is `Draft`. **Note**: This field is required in the subscribe call. If you set the value of this field to null and both the ServiceActivationDate and ContractAcceptanceDate fields are not required, the subscribe call still returns success, but the new subscription is in `DRAFT` status. To activate the subscription, you must set a valid date to this field.   # noqa: E501

        :param contract_effective_date: The contract_effective_date of this ProxyGetSubscription.  # noqa: E501
        :type: date
        """

        self._contract_effective_date = contract_effective_date

    @property
    def created_by_id(self):
        """Gets the created_by_id of this ProxyGetSubscription.  # noqa: E501

        The user ID of the person who created the subscription. **Character limit**: 32 **Values**: automatically generated   # noqa: E501

        :return: The created_by_id of this ProxyGetSubscription.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this ProxyGetSubscription.

        The user ID of the person who created the subscription. **Character limit**: 32 **Values**: automatically generated   # noqa: E501

        :param created_by_id: The created_by_id of this ProxyGetSubscription.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def created_date(self):
        """Gets the created_date of this ProxyGetSubscription.  # noqa: E501

         The date the subscription was created. This value is the same as the OriginalCreatedDate value until the subscription is amended. **Values**: automatically generated   # noqa: E501

        :return: The created_date of this ProxyGetSubscription.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this ProxyGetSubscription.

         The date the subscription was created. This value is the same as the OriginalCreatedDate value until the subscription is amended. **Values**: automatically generated   # noqa: E501

        :param created_date: The created_date of this ProxyGetSubscription.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def creator_account_id(self):
        """Gets the creator_account_id of this ProxyGetSubscription.  # noqa: E501

         The account ID that created the subscription or the amended subscription. **Character limit**: 32 **Values**: automatically generated   # noqa: E501

        :return: The creator_account_id of this ProxyGetSubscription.  # noqa: E501
        :rtype: str
        """
        return self._creator_account_id

    @creator_account_id.setter
    def creator_account_id(self, creator_account_id):
        """Sets the creator_account_id of this ProxyGetSubscription.

         The account ID that created the subscription or the amended subscription. **Character limit**: 32 **Values**: automatically generated   # noqa: E501

        :param creator_account_id: The creator_account_id of this ProxyGetSubscription.  # noqa: E501
        :type: str
        """

        self._creator_account_id = creator_account_id

    @property
    def creator_invoice_owner_id(self):
        """Gets the creator_invoice_owner_id of this ProxyGetSubscription.  # noqa: E501

         The account ID that owns the invoices associated with the subscription or the amended subscription. **Character limit**: 32 **Values**: automatically generated   # noqa: E501

        :return: The creator_invoice_owner_id of this ProxyGetSubscription.  # noqa: E501
        :rtype: str
        """
        return self._creator_invoice_owner_id

    @creator_invoice_owner_id.setter
    def creator_invoice_owner_id(self, creator_invoice_owner_id):
        """Sets the creator_invoice_owner_id of this ProxyGetSubscription.

         The account ID that owns the invoices associated with the subscription or the amended subscription. **Character limit**: 32 **Values**: automatically generated   # noqa: E501

        :param creator_invoice_owner_id: The creator_invoice_owner_id of this ProxyGetSubscription.  # noqa: E501
        :type: str
        """

        self._creator_invoice_owner_id = creator_invoice_owner_id

    @property
    def current_term(self):
        """Gets the current_term of this ProxyGetSubscription.  # noqa: E501

         The length of the period for the current subscription term. If TermType is set to `TERMED`, this field is required and must be greater than `0`. If TermType is set to `EVERGREEN`, this value is ignored. Default is `0`. **Character limit**: 20 **Values**: automatically generated   # noqa: E501

        :return: The current_term of this ProxyGetSubscription.  # noqa: E501
        :rtype: int
        """
        return self._current_term

    @current_term.setter
    def current_term(self, current_term):
        """Sets the current_term of this ProxyGetSubscription.

         The length of the period for the current subscription term. If TermType is set to `TERMED`, this field is required and must be greater than `0`. If TermType is set to `EVERGREEN`, this value is ignored. Default is `0`. **Character limit**: 20 **Values**: automatically generated   # noqa: E501

        :param current_term: The current_term of this ProxyGetSubscription.  # noqa: E501
        :type: int
        """

        self._current_term = current_term

    @property
    def current_term_period_type(self):
        """Gets the current_term_period_type of this ProxyGetSubscription.  # noqa: E501

         The period type for the current subscription term. This field is used with the CurrentTerm field to specify the current subscription term. **Values**:  - `Month` (default) - `Year` - `Day` - `Week`   # noqa: E501

        :return: The current_term_period_type of this ProxyGetSubscription.  # noqa: E501
        :rtype: str
        """
        return self._current_term_period_type

    @current_term_period_type.setter
    def current_term_period_type(self, current_term_period_type):
        """Sets the current_term_period_type of this ProxyGetSubscription.

         The period type for the current subscription term. This field is used with the CurrentTerm field to specify the current subscription term. **Values**:  - `Month` (default) - `Year` - `Day` - `Week`   # noqa: E501

        :param current_term_period_type: The current_term_period_type of this ProxyGetSubscription.  # noqa: E501
        :type: str
        """

        self._current_term_period_type = current_term_period_type

    @property
    def id(self):
        """Gets the id of this ProxyGetSubscription.  # noqa: E501

        Object identifier.  # noqa: E501

        :return: The id of this ProxyGetSubscription.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProxyGetSubscription.

        Object identifier.  # noqa: E501

        :param id: The id of this ProxyGetSubscription.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def initial_term(self):
        """Gets the initial_term of this ProxyGetSubscription.  # noqa: E501

         The length of the period for the first subscription term. This field can be updated when Status is `Draft`. **Required**: If TermType is Termed **Character limit**: 20 **Values**: any valid number. The default value is 0.   # noqa: E501

        :return: The initial_term of this ProxyGetSubscription.  # noqa: E501
        :rtype: int
        """
        return self._initial_term

    @initial_term.setter
    def initial_term(self, initial_term):
        """Sets the initial_term of this ProxyGetSubscription.

         The length of the period for the first subscription term. This field can be updated when Status is `Draft`. **Required**: If TermType is Termed **Character limit**: 20 **Values**: any valid number. The default value is 0.   # noqa: E501

        :param initial_term: The initial_term of this ProxyGetSubscription.  # noqa: E501
        :type: int
        """

        self._initial_term = initial_term

    @property
    def initial_term_period_type(self):
        """Gets the initial_term_period_type of this ProxyGetSubscription.  # noqa: E501

         The period type for the first subscription term. **Values**:  - `Month` (default) - `Year` - `Day` - `Week` **Note**:  - This field can be updated when Status is `Draft`. - This field is used with the InitialTerm field to specify the initial subscription term.   # noqa: E501

        :return: The initial_term_period_type of this ProxyGetSubscription.  # noqa: E501
        :rtype: str
        """
        return self._initial_term_period_type

    @initial_term_period_type.setter
    def initial_term_period_type(self, initial_term_period_type):
        """Sets the initial_term_period_type of this ProxyGetSubscription.

         The period type for the first subscription term. **Values**:  - `Month` (default) - `Year` - `Day` - `Week` **Note**:  - This field can be updated when Status is `Draft`. - This field is used with the InitialTerm field to specify the initial subscription term.   # noqa: E501

        :param initial_term_period_type: The initial_term_period_type of this ProxyGetSubscription.  # noqa: E501
        :type: str
        """

        self._initial_term_period_type = initial_term_period_type

    @property
    def invoice_owner_id(self):
        """Gets the invoice_owner_id of this ProxyGetSubscription.  # noqa: E501

         This field can be updated when **Status** is `Draft`. A valid account ID.   # noqa: E501

        :return: The invoice_owner_id of this ProxyGetSubscription.  # noqa: E501
        :rtype: str
        """
        return self._invoice_owner_id

    @invoice_owner_id.setter
    def invoice_owner_id(self, invoice_owner_id):
        """Sets the invoice_owner_id of this ProxyGetSubscription.

         This field can be updated when **Status** is `Draft`. A valid account ID.   # noqa: E501

        :param invoice_owner_id: The invoice_owner_id of this ProxyGetSubscription.  # noqa: E501
        :type: str
        """

        self._invoice_owner_id = invoice_owner_id

    @property
    def is_invoice_separate(self):
        """Gets the is_invoice_separate of this ProxyGetSubscription.  # noqa: E501

         Determines if the subscription is invoiced separately. If `TRUE`, then all charges for this subscription are collected into the subscription's own invoice. **V****alues**: `TRUE`, `FALSE `(default)   # noqa: E501

        :return: The is_invoice_separate of this ProxyGetSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._is_invoice_separate

    @is_invoice_separate.setter
    def is_invoice_separate(self, is_invoice_separate):
        """Sets the is_invoice_separate of this ProxyGetSubscription.

         Determines if the subscription is invoiced separately. If `TRUE`, then all charges for this subscription are collected into the subscription's own invoice. **V****alues**: `TRUE`, `FALSE `(default)   # noqa: E501

        :param is_invoice_separate: The is_invoice_separate of this ProxyGetSubscription.  # noqa: E501
        :type: bool
        """

        self._is_invoice_separate = is_invoice_separate

    @property
    def name(self):
        """Gets the name of this ProxyGetSubscription.  # noqa: E501

         The unique identifier of the subscription. If you don't specify a value, then Zuora generates a name automatically. Whether auto-generated or manually specified, the subscription name must be unique. Otherwise an error will occur. **Character limit**: 100 **Values**: one of the following:  - leave null to automatically generate - a string of 100 characters or fewer   # noqa: E501

        :return: The name of this ProxyGetSubscription.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProxyGetSubscription.

         The unique identifier of the subscription. If you don't specify a value, then Zuora generates a name automatically. Whether auto-generated or manually specified, the subscription name must be unique. Otherwise an error will occur. **Character limit**: 100 **Values**: one of the following:  - leave null to automatically generate - a string of 100 characters or fewer   # noqa: E501

        :param name: The name of this ProxyGetSubscription.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this ProxyGetSubscription.  # noqa: E501

         Use this field to record comments about the subscription. **Character limit**: 500 **Values**: a string of 500 characters or fewer   # noqa: E501

        :return: The notes of this ProxyGetSubscription.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this ProxyGetSubscription.

         Use this field to record comments about the subscription. **Character limit**: 500 **Values**: a string of 500 characters or fewer   # noqa: E501

        :param notes: The notes of this ProxyGetSubscription.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def original_created_date(self):
        """Gets the original_created_date of this ProxyGetSubscription.  # noqa: E501

         The date when the subscription was originally created. This value is the same as the CreatedDate value until the subscription is amended. **Values**: automatically generated   # noqa: E501

        :return: The original_created_date of this ProxyGetSubscription.  # noqa: E501
        :rtype: datetime
        """
        return self._original_created_date

    @original_created_date.setter
    def original_created_date(self, original_created_date):
        """Sets the original_created_date of this ProxyGetSubscription.

         The date when the subscription was originally created. This value is the same as the CreatedDate value until the subscription is amended. **Values**: automatically generated   # noqa: E501

        :param original_created_date: The original_created_date of this ProxyGetSubscription.  # noqa: E501
        :type: datetime
        """

        self._original_created_date = original_created_date

    @property
    def original_id(self):
        """Gets the original_id of this ProxyGetSubscription.  # noqa: E501

         The original ID of this subscription. **Values**: automatically generated   # noqa: E501

        :return: The original_id of this ProxyGetSubscription.  # noqa: E501
        :rtype: str
        """
        return self._original_id

    @original_id.setter
    def original_id(self, original_id):
        """Sets the original_id of this ProxyGetSubscription.

         The original ID of this subscription. **Values**: automatically generated   # noqa: E501

        :param original_id: The original_id of this ProxyGetSubscription.  # noqa: E501
        :type: str
        """

        self._original_id = original_id

    @property
    def previous_subscription_id(self):
        """Gets the previous_subscription_id of this ProxyGetSubscription.  # noqa: E501

         The subscription ID immediately prior to the current subscription. **Character limit**: 32 **Values**: automatically generated   # noqa: E501

        :return: The previous_subscription_id of this ProxyGetSubscription.  # noqa: E501
        :rtype: str
        """
        return self._previous_subscription_id

    @previous_subscription_id.setter
    def previous_subscription_id(self, previous_subscription_id):
        """Sets the previous_subscription_id of this ProxyGetSubscription.

         The subscription ID immediately prior to the current subscription. **Character limit**: 32 **Values**: automatically generated   # noqa: E501

        :param previous_subscription_id: The previous_subscription_id of this ProxyGetSubscription.  # noqa: E501
        :type: str
        """

        self._previous_subscription_id = previous_subscription_id

    @property
    def renewal_setting(self):
        """Gets the renewal_setting of this ProxyGetSubscription.  # noqa: E501

         This field can be updated when **Status** is `Draft`. Specifies whether a termed subscription will remain termed or change to evergreen when it is renewed. **Required**: If TermType is Termed **Values**: `RENEW_WITH_SPECIFIC_TERM `(default), `RENEW_TO_EVERGREEN`   # noqa: E501

        :return: The renewal_setting of this ProxyGetSubscription.  # noqa: E501
        :rtype: str
        """
        return self._renewal_setting

    @renewal_setting.setter
    def renewal_setting(self, renewal_setting):
        """Sets the renewal_setting of this ProxyGetSubscription.

         This field can be updated when **Status** is `Draft`. Specifies whether a termed subscription will remain termed or change to evergreen when it is renewed. **Required**: If TermType is Termed **Values**: `RENEW_WITH_SPECIFIC_TERM `(default), `RENEW_TO_EVERGREEN`   # noqa: E501

        :param renewal_setting: The renewal_setting of this ProxyGetSubscription.  # noqa: E501
        :type: str
        """

        self._renewal_setting = renewal_setting

    @property
    def renewal_term(self):
        """Gets the renewal_term of this ProxyGetSubscription.  # noqa: E501

         The length of the period for the subscription renewal term. This field can be updated when **Status** is `Draft`. **Required**: If TermType is Termed. **Character limit**: 20 **Values**: one of the following:  - leave null to default to `0` - any number   # noqa: E501

        :return: The renewal_term of this ProxyGetSubscription.  # noqa: E501
        :rtype: int
        """
        return self._renewal_term

    @renewal_term.setter
    def renewal_term(self, renewal_term):
        """Sets the renewal_term of this ProxyGetSubscription.

         The length of the period for the subscription renewal term. This field can be updated when **Status** is `Draft`. **Required**: If TermType is Termed. **Character limit**: 20 **Values**: one of the following:  - leave null to default to `0` - any number   # noqa: E501

        :param renewal_term: The renewal_term of this ProxyGetSubscription.  # noqa: E501
        :type: int
        """

        self._renewal_term = renewal_term

    @property
    def renewal_term_period_type(self):
        """Gets the renewal_term_period_type of this ProxyGetSubscription.  # noqa: E501

         The period type for the subscription renewal term. **Values**:  - `Month` (default) - `Year` - `Day` - `Week` **Note**:  - This field is used with the RenewalTerm field to specify the subscription renewal term. - This field can be updated when Status is `Draft`.   # noqa: E501

        :return: The renewal_term_period_type of this ProxyGetSubscription.  # noqa: E501
        :rtype: str
        """
        return self._renewal_term_period_type

    @renewal_term_period_type.setter
    def renewal_term_period_type(self, renewal_term_period_type):
        """Sets the renewal_term_period_type of this ProxyGetSubscription.

         The period type for the subscription renewal term. **Values**:  - `Month` (default) - `Year` - `Day` - `Week` **Note**:  - This field is used with the RenewalTerm field to specify the subscription renewal term. - This field can be updated when Status is `Draft`.   # noqa: E501

        :param renewal_term_period_type: The renewal_term_period_type of this ProxyGetSubscription.  # noqa: E501
        :type: str
        """

        self._renewal_term_period_type = renewal_term_period_type

    @property
    def service_activation_date(self):
        """Gets the service_activation_date of this ProxyGetSubscription.  # noqa: E501

         The date when the subscription is activated. This field can be updated when **Status** is `Draft`.   # noqa: E501

        :return: The service_activation_date of this ProxyGetSubscription.  # noqa: E501
        :rtype: date
        """
        return self._service_activation_date

    @service_activation_date.setter
    def service_activation_date(self, service_activation_date):
        """Sets the service_activation_date of this ProxyGetSubscription.

         The date when the subscription is activated. This field can be updated when **Status** is `Draft`.   # noqa: E501

        :param service_activation_date: The service_activation_date of this ProxyGetSubscription.  # noqa: E501
        :type: date
        """

        self._service_activation_date = service_activation_date

    @property
    def status(self):
        """Gets the status of this ProxyGetSubscription.  # noqa: E501

         The status of the subscription. **Character limit**: 17 **Values**: automatically generated **Possible values**: one of the following:  - `Draft` - `PendingActivation` - `PendingAcceptance` - `Active` - `Cancelled` - `Expired` - `Suspended` (This value is in **Limited Availability**.)   # noqa: E501

        :return: The status of this ProxyGetSubscription.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProxyGetSubscription.

         The status of the subscription. **Character limit**: 17 **Values**: automatically generated **Possible values**: one of the following:  - `Draft` - `PendingActivation` - `PendingAcceptance` - `Active` - `Cancelled` - `Expired` - `Suspended` (This value is in **Limited Availability**.)   # noqa: E501

        :param status: The status of this ProxyGetSubscription.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def subscription_end_date(self):
        """Gets the subscription_end_date of this ProxyGetSubscription.  # noqa: E501

         The date when the subscription term ends, where the subscription ends at midnight the day before. For example, if the SubscriptionEndDate is 12/31/2016, the subscriptions ends at midnight (00:00:00 hours) on 12/30/2016. This date is the same as the term end date or the cancelation date, as appropriate. **Character limit**: 29 **Values**: automatically generated   # noqa: E501

        :return: The subscription_end_date of this ProxyGetSubscription.  # noqa: E501
        :rtype: date
        """
        return self._subscription_end_date

    @subscription_end_date.setter
    def subscription_end_date(self, subscription_end_date):
        """Sets the subscription_end_date of this ProxyGetSubscription.

         The date when the subscription term ends, where the subscription ends at midnight the day before. For example, if the SubscriptionEndDate is 12/31/2016, the subscriptions ends at midnight (00:00:00 hours) on 12/30/2016. This date is the same as the term end date or the cancelation date, as appropriate. **Character limit**: 29 **Values**: automatically generated   # noqa: E501

        :param subscription_end_date: The subscription_end_date of this ProxyGetSubscription.  # noqa: E501
        :type: date
        """

        self._subscription_end_date = subscription_end_date

    @property
    def subscription_start_date(self):
        """Gets the subscription_start_date of this ProxyGetSubscription.  # noqa: E501

         The date when the subscription term starts. This date is the same as the start date of the original term, which isn't necessarily the start date of the current or new term. **Character limit**: 29 **Values**: automatically generated   # noqa: E501

        :return: The subscription_start_date of this ProxyGetSubscription.  # noqa: E501
        :rtype: date
        """
        return self._subscription_start_date

    @subscription_start_date.setter
    def subscription_start_date(self, subscription_start_date):
        """Sets the subscription_start_date of this ProxyGetSubscription.

         The date when the subscription term starts. This date is the same as the start date of the original term, which isn't necessarily the start date of the current or new term. **Character limit**: 29 **Values**: automatically generated   # noqa: E501

        :param subscription_start_date: The subscription_start_date of this ProxyGetSubscription.  # noqa: E501
        :type: date
        """

        self._subscription_start_date = subscription_start_date

    @property
    def term_end_date(self):
        """Gets the term_end_date of this ProxyGetSubscription.  # noqa: E501

         This field can be updated when **Status** is `Draft`. The date when the subscription term ends. If the subscription is evergreen, the TermEndDate value is null or is the cancelation date, as appropriate. **Character limit**: 29 **Values**: automatically generated   # noqa: E501

        :return: The term_end_date of this ProxyGetSubscription.  # noqa: E501
        :rtype: date
        """
        return self._term_end_date

    @term_end_date.setter
    def term_end_date(self, term_end_date):
        """Sets the term_end_date of this ProxyGetSubscription.

         This field can be updated when **Status** is `Draft`. The date when the subscription term ends. If the subscription is evergreen, the TermEndDate value is null or is the cancelation date, as appropriate. **Character limit**: 29 **Values**: automatically generated   # noqa: E501

        :param term_end_date: The term_end_date of this ProxyGetSubscription.  # noqa: E501
        :type: date
        """

        self._term_end_date = term_end_date

    @property
    def term_start_date(self):
        """Gets the term_start_date of this ProxyGetSubscription.  # noqa: E501

         This field can be updated when **Status** is `Draft`. The date when the subscription term begins. If this is a renewal subscription, then this date is different from the subscription start date. **Character limit**: 29 **Version notes**: --   # noqa: E501

        :return: The term_start_date of this ProxyGetSubscription.  # noqa: E501
        :rtype: date
        """
        return self._term_start_date

    @term_start_date.setter
    def term_start_date(self, term_start_date):
        """Sets the term_start_date of this ProxyGetSubscription.

         This field can be updated when **Status** is `Draft`. The date when the subscription term begins. If this is a renewal subscription, then this date is different from the subscription start date. **Character limit**: 29 **Version notes**: --   # noqa: E501

        :param term_start_date: The term_start_date of this ProxyGetSubscription.  # noqa: E501
        :type: date
        """

        self._term_start_date = term_start_date

    @property
    def term_type(self):
        """Gets the term_type of this ProxyGetSubscription.  # noqa: E501

         This field can be updated when **Status** is `Draft`. Indicates if a subscription is termed or evergreen. **Character limit**: 9 **Values**: `TERMED`, `EVERGREEN`   # noqa: E501

        :return: The term_type of this ProxyGetSubscription.  # noqa: E501
        :rtype: str
        """
        return self._term_type

    @term_type.setter
    def term_type(self, term_type):
        """Sets the term_type of this ProxyGetSubscription.

         This field can be updated when **Status** is `Draft`. Indicates if a subscription is termed or evergreen. **Character limit**: 9 **Values**: `TERMED`, `EVERGREEN`   # noqa: E501

        :param term_type: The term_type of this ProxyGetSubscription.  # noqa: E501
        :type: str
        """

        self._term_type = term_type

    @property
    def updated_by_id(self):
        """Gets the updated_by_id of this ProxyGetSubscription.  # noqa: E501

         The ID of the user who last updated the subscription. **Character limit:** 32 **Values: **automatically generated   # noqa: E501

        :return: The updated_by_id of this ProxyGetSubscription.  # noqa: E501
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """Sets the updated_by_id of this ProxyGetSubscription.

         The ID of the user who last updated the subscription. **Character limit:** 32 **Values: **automatically generated   # noqa: E501

        :param updated_by_id: The updated_by_id of this ProxyGetSubscription.  # noqa: E501
        :type: str
        """

        self._updated_by_id = updated_by_id

    @property
    def updated_date(self):
        """Gets the updated_date of this ProxyGetSubscription.  # noqa: E501

         The date when the subscription was last updated. **Character limit:** 29 **Values**: automatically generated   # noqa: E501

        :return: The updated_date of this ProxyGetSubscription.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this ProxyGetSubscription.

         The date when the subscription was last updated. **Character limit:** 29 **Values**: automatically generated   # noqa: E501

        :param updated_date: The updated_date of this ProxyGetSubscription.  # noqa: E501
        :type: datetime
        """

        self._updated_date = updated_date

    @property
    def version(self):
        """Gets the version of this ProxyGetSubscription.  # noqa: E501

         The version number of the subscription. **Values**: automatically generated   # noqa: E501

        :return: The version of this ProxyGetSubscription.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ProxyGetSubscription.

         The version number of the subscription. **Values**: automatically generated   # noqa: E501

        :param version: The version of this ProxyGetSubscription.  # noqa: E501
        :type: int
        """

        self._version = version

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
        if not isinstance(other, ProxyGetSubscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
