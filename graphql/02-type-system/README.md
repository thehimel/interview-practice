# Type System

The GraphQL **type system** describes what data an API exposes. The schema is the collection of types and fields that clients can request. This chapter covers the main building blocks.

## Object Types and Fields

**Object types** represent entities you can fetch. Each has a name and a set of **fields**:

```graphql
type Product {
  id: ID!
  title: String!
  price: Float
}
```

- `Product` is an Object type.
- `id` and `title` use `!` for **non-null** — the server must return a value.
- `price` is nullable (no `!`).

### Field Arguments

Fields can take **arguments** to customize the result:

```graphql
type Product {
  id: ID!
  title: String!
  price(currency: Currency = USD): Float
}

enum Currency {
  USD
  EUR
}
```

Arguments are named. The `currency` argument has a default of `USD`, so it is optional.

## Root Operation Types

Every schema has at least a **Query** type as the entry point for reads. Optionally, **Mutation** and **Subscription** types handle writes and real-time updates:

```graphql
type Query {
  product(id: ID!): Product
}

type Mutation {
  createProduct(input: ProductInput!): Product
}

type Subscription {
  productUpdated: Product
}
```

You can rename these via the `schema` keyword if needed.

## Scalar Types

**Scalars** are leaf types — no sub-fields. GraphQL provides five built-in scalars:

| Scalar   | Description                                      |
|----------|--------------------------------------------------|
| `Int`    | Signed 32-bit integer                             |
| `Float`  | Double-precision floating-point                   |
| `String` | UTF-8 character sequence                         |
| `Boolean`| `true` or `false`                                 |
| `ID`     | Unique identifier; serialized like `String`       |

Servers can define custom scalars (e.g., `Date`, `JSON`).

## Enum Types

**Enums** restrict a value to a fixed set of options:

```graphql
enum OrderStatus {
  PENDING
  SHIPPED
  DELIVERED
}

type Order {
  id: ID!
  status: OrderStatus!
}
```

Use enums when a field has a finite set of valid values.

## Type Modifiers

### Non-Null (`!`)

Adding `!` means the value cannot be `null`:

```graphql
name: String!    # always a string
title: String   # string or null
```

### List (`[]`)

Square brackets denote a list of values:

```graphql
tags: [String!]!   # non-null list of non-null strings
tags: [String]!    # non-null list; items may be null
tags: [String!]    # nullable list; items are non-null
```

## Interface Types

**Interfaces** define a contract: any implementing type must include those fields:

```graphql
interface Node {
  id: ID!
}

type User implements Node {
  id: ID!
  email: String
}

type Post implements Node {
  id: ID!
  title: String
}
```

When a field returns an interface, clients use **inline fragments** to request type-specific fields.

## Union Types

**Unions** represent "one of several types" without shared fields:

```graphql
union SearchResult = User | Post | Tag

type Query {
  search(term: String!): [SearchResult!]!
}
```

Clients must use inline fragments to query fields on each possible type.

## Input Object Types

**Input types** let you pass structured objects as arguments (common in mutations):

```graphql
input CreateProductInput {
  title: String!
  price: Float
}

type Mutation {
  createProduct(input: CreateProductInput!): Product
}
```

Input types cannot have arguments on their fields. Use only scalars, enums, and other input types.

## Directives

**Directives** modify schema or operation behavior. The built-in `@deprecated` marks fields for removal:

```graphql
type User {
  fullName: String
  name: String @deprecated(reason: "Use fullName instead.")
}
```

## Documentation

Add descriptions with triple-quoted strings or `"` for single lines:

```graphql
"""
A product in the catalog.
"""
type Product {
  "The product display name."
  title: String!
}
```

Descriptions appear in introspection and tooling.

## Summary

| Type Kind     | Purpose                                      |
|---------------|----------------------------------------------|
| **Object**    | Entity with fields                           |
| **Scalar**    | Leaf value (Int, String, etc.)               |
| **Enum**      | Fixed set of values                          |
| **Interface** | Shared contract for multiple types          |
| **Union**     | One of several types                         |
| **Input**     | Structured input for arguments               |

Next: [Reading Data](../03-reading-data/README.md) — Queries, fields, variables, fragments.
