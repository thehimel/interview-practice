# HTTP Transport

GraphQL does not specify a transport, but **HTTP** is the most common choice for queries and mutations. This chapter covers how to serve GraphQL over HTTP.

## Single Endpoint

Unlike REST, where each resource has its own URL, a GraphQL API typically uses **one endpoint** (e.g., `/graphql`). All operations go to that URL. The operation type and document determine what runs.

## Request Methods

### POST (Required)

Servers must support **POST** for queries and mutations. The body is JSON:

```json
{
  "query": "{ user(id: \"1\") { name } }",
  "operationName": "GetUser",
  "variables": { "id": "1" }
}
```

- **`query`** — Required. The GraphQL document (query, mutation, or subscription).
- **`operationName`** — Required when the document has multiple operations.
- **`variables`** — Optional. JSON object of variable values.

### GET (Optional)

Some servers support **GET** for query-only operations. The document goes in the `query` query parameter:

```
GET /graphql?query={user(id:"1"){name}}
```

Variables can be sent as a JSON string in a `variables` parameter. GET is useful for caching but URLs have length limits, so complex queries may not fit.

## Headers

**Request:**

- `Content-Type: application/json` — Required for POST with a JSON body.
- `Accept: application/graphql-response+json` — Preferred response format.

**Response:**

- `Content-Type: application/graphql-response+json` or `application/json` — Indicates the response format.

## Authentication

Authentication (e.g., cookies, JWT) usually happens **before** the request reaches GraphQL. Place auth middleware earlier in the pipeline. Authorization (who can access which fields) is enforced inside resolvers during execution.

## Response Status Codes

- **2xx** — When `data` is non-null (success or partial success).
- **4xx** — For invalid requests (e.g., validation errors).
- **5xx** — For server failures.

Some legacy servers return 2xx even for validation errors when using `application/json`. The GraphQL-over-HTTP spec recommends `application/graphql-response+json` and clearer status code usage.

## Subscriptions

Subscriptions use a **stateful** transport (WebSockets or SSE), not plain HTTP. The setup differs from queries and mutations. See the Realtime Updates chapter.

## Summary

| Aspect       | Recommendation                                  |
|--------------|--------------------------------------------------|
| **Endpoint** | Single URL, e.g. `/graphql`                      |
| **POST**     | Required for all operations                      |
| **GET**      | Optional for queries; useful for caching         |
| **Body**     | JSON with `query`, optional `operationName`, `variables` |
| **Auth**     | Handle before GraphQL; authorize in resolvers    |

| Header        | Purpose                                      |
|---------------|----------------------------------------------|
| `Content-Type`| `application/json` for POST body             |
| `Accept`      | `application/graphql-response+json` preferred |

