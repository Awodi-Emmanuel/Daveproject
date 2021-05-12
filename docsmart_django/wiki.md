# DocSmart Wiki

This wiki define the workflows of relevant DocSmart APIs. This wiki will explain what's missing from the Readme, Postman Doc or Swagger doc.

## Onboarding

The onboarding of users is starightforward. Implinentation and usage can be found in the readme and postman collection provided in the repo.
A user onboards by creating a user account via the registration endpoint,
The user provides relevant information about themselevs and the company that they work for. Upon successful resgistration the user and a corresponding company whcih they belong to are created and said user is marked as owner.
There are several enpoint that can only be access bythe owner of a company. E.g Pay for subscription. 

####Invite User
Users can be onboarded by invites as well. A company owner can invite another user via the invite endpoint. The invited user gets an email to join the inviters company of which when the link is clicked they're provided a page to fil in theire customer info.

##Document

The document module and corresponding endpoints provide access to all APIs needed to create, update and delete a document.
Upon registration users get a directory created for the, the directory name is the user id concatinated to a user prefix.

The document files are saved in the user directory, while document related data are saved in the DB.

##Permissions
The persmission module handle access ti company and user documents.
A user can access user(documents they own) documents without restriction. These documents are fecthed from the users folder and corresponding database records.
Company documents however have much more restrictions. A user can have one or 4 access rights to a company document.

- Read
- Write
- Delete
- Owner

Read, write and delete permissions are applied as implied, while Oner permissions allow a user to do all 3 including share, grant aceess to the document to other user.

Companies also have directories and users have right to see all directories they have under their company.

##Sales Offer
Users can create a sales offer as long as the company has access to the sales plugin. Sales offer api are housed under the sales module.

Users can create a sales offer by just providing the title. Subsequent updates can then be made on the offer. Each sales offer must have a document, the document must be attched to the sales offer beffore the offer can be sent to customers.

A sales offer must also have cistomers attached to them, the customers awill recieve an email inviting them to sign the offer. Email reminders are also sent to remind custoomers about expiring sales offers.

A customer can be created vis the customer API. All customers created are accessible company wide.

##Plugins

The Plugin module acts as guards to various plugin resources on DocSmart. The plugin guards check users if they belong to a particular company and that company hass access to that particular plugin.

##BankId

When DocSmart users are done creating proposals, users add customers to that document and save(Via the update document endpoint). Upon sending the document(Via the send document endpoint) All customers attached to that document are sent an email and are added to a scheduled reminders table(To be reminded when documents are getting due) 
When the customer clicks the link on the email they're directed to the docsmart webpage for signing. Once the necessary information has been provided, users click sign and we send the relevant information over to bankid. Response from bank id is persisted in a signed document's table, which houses the id of the signed document, response from bankid(stored in a JSON field), customerid, company id(the company of the Docsnart user who sent the proposal) Reminders stop going out to customers once the document is signed.
