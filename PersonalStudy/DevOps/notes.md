# DevOps Course

## What's  DevOps?
* Is a methodology that helps engineering teams build products by continuously getting user feedback.

* In the context of DevOps engineer is "infrastructure for building and deploying code."

# DevOps Engineer functions
The goal of DevOps engineering is to release high quality software quickly, and make sure it continues being delightful and bug-free for end users.

* Build
* Test
* Relase
* Monitor

## Pillars of DevOps
1. **Pull Request Automation**
2. **Deployment Automation**
3. **Application Performance Management**

### Pull Request Automation
The goal is that developers can tell very quickly whether the code is good or not. 

Automate test and gates for the pull request's code. Then the code has to go through the code review from a peer, product manager, or "code owner".

**What can you automate?**
* Automated test running with a CI provider, which gives developers confidence that the change does not break existing functionality
* Per-change ephemeral environments, which helps interested parties actually interact with the proposed change to ensure it solves all required business goals.
* Automated security scanning, which helps ensure that proposed changes do not introduce new vulnerabilities into the product.
* Notifications to reviewers automatically, so that the correct reviewers can quickly request changes to a pull request.

**Goal as a DevOps**
The goal is to help developers change proposals, get reviewed and merged within 24 hours of when they are made.

### Deployment Automation
It's easy to overcomplicate deployments. Many companies have complex internal platforms for building and distributing releases.

Broadly, success in deployment automation is finding the appropriate deployment tools to fulfill business goals, and configuring them. In an ideal world, there should be little-to-no custom code for deploying.

**Goal as a DevOps**
* "Can you make a build in one step?"
* Deploying a feature to a certain set of users as a final test before rolling it out more publicly (feature flagging and canary deployments)
* Starting new versions of services without causing downtime (blue/green deployments and rolling deployments)
* Rolling back to the prior version in case something does go wrong.

### Application Performance Management
1. Metrics: Numerical measurements of key numbers in production. Usually in the form of finite resources (disk space, memory usage) and times (average response time, job processing time, etc)
2. Logging: Text descriptions of what is happening during processing. Logs often come with metadata about their source, time, and related metrics.
3. Monitoring: Take the metrics and logs and convert them into health metrics: Does the product feel slow, is it down, are all of the features working without errors?
4. Alerting: If monitoring detects a problem, the correct problem-solver should be notified automatically: In the case of an outage, an on-call engineer should be notified. Performance issues and errors with features often automatically log tickets.

# Test and Test driven development
Methodology where test are written before the code

* Unit Test
* Integration Test
* System (End to end) test
* Acceptace tests

### TDD goals
* Know then something breaks
* Know that the whole system is working correctly

# CI - Continuos integration
Is a vital tooll for developer colaboration, prevent errors, and increase user satisfaction. 

- There's mutiple testing platform such as LayerCi or Heroku Review apps that will use a server/container to run automated test, Unit Test, Linters, etc.
- CI should be the first thing to be automated

# Virtual Machines vs Containers


# Deployment
## Rolling deployments
Deployment strategy to deploy a new version of an application without causing downtime. They work by creating a single instance of the new version of an application, then shutting off one instance of the old version until all instances have been upgraded

- Well supported
- No huge burst
- Easily reverted

## Blue/Green deployment
Consist of starting an entirely new instance of the application and then routing traffic over it.
- Easy to understand
- Powerful
- Exntendable to workflows

### Rainbow deployments
Similar to Blue/Green but having more than two deployment clusters.
