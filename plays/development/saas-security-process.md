---
order: 55
slug: saas-security-process
anchor: security-process
title: Security Process
h1: How to Build a Security Process for a B2B SaaS Company
category: development
players: CTO, Security Lead
initialEffort: 21 SP
ongoingEffort: 13 SP
frequency: Quarterly
stage: Early Traction
templates:
  - file: 5.50-security-process-template.xlsx
    name: Security Process Template
summary: Implement security controls—server security, role-based access control, strong passwords, encryption, and penetration testing—to protect customer data.
keywords:
  - security
  - cybersecurity
  - data protection
  - compliance
  - SOC 2
  - penetration testing
  - security controls
  - incident response
questions:
  - What security practices should a SaaS startup implement?
  - What is a penetration test and when should I run one?
  - What password requirements should I enforce for users?
  - How do I control which users can access which resources?
  - How should I encrypt data in the cloud?
preventsMistakes:
---
Security is a very crucial part of your product. Both inside your application and in between your infrastructure, you should have a robust set of security rules and a strict implementation. Network security consists of the policies and practices adopted to prevent and monitor unauthorized access, misuse, modification, or denial of a computer network and network-accessible resources.

> **The goal**: Create a robust set of security rules and implementation processes to protect the security rules.

#### Best Practices

The following are aspects of the security process that need to be considered:

#### Server Security

Golden Section recommends:

- Conducting an annual security assessment (alternatively, you can hire an "ethical hacking" group to do a penetration test -- see below)
- Establish a "Shared Responsibility" policy with your clients on security responsibilities
- Establish both Technical and Administrative safeguards
- Encrypt your database

**Role Based Access Control (RBAC)**: User Roles should be well-defined for your software to control who can access what resources.

#### Application Security

*Passwords*: Passwords should be chosen so that they are hard for an attacker to guess and hard for an attacker to discover using any of the available automatic attack schemes. Requiring a strong password for each user who can access the system should be your first line of defense when dealing with security reinforcement.

Common requirements for a strong password:

- Use at least 8 characters
- Use a mix of lowercase and uppercase letters, numbers, and symbols
- Avoid names and dictionary words
- Stay away from patterns and predictable formulas
- Create unique passwords for all accounts

*Password rotation:* Password rotation refers to the changing/resetting of a password(s). Limiting the lifespan of a password reduces the risk from and effectiveness of password-based attacks and exploits by condensing the window of time during which a stolen password may be valid.

*Data Encryption / Transmission Encryption*: Even Julius Caesar used encryption for his communications. The method was shifting the alphabet by three characters. Golden Section also recommends encryption. Data encryption in the cloud is the process of transforming or encoding data before it's moved to cloud storage. Typically cloud service providers offer encryption services --- ranging from an encrypted connection to limited encryption of sensitive data --- and provide encryption keys to decrypt the data as needed.

*Penetration Test*: A Penetration Test, also colloquially known as a pen test, pentest, or ethical hacking, is an authorized simulated cyberattack on a computer system, performed to evaluate the security of the system.

The process typically identifies the target systems and a particular goal, then reviews available information and undertakes various means to attain that goal. A penetration test target may be a white box (which provides background and system information) or black box (which provides only basic or no information except the company name).

A gray box penetration test is a combination of the two (where limited knowledge of the target is shared with the auditor). A penetration test can help determine whether a system is vulnerable to attack, whether the defenses were sufficient, and which defenses (if any) the test defeated.

There are a number of penetration test tools, including:

1. **Acunetix** is an automated web application security testing and ethical hacking tool. It is used to audit your web applications by checking for vulnerabilities like SQL Injection, cross-site scripting, and other exploitable vulnerabilities.
2. **Nmap**, short for Network Mapper, is a reconnaissance tool that is widely used by ethical hackers to gather information about a target system. This information is key to deciding the proceeding steps to attack the target system.
3. Metasploit
4. **WireShark** is free open-source software that allows you to analyze network traffic in real-time.
5. **John the Ripper** is a (free) password cracking software tool
6. **Nikto** is an Open Source (GPL) web server scanner which performs comprehensive tests against web servers for multiple items, including potentially dangerous files/programs, checks for outdated versions of servers, and version specific problems on servers. It also checks for server configuration.
7. **SQLNinja** is a SQL Server injection & takeover tool
8. **Wapiti** is a web-application vulnerability scanner, Wapiti allows you to audit the security of your websites or web applications. It performs \"black-box\" scans (it does not study the source code) of the web application by crawling the webpages of the deployed web app, looking for scripts and forms where it can inject data.
9. **Kismet** is a network detector, packet sniffer, and intrusion detection system for wireless LANs.

#### Steps

1. Use the template provided to judge the security of your server and application. Working with your Product Manager, answer whether each component of security is currently in place and related details.
2. For components not in place, task your Product Manager and team as necessary to put those security elements in place.

<!-- GS:LINKS start — generated by scripts/build.mjs, do not edit by hand -->

---

**Templates** · [Security Process Template](../../templates/5.50-security-process-template.xlsx)

**Category** · [Development](../README.md) · **Effort** · 21 SP initial, 13 SP ongoing · **Cadence** · Quarterly

<!-- GS:LINKS end -->
