---
order: 54
slug: saas-cloud-infrastructure
anchor: cloud-infrastructure
title: Cloud & Server Infrastructure
h1: How to Set Up Cloud and Server Infrastructure for B2B SaaS
category: development
players: CTO, DevOps
initialEffort: 21 SP
ongoingEffort: 8 SP
frequency: Quarterly
stage: Pre-Revenue
templates:
  - file: 5.42-cloud-server-infrastructure-template.xlsx
    name: Cloud & Server Infrastructure Template
summary: Plan cloud infrastructure for high availability, scalability, and backup/disaster recovery—assessing your current setup against best practices and creating a plan to close the gaps.
keywords:
  - cloud infrastructure
  - AWS
  - DevOps
  - infrastructure scaling
  - disaster recovery
  - cloud costs
  - availability and reliability
questions:
  - Why should I use cloud infrastructure instead of physical servers?
  - How do I architect for high availability?
  - How does autoscaling help my infrastructure handle changing demand?
  - How do I assess whether my current cloud setup needs improvement?
  - What disaster recovery strategy should I have?
preventsMistakes:
  - 9
  - 31
---
The decisions you make when setting up your server and cloud infrastructure affect your ability to maximize the efficiency of your software development and deployment.

> **The goal:** The infrastructure should be set up in a way that is cost efficient, performant and secure.

#### Background

Cloud Infrastructure is shared pools of configurable computer system resources and higher-level services that can be rapidly provisioned with minimal management effort, often over the Internet. Advocates note that it often allows companies to avoid or minimize up-front IT infrastructure costs. Cloud Infrastructure can be managed much more efficiently than traditional physical infrastructure, which typically requires that individual servers, storage, computational and networking components be procured and assembled to support an application. With cloud infrastructure, DevOps teams can deploy infrastructure programmatically, as part of an application's code.

There are three aspects of server design that we want to optimize: high availability, scalability, and backup / disaster recovery.

*High Availability*: a characteristic of a system which aims to ensure an agreed level of operational performance, usually uptime, for a higher than normal period. Availability refers to the ability of the user community to obtain a service or good or access the system, whether to submit new work, update or alter existing work, or collect the results of previous work. If a user cannot access the system, it is - from the users' point of view - unavailable. Generally, the term downtime is used to refer to periods when a system is unavailable. Modernization has resulted in an increased reliance on these systems. For example, hospitals and data centers require high availability of their systems to perform routine daily activities.

There are three principles of systems design in reliability engineering which can help achieve high availability.

1. Elimination of single points of failure. This means adding redundancy to the system so that the failure of a component does not mean failure of the entire system.
2. Reliable crossover. In redundant systems, the crossover point itself tends to become a single point of failure. Reliable systems must provide for reliable crossover.
3. Detection of failures as they occur. If the two principles above are observed, then a user may never see a failure -- but the maintenance activity must.

*Scalability / Auto-scaling*: Scalability in the context of cloud computing can be defined as the ability to handle growing or diminishing resources to meet business demands in a scalable way. In essence, scalability is a planned level of capacity that can grow or shrink as needed.

Autoscaling is a method used in cloud computing, whereby the number of computational resources in a server farm, typically measured in terms of the number of active servers, scales automatically based on the load on the farm. It is closely related to and builds upon, the idea of load balancing.

*Backup, Disaster Recovery Assessment*: Cloud-based backup and recovery solutions enable you to backup and restore your business-critical files in case they are compromised. The cloud technology enables efficient disaster recovery, regardless of the type or intensity of workloads. The data is stored in a secure cloud environment architected to provide high availability. The service is available on-demand, which enables organizations of different sizes to tailor DR solutions to their needs.

*Best Practices in Server / Cloud Infrastructure Design:*

- Always have both onsite and offsite backup in place
- Virtualize the server

#### Steps:

1. Given the background and best practices listed above, what aspects of your Cloud and Server infrastructure need to be improved?
    - Do you have your infrastructure designed to ensure high availability for your software? If yes, can you describe the details of your system design related to that?
    - With your current infrastructure configuration, is it scalable?
    - Do you have autoscaling configured?
    - Do you have backup and recovery mechanisms implemented? If yes, can you describe them?
2. Create an actionable plan to address the issues identified.

<!-- GS:LINKS start — generated by scripts/build.mjs, do not edit by hand -->

---

**Prevents** · [#9 Building for single tenancy](../../MISTAKES.md#m009) · [#31 Not engineering for scale](../../MISTAKES.md#m031)

**Templates** · [Cloud & Server Infrastructure Template](../../templates/5.42-cloud-server-infrastructure-template.xlsx)

**Category** · [Development](../README.md) · **Effort** · 21 SP initial, 8 SP ongoing · **Cadence** · Quarterly

<!-- GS:LINKS end -->
