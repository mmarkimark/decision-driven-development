# Rule Hierarchy

This defines the authority order of rules in the methodology.

| Level | Authority | Scope |
|------|-----------|-------|
| 1️⃣ Decisions | Architecture and system model | Highest authority |
| 2️⃣ Architecture Rules | DDD boundaries of the method | Structural rules |
| 3️⃣ Domain Rules | Derivation, bugs, domain events | Domain behavior |
| 4️⃣ Workflow Rules | Git flow, Fast-Lanes, PR rules | Operational execution |
| 5️⃣ AI Constraints | How AI agents are allowed to operate | Agent boundaries |

Higher levels override lower ones.
