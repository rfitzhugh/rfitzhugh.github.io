---
title: "Delving into Immutable Infrastructure"
date: 2018-01-09
slug: "delving-into-immutable-infrastructure"
categories:
  - "Architecture"
  - "DevOps"
  - "Architecture"
---

Before getting too far into the topic, let’s first take a quick look at the difference between mutability and immutability.

|  |  |
|----|----|
| **Mutable** | **Immutable** |
| Continually updated, patched, and tuned to meet the ongoing needs of the purpose it serves. | State does not change or deviated once constructed. Any changes result in the deployment of a new version rather than modifying existing. |

I found this incredible GIF on Giphy, but with some light googling I found that this image came from an O’Reilly [blog post](https://www.oreilly.com/ideas/an-introduction-to-immutable-infrastructure). But I think it does an excellent job of visualizing the difference.

![alt text](/images/2018/01/giphy.gif)

Now that we have the obligatory definitions out of the way, let’s dive in.

## Pitfalls of Mutable Infrastructure

In a traditional server infrastructure, servers are continually updated and modified in place. Administrators upgrade or downgrade packages manually, modify configurations on a server-by-server basis, and deploy new code directly onto existing servers. Over time, as more updates are applied, each server eventually has its own unique history of changes.

In other words, these servers are mutable as they can be changed after creation. This results in each service becoming slightly different than all the others, leading to configuration drift. This can potentially lead to bugs that are difficult to diagnose and reproduce. Because of the potential for many different versions and configurations, it is important to be aware of the history…but that gets complicated when working with a massive server infrastructure. Configuration management is paramount to ensure import system parts are at a known state. But that’s easier said than done.

## What about Immutable?

An immutable infrastructure is a different infrastructure paradigm in which servers are never modified after deployment. If something needs to be updated, fixed, or modified in any way, new servers containing the appropriate changes are provisioned from a common image to replace the old ones. After validation, the new servers are put into use and the old ones are decommissioned.

Compared to mutable, an immutable infrastructure provides stability, efficiency, and fidelity to your applications through automation. This concept is not new in the wild world of tech, it is a successful pattern taken from programming.

Immutable infrastructure all but requires full automation of your environment. Imagine building new servers and retiring the old with each update or patch…manually. No thank you. This infrastructure paradigm doubles down on the idea that compute environments should have an API for all aspects of configuration and monitoring.

## Virtualization, Cloud, Containers…oh my!

The advent of virtualization and, more recently, cloud computing represented different watershed moments for server architecture. Virtual machines are less expensive than physical servers, and can be created and destroyed, even at scale, in minutes instead of days or weeks. This brought forth of wave of new deployment workflows and server management techniques, for example, using configuration management tools to provision new workloads using quick, automatic, programmatic method. The speed and low cost of provisioning new virtual workloads is what has truly enabled immutability principles for infrastructure.

Immutable infrastructure has been a relatively more recent discussion within DevOps. By creating machine images and replacing rather than modifying existing components, the idea is that we can build a more reliable compute infrastructure, and minimize the differences between test/dev and production systems. The goal is to reduce, if not eliminate, the amount of error-prone, manual fidgeting with configurations that leads to 1am emergency troubleshooting sessions fueled by Red Bull.

![alt text](/images/2018/01/giphy1.gif)

It’s no secret that containers in general — and Docker, in particular — have become very popular in the DevOps space. For an agile organization, containers can be much faster to build, test and deploy than snapshotting VMs or running scripts to configure servers. Once an application image has been built, tested and tagged, deploying it is a very efficient process because the configuration of the underlying OS from the equation has been effectively removed.

The heavy lifting can be delegated to the choice cloud provider by deploying* *the provider’s base template for a vanilla up-to-date OS. It may even perform better if it’s patched and optimized for their hypervisor. The icing on the cake is that it really doesn’t matter…as long as it runs Docker.

Containers also remove the need to deploy new servers every time it is desired to push a new version of an application. By committing the state of a container, it creates a new image with the previous image untouched. Because all the application’s dependencies and logic are inside containers and are completely replaced with every new version, all servers can persist and still gain all the benefits from the immutable infrastructure model.

The best part is that you reap the benefits of containers: not being tied to any cloud provider or any Linux distribution (as long as it runs Docker). If the application works locally during testing, then it will work in production on any provider. Isn’t that *\#InfrastructureGoals?*

## Is it too good to be true?

Realistically, there is not much precedent in how this should be used. For a successful adoption, it is more than just immutable infrastructure — it requires a bigger shift in mindset with things like Infrastructure as Code. However, the publicly available technology is relatively new in the scheme of tech. (Mutable infrastructures have been around forever!) Infrastructure as Code is an ideal way to create immutable infrastructure.

DevOps organizations have embraced this thinking and architecture across virtualized platforms and public cloud providers. But, keep in mind, it also requires a high degree of maturity from organizations in terms of processes and operational knowledge. The hardest part may be weaning off existing tools and processes that are in place for the existing way of doing things.

# Closing Thoughts

Continuous delivery is Promised Land for most DevOps organizations. The central philosophy of continuous delivery is to deploy a package and its dependencies the same way every time so there is no doubt that the environment is the same. The underlying dependencies are where immutable infrastructure comes into play.

Immutable infrastructure as the underpinning component of the currently running version of the application makes the job of operations so much easier. If there is a problem, just rebuild that instance. If load increases, spin up a couple extra instances without having to think about it.

Think of places you have worked that handle application deployments to multiple environments, including production. I’m imagining how many stressful hours I spent working with the kerfuffle known as Altiris that could have avoided. Wouldn’t boring deployments be a nice change?
