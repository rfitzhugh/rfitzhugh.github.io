---
title: "Guide to Keeping a Brag Doc"
date: 2023-03-08
slug: "guide-to-brag-doc"
categories:
  - "Mentorship"
---

# Guide to Keeping a Brag Doc

Julia Evans wrote the [canonical post on brag documents](https://jvns.ca/blog/brag-documents/) back in 2019, and if you haven't read it, go read it. The core idea is right and it holds up. This post isn't a replacement. It's the more prescriptive version I wish someone had handed me earlier in my career: a specific structure, a specific cadence, and specific rules for turning a running list of things you did into something that actually moves a performance review, a promotion packet, or a resume. Why keep one? 

- **You will not remember what you did in January.** By review season, recency bias has already won. The production incident you handled in June feels vivid; the design review that saved a team three months of rework in February is gone unless you wrote it down. Memory is not a reliable evidence store, and performance reviews run on evidence
- **Your manager does not see everything you do**, and at Principal-plus levels this gap widens, not narrows. Influence work — the design you unblocked in a hallway conversation, the roadmap you shifted in a review you weren't even the presenter for - is exactly the kind of impact that's real, valuable, and invisible unless someone records it
- **It collapses review-season panic into an editing exercise.** Instead of reconstructing a year from Git history, Slack search, and calendar archaeology, you're editing a document that already exists
- **It surfaces patterns you can't see in the moment.** I didn't set out to become the person who builds measurement systems from scratch. I noticed it by rereading three years of FY in Review documents and seeing the same shape repeat: no standard exists, I define one, adoption follows. That pattern became a career thesis, not just a job description
- **It outlives the review cycle.** The same document becomes the raw material for a resume, a promotion packet, an interview loop, or when you're ready to leave - the background document a recruiter or hiring manager needs to actually understand what you did

I've kept a version of this document (mine is usually called "FY in Review") pretty much every year for over a decade, across different companies and every level (both as an IC and a manager). The format changes but the habit hasn't.

## The core rule: situation, behavior, impact

Most brag docs fail for the same reason: they list activity instead of outcome. "Led the migration" is activity. "Led the migration of 1,200 repositories to Bitbucket Cloud, reducing build latency 22% and cutting the associated support ticket volume in half" is outcome. 

Use **Situation, Behavior, Impact (SBI)** for every entry that matters -

- **Situation**: what was the problem or context? One sentence. What was broken, missing, or at risk before you acted?
- **Behavior**: what did you specifically do? Not your team. You. If you led a team, say what leading meant in concrete terms - the decisions you made, the design you owned, the escalation you drove
- **Impact**: what changed as a result, and how do you know? A number if you have one. A qualitative outcome if you don't, stated as specifically as the number would be

A one-line entry — "helped with the CI migration" - is nearly worthless six months later; you won't remember what "helped" meant. An SBI entry survives the memory decay that makes brag docs necessary in the first place.

## Cadence: capture now, refine later

Bt it's unrealistic to expect you write polished SBI entries in the moment. You're in the middle of the work; you don't yet know the full impact, and stopping to craft prose is friction that makes you skip the habit entirely.

Instead, run two passes:

1. **Capture, weekly or biweekly.** Drop a raw entry the moment something happens - a link to a key PR, the design doc, the Slack thread, the incident retro, a single sentence of context. This takes under two minutes and is the only step that has to survive contact with a busy week. Don't edit. Don't format. Just don't lose it.
2. **Refine, quarterly.** Once a quarter, sit down and convert the raw links into SBI entries. By this point you usually know the actual impact — the metric moved, the team adopted the pattern, the customer renewed — in a way you couldn't have known the day you shipped it. This is also when you notice the raw list was incomplete, because writing the impact often jogs your memory about the situation.

At review time, you're not starting from zero and you're not starting from a pile of unrefined links either. You're assembling four quarters of already-polished entries into a narrative.

## The template

I organize by theme, not strict chronology, once I'm above senior engineer - at Staff or Principal-plus levels, the story a reviewer needs isn't "here's what happened each month," it's here's the shape of my impact this year (usually dictated by the decisions I made the previous FY). Chronology lives inside each theme, not as the top-level structure.

### Goals - this year and next

State what you set out to do at the start of the period, and what you think you should be aiming at next. This gives your manager and peer reviewers the context to interpret everything below it, and it's the section that makes your promotion narrative feel intentional rather than reconstructed after the fact.

### Programs and projects

For each major body of work: Situation, Behavior, Impact, in that order. Name the project. If it has an internal codename nobody outside your org will recognize, translate it - lead with the outcome, then the name, not the other way around. "Reduced median PR cycle time 60%" reads better than "Led Project Sonic".

### Organizational leverage and mentorship

This is the category most senior engineers under-report, because it doesn't produce a shippable artifact. Include:

- Engineers or teams you unblocked, even briefly
- People you mentored, formally or not, and what changed for them
- Reviews, design critiques, or escalations where your involvement changed the outcome
- Any case where your judgment was sought out specifically because of a reputation you'd built

### Cross-functional and executive influence

At senior levels this is often where the real impact lives and where it's easiest to lose track of. Roadmap decisions you shaped without owning the roadmap. Reporting or analysis that changed how leadership allocated investment. A framework or standard you introduced that other teams adopted without being told to.

### Standards, documentation, and systems that outlast the project

Anything you built that keeps producing value after you've moved on, such as a measurement framework, a golden-path template, a runbook that's now how the org does something. Include adoption numbers if you have them; they're usually more persuasive than the artifact itself

### What you learned

Skills, domains, or tools you meaningfully leveled up on. This section is easy to skip, but genuinely useful - it's the fastest way to notice, a year later, that you didn't grow the direction you meant to.

### Outside the day job

Talks, writing, open source, community involvement, industry recognition. Optional, but if you're building a public technical reputation, this is where the evidence for it lives.

## Rules I follow

- **Toss links in raw, refine on a schedule - never in the moment**  the habit dies the first week you try to write polished prose while still mid-project
- **You, not the team, in the Behavior line** - "we shipped X" tells a reviewer nothing about your contribution; "I designed the rollout sequence and drove adoption across 10 orgs" does
- **A number beats an adjective, every time** - if you don't have one, get specific instead of vague; "adopted by every platform team within two quarters" is not a number, but it's still concrete
- **Don't wait to fill in the impact** - go back a few months after launch and update the entry with what actually happened; the impact you predicted at ship time is rarely the impact you can prove later, and the later number is the one that survives scrutiny
- **Fuzzy work goes in, explicitly** - improving on-call, raising code review quality, reducing tech debt - none of this produces a launch email, all of it is real; state the goal, what you did toward it, and any effect you observed, even an indirect one
- **Share it** - with your manager, with peer reviewers or mentors, with a new manager who inherited you three months before a review cycle

## Conclusion

A brag document is not about making your work sound better than it was. It's about making it sound exactly as good as it was...which, if you've been doing real work, is usually more than you'd remember unprompted. The discipline isn't the writing. It's the two-minute habit of capturing the moment it happens, so that by the time anyone asks you to prove your year, you're editing a record instead of reconstructing a memory.
