---
order: 74
slug: saas-ai-vendor-continuity
anchor: ai-vendor-continuity
title: AI Vendor Continuity
h1: How to Keep Access to the AI Models Your Product Depends On
category: vendor
players: CTO, Founder, CFO
initialEffort: 13 SP
ongoingEffort: 3 SP
frequency: Quarterly
stage: Early Traction
summary: Rank the ways you could lose model access, build portability you actually exercise, and buy committed capacity in proportion to the revenue at risk—before a vendor makes the decision for you.
keywords:
  - AI vendor risk
  - model portability
  - inference capacity
  - vendor concentration
  - committed capacity
  - failover testing
  - infrastructure diligence
questions:
  - What happens to my product if my model provider cuts me off?
  - Should I self-host an open-weight model as a backup?
  - How much should I spend insuring against losing model access?
  - How do I know whether my hosting provider actually owns its infrastructure?
  - Is my failover real if I have never run traffic through it?
preventsMistakes:
  - 92
  - 170
---
Once an AI feature is in your product, a third party you do not control sits inside your critical path. The question is not whether that is risky—it is which risk, and how much it is worth spending to cover.

> **The goal:** Your product keeps working, in a known and degraded-but-acceptable state, when a model vendor raises prices, tightens limits, deprecates a model, or stops selling to you.

#### Background

Founders reliably rank these risks in the wrong order. The usual instinct is to worry about a dramatic physical event—a regional grid failure, a data center going dark—and to under-weight the mundane commercial one. The order of likelihood is the reverse:

1. **Commercial deprioritization.** Your vendor changes its terms, withdraws a capacity product, deprecates the model your prompts are tuned to, or simply serves larger contracts first when demand spikes. This is the common case, it arrives by email, and small accounts absorb it first.
2. **Capability and quality drift.** A model version changes underneath you and your outputs move. Your evaluation suite either catches this or you learn from a customer.
3. **Physical or regulatory interruption.** A grid event or a regulator-ordered curtailment takes a facility offline. Real, rare, and the one most likely to be over-engineered against.

Two structural facts shape the response.

*Your fallback does not have to match your primary.* A smaller open-weight model running on modest hardware will not equal a frontier model, and does not need to. What it needs to do is keep the workflow functioning at reduced capability while you recover. Decide in advance what "degraded but acceptable" means for your product, and make sure your customer contracts permit it.

*A failover that has never carried production traffic is not a failover.* It is a configuration file and an assumption. The only way to know your second provider works is to keep sending it a small, continuous share of real requests.

*Owning hardware is almost never the right first move at this stage.* Buying accelerators means buying a depreciating asset with a three-to-six year economic life, plus the colocation, the spares and the person who owns it—to insure against a risk you have not yet experienced. It converts a margin question into a balance sheet question. Revisit it only when a vendor has actually restricted you, or when steady-state volume means the hardware would run at genuine utilization rather than sitting idle.

**The ladder, in order of return on spend:**

| Rung | What it is | Rough cost |
|---|---|---|
| 1 | Model portability: an abstraction layer, an evaluation suite, and continuous shadow traffic to a second provider | Engineering time, no capital |
| 2 | Committed or provisioned capacity bought from your primary provider, and a smaller commitment on the second | Low single-digit % of revenue |
| 3 | Reserved GPU capacity rented from a cloud provider on a term commitment | Materially more than rung 2 |
| 4 | Owned hardware in colocation | Capital, plus ongoing operations and a depreciating asset |

Most companies at this stage should be fully at rung 1, partially at rung 2, and nowhere near rungs 3 and 4.

#### Steps:

1. **Write down the failure modes and rank them.** For each of the three risks above, state what actually happens to your product, which customers notice first, and what your contracts oblige you to do about it.
2. **Define degraded mode explicitly.** Which features must keep working, which may fail, and what does the customer see? Check this against your SLA and your master service agreements before you need it.
3. **Build portability and prove it.**
    - Is every model call routed through one abstraction, or are provider SDKs scattered through the codebase?
    - Do you have an evaluation suite that scores output quality, so you can tell whether the second provider is good enough?
    - **Is a share of production traffic continuously served by the second provider?** If the answer is "we could switch," the answer is no.
    - What is your gross margin at the second-best model? If it is materially worse, that is a pricing decision, not just an engineering one.
4. **Size the insurance against revenue at risk, not against fear.** Work out the share of ARR that depends on the AI feature. Buy committed capacity in proportion to that number. Note that committed capacity is usually priced to break even only at very high sustained utilization—**budget it as an insurance premium, not as a discount**, and be sceptical of any account team that sells it as a saving.
5. **Diligence the vendors underneath your vendor.** For any hosting or infrastructure provider, ask for—and read:
    - The utility service or interconnection agreement **in the provider's own name**. A reseller cannot produce one, because the power contract belongs to whoever actually owns the facility. This is the single most diagnostic document.
    - The SOC 2 Type II **with the entity name on the cover checked**, and the carve-out section read. Controls carved out to a subservice organization are where reselling becomes visible.
    - Title to the specific hardware serving you, and whether it is pledged as collateral to a lender.
    - Facility certification of the **constructed facility**, with a registry number. "Built to Tier III standards" is marketing.
    - Hours of backup fuel **at your contracted load**, the resupply contract, whether it is guaranteed-delivery or best-efforts, and how many other customers hold the same priority claim.
    - Their written incident report from the last regional event in that market.
6. **Check your regulatory exposure to curtailment.** In some markets, large electrical loads now carry a mandatory obligation to disconnect on instruction from the grid operator during an emergency—uncompensated, and not capped by the size of any on-site generation. Ask your provider in writing whether the facility is a registered large load, how it is classified, and what its curtailment obligations are. Most providers have never been asked. A regulator-ordered curtailment is also precisely what a force-majeure clause exists to excuse, so your SLA will not protect you.
7. **Apply the counterparty test.** Do not buy continuity insurance from a vendor whose own continuity is uncertain. Ask for audited financials, the debt maturity schedule and customer concentration. A provider whose hardware is pledged against debt maturing inside your contract term is a risk, not a mitigation.
8. **Review quarterly.** Re-run the ranking, confirm shadow traffic is still flowing, confirm the second provider still passes evaluation, and re-check vendor terms for changes to capacity products and model deprecation schedules.

#### A note on figures

Specific prices in this area move fast enough that quoting them dates the play. Two anchors that have held: committed capacity from a major provider is generally available at a low single-digit percentage of revenue for a company at this stage, and owned hardware does not beat reserved rental on a three-year horizon at small scale. Get three written quotes before budgeting anything.

<!-- GS:LINKS start — generated by scripts/build.mjs, do not edit by hand -->

---

**Prevents** · [#92 Lack of vendor contract control](../../MISTAKES.md#m092) · [#170 Assuming your model vendor will keep selling you capacity](../../MISTAKES.md#m170)

**Category** · [Vendor](../README.md) · **Effort** · 13 SP initial, 3 SP ongoing · **Cadence** · Quarterly

<!-- GS:LINKS end -->
