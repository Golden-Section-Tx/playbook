---
order: 52
slug: saas-database-selection
anchor: database-selection
title: Database Selection
h1: How to Choose a Database for a B2B SaaS Product
category: development
players: CTO, Engineering Lead
initialEffort: 21 SP
ongoingEffort: 5 SP
frequency: As Needed
stage: Pre-Revenue
templates:
  - file: 5.40-database-selection-template.xlsx
    name: Database Selection Template
summary: Choose a database technology (SQL, NoSQL, etc.) that matches your product requirements for consistency, scale, query patterns, and operational simplicity.
keywords:
  - database selection
  - SQL
  - NoSQL
  - PostgreSQL
  - MongoDB
  - database scaling
  - data architecture
  - database performance
questions:
  - Should I use a SQL or NoSQL database?
  - What databases work best for SaaS?
  - How do I decide which database best fits my needs?
  - What database management best practices should I follow?
  - What's the cost impact of database choice?
preventsMistakes:
  - 2
  - 9
  - 12
format: html
---
<p>With a process in place to ensure your dev team is building the thing right, attention now needs to be paid to ensuring your company is utilizing the proper technology. Database selection is a key technical decision. The database is foundational to your technology and can cause serious issues if not chosen well.</p>
<p class="goal-callout"><strong>The Goal:</strong> Systematically decide which database best serves your company's needs and priorities.</p>
<h4>Background</h4>
<p><em>Best Practices in Database Management:</em></p>
<ul><li>Allow Multi-tenant Architecture at the database level</li><li>Do not allow multiple databases on a single customer (opposite of Multitenancy)</li><li>Streamlined Database Schema to simplify each release</li><li>Locate business logics on Web Services layer (i.e. code level) instead of Database level to reduce complexity in version updates.</li><li>Prioritize reducing Technical Debt in the Database Level. This improves the database performance and prevents data from being accumulated in the wrong structure, which would make future clean-up and migration extremely difficult</li></ul>
<p><em>Golden Section's Pros and Cons for Popular Databases:</em></p>
<h4>Oracle 12c</h4>
<p>Ideal for: Large organizations that handle enormous databases and need a variety of features.</p>
<h4>Pros</h4>
<ul><li>You'll find the latest innovations and features coming from their products since Oracle tends to set the bar for other database management tools.</li></ul>
<ul><li>Oracle database management tools are also incredibly robust, and you can find one that can do just about anything you can possibly think of.</li></ul>
<h4>Cons</h4>
<ul><li>The cost of Oracle can be prohibitive, especially for smaller organizations.</li><li>The system can require significant resources once installed, so hardware upgrades may be required to even implement Oracle.</li></ul>
<h4>MySQL</h4>
<p>MySQL is one of the most popular databases for web-based applications. It's freeware, but it is frequently updated with features and security improvements.</p>
<p>Ideal for: Organizations that need a robust database management tool but are on a budget.</p>
<p>This database engine allows you to select from a variety of storage engines that enable you to change the functionality of the tool and handle data from different table types. It also has an easy to use interface, and batch commands let you process enormous amounts of data. The system is also incredibly reliable and doesn't tend to hog resources.</p>
<h4>Pros</h4>
<ul><li>It's free.</li><li>It offers a lot of functionality even for a free database engine.</li><li>There are a variety of user interfaces that can be implemented.</li><li>It can be made to work with other databases, including DB2 and Oracle.</li></ul>
<h4>Cons</h4>
<ul><li>You may spend a lot of time and effort to get MySQL to do things that other systems do automatically, like create incremental backups.</li><li>There is no built-in support for XML or OLAP.</li><li>Support is available for the free version, but you'll need to pay for it.</li></ul>
<h4>Microsoft SQL Server</h4>
<p>Ideal for: Large organizations that use a number of Microsoft products.</p>
<h4>Pros</h4>
<ul><li>It is very fast and stable.</li><li>The engine offers the ability to adjust and track performance levels, which can reduce resource use.</li><li>You are able to access visualizations on mobile devices.</li><li>It works very well with other Microsoft products.</li></ul>
<h4>Cons</h4>
<ul><li>Enterprise pricing may be beyond what many organizations can afford.</li><li>Even with performance tuning, Microsoft SQL Server can gobble resources.</li><li>Many individuals have issues using the SQL Server Integration Services to import files.</li></ul>
<h4>PostgreSQL</h4>
<p>Ideal for: Organizations with a limited budget that want the ability to select their interface and use JSON.</p>
<p>This database management engine can be hosted in a number of environments, including virtual, physical and cloud-based environments. The latest version, PostgreSQL 9.5, offers larger data volumes and an increase in the number of concurrent users. Security has also been improved thanks to support for both DBMS\_SESSION and expanded password profiles.</p>
<h4>Pros</h4>
<ul><li>This database management engine is scalable and can handle terabytes of data.</li><li>It supports JSON.</li><li>There are a variety of predefined functions.</li><li>A number of interfaces are available.</li></ul>
<h4>Cons</h4>
<ul><li>Documentation can be spotty, so you may find yourself searching online in an effort to figure out how to do something.</li><li>Configuration can be confusing.</li><li>Speed may suffer during large bulk operations or read queries.</li></ul>
<h4>MongoDB</h4>
<p>MongoDB is designed for applications that use both structured and unstructured data. The database engine is very versatile. There is a comprehensive selection of drivers available, so it's easy to find a driver that will work with the programming language being used.</p>
<p>Since MongoDB wasn't designed to handle relational data models, even though it can, performance issues are likely to crop up if you attempt to use it this way.</p>
<h4>Pros</h4>
<ul><li>It's fast and easy to use.</li><li>The engine supports JSON and other NoSQL documents.</li><li>Data of any structure can be stored and accessed quickly and easily.</li><li>Schema can be written without downtime.</li></ul>
<h4>Cons</h4>
<ul><li>SQL is not used as a query language.</li><li>Tools to translate SQL to MongoDB queries are available, but they add an extra step to using the engine.</li><li>Setup can be a lengthy process.</li><li>Default settings are not secure.</li></ul>
<h4>Steps</h4>
<ol><li>Identify selection criteria. Use the template provided to identify the 5-6 factors that are most important to your company. It is unlikely one database can answer all your needs, so the priorities you identify will drive the decision.</li><li>Identify a database shortlist. Using Golden Section's list of popular databases above, choose 3-4 databases you want to evaluate.</li></ol>
<ol><li>Enter your identified selection criteria and database shortlist into the template provided.</li><li>Research whether each database on your shortlist meets the selection factor. For factors that don't lend themselves to a simple "meet" or "does not meet," you can rank to what degree the factor meets your needs (i.e. 5 = closely meets, 1 = does not meet).</li><li>Upon completion of your decision matrix, choose the database that best meets your needs and priorities.</li><li><strong>Technical Debt:</strong> Work with your dev team to identify and then mitigate sources of Technical Debt in your Database Level.</li></ol>

<!-- GS:LINKS start — generated by scripts/build.mjs, do not edit by hand -->

---

**Prevents** · [#2 Letting logic get into the database](../../MISTAKES.md#m002) · [#9 Building for single tenancy](../../MISTAKES.md#m009) · [#12 Wrong programing language](../../MISTAKES.md#m012)

**Templates** · [Database Selection Template](../../templates/5.40-database-selection-template.xlsx)

**Category** · [Development](../README.md) · **Effort** · 21 SP initial, 5 SP ongoing · **Cadence** · As Needed

<!-- GS:LINKS end -->
