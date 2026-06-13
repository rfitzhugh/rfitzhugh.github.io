---
title: "Technical Design: Conceptual, Logical, Physical"
date: "2017-07-07T16:00:21+00:00"
modified: "2018-08-06T05:02:47+00:00"
slug: "conceptual-logical-physical"
author: "Rebecca"
categories:
  - "Architecture"
---

One of the things that I have noticed as I do design reviews is that many engineers do not correctly document conceptual, logical, and physical design.

The best non-tech example that I have seen of this concept the following image:

![alt text](/images/2017/07/idea.jpeg)

The way I always describe and diagram design methodology is using the following image:

![alt text](/images/2017/07/concept.png)

I will continue to refer to both images as we move forward in this post.

# **Conceptual**

During the assess phase, the architect reaches out to the business’ key stakeholders for the project and explore what each need and want to get out of the project. The job is to identify key constraints and the business requirements that should be met for the design, deploy, and validation phases to be successful.

The assessment phase typically coincides with building the conceptual model of a design. Effectively, the conceptual model categorizes the assessment findings into requirements, constraints, assumptions, and risks categories.

For example:

**Requirements**

1.  technicloud.com should create art.
2.  The art should be durable and able to withstand years of appreciation.
3.  Art should be able to be appreciated by millions around the world.

**Constraints**

1.  Art cannot be a monolithic installation piece taking up an entire floor of the museum.
2.  Art must not be so bourgeoisie that it cannot be appreciated with an untrained eye.
3.  Art must not be paint-by-numbers.

**Risks**

1.  Lead IT architect at technicloud.com has no prior experience creating art.
    - Mitigation – will require art classes to be taken at local community college.
2.  Lead IT architect is left-handed which may lead to smearing of art.
    - Mitigation – IT architect will retrain as ambidextrous.

**Assumptions**

1.  Art classes at community college make artists.
2.  Museum will provide security as to ensure art appreciators do not damage artwork.

As you read through the requirements and constraints, the idea of how the design should look should be getting clearer and clearer. More risks and assumptions will be added as design decisions are made and the impact is analyzed. Notice that the conceptual model was made up entirely of words? Emphasis on “concept” in the word “conceptual”!

# **Logical**

Once the conceptual model is built out, the architect moves into the logical design phrase (which indicated by the arrows pointing backwards in Figure 2, demonstrating dependence on conceptual). Logical design is where the architect begins making decisions but at a higher level.

**Logical art work design decisions**

1.  Art will be a painting.
2.  The painting will be of a person.
3.  The person will be a woman.

For those who are having a hard time following with the art example, a **tech example** would be:

![alt text](/images/2017/07/ldd.png)

An example of what a logical diagram may look something like this:

![alt text](/images/2017/07/logical.png)

Notice that these are ‘higher’ level decisions and diagrams. We’re not quite to filling in the details yet when working on logical design. However, note that these design decisions should map back to the conceptual model.

# **Physical**

Once the logical design has been mapped out, architect moves to physical design where hardware and software vendors are chosen and configuration specifications are made. Simply put, this is the phase where the details are determined.

**Physical art work design decisions –**

1.  The painting will be a half-length portrait.
2.  The medium will be oil on a poplar panel.
3.  The woman will have brown hair.

Once again, if you hate the Mona Lisa then the **technical design decision example** would be:

1.  XYZ vendor and model of storage array will be purchased.
2.  Storage policy based management will be used to place VMs on the correct storage tier.
3.  Tier-1 LUNs will be replicated hourly.

These are physical design decisions, which directly correlate and extend the logical design decisions with more information. But, again, at the end of the day, this should all tie back to meeting the business requirements.

![alt text](/images/2017/07/pdd.png)

An example of a physical design would be something like:

![alt text](/images/2017/07/phys.png)

Notice that in this diagram, we’re starting to see more details: vendor, model, how things are connected, etc. Remember that physical should expand on logical design decisions and fill in the blanks. At the end of the day, both logical and physical design decisions should map back to meeting the business requirements set forth in the conceptual model (as evidenced by Figure 2).

# **Final Thoughts**

Being able to quickly and easily distinguish takes time and practice. I am hoping this clarifies some of the mystery and confusion surrounding this idea.