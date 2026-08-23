---
order: 51
slug: saas-product-engineering-process
anchor: product-engineering
title: Product Engineering Process
h1: How to Run a Product Engineering Process for B2B SaaS
category: development
players: CTO, Engineering Lead
initialEffort: 34 SP
ongoingEffort: 13 SP
frequency: Continuous
stage: Pre-Revenue
templates:
  - file: 5.30-product-engineering-process-template.xlsx
    name: Product Engineering Process Template
summary: Establish product engineering practices—sprint discipline, code review, testing, CI/CD—that ensure quality, speed, and predictability in feature delivery.
keywords:
  - software development
  - agile methodology
  - code quality
  - deployment
  - testing
  - continuous integration
  - development practices
questions:
  - How should I structure my development process?
  - What practices ensure code quality?
  - How long should each sprint last?
  - What sprint metrics should I track?
  - How should I manage version control and branching?
preventsMistakes:
  - 25
  - 26
  - 29
  - 30
  - 31
  - 120
---
As mentioned in the Play: Product Management Process, the Product Management team works in conjunction with the Product Engineering team. While the Product Management team focuses on building the right thing, the Product Engineering team is responsible for building the thing right. There are two elements to building the thing right: Process and Engineering. We will discuss proper Product Engineering process in this play.

> **The Goal**: Establish a comprehensive and effective process to optimize your company's delivery of the right products for your customers.

#### Background

*Release Cycle Overview*

The development process is divided into releases. A release cycle starts from a previous stable release and plan. Releases are achieved by a Scrum process, an iteration-based agile development process. Each release is broken into Sprints. A Sprint is the basic unit of development in Scrum. The Sprint is a timeboxed effort; that is, it is restricted to a specific duration.

Each Sprint starts with a Sprint Planning event that aims to: define a Sprint Backlog, identify the work for the Sprint, and make an estimated commitment for the Sprint goal. At the beginning of a Sprint, the Scrum Team holds a Sprint Planning event to communicate the scope of work that is intended to be done during that Sprint. During the first half, the whole Scrum Team (Development Team, Scrum Master, and Product Owner) selects the Product Backlog Items that might be achievable in that Sprint.

During the second half, the Development Team decomposes the work items (tasks) required to deliver those Product Backlog Items, resulting in a confirmed Sprint Backlog. Once the Development Team prepares the Sprint Backlog, they commit (usually by voting) to deliver tasks within the Sprint. During daily development, code is committed to the code repository. Before code is committed, it will be peer reviewed and team reviewed.

Each Sprint ends with a Sprint Review and Sprint Retrospective that reviews progress to show to stakeholders and identify lessons and improvements for the next Sprints. Scrum emphasizes having a completed working product at the end of each Sprint. During each sprint, the code is fully integrated, tested and documented.

Benefits of maintaining a disciplined Sprint Process:

- Incremental approach breaks complex software modules down into simpler mini-features
- Accommodates change easily
- Improves ROI through frequent and regular delivery of value to the business
- Increased visibility (progress, obstacles, risks, etc.)
- Shorter cycles produce working software and incremental product quickly
- Progress measured by running tested software
- Early and regular process improvement driven by frequent inspection
- Solves the common problem of a user not knowing what they want until after they see an initial version of the software.

*Best Practices in the Sprint Process*

- Maintain a set Sprint rhythm and discipline.
- Golden Section recommends each Sprint last 2-4 weeks.
- Always start a Sprint with ready-to-go user stories (produced by the Product Management team)
- Break each user story into the smallest sizes
- Ensure no dependencies exist in the current Sprint's user stories
- Be diligent at assigning user story size (either Fibonacci sequence or T- Shirt size) to maintain the momentum and accountability that defines the Sprint process
- To that end, close out a Sprint when the timebox is met, regardless of whether the user story is finished
- Establish Sprint Metrics and then monitor them. Potential Sprint Metrics include:
    - User Story Points per Sprint
    - Successful Sprints ratio (met when finished all user stories set for that Sprint)
    - Defects per release
    - Release defects per KLOC
    - Pre-release defects per KLOC
    - $Cost per KLOC
    - Production Defects Fixed Efficiency (within 48 hours)
    - Engineer Hours per KLOC

*Best Practices in Version Control*

GitHub is generally used for Version Control efforts. Version Control Process should include:

- Code is maintained by trunk and branch. A trunk is used for stable, versioned releases, while branch is for rapid, small releases.
- Codes are reconciled between trunk and branch
- Unit Testing, Automated Build and Continuous Integration processes are in place for each build and release
- Quick-Fix Engineering (QFE) is conducted on trunk to deal with defects in between releases.

*Best Practices in QA Process*

Golden Section recommends establishing a rigorous quality assurance process for your software that includes:

- All code is unit-tested before being committed to the version control server.
- Automated Build and Continuous Integration processes are in place for each build and release.
- Fully leverage available DevOps and CI/CD tools and process.
- Utilizing these tools will help your company accelerate application development and development lifecycles, building quality and consistency into the automated build and release process, and increase your release frequency while reducing defects.
*Best Practices in Configuration Management (CM)*

- All Production configuration changes go through a change control
- All configuration changes are tracked, tested, and documented
- A Roll-back Contingency Plan is in place in the case of unforeseen outcomes

#### Steps

1\. There are many elements necessary to build an executable, successful process to guide your Product Engineering Group. Using the Best Practices above and the PDCA methodology detailed in the Play: Quality Management Systems, create the standards and expectations that will guide your Product Engineering Group's delivery process.

<!-- GS:LINKS start — generated by scripts/build.mjs, do not edit by hand -->

---

**Prevents** · [#25 Breaking tech sprints](../../MISTAKES.md#m025) · [#26 All in-house tech team](../../MISTAKES.md#m026) · [#29 Obsession with full-stack engineers](../../MISTAKES.md#m029) · [#30 Outsourcing core product with off the shelf](../../MISTAKES.md#m030) · [#31 Not engineering for scale](../../MISTAKES.md#m031) · [#120 Not forcing engineers to QA their own submissions](../../MISTAKES.md#m120)

**Templates** · [Product Engineering Process Template](../../templates/5.30-product-engineering-process-template.xlsx)

**Category** · [Development](../README.md) · **Effort** · 34 SP initial, 13 SP ongoing · **Cadence** · Continuous

<!-- GS:LINKS end -->
