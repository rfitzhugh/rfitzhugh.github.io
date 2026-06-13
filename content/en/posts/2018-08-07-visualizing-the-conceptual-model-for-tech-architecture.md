---
title: "Visualizing the Conceptual Model for Technical Architecture"
date: 2018-08-07
slug: "visualizing-the-conceptual-model-for-tech-architecture"
categories:
  - "Architecture"
  - "VMware"
---

I have [previously written](/2017-07-07-conceptual-logical-physical.md) about putting together the conceptual model with logical and physical design; however, I want to dig a little deeper into the conceptual model. The conceptual model categorizes the assessment findings into requirements, constraints, assumptions, and risks:

- Business **requirements** are provided by key stakeholders and the goal of every solution is to achieve each of these requirements.
- **Constraints** are conditions that provide boundaries to the design.
  - These often get confused with requirements, but remember that a requirement should allow the architect to evaluate multiple options and make a design decision whereas a constraint dictates the answers and removes the ability for the architect to decide.
- **Assumptions** list the conditions that are believed to be true, but are not confirmed:
  - By the time of deployment, all assumptions should be validated.
- **Risks** are factors that might have a negatively affect the design.
  - All risks should be mitigated, if possible.

## Requirements

Describes what should be achieved in the project; describes what the solution will look like.

- *Example:* The organization should comply with Sarbanes-Oxley regulations.
- *Example:* The underlying infrastructure for any service defined as strategic should support a minimum of four 9s of uptime (99.99%).

The part that tends to trip people up is functional versus non-functional requirements.

### Functional Requirements

A requirement specifies a function that a system or component should perform. These may include:

- Business Rules
- Authentication
- Audit Tracking
- Certification Requirements
- Reporting Requirements
- Historical Data
- Legal or Regulatory Requirements

### Non-Functional Requirements

A non-functional requirement is a statement of how a system should behave. These may include:

- Performance – Response Time, Throughput, Utilization, Static Volumetric
- Scalability
- Capacity
- Availability
- Recoverability
- Security
- Manageability
- Interoperability

Often times, non-functional requirements will be laid out as constraints — the part makes this concept murkier. In the context of a VCDX design, these should typically be defined as a constraint, whereas requirements are more typically functional requirements. Be careful how you word a non-functional requirement: if it’s stated as a **must** and there is no room for the architect to make a decision, then it’s a constraint. But if it is a **should** statement is gives more than one choice for a design decision then leave it as a requirement.

## Constraints

Anything that limits the design choice made by the architect. If multiple options are not available to make a design decision, then it’s a constraint.

- *Example:* Due to a pre-existing vendor relationship, host hardware has already been selected.

If this is a bit difficult to grasp, don’t worry, you are in good company. This is a question that appears often.

![alt text](/images/2018/08/untitled.png)

In this example, because the business dictates that HP ProLiant blade servers **must** be used, then it is a constraint. This leaves no room for me, as the architect, to make a design decision — it has been already made for me.

## Assumptions

Assumptions are design components that are assumed to be valid without proof. Documented assumptions should be validated during the design process. This means by the time the design is implemented, there should be no assumptions.

- *Example:* The datacenter uses shared (core) networking hardware across production and nonproduction infrastructures.
- *Example:* The organization has sufficient network bandwidth between sites to facilitate replication.
- *Example:* Security policies dictate server hardware separation between DMZ servers and internal servers.

These examples are a bit of low-hanging fruit. Don’t be afraid to dig a little bit deeper. If there’s anything documented or stated without empirical proof, then it is an assumption and needs to be validated.

## Risks

A risk is *anything* that may prevent achieving the project goals. All risks should be mitigated with clear SOPs.

- *Example:* The organization’s main datacenter contains only a single core router, which is a single point of failure.
- *Example:* The proposed infrastructure leverages NFS storage, with which the storage administrators have no experience.

No design is perfect and it is important to document as many risks as you can identify. This will give you the opportunity to be prepared and craft mitigation plans. Not paying close attention here may leave the design in a vulnerable state.

## Additional Examples

Can you specify which conceptual model category is correct for each example?

|  |  |
|----|----|
| **Category** | **Description** |
| Requirement | The design should provide a centralized management console to manage both data centers. |
| Assumption | The customer provides sufficient storage capacity for building the environment. |
| Constraint | The storage infrastructure must use existing EMC storage arrays for this project. |
| Requirement | The platform should be able to function with project growth of 20% per year. |
| Assumption | Active Directory is available in both sites. |
| Requirement | Solution should leverage and integrate with existing directory services. |
| Risk | Both server racks are subject to the same environmental hazards. |
| Assumption | BC/DR plans will be updated to include new hardware and workloads. |
| Requirement | The SLA is 99% uptime. |
| Constraint | External access must be through the standard corporate VPN client. |
| Risk | Having vMotion traffic and VM data traffic on the same physical network can lead to security vulnerability because vMotion is clear text by default. |

## Resources

- [Differentiating between Functional and Nonfunctional Requirements](https://searchsoftwarequality.techtarget.com/answer/Differentiating-between-Functional-and-Nonfunctional-Requirements)
- [Working with design assumptions, the VCDX way](https://www.jeffreykusters.nl/2017/12/19/working-design-assumptions-vcdx-way/)
- [Risk management for the VCDX candidate](http://www.elasticsky.co.uk/risk-management-for-the-vcdx-candidate/)
