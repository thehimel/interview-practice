# Response Format

A GraphQL response is a JSON object with up to three top-level keys: **`data`**, **`errors`**, and **`extensions`**. At least one of `data` or `errors` is present. The format is defined by the specification.

## The `data` Key

When execution succeeds, the result lives under `data`:

```json
{
  "data": {
    "user": {
      "id": "42",
      "name": "Alice"
    }
  }
}
```

The structure under `data` matches the query. The key is the root operation type name (e.g., `query`) or the field/alias. Nested objects and arrays follow the selection set.

## The `errors` Key

When something goes wrong, details appear under `errors`:

```json
{
  "errors": [
    {
      "message": "User not found",
      "locations": [{"line": 2, "column": 3}],
      "path": ["user"]
    }
  ]
}
```

Common fields:

- **`message`** — Error description.
- **`locations`** — Where in the document the error occurred.
- **`path`** — Path to the field that failed (for execution errors).

## Request vs. Field Errors

**Request errors** (syntax, validation) occur before execution. The response has no `data` key — only `errors`:

```json
{
  "errors": [
    {
      "message": "Cannot query field 'xyz' on type 'Query'."
    }
  ]
}
```

**Field errors** occur during execution. The response can include both `data` and `errors` (a **partial response**). Successful fields appear under `data`; failed fields are null and described in `errors`:

```json
{
  "data": {
    "user": null
  },
  "errors": [
    {
      "message": "User not found",
      "path": ["user"]
    }
  ]
}
```

## The `extensions` Key

Implementations may add extra information under `extensions`:

```json
{
  "data": { ... },
  "extensions": {
    "tracing": { ... },
    "rateLimit": { "remaining": 99 }
  }
}
```

The spec does not define `extensions` contents. Use it for tracing, rate limits, or other metadata.

## Serialization

The spec does not require JSON, but JSON is the usual format. Transport (e.g., HTTP) and media types are separate from the GraphQL response structure.

## Summary

| Key         | Purpose                                      |
|-------------|----------------------------------------------|
| **`data`**  | Result of the executed operation             |
| **`errors`**| Descriptions of what went wrong              |
| **`extensions`** | Optional implementation-specific metadata |

| Error type   | When           | `data` present? |
|--------------|----------------|-----------------|
| **Request**  | Parse/validate | No              |
| **Field**    | During execution | Possibly (partial) |

Next: [Schema Discovery](../09-schema-discovery/README.md) — Introspection and `__schema`.
