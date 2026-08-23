---
order: 58
slug: saas-product-documentation
anchor: product-documentation
title: Product Level Documentation
h1: How to Build Product-Level Documentation for B2B SaaS
category: development
players: Product Manager
initialEffort: 13 SP
ongoingEffort: 8 SP
frequency: Quarterly
stage: Early Traction
templates:
  - file: 5.61-product-level-documentation-template.xlsx
    name: Product Level Documentation Template
summary: Create comprehensive product-level documentation—requirements, technical design, user manuals, quality plans, and API docs—to codify internal knowledge and prepare for your next equity round.
keywords:
  - product documentation
  - user guides
  - help center
  - knowledge base
  - API documentation
  - tutorial videos
  - customer support documentation
questions:
  - What product documentation should I create?
  - How much documentation is enough?
  - How do I keep product documentation current?
  - Who should own product documentation?
  - What goes into a Quality Management Plan?
preventsMistakes:
  - 61
---
Product Level Documentation exists to explain product functionality, unify project-related information, and allow for the discussion of all significant questions that arise between stakeholders and developers. In general, product documentation includes requirements, tech specifications, business logic and manuals.

> **The goal**: Establish a robust set of documentation surrounding your product to codify internal knowledge and processes and in preparation to share this documentation in the next equity round.

#### Best Practices

*Write just enough documentation*: There is a middle ground between no documentation and too much documentation. Golden Section recommends you find that middle ground and document only the necessary and relevant information.

*Consider documentation as an ongoing process*. Set a process for keeping your documentation up-to-date so that it doesn't become stale and useless. Consider automatic version control to manage the updating process.

*Treat documentation as a collaborative effort*. While one person should be responsible for the documentation, the products of the documentation process should be created by the team.

#### Components of Product Documentation:

*Requirements Specifications Document:* this document outlines the product you have built, including its purpose, features, functionalities, and behavior. It is typically created with input from both your operational and technical teams to align the company on the purpose of the product you have created. It includes such details as how this product fits into the company's objectives, the technical, business and user assumptions the company has made, use cases, and what the product will not be.

*Technical Design Document*: this should include the main architectural decisions, including a software design document, architecture and design principles, user stories, and a diagrammatic representation of the solution.

*Development Plan / Product Roadmap:* Reference Play: Product Roadmap

*User Manual:* this is a user guide to teach the people using your product how to properly use the system. You will likely include workflows, processes, descriptions of features, and a troubleshooting guide. The more thorough this document is the fewer support calls you will have.

*Installation and Maintenance Manual*: this manual describes the requirements and workflow to properly install and maintain your product.

*Quality Management Plan*: this is an analog of a requirement document dedicated to testing. This document sets the required standard for product quality and describes the methods to achieve this level. The plan helps to schedule QA tasks and manage testing activity for product managers, but, it is mainly used for large-scale projects. The Quality Management plan includes:

- *Test Strategy*: this is a document that describes the software testing approach to achieve testing objectives. This document includes information about team structure and resource needs along with what should be prioritized during testing. A test strategy is usually static as the strategy is defined for the entire development scope.
- *Test Cases*: a detailed list of the actions required to verify each feature / functionality of a product.
- *Test Case Specifications*: this document is a set of detailed actions to verify each feature or functionality of a product. Usually, a QA team writes a separate specifications document for each product unit. Test case specifications are based on the approach outlined in the test plan. A good practice is to simplify specifications descriptions and avoid test case repetitions.
- *Test Checklist*: a list of tests that should be run at a particular time. It represents what tests are completed and how many have failed. All points in the test checklists should be defined correctly. Try to group test points in the checklists. This approach will help you keep track of them during your work and not lose any. If it helps testers to check the app correctly, you can add comments to your points on the list.
- *Test Plan*: this document is typically one to two pages that describes what should be tested during any specific test. This plan includes: a list of features being tested, testing methods, the time frame, and the roles and responsibilities of those involved.

*API Documentation:* Nearly any product has its APIs or Application Programming Interfaces. Their documentation informs developers how to effectively use and connect to the required APIs. API documentation is a deliverable produced by technical writers as tutorials and guides. This type of documentation should also contain the list of all available APIs with specs for each one.

*Standards:* The section on standards should include all coding and UX standards that the team adheres to along the project's progression.

#### Steps

1. Many of these processes have already been put in place and plans created. Here we want to ensure proper documentation of your work. Use the template provided to judge the codification of your product documentation. Working with your Product Manager, answer whether each component of documentation is currently in place and related details.
2. For components not in place, task your Product Manager and team as necessary to put those components in place.

<!-- GS:LINKS start — generated by scripts/build.mjs, do not edit by hand -->

---

**Prevents** · [#61 Not having a knowledge base for customer issues](../../MISTAKES.md#m061)

**Templates** · [Product Level Documentation Template](../../templates/5.61-product-level-documentation-template.xlsx)

**Category** · [Development](../README.md) · **Effort** · 13 SP initial, 8 SP ongoing · **Cadence** · Quarterly

<!-- GS:LINKS end -->
