[[_TOC_]]
# Overview of Neo4j and graph databases

Neo4j is a graph database where data is stored as **nodes** (entities) and **relationships** (edges) instead of tables and rows. It’s ideal when your main questions are about how things are connected—social networks, recommendation engines, fraud detection, knowledge graphs, etc. Neo4j is queried using **Cypher**, a pattern‑matching query language designed specifically for graphs.

---

# Step 1: Install Neo4j

You have three common options:

- **Neo4j Desktop (good for local development):**  
  - Download Neo4j Desktop from the official site and install it like a normal application.  
  - Create a new “Local DBMS”, choose a version, set a password, and start it.

- **Neo4j Aura (cloud, no install):**  
  - Sign up for Neo4j Aura (free tier available).  
  - Create a new database instance; you’ll get a connection URI, username, and password.

- **Neo4j Server (for more manual control):**  
  - Download the Neo4j Community/Enterprise server distribution.  
  - Unzip, configure `neo4j.conf` if needed, and start the server using the provided scripts.

Once running, Neo4j exposes a web interface (Neo4j Browser) typically at `http://localhost:7474` for local setups.

---

# Step 2: Understand core concepts

- **Nodes:** Represent entities like `Person`, `Movie`, `Product`.  
- **Labels:** Tags on nodes, e.g. `:Person`, `:Movie`.  
- **Relationships:** Directed connections between nodes, e.g. `(:Person)-[:ACTED_IN]->(:Movie)`.  
- **Properties:** Key–value pairs on nodes or relationships, e.g. `name: "Alice"`, `released: 1999`.  
- **Cypher patterns:** Use ASCII‑art style patterns like `(p:Person)-[:ACTED_IN]->(m:Movie)` to describe graph structures.

These concepts are the foundation of all Cypher queries and tutorials, including Neo4j’s official “Movie Graph” examples.

---

# Step 3: Open Neo4j Browser and connect

1. **Start your database** (Desktop, Aura, or Server).  
2. **Open Neo4j Browser** at the provided URL (e.g. `http://localhost:7474` or the Aura link).  
3. **Log in** with username and password.  
4. You’ll see a command input at the top—this is where you run Cypher queries.

Neo4j Browser also includes built‑in guides and sample datasets (like the Movie Graph) to help you learn interactively.

---

# Step 4: Create your first graph (Movie example)

Run these Cypher statements in Neo4j Browser to create a tiny movie graph:

```cypher
CREATE (m:Movie {title: "The Matrix", released: 1999});
CREATE (k:Person {name: "Keanu Reeves"});
CREATE (c:Person {name: "Carrie-Anne Moss"});
CREATE (k)-[:ACTED_IN]->(m);
CREATE (c)-[:ACTED_IN]->(m);
```

- **What this does:**  
  - Creates one `Movie` node and two `Person` nodes.  
  - Creates `ACTED_IN` relationships from each person to the movie.

This mirrors the style of Neo4j’s official “Getting Started with Cypher” tutorial using a movie graph.

---

# Step 5: Query the graph with Cypher

Now try some basic queries:

1. **Return all nodes:**

   ```cypher
   MATCH (n)
   RETURN n;
   ```

2. **Find all movies:**

   ```cypher
   MATCH (m:Movie)
   RETURN m;
   ```

3. **Find actors in “The Matrix”:**

   ```cypher
   MATCH (p:Person)-[:ACTED_IN]->(m:Movie {title: "The Matrix"})
   RETURN p.name AS actor;
   ```

4. **Add a property to a node:**

   ```cypher
   MATCH (m:Movie {title: "The Matrix"})
   SET m.tagline = "Welcome to the Real World"
   RETURN m;
   ```

These examples show how Cypher uses pattern matching (`MATCH`) and simple clauses (`RETURN`, `SET`) to traverse and update the graph.

---

# Step 6: Update and delete data

- **Create more data:**

  ```cypher
  CREATE (l:Person {name: "Laurence Fishburne"})
  CREATE (l)-[:ACTED_IN]->(:Movie {title: "The Matrix Reloaded", released: 2003});
  ```

- **Update properties:**

  ```cypher
  MATCH (p:Person {name: "Keanu Reeves"})
  SET p.born = 1964
  RETURN p;
  ```

- **Delete relationships and nodes:**

  ```cypher
  MATCH (p:Person {name: "Carrie-Anne Moss"})-[r:ACTED_IN]->(m:Movie {title: "The Matrix"})
  DELETE r;

  MATCH (m:Movie {title: "The Matrix Reloaded"})
  DETACH DELETE m;
  ```

`DETACH DELETE` removes a node and all its relationships, which is often needed in graph cleanup operations.

---

# Step 7: Explore more advanced Cypher

Once you’re comfortable with basics, you can move into:

- **Filtering and aggregation:**

  ```cypher
  MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
  RETURN p.name AS actor, count(m) AS movies
  ORDER BY movies DESC;
  ```

- **Paths and variable‑length relationships:**

  ```cypher
  MATCH path = (p:Person)-[:ACTED_IN*1..3]->(m:Movie)
  RETURN path
  LIMIT 10;
  ```

- **Recommendation‑style queries:**  
  For example, “people who acted in the same movies” or “movies similar by shared actors”—Neo4j’s tutorials include a Cypher recommendation engine built on the Movie Graph.

---

# Step 8: Import data from other sources

When you’re ready to move beyond toy data:

- **From CSV:** Use `LOAD CSV` in Cypher to import data from CSV files into nodes and relationships.  
- **From relational databases:** Neo4j provides guides on translating relational schemas into graph models and importing data using tools and Cypher scripts.  
- **For knowledge graphs and AI use cases:** You can model entities and relationships as a knowledge graph and interact with Neo4j from languages like Python using official drivers.

---

# Step 9: Use drivers and integrate with code

Neo4j has official drivers for languages like Java, JavaScript, Python, and .NET. Typical flow:

1. **Install the driver** in your project (e.g. `neo4j` Python package).  
2. **Create a driver instance** with your URI, username, and password.  
3. **Open a session** and run Cypher queries from your code.  
4. **Map results** to your application’s data structures.

This is how you turn your Neo4j graph into a backend for applications, recommendation engines, or AI pipelines.

---

# Step 10: Where to go next

Good next steps:

- **Official “Getting Started with Cypher” tutorial** to deepen your query skills.  
- **Beginner’s guides** that walk from installation through first queries and use cases.  
- **Full Neo4j tutorials** that cover admin, CQL functions, and integration with Java/Spring if you’re going deeper into backend work.

If you tell me what you want Neo4j for—recommendations, social graph, knowledge graph—I can sketch a concrete mini‑project and the exact Cypher you’d use.