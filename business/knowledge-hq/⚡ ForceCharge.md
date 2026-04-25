---
mentor: "[[Jack M]]"
org: "[[Impression Empire]]"
source: "[[consulting-calls]]"
tags: [sma, jack-m, forcecharge]
---

# ⚡ ForceCharge

<aside>
📚 📚 Added from Skool Classroom — ForceCharge Course (April 2026)

</aside>

## What ForceCharge Is

Payment orchestration engine (not a processor). Routes charges through 25+ live gateways intelligently to maximize approval rates.

**Stats:** 99.2% approval rate, <80ms routing decision, 34 declined tokens recovered

## Why Declines Drop

- **Cross-border:** Matches card BIN country to gateway with local acquiring presence (typical 40% decline rate → near zero)
- **Security declines:** Cascades through multiple gateways with different fraud models
- **Merchant block recovery:** Routes as different acquirer/entity to get through merchant blocks on cards
- **Processor flagged:** Reroutes to alternative gateway with zero customer-facing interruption
- **Geosmart routing:** Matches local acquiring down to city level

## Whop Setup (One-Time)

1. Settings → Insert full name
2. Whop API: Whop dashboard → Developer → Create company API key (all permissions) → paste into ForceCharge
3. Whop Company ID: Top of browser URL after "dashboard" (biz_host ID) → paste
4. Whop Webhook: Create webhook → paste ForceCharge endpoint → set B1 → enable `membership_activated` + `payments_succeeded`

## Onboarding Existing Clients

- Send them a $1 product on Whop → they charge it → Whop saves card → ForceCharge auto-syncs
- Then you can manually charge them from the Customers tab

## Manual Charge Flow

- Open customer → type amount + note (e.g., "5 leads") → "Fire the charge"
- Routes through 25+ gateways automatically

## Ground Rules

**Allowed (requires written contract as consent):**

- Charging without client on phone
- Merchant block recovery — requires contract + call recording proof

**NEVER do:**

- Charge washing: max 2 manual retries/day; stop after 3 days
- Charge stolen/revoked cards (hard decline codes)
- Charge for services not yet delivered
- Split charges across gateways to obscure chargeback ratios
- Share merchant credentials with third parties

**Chargeback target:** Keep under 1%

**Every charge must have:** Billing descriptor (e.g., "5 leads — Contractor Growth") + advance client notification