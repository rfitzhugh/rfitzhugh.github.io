---
title: "Get Mapped: Value Stream Mapping"
date: 2018-06-19
slug: "get-mapped-value-stream-mapping"
categories:
  - "Architecture"
  - "DevOps"
  - "Design Patterns"
---

![alt text](/images/2018/06/twain.png)

Value stream mapping (VSM) does exactly that: it is a DevOps framework (“borrowed” from manufacturing) that provides a structured way for cross-functional teams to collectively see where we are today (long release cycles, silos, damage control afterwards, etc.) and where we want to be in the future (short release cycles, infrastructure as code, iterative development, continuous delivery, etc.).

A VSM is a way of getting people to collaborate and see what is really happening. These exercises are often amazing “aha!” moment workshops that make three objectives (flow, feedback, and continuous integration) turn into a sustainable engine of improvement.

Who should participate in a VSM?

-     Service Stakeholders and Customers
-     Executors of a Process Tasks
-     Management

…but not all at the same time.

The VSM process assembles everyone involved with a workflow in the same room to clarify their roles in the product delivery process and identify bottlenecks, friction points and handoff concerns. Realistically, if we include everyone at the same time, the likelihood of honesty decreases. Let’s be for real – if upper management were in the room with you, would you be 100% honest as to where the bodies are buried or exactly what processes each step entails? VSM reveals steps in development, test, release and operations support that waste time or are needlessly complicated and this requires complete transparency.

## **Lead Time versus Time on Task**

If you can’t measure it, you can’t improve it. Why do companies go for Continuous Delivery (CD)? Why do people care about DevOps? The main reason I hear is *cycle time*. This is the time it takes me to get from an idea to a product or feature that your customers can use. Measurement is one of the core foundations of DevOps, and the VSM is the measurement phase. If you do it right, it’s the sharing phase as well – share the measurements and proposed changes with the entire group. Doing that well allows you to start to change culture simultaneously.

![alt text](/images/2018/06/lead-time-vs-time-on-task.png)

With a solid foundation in place, it becomes easier to capture more sophisticated metrics around feature usage, customer journeys, and ensuring that service level agreements (SLAs) are met. The information received becomes handy when it’s time for road mapping and spec’ing out the next big project.

“Lead time” is a term borrowed from manufacturing, but in the software domain, lead time can be described more abstractly as the time elapsed between the identification of a requirement and its fulfillment.

The goal of VSM development is to measure how time is spent on each task and identify processes required for each task. It becomes easier to see what processes are inefficient and creating a bottleneck. In turn, this will reduce the lead time to deliver the finished release.

## **Current State**

The following VSM demonstrates a current state analysis of the current software release process. The main thing to note in this example is how linear it is – there are only two feedback loops: at the very beginning and towards the end at new feature testing.

![alt text](/images/2018/06/current-state.png)

The apparent lack of feedback loops presents a potential problem area – there are 8 steps between the two feedback loops. Imagine getting all the way to the end before realizing there’s an issue and providing feedback. How far will the software release be set back if the problem is not detected and communicated until the new release testing phase?

## **Future State**

Once you have the current state VSM mapped, the next step is to figure out a way to make the mapping more efficient. This is typically driven by the following:

- How can we significantly increase the percent complete and accurate work for each step in our current state VSM?
- How can we dramatically reduce, or even eliminate the non-productive time in the lead time of each current state step?
- How can we improve the performance of the value added time in each current state step?

![alt text](/images/2018/06/future.png)

Realistically, no VSM is perfect. However, the future state that we see above demonstrates a set of processes that create a mostly ongoing feedback loop. This allows for continuous communication about the processes and release as it moves forward towards a qualified build.

## **Demonstrating Business Value**

In the manufacturing plants, they would have one pipeline, one production line at a time. As we know, the modern software development world is not like that.

A VSM is about more than just dissecting the software delivery lifecycle to find bottlenecks and pain points, although it is certainly helpful in that area. Analyzing value streams gives management confidence that the business is focusing on the right projects and initiatives. By taking a clearer look at the KPIs and metrics across the tooling and scaling the entire organization, these leaders can make informed decisions the way most business leaders prefer to—with data to back them up.
