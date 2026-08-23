---
order: 44
slug: saas-support-ticket-system
anchor: support-ticket-system
title: Support Ticket System
h1: How to Set Up a Support Ticket System for B2B SaaS
category: operations
players: CS Lead, CTO
initialEffort: 13 SP
ongoingEffort: 8 SP
frequency: Monthly
stage: Early Traction
templates:
  - file: 4.30-support-ticket-system-template.xlsx
    name: Support Ticket System Template
summary: Implement a ticketing system that captures customer issues, routes them efficiently, tracks resolution, and provides data for support process improvement.
keywords:
  - support ticketing
  - helpdesk
  - support system
  - ticket management
  - support efficiency
  - first response time
  - resolution time
questions:
  - Why does support quality matter for revenue retention and growth?
  - What process should a support ticket follow from identification to resolution?
  - Who should provide support at a B2B SaaS company?
  - What information should I track for each support ticket?
  - How do I handle a frustrated customer?
preventsMistakes:
  - 59
  - 60
  - 61
  - 63
---
The quick and effective resolution of support needs is vital to customer satisfaction. A survey(https://d16cvnquvjw7pr.cloudfront.net/resources/whitepapers/Zendesk_WP_Customer_Service_and_Business_Results.pdf) conducted by Dimensional Research and Zendesk found that 66% of B2B customers stopped buying a product after a negative customer service interaction, while 62% of B2B customers bought more after a positive customer service interaction. To reiterate, a customer had a support need (a potentially negative experience) and *expanded* their account in response simply because the company responded effectively. Interestingly, timeliness of response had the biggest impact on customer satisfaction; 69% of customers pointed to a quick resolution of their problem to justify their good customer service experience. On the other hand, 72% of customers attributed having to explain their problem to multiple people as the cause of their negative customer service experience.

We point out these numbers to underline how important it is to have a process for responding to and resolving support requests.

**The Impact**: A well-designed support ticket system improves customer service satisfaction, which protects and potentially grows your revenue.

> **The Goal**: Establish a support ticket system that ensures the timely response and quick resolution of customer support needs.

#### Background

There are sophisticated subscription products available to automate your support ticket system. At the beginning stage of your company, you can also track customer support requests yourself. Regardless, the process is similar:

1. Identify: How do you identify support issues? Typically, identification will occur when a customer directly contacts you. But how do they contact you? It is good to have a single, separate support phone number that is broadly publicized to your customers to make the process as easy to initiate as possible for a customer. Additionally, consider whether there are additional modes of identification relevant to your company (ie automatic detection to monitor loss of service or bugs before your customer notices or social media monitoring).
2. Record: How and where are support tickets recorded? What information is necessary to collect to ensure the customer is appropriately engaged, the problem is fully resolved, and patterns in issues can be identified to flag opportunities for improvement?
3. Manage and Track: What process needs to be put in place to ensure the necessary people are notified and involved in resolving the issue? How can you ensure the ticket is addressed in a timely manner?
4. Resolve: At what point will the support ticket be marked as resolved? Who needs to be informed of support needs? How are support needs going to be leveraged to improve your knowledge base and make continual service improvements? How do you ensure the customer is satisfied with the resolution?

#### Steps:

1. Use the PDCA methodology described in Play: Quality Management Systems and the template provided to create a support ticket system. Considerations:
    - Who provides support? In B2B SaaS, your product is often highly technical, which makes the traditional tiered support model where a support call is first taken and then escalated to more qualified individuals inefficient. In all likelihood, the support ticket will be escalated and so you're causing unnecessary inefficiency by insisting on a tiered escalation model. Golden Section has found success having your SEs take on support for the accounts they have supported during the implementation phase. A SE is technically inclined and well-versed in the product and can often resolve support issues quickly and effectively. Moreover, they already have a relationship with the customer and knowledge of the customer's use case to maximize the effectiveness of their support.
    - Who needs to be informed of support needs? In some instances, the support request is not actually a support need but a new feature request. In that case, the request needs to be kicked back to a sales lead to facilitate the conversation.
    - How do you make sure that insights and opportunities for improvement learned from the support process get to the right people to push process and product improvements?
2. Create an issue tracker to track your support ticket system. A template has been provided, but modify it to fit your company's specific needs.

- Issue Ref No. - Use to reference the support ticket number or issue number from your support or dev ticket system.
- Issue Name - The at a glance descriptive name of the issue.
- Issue Description - Long form overview of the issue.
- Customer Owner - Customer point of contact on the issue
- Resolution Description - Common description of 'resolved' - treat this as a statement.
- Value Description - A description that links the issue to the value the customer receives when the product is delivering for them.
- Owner - Internal company owner of the issue
- Next Step - The immediate next step to be taken on the issue
- Status - Status of the issue; example Status gates could include Reported, Discovery, Dev, Implementation, Complete
- Complete? - Yes for when the issue is complete.
- Email Customer - Link an email to the customer owner for the issue.

*A note on making the best of a frustrated customer*:

The confluence of development, sales, implementation and support will certainly create confusion and friction. To a certain extent this is unavoidable but still leads to dissatisfied customers. We believe customer dissatisfaction should be seen as an opportunity.

- Seek first to understand - but vocalize your intent. Be sure to give customers the space to share their frustrations without interruption. This probably means hearing things you know are incorrect. Don't worry, you can address that later. Stepping in to correct in that moment risks shutting down the conversation all together. The customer will still share their frustration, but next time it won't be with you but with a competitor.
- Be careful with promises. Most people's default response to hearing about broken things is to start to fix them or commit to a timeline to solve them. It is easy to let the urgency of the complaint cause a hasty promise, but the key to delivering a true resolution to the customer is knowing the context of the issue and what is required to truly resolve it. Instead, Golden Section recommends making a list of needs and committing to review the list with your team.
- Focus on value rather than the issues. Frustrated B2B SaaS customers come to you with issues, typically in the form of feature requests or bugs. These frustrations can also be seen as symptoms of the root cause: lack of value. To achieve a value-based approach, we recommend the following order of activities to create an achievable definition of success. Rather than allow a customer to create a laundry list of issues that aren't accretive to the value of the system, your conversations will be focused on delivering improved value.

1. Spend some time thinking through the value the customer was expecting.
2. Look at whether the main source of frustration is aware of that value promise.
3. Engage the customer in a value conversation to resell the value promise.
4. Invite the customer to share with you the current status of the value received.
5. Create a framework with the customer to track the value going forward.
6. After focusing on the value, engage the customer on the list of issues.
7. Follow-up! Set a cadence on meetings internally and with the client, and do not be afraid to engage the customer on a pushed deadline. This happens in business. When a customer's issue is pushed back, hopefully it is because something else that also benefits them took precedence. In the rare case that it does not, it is still best to proactively engage them with the news with no ambiguities.

<!-- GS:LINKS start — generated by scripts/build.mjs, do not edit by hand -->

---

**Prevents** · [#59 No customer support](../../MISTAKES.md#m059) · [#60 Not using a support ticket system](../../MISTAKES.md#m060) · [#61 Not having a knowledge base for customer issues](../../MISTAKES.md#m061) · [#63 Building your own support tools](../../MISTAKES.md#m063)

**Templates** · [Support Ticket System Template](../../templates/4.30-support-ticket-system-template.xlsx)

**Category** · [Operations](../README.md) · **Effort** · 13 SP initial, 8 SP ongoing · **Cadence** · Monthly

<!-- GS:LINKS end -->
