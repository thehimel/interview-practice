# Field Resolution

**Resolution** is the process of computing values for each field in a query. The server uses **resolver functions** (or equivalent logic) to fetch or compute data. Understanding resolution helps you reason about performance and error handling.

## Resolvers

Each field can have a **resolver** — a function that returns the value for that field. Resolvers receive:

- **Parent** — The value from the parent field (null for root fields).
- **Arguments** — The arguments passed to the field.
- **Context** — Shared data (e.g., request, database, auth).
- **Info** — Metadata about the field and schema.

Conceptually, each field is a function: `(parent, args, context) → value`.

## Root Fields

Resolution starts at the root operation type (`Query`, `Mutation`, or `Subscription`). For a query:

```graphql
{
  user(id: "42") {
    name
  }
}
```

The `user` resolver runs first. It receives `args: { id: "42" }` and returns a user object. Then the `name` resolver runs with that object as the parent.

## Trivial Resolvers

Many fields need no custom logic. If a resolver is omitted, implementations often use a default: return the property with the same name from the parent. For `name` on a user object, the default might be `parent["name"]` or `parent.name`.

## Async Resolution

Resolvers can be **asynchronous**. Loading from a database or another service returns a Promise (or equivalent). The runtime waits for async values before continuing. Sibling fields can resolve in parallel when they have no dependency on each other.

## Scalar Coercion

Resolvers may return values that differ slightly from the schema. For example, an enum field might be stored as an integer internally. The server **coerces** the value to match the declared type (e.g., mapping `4` to `"SHIPPED"`). Coercion happens at the boundary between resolver output and the response.

## List Resolution

When a field returns a list of objects, the resolver returns an array. The runtime then resolves each item's sub-fields. If the resolver returns IDs and the schema expects full objects, the resolver (or a nested layer) must fetch those objects — GraphQL does not auto-expand IDs.

## Building the Result

As each field resolves, its value is placed in a result map keyed by the field name (or alias). The process continues from leaves back to the root. The final structure mirrors the query shape and is serialized (usually as JSON) for the client.

## Summary

| Concept          | Description                                      |
|------------------|--------------------------------------------------|
| **Resolver**     | Function that provides a field's value           |
| **Root fields**  | Entry points; start resolution                    |
| **Async**        | Resolvers can return Promises; runtime awaits    |
| **Coercion**     | Values are converted to match schema types       |
| **Result shape** | Mirrors the query structure                      |

Next: [Response Format](../08-response-format/README.md) — Structure of server responses.
