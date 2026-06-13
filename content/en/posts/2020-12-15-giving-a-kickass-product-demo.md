---
title: "Giving a Kickass Product Demo"
date: 2020-12-15
slug: "giving-a-kickass-product-demo"
categories:
  - "Technical Craft"
---

Technologists of all career paths should be able to ace giving a technical demo — not just folks in public facing roles. As an architect, product manager, or engineer you may need to give an internal product demo for a prototype or proof of concept. It takes a mix of science (methodology) and art (storytelling) to give a kickass demo. 

This post summarizes the methodology established by our team to ensure consistently successful demonstrations and a repeatable pattern that could be adopted by other public speakers. 

## Introducing the “Tan France Method” 

Earlier this year, I led a session track, co wrote the product keynote, and presented a new product announcement at the inaugural Rubrik FORWARD conference. During this time, our team hunkered down to study what makes a technical demo successful. We determined that a presenter with great demo has a defined: 

- **Structure** 🗺️ – story-based narrative with a clear progression, think a three-act structure
- **Focus 📍**– addresses a specific use case or workflow and doesn’t meander
- **Audience** 👥 – defined persona(s) that will be viewing this demonstration

When conducting a product or feature demonstration, I use a simple 3-step method that our team referred to as the Tan France Method™️. For those unfamiliar, Tan France is a stylist, fashion designer, and style icon that often uses a simple instructional method when styling someone.

![alt text](/images/2020/12/tanfrance.png)

Now, let’s apply this methodology to a technical product demo. It consists of the following steps:

1.  **Set it up** – consider using a slide that quickly summaries the demo, intended outcomes, and any applicable metrics and status. Keep it simple and use it to streamline the demo introduction. Explain exactly what the viewer is about to see: *“In this demonstration, I will show you how to configure X. This consists of two steps, first A and then B.”* Be sure to include any additional context that the viewer will need.

![alt text](/images/2020/12/demo.gif)

2.  **Do the thing** – “Imagine I am a *\[persona\]* attempting to *\[insert action or workflow\]*…” and complete the problem statement. Explain the value proposition of what you’re about to demonstrate and outline any key constructs. Demo the thing! Only show one action at a time. If you are showing multiple actions, make sure there’s connective tissue tying these actions together into a workflow. Let’s illustrate this idea by connecting provisioning and policy management actions:

😐 “*while the instance is provisioning, let’s look at policies. A policy can be assigned to an instance to enforce a number of security and data retention requirements.”*

🤩 “*a benefit of this design is that you can apply policies during provisioning. This means that as soon as an instance starts, it has already inherited the assigned policies and is compliant to any security or data retention standards. While this instance is provisioning, let’s take a look at policies.”*

Though it may be tempting to make an ad-hoc change during the demo, stick to the script and stay focused on the task at hand. It is important to have a logical flow to the story being told in the demonstration. 

Your demo will fail if it is too product focused — think about the story you’re telling. Why should your audience care? The demo should be driving towards a clear outcome that solves the problem you set up at the beginning. I recommend reading the chapter on giving demos in Guy Kawasaki’s “The Macintosh Way”. He asserts that a good demo is short, simple, sweet, swift, and substantial. Outline your demo using these qualities as the foundation. 

3.  **Sum it up** – Don’t overthink this, it can be as simple as: *“In this demonstration, you saw X do 321, Y, and Z.”* Make sure to highlight any key result or emphasize the desired outcome. Similarly to \#1, I generally leverage a slide as a reminder to neatly wrap up the demo and move on. If code or config specs were shown during the demo, then I provide the code in a corresponding GitHub repository via a simple [bit.ly](https://bit.ly/) link on the demo summary slide. 

It may seem rote to introduce and conclude a technical demo in such a formal manner, but keep in mind that the viewer is generally seeing this for the first time. Repetition is the mother of learning. This methodology ensures that the viewer begins and ends the demonstration hearing the value proposition.

## Ace It

There have been demos in my career where I was flew by the seat of my pants but those days are gone. I strive to operate using the principle of 7 Ps: proper prior planning prevents piss poor performance. Simply put, your audience deserves better than you trying to figure it out in real-time. Here’s my process:

1.  **Outline or mindmap the demo** – be sure to highlight the “aha” moments. This helps me focus the narrative and ensure I’m telling a coherent and simple story. My demos are always use case driven and I like to reference specific customer examples throughout. Here’s an example of a mindmap created for a demonstration. 

![alt text](/images/2020/12/mindmap.jpg)

1.  **Build or prestage demo resources** – use simple, straightforward resource names but be a little creative (e.g. use “John the DBA” and “Jane DevOps” instead of “user1” and “user2”). 
2.  **Test and rehearse demo** – time yourself, if lengthy determine what else can be pre-staged using a little smoke & mirrors. This also ensures your main points are crisp and aren’t rushed. Sometimes nerves can make presenters a little rambly when speaking so it’s important to rehearse and lock in timings. Consider recording a backup copy in case there are issues on game day. 
3.  **Create intro/outro demo slide(s)**, as applicable – these are a reminder for me to make I begin and end with the intended outcome

Make sure to put thought to the aesthetics of your demo. Think of ways to make the demonstration more visually appealing: pleasing colors, bigger fonts, visible mouse. Thomas Maurer wrote a great post on this topic that you can find [here](https://www.thomasmaurer.ch/2020/01/how-to-create-great-tech-demos-and-presentations/).  

A word on live demos — *keep track of time and always have a backup plan*. Sometimes shit happens and things break. If something isn’t going to plan, do an initial assessment and make a judgement call. When on stage, I do a quick [OODA loop](https://fs.blog/2018/01/john-boyd-ooda-loop/) and then decide whether to bail out or troubleshoot the issue. It may be compelling for some to troubleshoot live and bring the audience on that journey with you. However, this is not always the case and can often lose the audience thus reducing the effectiveness of your demo. Keep in mind the audience, their user personas, and familiarity with the topic. For these reasons, it’s always handy to have a recording that you can narrative over in the worst case scenario.

## Summary

Giving a kickass demo should be a skill in every technologist’s repertoire. This post outlined a simple methodology that can be customized to fit the use case you plan to demo. Remember: proper prior planning prevents piss poor performance.