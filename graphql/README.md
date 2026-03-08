# GraphQL Tutorial

A documentation-based tutorial for learning GraphQL.

## How to Use

1. **Choose a chapter** — Each directory is a sequential chapter.
2. **Read [README.md](./01-getting-started/README.md)** — Study the concepts and examples for each chapter.
3. **Progress in order** — Chapters build on each other; start from 01.

## Chapters

| #  | Directory                 | Topic              | Description                                              |
|----|---------------------------|--------------------|----------------------------------------------------------|
| 01 | [01-getting-started](./01-getting-started/README.md)       | Getting Started     | What is GraphQL, key concepts, type system overview       |
| 02 | [02-type-system](./02-type-system/README.md)               | Type System         | Object types, Scalars, Enums, Interfaces, Unions, Inputs |
| 03 | [03-reading-data](./03-reading-data/README.md)             | Reading Data        | Fields, arguments, aliases, variables, fragments, directives |
| 04 | [04-writing-data](./04-writing-data/README.md)             | Writing Data        | Creating, updating, deleting data; purpose-built mutations |
| 05 | [05-realtime-updates](./05-realtime-updates/README.md)     | Realtime Updates    | Live data via subscriptions, pub/sub, transport considerations |
| 06 | [06-validating-requests](./06-validating-requests/README.md) | Validating Requests | Schema validation, request validation, error handling    |
| 07 | [07-field-resolution](./07-field-resolution/README.md)     | Field Resolution    | Resolvers, root fields, async execution, scalar coercion |
| 08 | [08-response-format](./08-response-format/README.md)      | Response Format     | Data, errors, extensions; partial responses               |
| 09 | [09-schema-discovery](./09-schema-discovery/README.md)     | Schema Discovery    | Introspection, `__schema`, `__type`, `__typename`        |
| 10 | [10-http-transport](./10-http-transport/README.md)         | HTTP Transport      | Endpoints, request/response format, headers, methods      |

## Backend References

When backend examples are needed, this tutorial uses:

- **Language:** Python
- **Framework:** FastAPI
- **GraphQL library:** Strawberry

The focus remains on **core GraphQL concepts**; backend references appear only when illustrating server-side behavior.

