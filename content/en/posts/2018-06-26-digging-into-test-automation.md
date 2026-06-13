---
title: "Digging into Test Automation"
date: 2018-06-26
slug: "digging-into-test-automation"
categories:
  - "DevOps"
  - "Automation"
  - "Design Patterns"
---

Part of making processes more efficient is relying on the crucial component, automation. In DevOps, automation is a near-must for successful performance, because it reduces the number of repetitive tasks thus decreasing the time required for quality results. It is the biggest quality maintainer and speed promoter.

As it’s impossible to automate everything, it’s important to have an automation strategy to get maximum ROI from time and money spent. A properly planned strategy can increase the speed of development and free up teams to concentrate on more essential tasks.

## Select the correct cases to automate

What cases do you choose for automation?

Repetitive tests, high-risk cases, large data sets or checks for different browsers and environments? 

Well…it depends…on the service you are developing and on your team’s capabilities. The goal is to automate the cases providing the most benefits for the development process and across the entire organization.

## Implement automation throughout a sprint

Short release cycles releases can be achieved only if the development and examination are finished simultaneously at the end of the sprint. That’s why quality assurance should begin as early as possible. For example, consider unit testing with each build.

## Continue to apply automated cases

It is important to build flexible tests because it is inevitable to cases to evolve over time. It may be ideal to write small cases rather than creating cases with dozens of steps at initial implementation. Consider separating test into smaller steps and individually check components rather than an entire app stack.

## Types of Tests

**Unit testing** is the practice of testing small pieces of code, typically individual functions in an isolated manner. If the test uses some external resource, such as a database, it’s not a unit test. **Functional testing** is the testing of complete functionality of an application. As the name suggests, **integration testing** is testing how parts of the system work together – the integration of the parts. For example, a unit test for database access code would not talk to a real database, but an integration test would. Unit and integration tests’ results are validated in code, whereas functional test results should be validated the same way as a user would validate it. Whenever code is modified, even a small tweak can have unexpected consequences. **Regression testing** ensures that a change or addition hasn’t broken any existing functionality. The goal is to catch bugs and to ensure bugs that were eradicated stay that way. As an example, re-running a test scenario that was originally created when a problem was initially fixed can help to validate new changes don’t cause components to fail.

## Test Framework

After deciding what types of tests to run, the next step is determining success criteria and then automating the tests. A test framework establishes a set of rules for designing and creating the test cases. Typically, a framework combines practices and tools to increase efficiency. Consider making the test environment closely resemble customer environments, as well as to accommodate for differences. When testing, ensure to test all options for a particular variable. For instance, when conducting web-based GUI tests, make sure to test all major browsers. Don’t only test with Firefox and call it a day. Don’t forget to test scalability and security. 

What is the point of running tests if there are no results? Don’t forget to account with how the metrics are reported. I am fond of the test pyramid approach popularized by [Mike Cohn](https://www.amazon.com/gp/product/0321579364?ie=UTF8&tag=martinfowlerc-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=0321579364). The pyramid says that tests on the lower levels are cheaper to write and maintain, and quicker to run. Tests on the upper levels are more expensive to write and maintain, and slower to run. Therefore you should have lots of unit tests, some service tests, and very few UI tests.  

![alt text](/images/2018/06/pyramid.png)

Most testing can and should take place during dev by running unit tests after every build. It is easy, cheap, and fast to conduct these tests and it allows for checking work as you go. After all unit tests pass, move into the component, integration, and API testing phases. These tests validate most logical and business processes without going through the UI. Therefore, it’s recommended to automate these as much as possible. 

UI tests run last and least; because these tests are costlier and more difficult, it is ideal to run as few as possible. Consider automating critical tests to remove the human element. From there, complete any manual tests. During this phase, it is critical to design based on user workflow. Start with user login and move forward from there.

If you are still interested in test automation, feel free to check out this corporate [blog post ](https://www.rubrik.com/blog/modern-development-automated-testing/) I authored.