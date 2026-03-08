# Schema Discovery

**Introspection** lets clients query the schema itself. You can discover types, fields, and documentation at runtime. This powers tools like GraphiQL and code generators.

## The `__typename` Meta-Field

Every object type exposes `__typename`, which returns the concrete type name at that point:

```graphql
{
  search(term: "graphql") {
    __typename
    ... on User { name }
    ... on Post { title }
  }
}
```

Useful when a field returns an interface or union and you need to know the actual type.

## The `__schema` Meta-Field

`__schema` is available on the root query type. It exposes the full schema:

```graphql
{
  __schema {
    types {
      name
    }
    queryType {
      name
    }
  }
}
```

- **`types`** — All types (objects, scalars, enums, etc.).
- **`queryType`** — The root type for queries.
- **`mutationType`** — The root type for mutations (if present).
- **`subscriptionType`** — The root type for subscriptions (if present).

## The `__type` Meta-Field

`__type(name: String)` returns details about a single type:

```graphql
{
  __type(name: "User") {
    name
    kind
    description
    fields {
      name
      type { name kind }
    }
  }
}
```

- **`kind`** — `OBJECT`, `SCALAR`, `ENUM`, `INTERFACE`, `UNION`, `INPUT_OBJECT`, etc.
- **`fields`** — For object/interface types, the list of fields.
- **`description`** — Documentation string.

## Wrapper Types

Fields can have wrapper types (`NON_NULL`, `LIST`). The `ofType` field unwraps one level:

```graphql
{
  __type(name: "User") {
    fields {
      name
      type {
        kind
        name
        ofType { kind name }
      }
    }
  }
}
```

For `name: String!`, the type has `kind: NON_NULL` and `ofType` pointing to `String`.

## Introspection in Production

Introspection is useful for development but can expose schema details. Many APIs **disable introspection in production** to reduce the attack surface. Client apps often rely on generated types or persisted queries, so runtime introspection is not required.

## Summary

| Meta-field   | Purpose                                      |
|--------------|----------------------------------------------|
| **`__typename`** | Concrete type name at current point      |
| **`__schema`**   | Full schema (types, root types)          |
| **`__type(name)`** | Details for one type                   |

| Use case        | Recommendation                          |
|-----------------|-----------------------------------------|
| **Development**  | Keep introspection enabled              |
| **Production**  | Consider disabling for public APIs      |

Next: [HTTP Transport](../10-http-transport/README.md) — Serving GraphQL over HTTP.
