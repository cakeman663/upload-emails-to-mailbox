# Upload emails to mailbox

In the process of migrating from server with a web panel to server without a web panel, I'm faced with a problem of using old mailboxes. The panel has special utilities for processing emails and storing each email in a separate file. I didn't find how to load old emails to a new mailbox. So I wrote a script to upload mail from each file to a mailbox

As a result of the script, 99.9% of successfully uploaded emails and no bounced emails

You should set **mailbox** and **path** variables in the script. If you set incorrect **mailbox** variable, all emails will be bounced to senders. Be warned, If your emails will be bounced your hosting provider may ban you due to the high-speed bounced emails sending
