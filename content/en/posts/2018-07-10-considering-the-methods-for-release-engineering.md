---
title: "Considering the Methods for Release Engineering"
date: 2018-07-10
slug: "considering-the-methods-for-release-engineering"
categories:
  - "DevOps"
  - "Design Patterns"
  - "DevOps"
---

The entire goal of release engineering is to accelerate rollout of new software or new releases as much as possible. Release engineering focuses on building a pipeline that transforms source code into an integrated, compiled, packaged, tested, and signed product that is ready for release.

Release management coordinates release workflows between various dev and ops personnel. Release engineers are more technically focused: working with the code, build systems, configuration management tools and container platforms, among other pipeline components, directly.

The goal is for the process to be as simple as possible. Complexity is the enemy of most things. Is my architecture good if it is so complex that no one can figure out how to implement and manage it? Same principles apply to DevOps frameworks. The architecture of the product that flows through the pipeline is a key factor that determines the structure of the continuous delivery pipeline.

For our processes to be simple, we need to automate as much as possible, including any approval gates that aren’t critical. There should be clear expectations of the release workflow and proper feedback loops. Not communicating results back will kill any process. It is imperative for the dev personnel to be communicating with ops to coordinate the release.

![alt text](/images/2018/07/devopselephant.png)

And then of course…a method of releasing the new version.

## Canary

The concept of canarying first emerged in the early 1900s when coal miners would take the caged bird into the mines. Canaries are more susceptible to carbon monoxide than humans; therefore it would quickly die signaling to the miners to get out.

Canary release is a release engineering technique used to reduce the risk of introducing a new software version in production. It accomplishes this by slowly rolling out the change to a small subset of users before rolling it out to the entire infrastructure and making it available to everybody.

Once the release environment and new version are ready, redirect a few selected users to it. Maybe 5-10%. But, how do you choose which users will see the new version? There are a few different options:

- Try out the release on internal users first
- Randomize the user selection
- Use specific characteristic-based criteria to determine the user subset

The idea is that the faster you can get feedback, the faster the deployment can fail or proceed.

![alt text](/images/2018/07/canary-release.jpeg)

As your comfort level increases with the new version, begin and wider release across the infrastructure and re-directing more and more users to it. Canary releases let you dip your toes in before pulling the trigger on a full release.

[Google Cloud Platform blog](https://cloudplatform.googleblog.com/2017/03/how-release-canaries-can-save-your-bacon-CRE-life-lessons.html) has a cool post about release canaries, and so does [Instagram](https://www.fastcompany.com/3047642/do-the-simple-thing-first-the-engineering-behind-instagram).

## Blue-Green Deployment

The concept with a blue-green deployment is fairly simple – there are two identical infrastructures: “green” with the current production load, say v1; “blue” is deployed with the newest version of the app.

![alt text](/images/2018/07/blue-green-deployment.jpeg)

Smoke tests or other kinds of tests have been run, and the “blue” environment is ready to go. Once ready, just change the router / load-balancer / reverse proxy to that “blue” environment. In any automated release, the cutover itself is the most challenging part. This must be done quickly in order to minimize downtime as much as possible. Blue-green deployments approach this by ensuring the two production environments are as identical as possible, minus the application version.

This option also provides a quick to way rollback. If something goes wrong, just switch the router / load-balancer / reverse proxy back to the “green” environment. The goal is to regularly cycle from “blue” to “green” and then “green” back to “blue”. Or, from live to staging for the next release.

## Feature Toggles

Feature Toggles (also referred to as Feature Flags) are a powerful technique that allows you to modify system behavior without changing code. The general idea is that you have a configuration file that defines a few toggles for a handful of pending features. The application will use the toggles to determine whether or not to how the new feature.

![alt text](/images/2018/07/feature-toggle.png)

Most of these decisions occur in the user interface of the application. There may be a set of toggles that surround any UI part of a pending feature. It will pass the new feature through if the toggle is enabled, if not, it will simply skip it.

Toggles introduce complexity. This complexity can be somewhat controlled by maintaining a clear process while using appropriate tools to manage the toggle configuration. It should be a goal to restrict the number of toggles in the system to the absolute minimum required.

This option seems to be a better fit for organizations with more mature CI/CD processes. [Etsy](https://codeascraft.com/2011/02/04/how-does-etsy-manage-development-and-operations/) and [Flickr](http://code.flickr.net/2009/12/02/flipping-out/) provide a great examples of using method this to manage deployments.
