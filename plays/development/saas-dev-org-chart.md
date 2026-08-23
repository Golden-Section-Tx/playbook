---
order: 61
slug: saas-dev-org-chart
anchor: dev-org-chart
title: Dev Org Chart
h1: How to Structure a SaaS Development Organization
category: development
players: CTO, Founder
initialEffort: 5 SP
ongoingEffort: 3 SP
frequency: Quarterly
stage: Growth
templates:
  - file: 5.70-dev-org-chart-template.xlsx
    name: Dev Org Chart Template
summary: Design an engineering organization structure—defining roles (product manager, BA, tech lead, engineers, QA), team organization, and reporting lines—that scales with growth.
keywords:
  - engineering team
  - tech team structure
  - CTO role
  - developer hiring
  - engineering hiring
  - tech leadership
  - team scaling
questions:
  - What roles make up a SaaS development team?
  - Which organizational structure is right for my dev team?
  - What's the difference between a Business Analyst and a QA engineer?
  - Should I outsource software development?
  - How do I clarify roles and accountability on my dev team?
preventsMistakes:
  - 26
  - 27
  - 28
  - 29
  - 108
  - 154
---
A dev team consists of dedicated professionals who can develop, test, and deploy a Story, Feature, or component. The team typically includes software developers and testers, engineers, and other dedicated specialists required to complete a vertical slice of functionality.

> **The goal**: Create a scalable, clear and accountable development organization that can hit cost and time targets and communicate clearly to the rest of the organization.

#### Background

A development team is typically comprised of the following roles: Product Manager, Business Analyst (BA), Technical Team Lead (TTL), UX/UI Engineer, Business Logics Engineer, Web Services and Microservices Engineer, Database Engineer, Quality Assurance Engineer (QA), and Software Architect.

*Product Manager:* A Product Manager is responsible for guiding the success of a product and leading the cross-functional team that is responsible for improving it. It is an important organizational role --- especially in technology companies --- that sets the strategy, roadmap, and feature definition for a product or product line.

Generally, a Product Manager's responsibilities include:

- Leading the product team (not necessarily the engineers)
- Prioritizing projects and tasks
- Allocate resources
- Keep product and project on schedule
- Maintain communication with company's operational teams

*Business Analyst*: A BA is someone who analyzes user workflow, translates user needs into software user stories, and makes user stories ready for development. A BA's output is the engineers' input. High-quality BA output is a prerequisite for efficient and effective development.

Generally a BA's responsibilities include:

- Analyze requirement and user workflow
- Write user stories
- Create related project documents
- Communicate with client
- Work with developers
- Validate development against user stories

A BA's job is to make sure you build the right thing, QA's job is to make sure you build the thing right!

*Quality Assurance Engineer:* A QA is someone who tests all aspects of product quality, including functionality, usability, performance and security. In DevOps, a QA is generally involved in the entire project development lifecycle so he can guide the product quality.

Generally, a QA's responsibilities include:

- Create comprehensive, well-structured test plans and test cases
- Design and implement quality testing activities
- Define and coordinate corrective actions
- Track quality assurance metrics

*Technical Team Lead:* A TTL is someone who manages the engineers to accomplish the product vision as outlined by the Product Manager to the specifications outlined in the user stories by the BA.

Generally, a TTL's responsibilities include:

- Provide input in the Sprint Planning and Sprint Retrospective meetings
- Provide feedback for estimation and quality of user stories by BA
- Run daily standup meetings with engineers
- Solve and own all roadblocks observed by engineers

*UX/UI Engineer, Business Logics Engineer, Web Services and Microservices Engineer, and Database Engineer:* The engineers on a development team will vary with the specifications of the product required. But they should always work for a technical team lead and be responsible to build what the BA has specified. This tight process ensures that the output can be verified by the QA and the product creation process smoothed out over time. Errors ought to be attributed to either: 1) faulty requirements that didn't meet customer objectives, 2) miscommunication from customer to BA, 3) miscommunication from BA to engineers on user story (i.e. bad user story), or 4) engineer not accomplishing user story, or 5) QA missing a non-conforming user story output.

*Software Architect*: A Software Architect designs and develops the software ecosystem.

Generally, a Software Architect's responsibilities include:

- Ensuring systems integration and interoperability
- Overseeing the database design
- Overseeing middle-tier business logic
- Overseeing the UI and front-end development

*A note on outsourcing*: Software outsourcing is an arrangement made by a business to hire a third party software contractor to do the software related work that could have been done in-house. But, developing a complete software application in-house demands both money as well as time. Once you start your outsourced software project with your provider, the last thing you want is for the outsourcing partnership to deteriorate into an order-taking relationship with developers who only do what they're told. When processes backslide, innovation is back-burned and continuous improvement is forgotten, you've officially arrived at low-performance outsourcing.

High-performance outsourcing requires consistent attention, assessment, and enhancement to remain optimized. Golden Section recommends using a partner like Golden Section to help navigate an engagement and find the right team for your company. Golden Section provides periodic engagement review with you and your development partner to manage expectations, ensure that milestones are achieved as scheduled and that your software is stable and scalable throughout the life of your software engagement. Potential issues should be identified and addressed before they become real problems that put your software at risk.

**Different organizational structures:**

#### Technical Product Owner Org Structure

This structure is meaningful when the product owner is technical and the product is technical by nature. It preserves the function of the engineering roles to execute what the product owner specifies and ensures accountability of what to build and whether it achieves goals within the product owner's purview. The weaknesses are that the TTL and product owner will need an extremely good working relationship to avoid downstream negative effects.

#### Customer Responsive UI Led Product Organization

This structure works for products that require rapid and meaningful customer engagement in the UI/UX of the product. It allows for better and more meaningful engineering tasks which will likely include UI with the user story. The QA is shown as its own vertical but could easily be within the TTL's organization for smaller teams. The weakness here is speed of communicating to the engineering group. This structure, despite providing flexibility to customers, needs to be monitored closely to ensure customer approvals occur quick enough to feed the engineering organization with input for productive work.

#### TTL-centric Engineering Driven Product Organization

This structure works well for products that are relatively simple in specification. Product owners are required to submit vision to the TTL and work with the BA directly. However, the BA reports to the TTL. This matrix allows the entire engineering function to work under the guidance of the TTL and for the TTL to be responsible to execute the vision the product owner specifies. This can breakdown on complex products where the product owner's vision isn't clearly specified enough, leading to incorrect outputs from the TTL's process.

*Note on organizational structure:* product organizational structures can accommodate a lot of complexities. There isn't one right answer for a product or team, but it is worth considering the roles, inputs, and accountability structure to ensure that there are clear lines.

#### Steps

1. Create a Team Responsibility Accountability Consulted Informed (RACI) Chart for your dev team. This chart will define the responsibility each role will take on and help facilitate effective communication.
2. Fill out the roles for your organization with at least one name in each role (at the early stage it is okay to have one person listed multiple times).

<!-- GS:LINKS start — generated by scripts/build.mjs, do not edit by hand -->

---

**Prevents** · [#26 All in-house tech team](../../MISTAKES.md#m026) · [#27 Overpaying for tech resources](../../MISTAKES.md#m027) · [#28 Non-technical people hiring technical people](../../MISTAKES.md#m028) · [#29 Obsession with full-stack engineers](../../MISTAKES.md#m029) · [#108 Fuzzy organizational chart](../../MISTAKES.md#m108) · [#154 Revolving Door of Technical Talent](../../MISTAKES.md#m154)

**Templates** · [Dev Org Chart Template](../../templates/5.70-dev-org-chart-template.xlsx)

**Category** · [Development](../README.md) · **Effort** · 5 SP initial, 3 SP ongoing · **Cadence** · Quarterly

<!-- GS:LINKS end -->
