---
title: "The Laws I Keep Coming Back To"
date: 2022-12-01
slug: "laws-i-keep-coming-back-to"
categories:
  - "Engineering Leadership"
  - "Leadership"
---

Every experienced engineer eventually builds a private library of principles.

Some come from books. Some come from painful incidents. Some come from watching a well-intentioned organization repeatedly make the same mistake with different vocabulary. Over time, these principles become shortcuts back into the right kind of thinking.

The ones I return to most often are not really “laws” in the scientific sense, but rather lessons in hard-earned judgment. They help explain why teams get stuck, why metrics mislead, why adding people can slow things down, why organizations ship systems that look suspiciously like their org charts, and why the obvious answer is often only obvious because we are looking at the wrong thing.

These are the principles I find myself referencing again and again.

## The McNamara Fallacy

The McNamara Fallacy is the mistake of making decisions only from what is easy to measure. The fallacy is named after Robert McNamara, whose approach during the Vietnam War over-indexed on enemy body count as a measure of success. The metric was available, legible, and operationally convenient. It was also tragically incomplete. It failed to capture territorial control, political legitimacy, public sentiment, morale, and the broader strategic picture.

Engineering organizations fall into milder versions of the same trap all the time. It follows a familiar progression:

1. Measure what can be measured
2. Ignore what cannot be measured easily
3. Assume what cannot be measured easily is not important
4. Assume what cannot be measured easily does not exist

This is a dangerous path because it often begins with something reasonable (e.g., measurement, instrumentation, dashboards are all useful). The problem starts when measurement becomes a substitute for judgment. For example, measuring story points and mistaking them for progress. 

The lesson is not “metrics are bad,” but rather that metrics are partial. They are shadows cast by a system, not the system itself. A mature engineering organization treats metrics as prompts for inquiry, not as replacements for it.

## Goodhart’s Law

Goodhart’s Law is usually summarized as:

> When a measure becomes a target, it ceases to be a good measure.

The reason is simple: people adapt.

A metric that begins as an observation becomes corrupted once it is used as the primary definition of success. The system reorganizes itself around satisfying the metric, often at the expense of the underlying outcome the metric was meant to represent.

If teams are rewarded for closing tickets, they will close more tickets but that does not necessarily mean customers are better served. Similarly, if teams are rewarded for reducing incidents, they may classify fewer things as incidents.

Goodhart’s Law does not mean we should avoid targets. It means we should be careful about lonely targets. A good metrics strategy has tension in it: speed should be balanced with quality, delivery with operability, efficiency with resilience, and so on. The question I like to ask is:

> If we optimize this metric aggressively, what behavior would we accidentally encourage?

That question is often more valuable than the metric itself.

## Conway’s Law

Melvin Conway observed that organizations design systems that mirror their communication structures. This is one of the most important ideas in software engineering because it explains why many architecture problems are not really architecture problems.

A tightly coupled organization will tend to produce tightly coupled systems. A fragmented organization will tend to produce fragmented user experiences. Teams that do not communicate well will often build interfaces that do not integrate well. Ambiguous ownership will show up as ambiguous boundaries in the code.

This is why architecture diagrams can feel like archeology. It reveals past decisions, past org structures, past incentives, and past communication failures.

Conway’s Law is also empowering because it gives us another lever. If we want a different system architecture, we may need a different team architecture. If we want independent services, we need teams that can own them independently. If we want coherent user journeys, we need communication paths that follow those journeys. If we want fast flow, we need to reduce the number of handoffs required to deliver value.

You cannot simply declare a modular architecture into existence. The organization has to be capable of sustaining it.

Architecture follows communication. Change the communication, and over time, you can change the architecture.

## Dunbar’s Number

Robin Dunbar is associated with the idea that humans can maintain only a limited number of stable social relationships, often cited around 150. The exact number is irrelevant, but the underlying lesson is useful: human coordination does not scale for free.

Small teams are an engineering asset. A small team can maintain shared context, make decisions quickly, notice when someone is blocked, and develop trust without needing a formal process for every interaction. This is part of the wisdom behind Scrum teams, Amazon’s “two-pizza team” idea, and many successful platform and product engineering models. Smaller groups tend to have lower communication overhead and higher ownership clarity.

However, the lesson is not simply “make every team small.” Even small teams still need clear interfaces with one another. Otherwise, you move the complexity from inside the team to between the teams.

The real design challenge is deciding where shared context is essential and where explicit contracts are sufficient. Inside a team, optimize for trust and shared understanding. Between teams, optimize for clear ownership, well-defined APIs, and predictable collaboration patterns.

## Brooks’ Law

Fred Brooks famously wrote:

> Adding manpower to a late software project makes it later.

This is one of those principles that every senior engineer has seen firsthand.

The mistake is treating people as interchangeable units of capacity. Software work is not simply a pile of independent tasks waiting to be picked up. It is full of context, dependencies, design tradeoffs, implicit assumptions, and partially understood constraints. Adding people creates onboarding cost. It increases communication paths. It requires existing team members to stop and explain. It can introduce coordination overhead exactly when the project is least able to absorb it.

This does not mean adding people is always wrong. It means timing and task structure matter. If the work is divisible, well-scoped, and supported by strong onboarding, additional people can help. If the work is late because of ambiguity, architectural complexity, unstable requirements, or unclear ownership, adding people often compounds the problem.

When a project is late, the first question should be "what is actually making this slow?" and not to just throw more bodies at the problem. Sometimes the answer is capacity, but often it is not.

## The Theory of Constraints

The Theory of Constraints, popularized by Eliyahu Goldratt in *The Goal*, starts from a simple premise that every system has a constraint.

There is always something limiting throughput. It may be a person, a process, a dependency, a review step, a build system, a decision-maker, a team boundary, a brittle component, or an overloaded database. The constraint determines the pace of the whole system.

This matters because many organizations spend enormous energy optimizing non-constraints. They improve the speed of development when the bottleneck is review, or improve review when the bottleneck is deployment, or focus on deployment when the problem is product decision-making, and so on. 

Optimizing anything other than the constraint may feel productive, but it rarely changes system throughput. The Theory of Constraints suggests a disciplined loop:

1. Identify the constraint
2. Exploit the constraint
3. Subordinate other work to the constraint
4. Elevate the constraint
5. Repeat, because the constraint will move

This is deeply applicable to engineering leadership. If build times are the constraint, focus there. If architectural coupling is the constraint, focus there. If unclear strategy is the constraint, no amount of sprint optimization will save you. If the approval process is the constraint, adding more engineers will not help.

The highest-leverage work is that which moves the bottleneck.

## The Pareto Principle

The Pareto Principle, or the 80/20 rule, says that roughly 80% of outcomes often come from 20% of causes. The point is asymmetry, not the numbers.

A small number of customers may generate most of the revenue, or a small number of bugs may cause most of the support burden, or a small number of services may create most operational incidents, and so on. 

Engineering effort is often distributed more evenly than impact is. That mismatch is expensive. The Pareto Principle reminds us to look for concentration. Where is the pain concentrated? Where is the value concentrated? Where is the risk concentrated? Where is the complexity concentrated?

This is not an argument for ignoring the long tail. The long tail matters, especially in platform and infrastructure work. But it is an argument for sequencing.

Prioritization is about saying “not yet” to work that is genuinely useful but not currently decisive. Do the most important things first. Fix the problems that unlock other problems. Invest where the marginal return is highest. Avoid the comforting fiction that every task has equal strategic weight.

## How These Principles Fit Together

I keep coming back to these laws because they are reliably useful to diagnose and understand situations in software engineering. What I like about these laws is that they reinforce one another:

- The McNamara Fallacy warns us not to confuse what is measurable with what matters
- Goodhart’s Law warns us that once we reward a measure, people will optimize for the measure rather than the meaning behind it
- Conway’s Law reminds us that systems reflect the organizations that build them
- Dunbar’s Number reminds us that coordination is constrained by human cognition
- Brooks’ Law reminds us that capacity is not linear and that adding people can increase complexity
- The Theory of Constraints reminds us to find the bottleneck before improving the machine
- The Pareto Principle reminds us that impact is unevenly distributed and that leverage matters

Together, these principles form a useful operating system for engineering judgment.

They push us _away_ from naive management: more metrics, more people, more process, more dashboards, more meetings, more parallel work.

They push us _toward_ systems thinking: understand the constraint, inspect the incentives, design the organization intentionally, preserve human-scale collaboration, and optimize for outcomes rather than proxies.