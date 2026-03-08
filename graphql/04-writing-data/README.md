# Writing Data

**Mutation operations** let clients change data on the server. Unlike queries, mutations are intended to have side effects. Only top-level mutation fields may perform writes; nested resolvers should remain side-effect free.

## Defining Mutations

Mutations live on the `Mutation` root type:

```graphql
type Mutation {
  createUser(input: CreateUserInput!): User
  updateUser(id: ID!, input: UpdateUserInput!): User
  deleteUser(id: ID!): Boolean
}
```

Mutation fields accept arguments and return output types, just like query fields. All query features (variables, fragments, aliases) apply to mutations.

## Creating Data

Use input types to pass structured data:

```graphql
input CreateUserInput {
  name: String!
  email: String!
}

type Mutation {
  createUser(input: CreateUserInput!): User
}
```

Client request:

```graphql
mutation CreateUser($input: CreateUserInput!) {
  createUser(input: $input) {
    id
    name
    email
  }
}
```

Returning the created object lets the client get the new state without a follow-up query.

## Updating Data

Purpose-built mutations make the schema clearer than a generic `updateUser` with many optional fields:

```graphql
type Mutation {
  updateUserName(id: ID!, name: String!): User
  updateUserEmail(id: ID!, email: String!): User
}
```

Each mutation has a focused input, so required fields can be non-null.

## Deleting Data

Deletion mutations typically return an ID or a boolean:

```graphql
type Mutation {
  deleteUser(id: ID!): ID!
}
```

The server performs the delete and returns the removed ID or a success flag.

## Serial Execution

**Query** fields can run in parallel. **Mutation** top-level fields run **serially** — one after another. This avoids race conditions when multiple mutations are sent in a single request:

```graphql
mutation {
  first: deleteItem(id: "1")
  second: deleteItem(id: "2")
}
```

`first` completes before `second` starts. Note: this is not a database transaction. If one mutation fails, earlier ones are not rolled back.

## Multiple Mutations in One Request

A single mutation operation can include several top-level fields:

```graphql
mutation BatchCreate {
  user1: createUser(input: { name: "Alice", email: "a@example.com" }) {
    id
  }
  user2: createUser(input: { name: "Bob", email: "b@example.com" }) {
    id
  }
}
```

Each field runs in order. Aliases keep the response keys distinct.

## Summary

| Concept           | Description                                      |
|-------------------|--------------------------------------------------|
| **Mutation type** | Root type for write operations                    |
| **Input types**   | Structured arguments for create/update           |
| **Serial execution** | Top-level mutation fields run one after another |
| **Return value**  | Often the created/updated object or an ID        |

Next: [Realtime Updates](../05-realtime-updates/README.md) — Subscriptions for live data.
