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


class ProxyModifyPaymentMethod(object):
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
        'ach_aba_code': 'str',
        'ach_account_name': 'str',
        'ach_account_type': 'str',
        'ach_address1': 'str',
        'ach_address2': 'str',
        'ach_bank_name': 'str',
        'bank_branch_code': 'str',
        'bank_check_digit': 'str',
        'bank_city': 'str',
        'bank_code': 'str',
        'bank_name': 'str',
        'bank_postal_code': 'str',
        'bank_street_name': 'str',
        'bank_street_number': 'str',
        'bank_transfer_account_name': 'str',
        'business_identification_code': 'str',
        'city': 'str',
        'country': 'str',
        'credit_card_address1': 'str',
        'credit_card_address2': 'str',
        'credit_card_city': 'str',
        'credit_card_country': 'str',
        'credit_card_expiration_month': 'int',
        'credit_card_expiration_year': 'int',
        'credit_card_holder_name': 'str',
        'credit_card_postal_code': 'str',
        'credit_card_state': 'str',
        'credit_card_type': 'str',
        'device_session_id': 'str',
        'email': 'str',
        'existing_mandate': 'str',
        'first_name': 'str',
        'iban': 'str',
        'ip_address': 'str',
        'last_name': 'str',
        'last_transaction_date_time': 'datetime',
        'last_transaction_status': 'str',
        'mandate_creation_date': 'date',
        'mandate_id': 'str',
        'mandate_received': 'str',
        'mandate_update_date': 'date',
        'max_consecutive_payment_failures': 'int',
        'num_consecutive_failures': 'int',
        'payment_method_status': 'str',
        'payment_retry_window': 'int',
        'phone': 'str',
        'postal_code': 'str',
        'state': 'str',
        'street_name': 'str',
        'street_number': 'str',
        'use_default_retry_rule': 'bool'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'ach_aba_code': 'AchAbaCode',
        'ach_account_name': 'AchAccountName',
        'ach_account_type': 'AchAccountType',
        'ach_address1': 'AchAddress1',
        'ach_address2': 'AchAddress2',
        'ach_bank_name': 'AchBankName',
        'bank_branch_code': 'BankBranchCode',
        'bank_check_digit': 'BankCheckDigit',
        'bank_city': 'BankCity',
        'bank_code': 'BankCode',
        'bank_name': 'BankName',
        'bank_postal_code': 'BankPostalCode',
        'bank_street_name': 'BankStreetName',
        'bank_street_number': 'BankStreetNumber',
        'bank_transfer_account_name': 'BankTransferAccountName',
        'business_identification_code': 'BusinessIdentificationCode',
        'city': 'City',
        'country': 'Country',
        'credit_card_address1': 'CreditCardAddress1',
        'credit_card_address2': 'CreditCardAddress2',
        'credit_card_city': 'CreditCardCity',
        'credit_card_country': 'CreditCardCountry',
        'credit_card_expiration_month': 'CreditCardExpirationMonth',
        'credit_card_expiration_year': 'CreditCardExpirationYear',
        'credit_card_holder_name': 'CreditCardHolderName',
        'credit_card_postal_code': 'CreditCardPostalCode',
        'credit_card_state': 'CreditCardState',
        'credit_card_type': 'CreditCardType',
        'device_session_id': 'DeviceSessionId',
        'email': 'Email',
        'existing_mandate': 'ExistingMandate',
        'first_name': 'FirstName',
        'iban': 'IBAN',
        'ip_address': 'IPAddress',
        'last_name': 'LastName',
        'last_transaction_date_time': 'LastTransactionDateTime',
        'last_transaction_status': 'LastTransactionStatus',
        'mandate_creation_date': 'MandateCreationDate',
        'mandate_id': 'MandateID',
        'mandate_received': 'MandateReceived',
        'mandate_update_date': 'MandateUpdateDate',
        'max_consecutive_payment_failures': 'MaxConsecutivePaymentFailures',
        'num_consecutive_failures': 'NumConsecutiveFailures',
        'payment_method_status': 'PaymentMethodStatus',
        'payment_retry_window': 'PaymentRetryWindow',
        'phone': 'Phone',
        'postal_code': 'PostalCode',
        'state': 'State',
        'street_name': 'StreetName',
        'street_number': 'StreetNumber',
        'use_default_retry_rule': 'UseDefaultRetryRule'
    }

    def __init__(self, account_id=None, ach_aba_code=None, ach_account_name=None, ach_account_type=None, ach_address1=None, ach_address2=None, ach_bank_name=None, bank_branch_code=None, bank_check_digit=None, bank_city=None, bank_code=None, bank_name=None, bank_postal_code=None, bank_street_name=None, bank_street_number=None, bank_transfer_account_name=None, business_identification_code=None, city=None, country=None, credit_card_address1=None, credit_card_address2=None, credit_card_city=None, credit_card_country=None, credit_card_expiration_month=None, credit_card_expiration_year=None, credit_card_holder_name=None, credit_card_postal_code=None, credit_card_state=None, credit_card_type=None, device_session_id=None, email=None, existing_mandate=None, first_name=None, iban=None, ip_address=None, last_name=None, last_transaction_date_time=None, last_transaction_status=None, mandate_creation_date=None, mandate_id=None, mandate_received=None, mandate_update_date=None, max_consecutive_payment_failures=None, num_consecutive_failures=None, payment_method_status=None, payment_retry_window=None, phone=None, postal_code=None, state=None, street_name=None, street_number=None, use_default_retry_rule=None):  # noqa: E501
        """ProxyModifyPaymentMethod - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._ach_aba_code = None
        self._ach_account_name = None
        self._ach_account_type = None
        self._ach_address1 = None
        self._ach_address2 = None
        self._ach_bank_name = None
        self._bank_branch_code = None
        self._bank_check_digit = None
        self._bank_city = None
        self._bank_code = None
        self._bank_name = None
        self._bank_postal_code = None
        self._bank_street_name = None
        self._bank_street_number = None
        self._bank_transfer_account_name = None
        self._business_identification_code = None
        self._city = None
        self._country = None
        self._credit_card_address1 = None
        self._credit_card_address2 = None
        self._credit_card_city = None
        self._credit_card_country = None
        self._credit_card_expiration_month = None
        self._credit_card_expiration_year = None
        self._credit_card_holder_name = None
        self._credit_card_postal_code = None
        self._credit_card_state = None
        self._credit_card_type = None
        self._device_session_id = None
        self._email = None
        self._existing_mandate = None
        self._first_name = None
        self._iban = None
        self._ip_address = None
        self._last_name = None
        self._last_transaction_date_time = None
        self._last_transaction_status = None
        self._mandate_creation_date = None
        self._mandate_id = None
        self._mandate_received = None
        self._mandate_update_date = None
        self._max_consecutive_payment_failures = None
        self._num_consecutive_failures = None
        self._payment_method_status = None
        self._payment_retry_window = None
        self._phone = None
        self._postal_code = None
        self._state = None
        self._street_name = None
        self._street_number = None
        self._use_default_retry_rule = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if ach_aba_code is not None:
            self.ach_aba_code = ach_aba_code
        if ach_account_name is not None:
            self.ach_account_name = ach_account_name
        if ach_account_type is not None:
            self.ach_account_type = ach_account_type
        if ach_address1 is not None:
            self.ach_address1 = ach_address1
        if ach_address2 is not None:
            self.ach_address2 = ach_address2
        if ach_bank_name is not None:
            self.ach_bank_name = ach_bank_name
        if bank_branch_code is not None:
            self.bank_branch_code = bank_branch_code
        if bank_check_digit is not None:
            self.bank_check_digit = bank_check_digit
        if bank_city is not None:
            self.bank_city = bank_city
        if bank_code is not None:
            self.bank_code = bank_code
        if bank_name is not None:
            self.bank_name = bank_name
        if bank_postal_code is not None:
            self.bank_postal_code = bank_postal_code
        if bank_street_name is not None:
            self.bank_street_name = bank_street_name
        if bank_street_number is not None:
            self.bank_street_number = bank_street_number
        if bank_transfer_account_name is not None:
            self.bank_transfer_account_name = bank_transfer_account_name
        if business_identification_code is not None:
            self.business_identification_code = business_identification_code
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if credit_card_address1 is not None:
            self.credit_card_address1 = credit_card_address1
        if credit_card_address2 is not None:
            self.credit_card_address2 = credit_card_address2
        if credit_card_city is not None:
            self.credit_card_city = credit_card_city
        if credit_card_country is not None:
            self.credit_card_country = credit_card_country
        if credit_card_expiration_month is not None:
            self.credit_card_expiration_month = credit_card_expiration_month
        if credit_card_expiration_year is not None:
            self.credit_card_expiration_year = credit_card_expiration_year
        if credit_card_holder_name is not None:
            self.credit_card_holder_name = credit_card_holder_name
        if credit_card_postal_code is not None:
            self.credit_card_postal_code = credit_card_postal_code
        if credit_card_state is not None:
            self.credit_card_state = credit_card_state
        if credit_card_type is not None:
            self.credit_card_type = credit_card_type
        if device_session_id is not None:
            self.device_session_id = device_session_id
        if email is not None:
            self.email = email
        if existing_mandate is not None:
            self.existing_mandate = existing_mandate
        if first_name is not None:
            self.first_name = first_name
        if iban is not None:
            self.iban = iban
        if ip_address is not None:
            self.ip_address = ip_address
        if last_name is not None:
            self.last_name = last_name
        if last_transaction_date_time is not None:
            self.last_transaction_date_time = last_transaction_date_time
        if last_transaction_status is not None:
            self.last_transaction_status = last_transaction_status
        if mandate_creation_date is not None:
            self.mandate_creation_date = mandate_creation_date
        if mandate_id is not None:
            self.mandate_id = mandate_id
        if mandate_received is not None:
            self.mandate_received = mandate_received
        if mandate_update_date is not None:
            self.mandate_update_date = mandate_update_date
        if max_consecutive_payment_failures is not None:
            self.max_consecutive_payment_failures = max_consecutive_payment_failures
        if num_consecutive_failures is not None:
            self.num_consecutive_failures = num_consecutive_failures
        if payment_method_status is not None:
            self.payment_method_status = payment_method_status
        if payment_retry_window is not None:
            self.payment_retry_window = payment_retry_window
        if phone is not None:
            self.phone = phone
        if postal_code is not None:
            self.postal_code = postal_code
        if state is not None:
            self.state = state
        if street_name is not None:
            self.street_name = street_name
        if street_number is not None:
            self.street_number = street_number
        if use_default_retry_rule is not None:
            self.use_default_retry_rule = use_default_retry_rule

    @property
    def account_id(self):
        """Gets the account_id of this ProxyModifyPaymentMethod.  # noqa: E501

         The ID of the customer account associated with this payment method. This field is not required for the account ID.   # noqa: E501

        :return: The account_id of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ProxyModifyPaymentMethod.

         The ID of the customer account associated with this payment method. This field is not required for the account ID.   # noqa: E501

        :param account_id: The account_id of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def ach_aba_code(self):
        """Gets the ach_aba_code of this ProxyModifyPaymentMethod.  # noqa: E501

         The nine-digit routing number or ABA number used by banks. Use this field for ACH payment methods. **Character limit**: 9 **Values**: a string of 9 characters or fewer   # noqa: E501

        :return: The ach_aba_code of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._ach_aba_code

    @ach_aba_code.setter
    def ach_aba_code(self, ach_aba_code):
        """Sets the ach_aba_code of this ProxyModifyPaymentMethod.

         The nine-digit routing number or ABA number used by banks. Use this field for ACH payment methods. **Character limit**: 9 **Values**: a string of 9 characters or fewer   # noqa: E501

        :param ach_aba_code: The ach_aba_code of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._ach_aba_code = ach_aba_code

    @property
    def ach_account_name(self):
        """Gets the ach_account_name of this ProxyModifyPaymentMethod.  # noqa: E501

         The name of the account holder, which can be either a person or a company. Use this field for ACH payment methods. **Character limit**: 70 **Values**: a string of 70 characters or fewer   # noqa: E501

        :return: The ach_account_name of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._ach_account_name

    @ach_account_name.setter
    def ach_account_name(self, ach_account_name):
        """Sets the ach_account_name of this ProxyModifyPaymentMethod.

         The name of the account holder, which can be either a person or a company. Use this field for ACH payment methods. **Character limit**: 70 **Values**: a string of 70 characters or fewer   # noqa: E501

        :param ach_account_name: The ach_account_name of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._ach_account_name = ach_account_name

    @property
    def ach_account_type(self):
        """Gets the ach_account_type of this ProxyModifyPaymentMethod.  # noqa: E501

         The type of bank account associated with the ACH payment. Use this field for ACH payment methods. **Character limit**: 16 **Values**:  - `BusinessChecking` - `Checking` - `Saving`   # noqa: E501

        :return: The ach_account_type of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._ach_account_type

    @ach_account_type.setter
    def ach_account_type(self, ach_account_type):
        """Sets the ach_account_type of this ProxyModifyPaymentMethod.

         The type of bank account associated with the ACH payment. Use this field for ACH payment methods. **Character limit**: 16 **Values**:  - `BusinessChecking` - `Checking` - `Saving`   # noqa: E501

        :param ach_account_type: The ach_account_type of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._ach_account_type = ach_account_type

    @property
    def ach_address1(self):
        """Gets the ach_address1 of this ProxyModifyPaymentMethod.  # noqa: E501

         Line 1 for the ACH address. Required on create for the Vantiv payment gateway. Optional for other gateways. **Character limit:** **Values:** an address   # noqa: E501

        :return: The ach_address1 of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._ach_address1

    @ach_address1.setter
    def ach_address1(self, ach_address1):
        """Sets the ach_address1 of this ProxyModifyPaymentMethod.

         Line 1 for the ACH address. Required on create for the Vantiv payment gateway. Optional for other gateways. **Character limit:** **Values:** an address   # noqa: E501

        :param ach_address1: The ach_address1 of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._ach_address1 = ach_address1

    @property
    def ach_address2(self):
        """Gets the ach_address2 of this ProxyModifyPaymentMethod.  # noqa: E501

         Line 2 for the ACH address. Required on create for the Vantiv payment gateway. Optional for other gateways. **Character limit:** **Values:** an address   # noqa: E501

        :return: The ach_address2 of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._ach_address2

    @ach_address2.setter
    def ach_address2(self, ach_address2):
        """Sets the ach_address2 of this ProxyModifyPaymentMethod.

         Line 2 for the ACH address. Required on create for the Vantiv payment gateway. Optional for other gateways. **Character limit:** **Values:** an address   # noqa: E501

        :param ach_address2: The ach_address2 of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._ach_address2 = ach_address2

    @property
    def ach_bank_name(self):
        """Gets the ach_bank_name of this ProxyModifyPaymentMethod.  # noqa: E501

         The name of the bank where the ACH payment account is held. Use this field for ACH payment methods. **Character limit**: 70 **Values**: a string of 70 characters or fewer   # noqa: E501

        :return: The ach_bank_name of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._ach_bank_name

    @ach_bank_name.setter
    def ach_bank_name(self, ach_bank_name):
        """Sets the ach_bank_name of this ProxyModifyPaymentMethod.

         The name of the bank where the ACH payment account is held. Use this field for ACH payment methods. **Character limit**: 70 **Values**: a string of 70 characters or fewer   # noqa: E501

        :param ach_bank_name: The ach_bank_name of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._ach_bank_name = ach_bank_name

    @property
    def bank_branch_code(self):
        """Gets the bank_branch_code of this ProxyModifyPaymentMethod.  # noqa: E501

         The branch code of the bank used for direct debit. Use this field for direct debit payment methods. **Character limit**: 10 **Values**:  string of 10 characters or fewer   # noqa: E501

        :return: The bank_branch_code of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._bank_branch_code

    @bank_branch_code.setter
    def bank_branch_code(self, bank_branch_code):
        """Sets the bank_branch_code of this ProxyModifyPaymentMethod.

         The branch code of the bank used for direct debit. Use this field for direct debit payment methods. **Character limit**: 10 **Values**:  string of 10 characters or fewer   # noqa: E501

        :param bank_branch_code: The bank_branch_code of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._bank_branch_code = bank_branch_code

    @property
    def bank_check_digit(self):
        """Gets the bank_check_digit of this ProxyModifyPaymentMethod.  # noqa: E501

        The check digit in the international bank account number, which confirms the validity of the account. Use this field for direct debit payment methods. **Character limit**: 4 **Values**:  string of 4 characters or fewer   # noqa: E501

        :return: The bank_check_digit of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._bank_check_digit

    @bank_check_digit.setter
    def bank_check_digit(self, bank_check_digit):
        """Sets the bank_check_digit of this ProxyModifyPaymentMethod.

        The check digit in the international bank account number, which confirms the validity of the account. Use this field for direct debit payment methods. **Character limit**: 4 **Values**:  string of 4 characters or fewer   # noqa: E501

        :param bank_check_digit: The bank_check_digit of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._bank_check_digit = bank_check_digit

    @property
    def bank_city(self):
        """Gets the bank_city of this ProxyModifyPaymentMethod.  # noqa: E501

         The city of the direct debit bank. Use this field for direct debit payment methods. **Character limit**:70 **Values**:  string of 70 characters or fewer   # noqa: E501

        :return: The bank_city of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._bank_city

    @bank_city.setter
    def bank_city(self, bank_city):
        """Sets the bank_city of this ProxyModifyPaymentMethod.

         The city of the direct debit bank. Use this field for direct debit payment methods. **Character limit**:70 **Values**:  string of 70 characters or fewer   # noqa: E501

        :param bank_city: The bank_city of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._bank_city = bank_city

    @property
    def bank_code(self):
        """Gets the bank_code of this ProxyModifyPaymentMethod.  # noqa: E501

         The sort code or number that identifies the bank. This is also known as the sort code. This field is required for direct debit payment methods. **Character limit**: 18 **Values**:  string of 18 characters or fewer   # noqa: E501

        :return: The bank_code of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._bank_code

    @bank_code.setter
    def bank_code(self, bank_code):
        """Sets the bank_code of this ProxyModifyPaymentMethod.

         The sort code or number that identifies the bank. This is also known as the sort code. This field is required for direct debit payment methods. **Character limit**: 18 **Values**:  string of 18 characters or fewer   # noqa: E501

        :param bank_code: The bank_code of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._bank_code = bank_code

    @property
    def bank_name(self):
        """Gets the bank_name of this ProxyModifyPaymentMethod.  # noqa: E501

         The name of the direct debit bank. Use this field for direct debit payment methods. **Character limit**:80 **Values**:  string of 80 characters or fewer   # noqa: E501

        :return: The bank_name of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._bank_name

    @bank_name.setter
    def bank_name(self, bank_name):
        """Sets the bank_name of this ProxyModifyPaymentMethod.

         The name of the direct debit bank. Use this field for direct debit payment methods. **Character limit**:80 **Values**:  string of 80 characters or fewer   # noqa: E501

        :param bank_name: The bank_name of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._bank_name = bank_name

    @property
    def bank_postal_code(self):
        """Gets the bank_postal_code of this ProxyModifyPaymentMethod.  # noqa: E501

         The zip code or postal code of the direct debit bank. Use this field for direct debit payment methods. **Character limit**:20 **Values**:  string of 20 characters or fewer   # noqa: E501

        :return: The bank_postal_code of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._bank_postal_code

    @bank_postal_code.setter
    def bank_postal_code(self, bank_postal_code):
        """Sets the bank_postal_code of this ProxyModifyPaymentMethod.

         The zip code or postal code of the direct debit bank. Use this field for direct debit payment methods. **Character limit**:20 **Values**:  string of 20 characters or fewer   # noqa: E501

        :param bank_postal_code: The bank_postal_code of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._bank_postal_code = bank_postal_code

    @property
    def bank_street_name(self):
        """Gets the bank_street_name of this ProxyModifyPaymentMethod.  # noqa: E501

         The name of the street of the direct debit bank. Use this field for direct debit payment methods. **Character limit**:60 **Values**:  string of 60 characters or fewer   # noqa: E501

        :return: The bank_street_name of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._bank_street_name

    @bank_street_name.setter
    def bank_street_name(self, bank_street_name):
        """Sets the bank_street_name of this ProxyModifyPaymentMethod.

         The name of the street of the direct debit bank. Use this field for direct debit payment methods. **Character limit**:60 **Values**:  string of 60 characters or fewer   # noqa: E501

        :param bank_street_name: The bank_street_name of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._bank_street_name = bank_street_name

    @property
    def bank_street_number(self):
        """Gets the bank_street_number of this ProxyModifyPaymentMethod.  # noqa: E501

         The number of the direct debit bank. Use this field for direct debit payment methods. **Character limit**:10 **Values**:  string of 10 characters or fewer   # noqa: E501

        :return: The bank_street_number of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._bank_street_number

    @bank_street_number.setter
    def bank_street_number(self, bank_street_number):
        """Sets the bank_street_number of this ProxyModifyPaymentMethod.

         The number of the direct debit bank. Use this field for direct debit payment methods. **Character limit**:10 **Values**:  string of 10 characters or fewer   # noqa: E501

        :param bank_street_number: The bank_street_number of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._bank_street_number = bank_street_number

    @property
    def bank_transfer_account_name(self):
        """Gets the bank_transfer_account_name of this ProxyModifyPaymentMethod.  # noqa: E501

         The name on the direct debit bank account. Use this field for direct debit payment methods. **Character limit**: 60 **Values**:  string of 60 characters or fewer   # noqa: E501

        :return: The bank_transfer_account_name of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._bank_transfer_account_name

    @bank_transfer_account_name.setter
    def bank_transfer_account_name(self, bank_transfer_account_name):
        """Sets the bank_transfer_account_name of this ProxyModifyPaymentMethod.

         The name on the direct debit bank account. Use this field for direct debit payment methods. **Character limit**: 60 **Values**:  string of 60 characters or fewer   # noqa: E501

        :param bank_transfer_account_name: The bank_transfer_account_name of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._bank_transfer_account_name = bank_transfer_account_name

    @property
    def business_identification_code(self):
        """Gets the business_identification_code of this ProxyModifyPaymentMethod.  # noqa: E501

         The business identification code for Swiss direct payment methods that use the Global Collect payment gateway. Use this field only for direct debit payments in Switzerland with Global Collect. **Character limit**: 11 **Values**: string of 11 characters or fewer   # noqa: E501

        :return: The business_identification_code of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._business_identification_code

    @business_identification_code.setter
    def business_identification_code(self, business_identification_code):
        """Sets the business_identification_code of this ProxyModifyPaymentMethod.

         The business identification code for Swiss direct payment methods that use the Global Collect payment gateway. Use this field only for direct debit payments in Switzerland with Global Collect. **Character limit**: 11 **Values**: string of 11 characters or fewer   # noqa: E501

        :param business_identification_code: The business_identification_code of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._business_identification_code = business_identification_code

    @property
    def city(self):
        """Gets the city of this ProxyModifyPaymentMethod.  # noqa: E501

         The city of the customer's address. Use this field for direct debit payment methods. **Character limit**:80 **Values**:  string of 80 characters or fewer   # noqa: E501

        :return: The city of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ProxyModifyPaymentMethod.

         The city of the customer's address. Use this field for direct debit payment methods. **Character limit**:80 **Values**:  string of 80 characters or fewer   # noqa: E501

        :param city: The city of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this ProxyModifyPaymentMethod.  # noqa: E501

         The two-letter country code of the customer's address. Use this field for direct debit payment methods. **Character limit**: 2 **Values**: a valid country code   # noqa: E501

        :return: The country of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ProxyModifyPaymentMethod.

         The two-letter country code of the customer's address. Use this field for direct debit payment methods. **Character limit**: 2 **Values**: a valid country code   # noqa: E501

        :param country: The country of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def credit_card_address1(self):
        """Gets the credit_card_address1 of this ProxyModifyPaymentMethod.  # noqa: E501

         The first line of the card holder's address, which is often a street address or business name. Use this field for credit card and direct debit payment methods. **Character limit**: 255 **Values**: a string of 255 characters or fewer   # noqa: E501

        :return: The credit_card_address1 of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_address1

    @credit_card_address1.setter
    def credit_card_address1(self, credit_card_address1):
        """Sets the credit_card_address1 of this ProxyModifyPaymentMethod.

         The first line of the card holder's address, which is often a street address or business name. Use this field for credit card and direct debit payment methods. **Character limit**: 255 **Values**: a string of 255 characters or fewer   # noqa: E501

        :param credit_card_address1: The credit_card_address1 of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._credit_card_address1 = credit_card_address1

    @property
    def credit_card_address2(self):
        """Gets the credit_card_address2 of this ProxyModifyPaymentMethod.  # noqa: E501

         The second line of the card holder's address. Use this field for credit card and direct debit payment methods. **Character limit**: 255 **Values**: a string of 255 characters or fewer   # noqa: E501

        :return: The credit_card_address2 of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_address2

    @credit_card_address2.setter
    def credit_card_address2(self, credit_card_address2):
        """Sets the credit_card_address2 of this ProxyModifyPaymentMethod.

         The second line of the card holder's address. Use this field for credit card and direct debit payment methods. **Character limit**: 255 **Values**: a string of 255 characters or fewer   # noqa: E501

        :param credit_card_address2: The credit_card_address2 of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._credit_card_address2 = credit_card_address2

    @property
    def credit_card_city(self):
        """Gets the credit_card_city of this ProxyModifyPaymentMethod.  # noqa: E501

         The city of the card holder's address. Use this field for credit card and direct debit payment methods **Character limit**: 40 **Values**: a string of 40 characters or fewer   # noqa: E501

        :return: The credit_card_city of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_city

    @credit_card_city.setter
    def credit_card_city(self, credit_card_city):
        """Sets the credit_card_city of this ProxyModifyPaymentMethod.

         The city of the card holder's address. Use this field for credit card and direct debit payment methods **Character limit**: 40 **Values**: a string of 40 characters or fewer   # noqa: E501

        :param credit_card_city: The credit_card_city of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._credit_card_city = credit_card_city

    @property
    def credit_card_country(self):
        """Gets the credit_card_country of this ProxyModifyPaymentMethod.  # noqa: E501

         The country of the card holder's address.   # noqa: E501

        :return: The credit_card_country of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_country

    @credit_card_country.setter
    def credit_card_country(self, credit_card_country):
        """Sets the credit_card_country of this ProxyModifyPaymentMethod.

         The country of the card holder's address.   # noqa: E501

        :param credit_card_country: The credit_card_country of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._credit_card_country = credit_card_country

    @property
    def credit_card_expiration_month(self):
        """Gets the credit_card_expiration_month of this ProxyModifyPaymentMethod.  # noqa: E501

         The expiration month of the credit card or debit card. Use this field for credit card and direct debit payment methods. **Character limit**: 2 **Values**: a two-digit number, 01 - 12   # noqa: E501

        :return: The credit_card_expiration_month of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: int
        """
        return self._credit_card_expiration_month

    @credit_card_expiration_month.setter
    def credit_card_expiration_month(self, credit_card_expiration_month):
        """Sets the credit_card_expiration_month of this ProxyModifyPaymentMethod.

         The expiration month of the credit card or debit card. Use this field for credit card and direct debit payment methods. **Character limit**: 2 **Values**: a two-digit number, 01 - 12   # noqa: E501

        :param credit_card_expiration_month: The credit_card_expiration_month of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: int
        """

        self._credit_card_expiration_month = credit_card_expiration_month

    @property
    def credit_card_expiration_year(self):
        """Gets the credit_card_expiration_year of this ProxyModifyPaymentMethod.  # noqa: E501

         The expiration month of the credit card or debit card. Use this field for credit card and direct debit payment methods. **Character limit**: 4 **Values**: a four-digit number   # noqa: E501

        :return: The credit_card_expiration_year of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: int
        """
        return self._credit_card_expiration_year

    @credit_card_expiration_year.setter
    def credit_card_expiration_year(self, credit_card_expiration_year):
        """Sets the credit_card_expiration_year of this ProxyModifyPaymentMethod.

         The expiration month of the credit card or debit card. Use this field for credit card and direct debit payment methods. **Character limit**: 4 **Values**: a four-digit number   # noqa: E501

        :param credit_card_expiration_year: The credit_card_expiration_year of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: int
        """

        self._credit_card_expiration_year = credit_card_expiration_year

    @property
    def credit_card_holder_name(self):
        """Gets the credit_card_holder_name of this ProxyModifyPaymentMethod.  # noqa: E501

         The full name of the card holder. Use this field for credit card and direct debit payment methods. **Character limit**: 50 **Values**: a string of 50 characters or fewer   # noqa: E501

        :return: The credit_card_holder_name of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_holder_name

    @credit_card_holder_name.setter
    def credit_card_holder_name(self, credit_card_holder_name):
        """Sets the credit_card_holder_name of this ProxyModifyPaymentMethod.

         The full name of the card holder. Use this field for credit card and direct debit payment methods. **Character limit**: 50 **Values**: a string of 50 characters or fewer   # noqa: E501

        :param credit_card_holder_name: The credit_card_holder_name of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._credit_card_holder_name = credit_card_holder_name

    @property
    def credit_card_postal_code(self):
        """Gets the credit_card_postal_code of this ProxyModifyPaymentMethod.  # noqa: E501

         The billing address's zip code. This field is required only when you define a debit card or credit card payment. **Character limit**: 20 **Values**: a string of 20 characters or fewer   # noqa: E501

        :return: The credit_card_postal_code of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_postal_code

    @credit_card_postal_code.setter
    def credit_card_postal_code(self, credit_card_postal_code):
        """Sets the credit_card_postal_code of this ProxyModifyPaymentMethod.

         The billing address's zip code. This field is required only when you define a debit card or credit card payment. **Character limit**: 20 **Values**: a string of 20 characters or fewer   # noqa: E501

        :param credit_card_postal_code: The credit_card_postal_code of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._credit_card_postal_code = credit_card_postal_code

    @property
    def credit_card_state(self):
        """Gets the credit_card_state of this ProxyModifyPaymentMethod.  # noqa: E501

         The billing address's state. Use this field is if the `CreditCardCountry' value is either Canada or the US. State names must be spelled in full.   # noqa: E501

        :return: The credit_card_state of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_state

    @credit_card_state.setter
    def credit_card_state(self, credit_card_state):
        """Sets the credit_card_state of this ProxyModifyPaymentMethod.

         The billing address's state. Use this field is if the `CreditCardCountry' value is either Canada or the US. State names must be spelled in full.   # noqa: E501

        :param credit_card_state: The credit_card_state of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._credit_card_state = credit_card_state

    @property
    def credit_card_type(self):
        """Gets the credit_card_type of this ProxyModifyPaymentMethod.  # noqa: E501

         The type of credit card or debit card. This field is required only when you define a debit card or credit card payment. **Character limit**: 32 **Values**: `AmericanExpress`, `Discover`, `MasterCard`, `Visa`   # noqa: E501

        :return: The credit_card_type of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_type

    @credit_card_type.setter
    def credit_card_type(self, credit_card_type):
        """Sets the credit_card_type of this ProxyModifyPaymentMethod.

         The type of credit card or debit card. This field is required only when you define a debit card or credit card payment. **Character limit**: 32 **Values**: `AmericanExpress`, `Discover`, `MasterCard`, `Visa`   # noqa: E501

        :param credit_card_type: The credit_card_type of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._credit_card_type = credit_card_type

    @property
    def device_session_id(self):
        """Gets the device_session_id of this ProxyModifyPaymentMethod.  # noqa: E501

         The session ID of the user when the `PaymentMethod` was created or updated. Some gateways use this field for fraud prevention. If this field is passed to Zuora, then Zuora passes this field to supported gateways. Currently only Verifi supports this field. **Character limit**: 255 **Values**:   # noqa: E501

        :return: The device_session_id of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._device_session_id

    @device_session_id.setter
    def device_session_id(self, device_session_id):
        """Sets the device_session_id of this ProxyModifyPaymentMethod.

         The session ID of the user when the `PaymentMethod` was created or updated. Some gateways use this field for fraud prevention. If this field is passed to Zuora, then Zuora passes this field to supported gateways. Currently only Verifi supports this field. **Character limit**: 255 **Values**:   # noqa: E501

        :param device_session_id: The device_session_id of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._device_session_id = device_session_id

    @property
    def email(self):
        """Gets the email of this ProxyModifyPaymentMethod.  # noqa: E501

         An email address for the payment method in addition to the bill to contact email address. **Character limit**: 80 **Values**: a string of 80 characters or fewer   # noqa: E501

        :return: The email of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ProxyModifyPaymentMethod.

         An email address for the payment method in addition to the bill to contact email address. **Character limit**: 80 **Values**: a string of 80 characters or fewer   # noqa: E501

        :param email: The email of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def existing_mandate(self):
        """Gets the existing_mandate of this ProxyModifyPaymentMethod.  # noqa: E501

         Indicates if the customer has an existing mandate or a new mandate. A mandate is a signed authorization for UK and NL customers. When you are migrating mandates from another system, be sure to set this field correctly. If you indicate that a new mandate is an existing mandate or vice-versa, then transactions fail. This field is used only for the direct debit payment method. **Character limit**: 3 **Values**: `Yes`, `No`   # noqa: E501

        :return: The existing_mandate of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._existing_mandate

    @existing_mandate.setter
    def existing_mandate(self, existing_mandate):
        """Sets the existing_mandate of this ProxyModifyPaymentMethod.

         Indicates if the customer has an existing mandate or a new mandate. A mandate is a signed authorization for UK and NL customers. When you are migrating mandates from another system, be sure to set this field correctly. If you indicate that a new mandate is an existing mandate or vice-versa, then transactions fail. This field is used only for the direct debit payment method. **Character limit**: 3 **Values**: `Yes`, `No`   # noqa: E501

        :param existing_mandate: The existing_mandate of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._existing_mandate = existing_mandate

    @property
    def first_name(self):
        """Gets the first_name of this ProxyModifyPaymentMethod.  # noqa: E501

         The customer's first name. This field is used only for the direct debit payment method. **Character limit**: 30 **Values**: a string of 30 characters or fewer   # noqa: E501

        :return: The first_name of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this ProxyModifyPaymentMethod.

         The customer's first name. This field is used only for the direct debit payment method. **Character limit**: 30 **Values**: a string of 30 characters or fewer   # noqa: E501

        :param first_name: The first_name of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def iban(self):
        """Gets the iban of this ProxyModifyPaymentMethod.  # noqa: E501

         The International Bank Account Number. This field is used only for the direct debit payment method. **Character limit**: 42 **Values**: a string of 42 characters or fewer   # noqa: E501

        :return: The iban of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this ProxyModifyPaymentMethod.

         The International Bank Account Number. This field is used only for the direct debit payment method. **Character limit**: 42 **Values**: a string of 42 characters or fewer   # noqa: E501

        :param iban: The iban of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._iban = iban

    @property
    def ip_address(self):
        """Gets the ip_address of this ProxyModifyPaymentMethod.  # noqa: E501

         The IP address of the user when the payment method was created or updated. Some gateways use this field for fraud prevention. If this field is passed to Zuora, then Zuora passes this field to supported gateways. Currently PayPal, CyberSource, Authorize.Net, and Verifi support this field. **Character limit**: 15 **Values**: a string of 15 characters or fewer   # noqa: E501

        :return: The ip_address of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this ProxyModifyPaymentMethod.

         The IP address of the user when the payment method was created or updated. Some gateways use this field for fraud prevention. If this field is passed to Zuora, then Zuora passes this field to supported gateways. Currently PayPal, CyberSource, Authorize.Net, and Verifi support this field. **Character limit**: 15 **Values**: a string of 15 characters or fewer   # noqa: E501

        :param ip_address: The ip_address of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def last_name(self):
        """Gets the last_name of this ProxyModifyPaymentMethod.  # noqa: E501

         The customer's last name. This field is used only for the direct debit payment method. **Character limit**: 70 **Values**: a string of 70 characters or fewer   # noqa: E501

        :return: The last_name of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this ProxyModifyPaymentMethod.

         The customer's last name. This field is used only for the direct debit payment method. **Character limit**: 70 **Values**: a string of 70 characters or fewer   # noqa: E501

        :param last_name: The last_name of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def last_transaction_date_time(self):
        """Gets the last_transaction_date_time of this ProxyModifyPaymentMethod.  # noqa: E501

         The date of the most recent transaction. **Character limit**: 29 **Values**: a valid date and time value   # noqa: E501

        :return: The last_transaction_date_time of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: datetime
        """
        return self._last_transaction_date_time

    @last_transaction_date_time.setter
    def last_transaction_date_time(self, last_transaction_date_time):
        """Sets the last_transaction_date_time of this ProxyModifyPaymentMethod.

         The date of the most recent transaction. **Character limit**: 29 **Values**: a valid date and time value   # noqa: E501

        :param last_transaction_date_time: The last_transaction_date_time of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: datetime
        """

        self._last_transaction_date_time = last_transaction_date_time

    @property
    def last_transaction_status(self):
        """Gets the last_transaction_status of this ProxyModifyPaymentMethod.  # noqa: E501

         The status of the most recent transaction. **Character limit**: 39 **Values**: automatically generated   # noqa: E501

        :return: The last_transaction_status of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._last_transaction_status

    @last_transaction_status.setter
    def last_transaction_status(self, last_transaction_status):
        """Sets the last_transaction_status of this ProxyModifyPaymentMethod.

         The status of the most recent transaction. **Character limit**: 39 **Values**: automatically generated   # noqa: E501

        :param last_transaction_status: The last_transaction_status of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._last_transaction_status = last_transaction_status

    @property
    def mandate_creation_date(self):
        """Gets the mandate_creation_date of this ProxyModifyPaymentMethod.  # noqa: E501

         The date when the mandate was created, in `yyyy-mm-dd` format. A mandate is a signed authorization for UK and NL customers. This field is used only for the direct debit payment method. **Character limit**: 29   # noqa: E501

        :return: The mandate_creation_date of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: date
        """
        return self._mandate_creation_date

    @mandate_creation_date.setter
    def mandate_creation_date(self, mandate_creation_date):
        """Sets the mandate_creation_date of this ProxyModifyPaymentMethod.

         The date when the mandate was created, in `yyyy-mm-dd` format. A mandate is a signed authorization for UK and NL customers. This field is used only for the direct debit payment method. **Character limit**: 29   # noqa: E501

        :param mandate_creation_date: The mandate_creation_date of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: date
        """

        self._mandate_creation_date = mandate_creation_date

    @property
    def mandate_id(self):
        """Gets the mandate_id of this ProxyModifyPaymentMethod.  # noqa: E501

         The ID of the mandate. A mandate is a signed authorization for UK and NL customers. This field is used only for the direct debit payment method. **Character limit**: 36 **Values**: a string of 36 characters or fewer   # noqa: E501

        :return: The mandate_id of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._mandate_id

    @mandate_id.setter
    def mandate_id(self, mandate_id):
        """Sets the mandate_id of this ProxyModifyPaymentMethod.

         The ID of the mandate. A mandate is a signed authorization for UK and NL customers. This field is used only for the direct debit payment method. **Character limit**: 36 **Values**: a string of 36 characters or fewer   # noqa: E501

        :param mandate_id: The mandate_id of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._mandate_id = mandate_id

    @property
    def mandate_received(self):
        """Gets the mandate_received of this ProxyModifyPaymentMethod.  # noqa: E501

         Indicates if  the mandate was received. A mandate is a signed authorization for UK and NL customers. This field is used only for the direct debit payment method. **Character limit**: 3 **Values**: `Yes`, `No `(case-sensitive)   # noqa: E501

        :return: The mandate_received of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._mandate_received

    @mandate_received.setter
    def mandate_received(self, mandate_received):
        """Sets the mandate_received of this ProxyModifyPaymentMethod.

         Indicates if  the mandate was received. A mandate is a signed authorization for UK and NL customers. This field is used only for the direct debit payment method. **Character limit**: 3 **Values**: `Yes`, `No `(case-sensitive)   # noqa: E501

        :param mandate_received: The mandate_received of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._mandate_received = mandate_received

    @property
    def mandate_update_date(self):
        """Gets the mandate_update_date of this ProxyModifyPaymentMethod.  # noqa: E501

         The date when the mandate was last updated, in `yyyy-mm-dd` format. A mandate is a signed authorization for UK and NL customers. This field is used only for the direct debit payment method. **Character limit**: 29   # noqa: E501

        :return: The mandate_update_date of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: date
        """
        return self._mandate_update_date

    @mandate_update_date.setter
    def mandate_update_date(self, mandate_update_date):
        """Sets the mandate_update_date of this ProxyModifyPaymentMethod.

         The date when the mandate was last updated, in `yyyy-mm-dd` format. A mandate is a signed authorization for UK and NL customers. This field is used only for the direct debit payment method. **Character limit**: 29   # noqa: E501

        :param mandate_update_date: The mandate_update_date of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: date
        """

        self._mandate_update_date = mandate_update_date

    @property
    def max_consecutive_payment_failures(self):
        """Gets the max_consecutive_payment_failures of this ProxyModifyPaymentMethod.  # noqa: E501

         Specifies the number of allowable consecutive failures Zuora attempts with the payment method before stopping. **Values**: a valid number   # noqa: E501

        :return: The max_consecutive_payment_failures of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: int
        """
        return self._max_consecutive_payment_failures

    @max_consecutive_payment_failures.setter
    def max_consecutive_payment_failures(self, max_consecutive_payment_failures):
        """Sets the max_consecutive_payment_failures of this ProxyModifyPaymentMethod.

         Specifies the number of allowable consecutive failures Zuora attempts with the payment method before stopping. **Values**: a valid number   # noqa: E501

        :param max_consecutive_payment_failures: The max_consecutive_payment_failures of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: int
        """

        self._max_consecutive_payment_failures = max_consecutive_payment_failures

    @property
    def num_consecutive_failures(self):
        """Gets the num_consecutive_failures of this ProxyModifyPaymentMethod.  # noqa: E501

        The number of consecutive failed payments for this payment method. It is reset to `0` upon successful payment.    # noqa: E501

        :return: The num_consecutive_failures of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: int
        """
        return self._num_consecutive_failures

    @num_consecutive_failures.setter
    def num_consecutive_failures(self, num_consecutive_failures):
        """Sets the num_consecutive_failures of this ProxyModifyPaymentMethod.

        The number of consecutive failed payments for this payment method. It is reset to `0` upon successful payment.    # noqa: E501

        :param num_consecutive_failures: The num_consecutive_failures of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: int
        """
        if num_consecutive_failures is not None and num_consecutive_failures > 100:  # noqa: E501
            raise ValueError("Invalid value for `num_consecutive_failures`, must be a value less than or equal to `100`")  # noqa: E501
        if num_consecutive_failures is not None and num_consecutive_failures < 0:  # noqa: E501
            raise ValueError("Invalid value for `num_consecutive_failures`, must be a value greater than or equal to `0`")  # noqa: E501

        self._num_consecutive_failures = num_consecutive_failures

    @property
    def payment_method_status(self):
        """Gets the payment_method_status of this ProxyModifyPaymentMethod.  # noqa: E501

         Specifies the status of the payment method. It is set to Active on creation. **Character limit**: 6 **Values**: `Active` or `Closed`   # noqa: E501

        :return: The payment_method_status of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._payment_method_status

    @payment_method_status.setter
    def payment_method_status(self, payment_method_status):
        """Sets the payment_method_status of this ProxyModifyPaymentMethod.

         Specifies the status of the payment method. It is set to Active on creation. **Character limit**: 6 **Values**: `Active` or `Closed`   # noqa: E501

        :param payment_method_status: The payment_method_status of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._payment_method_status = payment_method_status

    @property
    def payment_retry_window(self):
        """Gets the payment_retry_window of this ProxyModifyPaymentMethod.  # noqa: E501

         The retry interval setting, which prevents making a payment attempt if the last failed attempt was within the last specified number of hours. This field is required if the `UseDefaultRetryRule` field value is set to `false`. **Character limit**: 4 **Values**: a whole number between 1 and 1000, exclusive   # noqa: E501

        :return: The payment_retry_window of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: int
        """
        return self._payment_retry_window

    @payment_retry_window.setter
    def payment_retry_window(self, payment_retry_window):
        """Sets the payment_retry_window of this ProxyModifyPaymentMethod.

         The retry interval setting, which prevents making a payment attempt if the last failed attempt was within the last specified number of hours. This field is required if the `UseDefaultRetryRule` field value is set to `false`. **Character limit**: 4 **Values**: a whole number between 1 and 1000, exclusive   # noqa: E501

        :param payment_retry_window: The payment_retry_window of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: int
        """

        self._payment_retry_window = payment_retry_window

    @property
    def phone(self):
        """Gets the phone of this ProxyModifyPaymentMethod.  # noqa: E501

         The phone number that the account holder registered with the bank. This field is used for credit card validation when passing to a gateway. **Character limit**: 40 **Values**: a string of 40 characters or fewer   # noqa: E501

        :return: The phone of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this ProxyModifyPaymentMethod.

         The phone number that the account holder registered with the bank. This field is used for credit card validation when passing to a gateway. **Character limit**: 40 **Values**: a string of 40 characters or fewer   # noqa: E501

        :param phone: The phone of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def postal_code(self):
        """Gets the postal_code of this ProxyModifyPaymentMethod.  # noqa: E501

         The zip code of the customer's address. This field is used only for the direct debit payment method. **Character limit**: 20 **Values**: a string of 20 characters or fewer   # noqa: E501

        :return: The postal_code of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this ProxyModifyPaymentMethod.

         The zip code of the customer's address. This field is used only for the direct debit payment method. **Character limit**: 20 **Values**: a string of 20 characters or fewer   # noqa: E501

        :param postal_code: The postal_code of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def state(self):
        """Gets the state of this ProxyModifyPaymentMethod.  # noqa: E501

         The state of the customer's address. This field is used only for the direct debit payment method. **Character limit**: 70 **Values**: a string of 70 characters or fewer   # noqa: E501

        :return: The state of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ProxyModifyPaymentMethod.

         The state of the customer's address. This field is used only for the direct debit payment method. **Character limit**: 70 **Values**: a string of 70 characters or fewer   # noqa: E501

        :param state: The state of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def street_name(self):
        """Gets the street_name of this ProxyModifyPaymentMethod.  # noqa: E501

         The street name of the customer's address. This field is used only for the direct debit payment method. **Character limit**: 100 **Values**: a string of 100 characters or fewer   # noqa: E501

        :return: The street_name of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._street_name

    @street_name.setter
    def street_name(self, street_name):
        """Sets the street_name of this ProxyModifyPaymentMethod.

         The street name of the customer's address. This field is used only for the direct debit payment method. **Character limit**: 100 **Values**: a string of 100 characters or fewer   # noqa: E501

        :param street_name: The street_name of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._street_name = street_name

    @property
    def street_number(self):
        """Gets the street_number of this ProxyModifyPaymentMethod.  # noqa: E501

         The street number of the customer's address. This field is used only for the direct debit payment method. **Character limit**: 30 **Values**: a string of 30 characters or fewer   # noqa: E501

        :return: The street_number of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._street_number

    @street_number.setter
    def street_number(self, street_number):
        """Sets the street_number of this ProxyModifyPaymentMethod.

         The street number of the customer's address. This field is used only for the direct debit payment method. **Character limit**: 30 **Values**: a string of 30 characters or fewer   # noqa: E501

        :param street_number: The street_number of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: str
        """

        self._street_number = street_number

    @property
    def use_default_retry_rule(self):
        """Gets the use_default_retry_rule of this ProxyModifyPaymentMethod.  # noqa: E501

         Determines whether to use the default retry rules configured in the Zuora Payments settings. Set this to `true` to use the default retry rules. Set this to `false` to set the specific rules for this payment method. If you set this value to `false`, then the fields, `PaymentRetryWindow` and `MaxConsecutivePaymentFailures`, are required. **Character limit**: 5 **Values**: `t``rue`, `false`   # noqa: E501

        :return: The use_default_retry_rule of this ProxyModifyPaymentMethod.  # noqa: E501
        :rtype: bool
        """
        return self._use_default_retry_rule

    @use_default_retry_rule.setter
    def use_default_retry_rule(self, use_default_retry_rule):
        """Sets the use_default_retry_rule of this ProxyModifyPaymentMethod.

         Determines whether to use the default retry rules configured in the Zuora Payments settings. Set this to `true` to use the default retry rules. Set this to `false` to set the specific rules for this payment method. If you set this value to `false`, then the fields, `PaymentRetryWindow` and `MaxConsecutivePaymentFailures`, are required. **Character limit**: 5 **Values**: `t``rue`, `false`   # noqa: E501

        :param use_default_retry_rule: The use_default_retry_rule of this ProxyModifyPaymentMethod.  # noqa: E501
        :type: bool
        """

        self._use_default_retry_rule = use_default_retry_rule

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
        if not isinstance(other, ProxyModifyPaymentMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
