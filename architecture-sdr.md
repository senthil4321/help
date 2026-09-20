# ADR-[NUMBER]: [Short, Action-Oriented Title]

* **Status:** [Proposed | Accepted | Rejected | Superseded by ADR-XXXX | Deprecated]
* **Date:** YYYY-MM-DD
* **Deciders:** [List of key stakeholders and engineers involved]
* **Technical Context:** [Link to JIRA ticket, GitHub issue, or PRD]

## Context
[Describe the architectural issue or business requirement. Explain the background, current state, and the problem that needs to be solved. Keep this objective and focused on facts.]

## Decision Drivers
* [Driver 1: e.g., Sub-100ms latency requirement for checkout]
* [Driver 2: e.g., Need strong ACID compliance for order processing]
* [Driver 3: e.g., Operational budget limits for cloud infrastructure]

## Options Considered
* **Option 1:** [Option 1 Name]
* **Option 2:** [Option 2 Name]
* **Option 3:** [Option 3 Name]

## Decision Outcome
Chosen Option: **[Option Name]**, because [state core rationale briefly].

### Positive Consequences
* [Benefit 1]
* [Benefit 2]

### Negative Consequences & Trade-offs
* [Drawback or risk 1, plus any planned mitigation]
* [Drawback or risk 2]

## Pros and Cons of Options

### Option 1: [Option 1 Name]
* **Good, because** [Pro 1]
* **Good, because** [Pro 2]
* **Bad, because** [Con 1]

### Option 2: [Option 2 Name]
* **Good, because** [Pro 1]
* **Bad, because** [Con 1]
* **Bad, because** [Con 2]

--- 

# ADR-0012: Adopt gRPC for Inter-Service Communication

* **Status:** Accepted
* **Date:** 2026-03-15
* **Deciders:** Jane Doe (Lead Architect), John Smith (Backend Staff Engineer)
* **Technical Context:** [PROJ-4021] Core Payment Pipeline Performance Optimization

## Context
Our internal microservice communication relies entirely on HTTP/REST with JSON payloads. As the platform expanded to over 40 services, payload sizes and HTTP/1.1 connection overhead have caused latency spikes in our checkout pipeline. We need a faster, type-safe serialization format for high-throughput internal communication.

## Decision Drivers
* Internal P99 API response time must remain under 50ms during peak load.
* Strong type safety across Go and Node.js microservices.
* Minimal operational overhead for maintaining API schemas.

## Options Considered
* **Option 1:** REST over HTTP/1.1 with JSON payloads (Status Quo)
* **Option 2:** gRPC over HTTP/2 with Protocol Buffers
* **Option 3:** GraphQL over HTTP/1.1

## Decision Outcome
Chosen Option: **Option 2 (gRPC)**, because it delivers significantly smaller binary payloads, multiplexing over HTTP/2, and strict contract generation across multiple languages.

### Positive Consequences
* **Performance:** Payload sizes reduced by ~60% and network latency decreased by 35% in staging benchmarks.
* **Type Safety:** Automated code generation via `.proto` files eliminates manual API client construction.
* **Streaming:** Enables native bidirectional streaming for real-time order tracking services.

### Negative Consequences & Trade-offs
* **Debugging Friction:** Binary payloads make inspection via traditional tools (e.g., standard `curl`) harder without dedicated tooling like `grpcurl`.
* **Browser Limitations:** Web clients cannot consume gRPC directly without gRPC-Web proxies (REST will be retained for public-facing edge APIs).

## Pros and Cons of Options

### Option 1: REST over HTTP/1.1 with JSON
* **Good, because** simple to debug with standard tools and universally understood by developers.
* **Bad, because** JSON serialization and text-based HTTP payloads introduce high CPU and bandwidth overhead.
* **Bad, because** API contracts rely on OpenAPI specs that frequently drift out of sync with code implementations.

### Option 2: gRPC over HTTP/2 with Protocol Buffers
* **Good, because** binary protocol offers superior serialization speed and lower network footprint.
* **Good, because** HTTP/2 multiplexing allows multiple concurrent calls over a single TCP connection.
* **Bad, because** steeper learning curve for team members unfamiliar with Protocol Buffers and gRPC tooling.

### Option 3: GraphQL over HTTP/1.1
* **Good, because** allows callers to query exact data fields required.
* **Bad, because** introduces query-parsing CPU overhead and complex caching requirements for internal service-to-service calls.
