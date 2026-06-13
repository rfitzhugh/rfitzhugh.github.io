---
title: "The Laws I Keep Coming Back To"
date: 2022-12-01
slug: "laws-i-keep-coming-back-to"
categories:
  - "Engineering Leadership"
  - "Leadership"
---

Every experienced engineer eventually builds a private library of principles.

Some come from books. Some come from painful incidents. Some come from watching a well-intentioned organization repeatedly make the same mistake with different vocabulary. Over time, these principles become shortcuts: not shortcuts around thinking, but shortcuts back into the right kind of thinking.

The ones I return to most often are not really “laws” in the scientific sense. They are compression algorithms for hard-earned judgment. They help explain why teams get stuck, why metrics mislead, why adding people can slow things down, why organizations ship systems that look suspiciously like their org charts, and why the obvious answer is often only obvious because we are looking at the wrong thing.

These are the principles I find myself referencing again and again.

## The McNamara Fallacy: Not Everything Important Fits in a Dashboard

The McNamara Fallacy is the mistake of making decisions only from what is easy to measure.

It follows a familiar progression:

1. Measure what can be measured
2. Ignore what cannot be measured easily
3. Assume what cannot be measured easily is not important
4. Assume what cannot be measured easily does not exist

This is a dangerous path because it often begins with something reasonable. Measurement is useful. Instrumentation is useful. Dashboards are useful. The problem starts when measurement becomes a substitute for judgment.

The fallacy is named after Robert McNamara, whose approach during the Vietnam War over-indexed on enemy body count as a measure of success. The metric was available, legible, and operationally convenient. It was also tragically incomplete. It failed to capture territorial control, political legitimacy, public sentiment, morale, and the broader strategic picture.

Engineering organizations fall into milder versions of the same trap all the time.

We measure story points and mistake them for progress. We measure uptime and miss user trust. We measure incident count and miss incident severity. We measure deployment frequency and miss whether the deployments matter. We measure developer activity and miss whether developers are spending their time on the right work.

The lesson is not “metrics are bad.” The lesson is that metrics are partial. They are shadows cast by a system, not the system itself.

A mature engineering organization treats metrics as prompts for inquiry, not as replacements for it.

## Goodhart’s Law: When the Metric Becomes the Mission

Goodhart’s Law is usually summarized as:

> When a measure becomes a target, it ceases to be a good measure.

The reason is simple: people adapt.

A metric that begins as an observation becomes corrupted once it is used as the primary definition of success. The system reorganizes itself around satisfying the metric, often at the expense of the underlying outcome the metric was meant to represent.

If teams are rewarded for closing tickets, they will close more tickets. That does not necessarily mean customers are better served. If teams are rewarded for reducing incidents, they may classify fewer things as incidents.

If teams are rewarded for increasing test coverage, they may write tests that cover lines but not risk. If teams are rewarded for shipping more, they may ship smaller and less meaningful increments.

Goodhart’s Law does not mean we should avoid targets. It means we should be careful about lonely targets.

A good metrics strategy has tension in it. Speed should be balanced with quality. Delivery should be balanced with operability. Efficiency should be balanced with resilience. Customer acquisition should be balanced with retention. Local optimization should be balanced with system health.

The question I like to ask is:

> If we optimize this metric aggressively, what behavior would we accidentally encourage?

That question is often more valuable than the metric itself.

## Conway’s Law: Your Architecture Is an Organizational Fossil

Melvin Conway observed that organizations design systems that mirror their communication structures.

This is one of the most important ideas in software engineering because it explains why many architecture problems are not really architecture problems.

A tightly coupled organization will tend to produce tightly coupled systems. A fragmented organization will tend to produce fragmented user experiences. Teams that do not communicate well will often build interfaces that do not integrate well. Ambiguous ownership will show up as ambiguous boundaries in the code.

This is why architecture diagrams can feel like archeology. They reveal past decisions, past org structures, past incentives, and past communication failures.

Conway’s Law is also empowering because it gives us another lever. If we want a different system architecture, we may need a different team architecture. If we want independent services, we need teams that can own them independently. If we want coherent user journeys, we need communication paths that follow those journeys. If we want fast flow, we need to reduce the number of handoffs required to deliver value.

You cannot simply declare a modular architecture into existence. The organization has to be capable of sustaining it.

Architecture follows communication. Change the communication, and over time, you can change the architecture.

## Dunbar’s Number: Coordination Has a Cognitive Cost

Robin Dunbar is associated with the idea that humans can maintain only a limited number of stable social relationships, often cited around 150.

Whether or not the exact number applies neatly to modern organizations, the underlying lesson is useful: human coordination does not scale for free.

Small teams are not just a management preference. They are an engineering tool.

A small team can maintain shared context. A small team can make decisions quickly. A small team can notice when someone is blocked. A small team can develop trust without needing a formal process for every interaction.

This is part of the wisdom behind Scrum teams, Amazon’s “two-pizza team” idea, and many successful platform and product engineering models. Smaller groups tend to have lower communication overhead and higher ownership clarity.

But the lesson is not simply “make every team small.” Small teams still need clear interfaces with one another. Otherwise, you move the complexity from inside the team to between the teams.

The real design challenge is deciding where shared context is essential and where explicit contracts are sufficient.

Inside a team, optimize for trust and shared understanding. Between teams, optimize for clear ownership, well-defined APIs, and predictable collaboration patterns.

## Brooks’ Law: More People Is Not the Same as More Progress

Fred Brooks famously wrote:

> Adding manpower to a late software project makes it later.

This is one of those principles that every senior engineer has seen firsthand.

The mistake is treating people as interchangeable units of capacity. Software work is not simply a pile of independent tasks waiting to be picked up. It is full of context, dependencies, design tradeoffs, implicit assumptions, and partially understood constraints.

Adding people creates onboarding cost. It increases communication paths. It requires existing team members to stop and explain. It can introduce coordination overhead exactly when the project is least able to absorb it.

This does not mean adding people is always wrong. It means timing and task structure matter.

If the work is divisible, well-scoped, and supported by strong onboarding, additional people can help. If the work is late because of ambiguity, architectural complexity, unstable requirements, or unclear ownership, adding people often compounds the problem.

When a project is late, the first question should not be:

> Who else can we add?

It should be:

> What is actually making this slow?

Sometimes the answer is capacity. Often it is not.

## The Theory of Constraints: Find the Bottleneck Before Optimizing

The Theory of Constraints, popularized by Eliyahu Goldratt in *The Goal*, starts from a simple premise: every system has a constraint.

There is always something limiting throughput. It may be a person, a process, a dependency, a review step, a build system, a decision-maker, a team boundary, a brittle component, or an overloaded database. The constraint determines the pace of the whole system.

This matters because many organizations spend enormous energy optimizing non-constraints.

They improve the speed of development when the bottleneck is review. They improve review when the bottleneck is deployment. They improve deployment when the bottleneck is product decision-making. They improve individual productivity when the bottleneck is cross-team dependency management.

Optimizing anything other than the constraint may feel productive, but it rarely changes system throughput.

The Theory of Constraints suggests a disciplined loop:

1. Identify the constraint
2. Exploit the constraint
3. Subordinate other work to the constraint
4. Elevate the constraint
5. Repeat, because the constraint will move

This is deeply applicable to engineering leadership.

If build times are the constraint, focus there. If architectural coupling is the constraint, focus there. If unclear strategy is the constraint, no amount of sprint optimization will save you. If the approval process is the constraint, adding more engineers will not help.

The highest-leverage work is often not the most visible work. It is the work that moves the bottleneck.

## The Pareto Principle: Impact Is Not Evenly Distributed

The Pareto Principle, or the 80/20 rule, says that roughly 80% of outcomes often come from 20% of causes.

The exact numbers are not the point. The point is asymmetry.

A small number of customers may generate most of the revenue. A small number of bugs may cause most of the support burden. A small number of services may create most operational incidents. A small number of product flows may drive most user value. A small number of architectural decisions may explain most of the system’s complexity.

Engineering effort is often distributed more evenly than impact is. That mismatch is expensive.

The Pareto Principle reminds us to look for concentration. Where is the pain concentrated? Where is the value concentrated? Where is the risk concentrated? Where is the complexity concentrated?

This is not an argument for ignoring the long tail. The long tail matters, especially in platform and infrastructure work. But it is an argument for sequencing.

Do the most important things first. Fix the problems that unlock other problems. Invest where the marginal return is highest. Avoid the comforting fiction that every task has equal strategic weight.

Prioritization is not about saying “yes” to the important work. Everyone does that. Prioritization is about saying “not yet” to work that is genuinely useful but not currently decisive.

## How These Principles Fit Together

What I like about these laws is that they reinforce one another:

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

## The Real Lesson: Beware Simple Stories

Most organizational mistakes come from a story that is too simple.

- “We need to move faster, so let’s add more people”
- “We need better performance, so let’s set a target”
- “We need accountability, so let’s measure everyone”
- “We need architecture consistency, so let’s publish standards”
- “We need teams to collaborate, so let’s create a process”
 
Sometimes these are the right moves. Often they are incomplete.

Distinguished engineering work is rarely about knowing one clever law and applying it everywhere. It is about seeing the system clearly enough to know which principle applies, where it applies, and where it stops applying.

That is the hard part.

Metrics are useful, until they become the mission. Teams need autonomy, until autonomy becomes fragmentation. Small teams are powerful, until they lack the interfaces to coordinate. Adding people helps, until coordination costs dominate. Optimization is valuable, until we optimize the wrong part of the system.

The laws are not answers. They are lenses.

And when used well, they help us ask better questions:

- What are we measuring, and what are we missing?
- What behavior are our incentives creating?
- Where does our architecture mirror our organization?
- Where is coordination becoming the work?
- What is the actual constraint?
- Where is the leverage?
- What are we pretending is simple?

The best engineers I know are not the ones who have memorized the most principles. They are the ones who use principles to stay honest.

Honest about complexity. 

Honest about incentives.

Honest about human limits.

Honest about tradeoffs.

Honest about what the system is actually doing, not what we hoped it would do.

That is why I keep coming back to these laws. Not because they are always perfectly true. Because they are reliably useful.