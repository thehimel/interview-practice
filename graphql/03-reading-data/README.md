# Reading Data

**Query operations** are how clients read data from a GraphQL API. You start at the root `Query` type, select fields, and traverse nested objects until you reach scalar or enum values.

## Fields

At its simplest, a query selects **fields** on objects:

```graphql
{
  currentUser {
    id
    name
  }
}
```

The result shape matches the query. Fields that return objects allow **sub-selections**:

```graphql
{
  currentUser {
    id
    name
    profile {
      bio
      avatarUrl
    }
  }
}
```

## Arguments

Fields can accept **arguments** to filter or customize the result:

```graphql
{
  user(id: "42") {
    name
  }
}
```

Every field can have its own arguments. For example, a `price` field might accept a `currency` argument.

## Operation Type and Name

You can make the operation explicit and give it a name:

```graphql
query CurrentUserProfile {
  currentUser {
    id
    name
  }
}
```

- **Operation type:** `query`, `mutation`, or `subscription`.
- **Operation name:** Helps with logging and debugging.

For a single anonymous query, the `query` keyword can be omitted. Named operations require the type.

## Aliases

When you request the same field with different arguments, the result keys would collide. Use **aliases** to rename the output:

```graphql
query {
  firstUser: user(id: "1") {
    name
  }
  secondUser: user(id: "2") {
    name
  }
}
```

The response will have `firstUser` and `secondUser` instead of two `user` entries.

## Variables

Hardcoding values in the query string is inflexible. **Variables** let you pass dynamic values:

```graphql
query UserById($userId: ID!) {
  user(id: $userId) {
    name
  }
}
```

Variables are declared with `$name: Type`. The client sends a separate variables map: `{ "userId": "42" }`.

### Default Variables

Optional variables can have defaults:

```graphql
query Users($limit: Int = 10) {
  users(limit: $limit) {
    id
    name
  }
}
```

If `limit` is not provided, `10` is used.

## Fragments

**Fragments** are reusable selection sets. They reduce repetition when the same fields appear in multiple places:

```graphql
query {
  userA: user(id: "1") {
    ...UserFields
  }
  userB: user(id: "2") {
    ...UserFields
  }
}

fragment UserFields on User {
  id
  name
  email
}
```

Fragments are defined with `fragment Name on Type { ... }` and spread with `...Name`.

### Inline Fragments

When a field returns an **interface** or **union**, use **inline fragments** to request type-specific fields:

```graphql
query {
  search(term: "graphql") {
    __typename
    ... on User {
      name
      email
    }
    ... on Post {
      title
      slug
    }
  }
}
```

`... on Type` applies the selection only when the runtime type matches.

## Meta Fields

**`__typename`** is a built-in field that returns the concrete type name at that point in the query. Useful for unions and interfaces.

`__schema` and `__type` support introspection (covered in Schema Discovery).

## Directives

**Executable directives** change which parts of a query run based on variables:

| Directive        | Purpose                                      |
|------------------|----------------------------------------------|
| `@include(if: Boolean)` | Include the field only when `if` is true  |
| `@skip(if: Boolean)`    | Skip the field when `if` is true          |

```graphql
query User($includeEmail: Boolean!) {
  currentUser {
    name
    email @include(if: $includeEmail)
  }
}
```

## Summary

| Feature      | Use Case                                      |
|--------------|-----------------------------------------------|
| **Fields**   | Select data; traverse nested objects           |
| **Arguments**| Filter or customize field results             |
| **Aliases**  | Request the same field multiple times with different args |
| **Variables**| Pass dynamic values from the client           |
| **Fragments**| Reuse selection sets across the query         |
| **Inline fragments** | Query type-specific fields on interfaces/unions |
| **Directives** | Conditionally include or skip fields        |

Next: [Writing Data](../04-writing-data/README.md) — Mutations for creating, updating, and deleting.
