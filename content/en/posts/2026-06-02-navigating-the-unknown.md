---
title: "Navigating the Unknown"
date: 2026-06-02
slug: "navigating-the-unknown"
categories:
  - "Engineering Leadership"
  - "Architecture"
---

# Navigating the Unknown: Deciding Without Certainty

The hardest skill for senior engineers often isn't coding - it's deciding with incomplete information. 

Uncertainty is not a special case in software engineering. It's the default condition. Requirements are incomplete because the people writing them don't fully know what they want yet. New technology is unproven because if it were proven, someone would have already shipped the thing you're building. Organizations change shape underneath a decision while it's still being made. It's the daily terrain every technical leader operates in, at every scale, from a single pull request to a company-wide platform strategy.

The problem isn't the uncertainty itself. It's how people respond to the discomfort of it. I've seen engineers spin out on key projects not because the technical work was beyond them, but because the ambiguity was - and that gap is what separates senior leaders trusted with the hardest problems from people who've earned seniority in title without earning the trust that goes with it. 

Left unmanaged, that discomfort produces two failure modes: deciding too slowly because no amount of information ever feels sufficient, or deciding too carelessly because slowing down feels like weakness. Neither is a strategy. Here's a bit of what I've learned about making sound calls without waiting for certainty that isn't coming.

## The cost of chasing certainty

Analysis paralysis rarely announces itself as fear. It shows up dressed as diligence: one more round of research, one more design review, one more spike to "de-risk" a call that was never that risky to begin with. Each step feels responsible in isolation. In aggregate, it's a slow refusal to commit.

The tell is in the questions. Healthy investigation converges - each answer narrows the space of what's left to decide. Paralysis diverges...every answer spawns two more questions, and the scope of "things we should understand first" keeps expanding to match your appetite for avoiding the call.

I saw this constantly at Atlassian, on developer productivity work where we hadn't had defined what "good" looked like yet. The instinct is to wait until the plan is airtight before shipping anything. Waiting for a perfect model means shipping nothing, while teams keep making investment decisions on gut feel because there's nothing concrete to work from. A directionally correct approach in motion beats a theoretically perfect one still in review. Perfect is the enemy of good, and in ambiguous territory, it's also the enemy of momentum.

## The 75% method

I learned this one in the Marine Corps, and it's stayed the single most useful mental model I carry into technical decisions: gather until you have roughly 75% of the information you'd ideally want, then decide. Use judgment, experience, and pattern recognition to close the remaining 25%.

The number is a permission slip, not a formula. The value of new information drops sharply after a point, while the cost of waiting for it keeps climbing. Early information changes your decision. Late information mostly just makes you feel better about a decision you'd already effectively made, but that reassurance has a real price, paid in calendar time and organizational momentum.

A useful litmus test is: *if I learned this next fact, would I actually decide differently?* If not, it isn't worth pursuing right now, no matter how incomplete the picture still feels.

## Two ways of deciding: analytical and recognitional

Most decision-making training teaches one mode: lay out the options, weigh the criteria against a scorecard, pick the highest score. Call this **analytical decision-making**. It works well when time isn't the constraint and options are genuinely comparable - evaluating CI/CD platforms across a large engineering organizations, for instance, where the cost of a wrong call is measured in years and thousands of engineers.

But a large share of real decisions, especially the fast ones a technical leader makes daily, don't happen that way. [Gary Klein's research on naturalistic decision-making](https://www.gary-klein.com/rpd) describes a second mode: **recognitional decision-making**. An experienced person recognizes a situation as an instance of a pattern they've seen before, retrieves an approach that worked previously, mentally simulates whether it applies here, and acts - often without ever building a formal comparison.

This is why a senior engineer can glance at a build failure pattern and immediately suspect a golden-image drift issue, while someone newer to the environment is still opening logs. It isn't a shortcut around real thinking. It's compressed experience, and it's a legitimate mode in its own right.

The practical implication is matching the method to the moment. A production incident is not the time for a weighted decision matrix - that's when you want your most experienced responder pattern-matching as fast as possible. A multi-year platform investment with no time pressure is exactly when to slow down and go analytical, because there's no reliable pattern to draw on yet. Confusing the two is where expensive mistakes come from: analyzing your way through a fire, or pattern-matching your way through a decision nobody on the team has actually faced before.

## One-way doors and two-way doors

Not every decision deserves the same amount of caution, and applying uniform process to all of them is its own kind of error.

**Two-way door decisions** are reversible. Pick a wrong internal tool, a wrong first-pass metric definition, a wrong naming convention — you walk back through the door at some cost, but not a catastrophic one. Most day-to-day technical decisions live here, and they should be made quickly by the person closest to the problem. The 75% method applies especially well; sometimes even 50% is enough, because the downside of being wrong is an afternoon of rework.

**One-way door decisions** are different: migrating 1,200 repositories off a source control platform, changing how AI-assisted code is measured and attributed company-wide, committing to a pricing or governance model that teams will build workflows around. The cost of being wrong is high and the door doesn't swing back cleanly. These decisions warrant real deliberation, broader input, and the closer-to-100% information-gathering that would be wasteful everywhere else.

The failure mode I see most often isn't rushing one-way doors — though that happens. It's dragging one-way-door process into two-way-door decisions: treating a reversible tooling choice with the same review cycle as an irreversible platform migration. That doesn't make an organization careful. It makes it slow, and it teaches people to fear reversible decisions as much as irreversible ones, which is exactly backwards.

## Weighing risk: likelihood and impact

When a decision genuinely warrants formal risk analysis, the clearest tool is still the simplest: plot the risk on two axes, **likelihood** and **impact**. The [NASA Risk Management Handbook](https://ntrs.nasa.gov/api/citations/20120000033/downloads/20120000033.pdf) frames risk this way for a reason — under pressure, people instinctively focus on how likely something is and neglect how bad it would actually be if it happened. Risk is the combination of both.

- **Low likelihood, low impact** - not worth a meeting
- **High likelihood, high impact** - needs a mitigation plan before proceeding, full stop
- **Low likelihood, high impact** - usually deserves a contingency plan rather than a delay. Evaluating agentic coding tools during the AI Coding Bake-Off meant accepting that any single vendor's roadmap could shift unpredictably; the mitigation wasn't picking the "safest" tool, it was avoiding hard lock-in
- **High likelihood, low impact** - usually just needs defensive engineering, not a design review

What this framework buys is a shared vocabulary. "I have a bad feeling about this" versus "I think we'll be fine" is a standoff, not a conversation. Naming likelihood and impact separately usually reveals that people agree on the impact and disagree only on the likelihood...a much smaller, more tractable disagreement to resolve.

## Conclusion

None of these tools remove uncertainty. Nothing does. What they do provide is a way to be deliberate about how much certainty a given decision actually requires, so time and organizational trust (the two scarcest resources in any transformation effort) aren't spent buying more confidence than the situation calls for.

The technical leaders I respect most aren't the ones who are never wrong. They're the ones who are accurate and honest about quickly sorting a decision into the right bucket: which door am I walking through, which mode of thinking does this moment call for, and have I already learned enough to act. Everything else is commentary.