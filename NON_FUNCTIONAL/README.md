# Non-Functional Requirements (NFRs)

In the Decision-Driven Development framework, NFRs are first-class citizens. They are not checked at the end; they are designed from the beginning.

## Definition
NFRs define the **quality attributes** of the system (e.g., Security, Performance, Reliability, Maintainability, Usability).

## Handling NFRs

### 1. In Decisions
*   Architectural choices must explicitly evaluate NFR impact.
*   *Example*: "We choose PostgreSQL over Redis for persistence (Decision) because Reliability (NFR) is prioritized over Latency (NFR) for this use case."

### 2. In Specs
*   Every Spec must have a dedicated **NFR Section**.
*   Requirements must be **quantifiable** where possible.
    *   *Bad*: "The system should be fast."
    *   *Good*: "The API latency must be < 200ms for 95% of requests at 100 RPS."

### 3. In Implementation
*   **Performance Tests**: Automated tests that fail if latency thresholds are exceeded.
*   **Security Scans**: Automated static analysis (SAST/DAST) in the CI pipeline.

## Standard NFR List
(Adopt and adapt these for every project)

1.  **Security**: Authentication, Authorization, Data Encryption.
2.  **Performance**: Latency, Throughput.
3.  **Scalability**: Horizontal vs Vertical, Database limits.
4.  **Reliability**: Uptime, Recovery Time Objective (RTO).
5.  **Observability**: Logging, Metrics, Tracing.
6.  **Maintainability**: Code style, Documentation, Test coverage.
