---
order: 46
slug: saas-sla-hosting-support
anchor: sla-hosting-support
title: SLA Hosting & Support
h1: How to Set SLAs for Hosting and Support
category: operations
players: CTO, COO
initialEffort: 8 SP
ongoingEffort: 5 SP
frequency: Annual
stage: Growth
templates:
  - file: 4.32-sla-hosting-support-template.xlsx
    name: SLA Hosting & Support Template
summary: Define clear Service Level Agreements that commit to uptime, support response times, and support hours—setting customer expectations and establishing operational targets.
keywords:
  - SLA
  - service level agreement
  - uptime
  - support SLA
  - customer commitments
  - hosting reliability
  - SLA penalties
questions:
  - What uptime SLA should I commit to?
  - What components should a Service Level Agreement include?
  - What penalty structures for SLA breaches make sense?
  - How is downtime typically defined in an SLA?
  - How does an SLA protect my company in a customer dispute?
preventsMistakes:
  - 64
---
As a company, you contractually commit yourself to a minimum level of service standards when signing a Service Level Agreement. An SLA establishes service performance standards to which your company must conform. There are additional aspects of an SLA, including KPIs to measure compliance with set performance standards, timeframes for resolving hosting issues, and compensation agreements if performance standards are not met.

**The Impact:** A strong SLA clearly states the service expectations a customer can have for your company, preventing future disagreements. It also protects your company if a dispute does occur by outlining what the performance expectations are, exceptions to these commitments, and limits to compensation.

> **The Goal:** Understand the implications of the common components of an SLA and decide the maximum service specifications to which your company can contractually commit.

#### Background

#### Components of a Service Level Agreement

1. *Basic Service Specifications.* Outlines the services that your company provides with precise specifications. For example, your SLA may state that you provide "certain online tools to perform all account and server management tasks." The basic service specifications should also include a clear delineation of company and customer responsibilities. Finally, it will granularly outline the support your company will provide to maintain the service (i.e. network connectivity, server availability, maintenance, storage, data integrity, etc.)
2. *Desired Performance Levels.* The SLA will clearly set the minimum performance level in regards to service availability, frequency of disruptions, downtime, service request responsiveness, etc.
3. *Monitoring Process*. The exact monitoring process will be outlined for monitoring performance levels.
4. *Reporting Process*: The process which a customer follows to report issues, along with contractual response times, will be included. This is an important aspect of the SLA for your company to outline to protect yourself in case of disputes.
5. *Compensation*: Finally, a SLA will set contractual compensation due to the customer in the case your company fails to meet the set performance standards.

#### Steps

With the help of your legal counsel, draft the maximum service standards to which your company can commit. Using these, your company can draft a standard SLA with fallback provisions without committing yourself to an unachievable standard.

Key Clauses to consider(https://hostadvice.com/blog/the-importance-of-a-good-web-hosting-service-level-agreement-sla-when-choosing-a-hosting-service/):

1. Uptime Percentage. An uptime percentage standard will be set in the SLA. Typically, the standard is 99.8% - 99.999%. An uptime percentage of 99.999% ("five 9s") translates to a marginal service downtime of 5.26 minutes per year, or roughly 6 seconds per week. No one truly attains that standard, and that is important to point out in SLA negotiations. Providers attain that standard through the definition of "downtime." Downtime refers to the amount of time a customer can't access your product due to network or service failure but does not include the time required to perform scheduled or emergency maintenance. Thus, some SLAs will include a term that allows a planned maintenance event to be called within 1 hour of downtime so that the time will no longer be counted as a network or service failure and will not be counted against your uptime percentage.
2. Response time. The maximum amount of time that can pass before a representative from your company must respond to a support request.
3. Backup and Restoration. This clause will mandate how frequently data backups must occur and how fast data needs to be restored afterwards.
4. SLA Compensation or Credits. This sets the maximum compensation a customer can get from your company for performance outside the standards set in the SLA. We have seen SLAs that require any compensation to be requested in a short time frame (e.g. the month following the month in which the metric was not met) and limited to a certain percentage of the monthly subscription fee.

<!-- GS:LINKS start — generated by scripts/build.mjs, do not edit by hand -->

---

**Prevents** · [#64 Customer favorable SLA when not an absolute requirement](../../MISTAKES.md#m064)

**Templates** · [SLA Hosting & Support Template](../../templates/4.32-sla-hosting-support-template.xlsx)

**Category** · [Operations](../README.md) · **Effort** · 8 SP initial, 5 SP ongoing · **Cadence** · Annual

<!-- GS:LINKS end -->
