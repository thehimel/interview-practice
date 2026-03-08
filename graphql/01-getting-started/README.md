# Getting Started

GraphQL is a **query language** for APIs and a **runtime** for running those queries against a schema you define. Unlike REST, where endpoints dictate the shape of responses, GraphQL lets clients describe exactly what data they need.

## What GraphQL Is

- **Query language** — Clients send structured requests that describe the shape of the result.
- **Type system** — Every API exposes a schema that defines types and fields.
- **Runtime** — A server executes queries against that schema and returns matching data.

GraphQL is not tied to a specific database or language. You implement it on top of your existing backend (e.g., Python with FastAPI and Strawberry, Node.js, Go, etc.).

## Core Idea: Ask for What You Need

In REST, a call to `/users/1` might return a full user object with many fields. The client cannot easily request only `id` and `name`. With GraphQL, the client specifies the fields:

```graphql
{
  user(id: "1") {
    id
    name
  }
}
```

The response mirrors the request shape. No over-fetching, no under-fetching.

## Schema and Types

A GraphQL **schema** describes what data exists and how it can be queried. It is built from **types** and **fields**:

```graphql
type User {
  id: ID!
  name: String
}

type Query {
  user(id: ID!): User
}
```

- `Query` is the entry point for read operations.
- `user` is a field that takes an `id` and returns a `User`.
- `User` has `id` and `name` fields.

## Request Flow

1. **Client** sends a document (query, mutation, or subscription).
2. **Server** parses and validates it against the schema.
3. **Server** executes the operation and returns data (or errors) in a structured response.

## Evolving Without Versioning

GraphQL supports **additive changes** without breaking clients. You can add new fields and deprecate old ones. Clients that do not request deprecated fields keep working. When a field is no longer used, you can remove it.

## Key Takeaways

| Concept        | Description                                                |
|----------------|------------------------------------------------------------|
| **Schema**     | The type system that defines what can be queried           |
| **Query**      | Operation for reading data                                 |
| **Mutation**   | Operation for changing data                                |
| **Subscription** | Operation for real-time updates                         |
| **Resolver**   | Server-side function that provides data for a field       |

Next: [Type System](../02-type-system/README.md) — Object types, scalars, enums, and more.
