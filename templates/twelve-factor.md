# Twelve-Factor Status

Tracking how this project measures against the
[Twelve-Factor App](https://12factor.net/) methodology. Each factor is
marked `pending`, `partial`, `done`, or `n/a` with a short note.
Update as deployment decisions are made and record the rationale in
an ADR. (Applies to deployable services; mark `n/a` throughout for
libraries, CLIs, and one-off scripts.)

| # | Factor | Status | Notes |
|---|--------|--------|-------|
| 1 | [Codebase](https://12factor.net/codebase) — one codebase tracked in revision control, many deploys | pending | |
| 2 | [Dependencies](https://12factor.net/dependencies) — explicitly declare and isolate | pending | |
| 3 | [Config](https://12factor.net/config) — store config in the environment | pending | no secrets in repo from day 1 |
| 4 | [Backing services](https://12factor.net/backing-services) — treat as attached resources | pending | |
| 5 | [Build, release, run](https://12factor.net/build-release-run) — strictly separate stages | pending | |
| 6 | [Processes](https://12factor.net/processes) — stateless, share-nothing | pending | |
| 7 | [Port binding](https://12factor.net/port-binding) — export services via port binding | pending | |
| 8 | [Concurrency](https://12factor.net/concurrency) — scale out via the process model | pending | |
| 9 | [Disposability](https://12factor.net/disposability) — fast startup, graceful shutdown | pending | |
| 10 | [Dev/prod parity](https://12factor.net/dev-prod-parity) — keep environments similar | pending | |
| 11 | [Logs](https://12factor.net/logs) — treat as event streams | pending | |
| 12 | [Admin processes](https://12factor.net/admin-processes) — run as one-off processes | pending | |

When a factor moves out of `pending`, link to the ADR that justifies
the implementation choice.
