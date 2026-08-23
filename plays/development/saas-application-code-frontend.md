---
order: 53
slug: saas-application-code-frontend
anchor: app-code-frontend
title: Application Code & Front End
h1: How to Structure Application Code and Front End for SaaS
category: development
players: CTO, Engineering Lead
initialEffort: 34 SP
ongoingEffort: 13 SP
frequency: Continuous
stage: Pre-Revenue
templates:
  - file: 5.41-application-code-front-end-template.xlsx
    name: Application Code & Front End Template
summary: Establish standards and practices for application code quality, architecture, and front-end user experience—ensuring maintainability and customer delight.
keywords:
  - application architecture
  - code quality
  - frontend development
  - UI/UX
  - web frameworks
  - code maintainability
  - technical debt
questions:
  - What architecture patterns work best for SaaS?
  - How do I audit my application code and front end for weaknesses?
  - How do I improve my product's UX and UI?
  - How should I monitor application performance?
  - What code standards should my team follow?
preventsMistakes:
  - 12
  - 157
---
If the Database level is the bottom layer of your technology, the Application Code, or the Business Logic Layer, is the middle tier. The top tier is your Front End, or UX and UI.

> **The Goal:** Identify and address performance issues in your Business Logic and Front End.

#### Background

*Best Practices in Business Logic:*

Golden Section recommends adopting a "modular," Microservices architecture design as opposed to a monolithic design, which often causes features to break each other. Unlike monolithic architecture, Microservices are fine-grained and lightweight, easy to maintain, and more modular. This style is more elastic and resilient.

Specifically, Microservices is an approach to software development in which a large application is built as a suite of modular services; small, independently versioned, and scalable customer-focused services with specific business goals, which communicate with each other over standard protocols with well-defined interfaces.

Microservices solve challenges of rigid systems by being as modular as possible. They help build an application as a suite of small services, each running in its own process and are independently deployable. These services may be written in different languages and may use different data storage techniques. Microservice results in the development of systems that are scalable and flexible.

*Best Practices in Front End / UX and UI:*

The front end is how your customer interacts with your product, and the ease of interaction dictates their experience. UX and UI design are two different elements of a single consumer experience: UX refers to the user experience, which focuses on how something works and how people interact with it, while UI, or user interface, focus on the look and layout.

User Experience Design is the process of manipulating user behavior with a product by using data to inform the design process and continual updates to the usability, accessibility, and desirability provided in the interaction with a product.

Software is HumanWare. UX design is not an afterthought of software engineering. It is fundamental for your software's success and adoption.

- Golden Section always recommends using a User Interaction designer to play and optimize the UI prior to it actually being developed.
- A great UX design team engages and empathizes with users to understand their experiences and motivations.
- Design your UI to be responsive. The responsive UI design is a design concept in which a website displays the same content on all devices. However, the content is styled differently depending on the available space. Good responsive design will make a big improvement on the user experience.
- Consider your navigation trees: make sure they are not overly complex with multiple levels. This complexity makes using your product difficult for untrained users.
- Always make the Search feature prominent and easy to find.

*Best Practices in Code Quality:*

- Establish a coding style, which is a set of rules or guidelines used when writing the source code for a computer program. Golden Section believes following a particular programming style helps programmers read and understand source code conforming to that style and prevents errors from being introduced.
- Establish a Code Quality Review Process, leveraging a tool like SonarQube to assist. SonarQube can quickly generate reports covering code quality issues such as reliability issues, security issues, maintainability issues and code duplications.
- For source code management and documentation, GitHub is a popular platform for developers to collaborate and track progress. Golden Section also recommends using various 3rd party integration (i.e. Slack, CircleCI, Marker.IO) together to streamline the development flow.

*Best Practices in Application Performance:*

- Establish an App Performance measurement (Apex). Golden Section recommends using the right standard Apex measurement. Application Performance is estimated in terms of accuracy, efficiency, and speed of execution.
- There are many tools that provide performance monitoring. Golden Section recommends leveraging tools like New Relic's analytics for application performance monitoring (APM). New Relic delivers real-time and trending data about your web application's performance and the level of satisfaction that your end-users experience.

#### Steps:

1. Given the background and best practices listed above, what aspects of your Business Logic and Front End process need to be improved?
    - Do you have microservices designed in your software? If so, can you describe what each microservice does and how they interact with each other?
    - Do you have a UI/UX designer working on your software? If so, please describe your UI/UX design process and how it's embedded in the dev process?
    - Is your software responsive on the following devices: desktop, mobile phones, tablets?
    - Can you describe what tools or standards you use to ensure your coding style and quality?
    - Have you performed any performance test for your software? If so, can you describe the tool, the procedure, and the result?
2. Create an actionable plan to address any improvements that need to occur.

<!-- GS:LINKS start — generated by scripts/build.mjs, do not edit by hand -->

---

**Prevents** · [#12 Wrong programing language](../../MISTAKES.md#m012) · [#157 Overbuilding Function, Underbuilding Form](../../MISTAKES.md#m157)

**Templates** · [Application Code & Front End Template](../../templates/5.41-application-code-front-end-template.xlsx)

**Category** · [Development](../README.md) · **Effort** · 34 SP initial, 13 SP ongoing · **Cadence** · Continuous

<!-- GS:LINKS end -->
