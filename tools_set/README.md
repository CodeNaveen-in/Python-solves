# System Design Diagrams of Tools

## Bandname Generator

```mermaid
flowchart TD
    A[User] --> B[CLI / Terminal]

    B --> C[Greeting & Name Input]
    C --> D[City Name Input]
    D --> E[Pet Name Input]

    E --> F[Band Name Generator]

    F --> G[Concatenate City + Pet Name]

    G --> H[Display Generated Band Name]

    H --> I[Terminal Output]

    subgraph Python Application
        C
        D
        E
        F
        G
    end
```
