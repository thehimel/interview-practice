# Validating Requests

Before a GraphQL operation runs, the server **validates** it against the schema. Invalid requests are rejected with errors; no field execution occurs. Validation catches mistakes early and keeps the API predictable.

## Validation Phase

Request lifecycle: **Parse** → **Validate** → **Execute**.

Validation checks that the document is semantically correct for the schema. If validation fails, the server returns errors and does not execute the operation.

## Common Validation Errors

### Non-Existent Fields

Requested fields must exist on the type:

```graphql
# Invalid: Product has no "description" field
{
  product(id: "1") {
    description
  }
}
```

### Missing Selection Sets

Fields that return objects require a **selection set** (sub-fields). Scalar and enum fields must not have one:

```graphql
# Invalid: product returns Product, not a scalar
{
  product(id: "1")
}

# Invalid: name is a scalar; no sub-fields allowed
{
  product(id: "1") {
    name {
      first
    }
  }
}
```

### Abstract Type Fields

When a field returns an **interface** or **union**, you cannot request fields that exist only on some implementing types without using fragments:

```graphql
# Invalid: primaryFunction exists only on Droid, not on Character
{
  hero {
    name
    primaryFunction
  }
}

# Valid: use inline fragment
{
  hero {
    name
    ... on Droid {
      primaryFunction
    }
  }
}
```

### Cyclic Fragments

Fragments cannot reference themselves (directly or indirectly). That would create unbounded expansion:

```graphql
# Invalid: fragment references itself
fragment Bad on User {
  name
  friends {
    ...Bad
  }
}
```

### Variable Type Mismatch

Variable types must match the argument types they are passed to:

```graphql
# Invalid: $id is String but argument expects ID!
query($id: String!) {
  user(id: $id) { name }
}
```

## Validation vs. Execution Errors

| Phase      | When it happens      | Response contains `data`? |
|------------|----------------------|---------------------------|
| **Validation** | Before execution starts | No; only `errors`        |
| **Execution**  | During field resolution | May include partial `data` |

Validation errors are **request errors**. The client sent something invalid. Execution errors occur when resolvers fail or return invalid data.

## Error Format

Validation errors appear under the top-level `errors` key. Each error typically includes:

- `message` — Human-readable description.
- `locations` — Line and column in the document.
- `path` — (For execution errors) Path to the failing field.

## Summary

| Rule                    | Description                                      |
|-------------------------|--------------------------------------------------|
| **Fields must exist**   | Requested fields must be defined on the type    |
| **Selection sets**     | Objects need sub-fields; scalars must not       |
| **Abstract types**      | Use fragments for type-specific fields          |
| **No cyclic fragments** | Fragments cannot spread to themselves           |
| **Variable types**      | Variables must match argument types             |

Next: [Field Resolution](../07-field-resolution/README.md) — How resolvers provide data.
