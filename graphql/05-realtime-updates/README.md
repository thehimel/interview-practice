# Realtime Updates

**Subscription operations** let clients receive live updates from the server. Instead of polling, the client opens a long-lived connection and gets events as they occur.

## How Subscriptions Work

Subscriptions are defined on the `Subscription` root type:

```graphql
type Subscription {
  newMessage: Message
  orderStatusChanged(orderId: ID!): Order
}
```

The client subscribes with a selection set:

```graphql
subscription OnNewMessage {
  newMessage {
    id
    content
    createdAt
  }
}
```

When the server emits an event (e.g., a new message is created), it pushes data to the client over the open connection.

## Transport

Subscriptions need a **stateful** transport. Common choices:

- **WebSockets** — Bidirectional; widely used for GraphQL subscriptions.
- **Server-Sent Events (SSE)** — One-way server-to-client streams.

Queries and mutations usually use HTTP (POST). Subscriptions use a different protocol and endpoint in many setups.

## Single Root Field

Each subscription operation must have **exactly one** root field. This is invalid:

```graphql
subscription {
  newMessage { id }
  orderUpdated { id }
}
```

Valid approach: use separate operations and subscribe to one at a time:

```graphql
subscription Messages {
  newMessage { id content }
}

subscription Orders($orderId: ID!) {
  orderStatusChanged(orderId: $orderId) { status }
}
```

## Pub/Sub Under the Hood

Servers typically use a **pub/sub** system. When a mutation creates a message, it publishes an event. The subscription resolver subscribes to that event stream and forwards results to connected clients.

Implementation details depend on the library (e.g., Strawberry with Python, Apollo with Node.js).

## Scaling Considerations

Subscriptions are harder to scale than queries and mutations:

- Each client holds an open connection.
- Connections are often tied to a specific server instance.
- Reconnection and resubscription logic is needed on the client.

For infrequent updates, **polling** or **refetch-on-action** may be simpler than subscriptions.

## When to Use Subscriptions

| Use subscriptions when…        | Consider alternatives when…           |
|--------------------------------|---------------------------------------|
| Data changes often and incrementally | Updates are rare                  |
| Clients need near real-time updates  | Periodic refresh is acceptable   |
| You have pub/sub infrastructure     | Simpler architecture preferred    |

## Summary

| Concept        | Description                                      |
|----------------|--------------------------------------------------|
| **Subscription** | Long-lived operation for streaming data       |
| **Transport**  | WebSockets or SSE, not plain HTTP               |
| **Single root**| One root field per subscription operation      |
| **Pub/sub**    | Server publishes events; subscription resolvers stream them |

Next: [Validating Requests](../06-validating-requests/README.md) — How the server validates operations.
