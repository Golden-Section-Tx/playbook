---
order: 68
slug: saas-seasonal-churn-segmentation
anchor: seasonal-churn
title: Seasonal Churn Segmentation
h1: How to Stop Seasonal Pauses From Counting as Churn
category: customer
players: Founder, CFO, CS Lead
initialEffort: 8 SP
ongoingEffort: 5 SP
frequency: Monthly
stage: Growth
summary: Tag every seasonal pause the moment it happens and keep it out of your churn ledger, so net revenue retention reflects who actually left instead of who will be back in the spring.
keywords:
  - churn
  - seasonal churn
  - net revenue retention
  - NRR
  - exit readiness
  - customer success
questions:
  - How do I stop seasonal cancellations from showing up as churn?
  - What is the difference between a seasonal pause and real churn?
  - How do I report retention to a board when a third of my book goes quiet every winter?
preventsMistakes:
  - 57
  - 167
---
A tour operator books nothing in January. A holiday lighting company books nothing in July. If your product serves a seasonal industry, some share of your customers will cancel or downgrade every year on a schedule, then come back the next season and buy again. Log that the same way you log a customer who quit for good, and your churn number goes up every winter whether or not you did anything wrong.

That is not a rounding error. A board prices your growth off net revenue retention. A bank prices a covenant off it. An acquirer prices the whole company off the worst-looking cohort in the book. A company that watched its own churn events climb every winter for years, then recomputed retention with seasonal pauses pulled out, found a materially stronger number than the one it had been reporting the whole time. Nobody had lied. Nobody had checked.

> **The goal:** A churn ledger that tags a seasonal pause the moment it happens, separate from real churn, so your reported retention number is the true one.

#### Background

Two things get confused when they should not be. A seasonal pause is a customer following a calendar you already know, because you sold to that vertical on purpose. Real churn is a customer who is gone and staying gone. The two produce the same event in most billing systems, a canceled subscription, and from there they get counted the same way unless someone builds the second bucket.

The fix is not to hide the pause. It is to name it, watch it, and hold it to a standard: a seasonal account has to actually come back, on schedule, or it graduates into real churn and counts against you like it should.

#### Steps

1. Define the season, in writing, before you tag a single account. For each customer segment that follows a calendar, write down the months it goes quiet and the month it should return. Get this from the customer's business, not from your billing data. Ask them when they close instead of inferring it from when they stopped paying.
2. Tag the pause at cancellation, not later. When a seasonal account cancels or downgrades inside its known window, mark it "seasonal pause" in the same system that logs churn, with the expected return date attached. Every other cancellation is churn until proven otherwise.
3. Set a grace period and a graduation rule. Give a seasonal account a fixed number of weeks past its expected return date. If it has not reactivated by then, move it out of the seasonal bucket and into real churn, dated to when the grace period expired, not to when you noticed.
4. Recompute retention on committed revenue, not logo count. Net revenue retention should net out seasonal-pause revenue for the months an account is expected to be paused, then include it again the month it returns. A twelve-month trailing view smooths this out; a monthly view does not, and monthly is what a board asks for first.
5. Report both numbers, every time, to the same audience. Show gross churn including seasonal pauses, and net churn with them pulled out. The gap between the two is itself worth watching. It tells you how much of your book is seasonal, and whether that share is growing.
6. Review the ledger monthly. The CS Lead owns the seasonal tag and the graduation rule. The Founder or CFO owns the recomputed retention number that goes to the board. An account reactivating outside its expected window, early or late, is worth a look. It usually means something changed in that customer's business before they told you.

#### Troubleshooting

*This just sounds like a way to make the churn number look better.* It would be, if the seasonal bucket were a place accounts go to disappear. It is not. The grace period and the graduation rule mean a seasonal account that does not come back becomes real churn on a fixed date, counted in full. The two-number report is what keeps this honest: if your gross and net numbers never move relative to each other, the tag is being applied too generously.

*My board wants one number, not two.* Give them the net number as the headline and the gross number as a footnote, with the seasonal share named. A board member who later finds out a third of your "growth" was seasonal accounts coming back on schedule will ask why nobody said so.

<!-- GS:LINKS start — generated by scripts/build.mjs, do not edit by hand -->

---

**Prevents** · [#57 Not benchmarking results](../../MISTAKES.md#m057) · [#167 Counting a seasonal pause as churn](../../MISTAKES.md#m167)

**Category** · [Customer](../README.md) · **Effort** · 8 SP initial, 5 SP ongoing · **Cadence** · Monthly

<!-- GS:LINKS end -->
