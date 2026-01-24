# Data Warehousing - Question 1
## Comparison of Schema Models

---

## Problem Statement

Briefly compare the following concepts:
- **Snowflake schema**
- **Fact constellation**
- **Star model (Star schema)**

---

## Solution

### Overview Table

| Aspect | Star Schema | Snowflake Schema | Fact Constellation |
|--------|-------------|------------------|-------------------|
| **Structure** | Simple, denormalized | Normalized, complex | Multiple fact tables |
| **Dimension tables** | Denormalized (flat) | Normalized (multi-level) | Shared across facts |
| **Number of joins** | Fewer | More | Varies |
| **Query performance** | Fast | Slower | Depends on query |
| **Storage space** | More redundancy | Less redundancy | Most complex |
| **Complexity** | Low | Medium | High |
| **Maintenance** | Easy updates | Complex updates | Most complex |
| **Best for** | Simple queries, OLAP | Complex hierarchies | Enterprise-wide DW |

---

## 1. Star Schema (Star Model)

### Description

The **Star Schema** is the simplest and most widely used data warehouse schema. It consists of:
- **One central fact table** containing measures/metrics
- **Multiple dimension tables** directly connected to the fact table
- Dimension tables are **denormalized** (flat, single table per dimension)

### Structure Diagram

```
         DIM_TIME
             |
             |
DIM_PRODUCT--+--FACT_SALES--+--DIM_CUSTOMER
             |
             |
         DIM_LOCATION
```

**Visual representation:**
```
                ┌─────────────┐
                │  DIM_TIME   │
                │ (date_key)  │
                │  year       │
                │  quarter    │
                │  month      │
                │  day        │
                └──────┬──────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
┌───────┴────┐  ┌──────┴──────┐  ┌───┴────────┐
│DIM_PRODUCT │  │ FACT_SALES  │  │DIM_CUSTOMER│
│(prod_key)  │  │             │  │(cust_key)  │
│product_name│--│ time_key FK │--│customer_   │
│category    │  │ prod_key FK │  │  name      │
│brand       │  │ cust_key FK │  │city        │
│price       │  │ loc_key  FK │  │state       │
└────────────┘  │             │  │country     │
                │ quantity    │  └────────────┘
                │ amount      │
                │ discount    │
                └──────┬──────┘
                       │
                ┌──────┴────────┐
                │ DIM_LOCATION  │
                │(location_key) │
                │  store_name   │
                │  city         │
                │  state        │
                │  country      │
                └───────────────┘
```

### Characteristics

✅ **Advantages:**
- **Simple structure** - Easy to understand and navigate
- **Fast query performance** - Fewer joins required
- **Easy to implement** - Straightforward design
- **Optimized for OLAP** - Quick aggregations

❌ **Disadvantages:**
- **Data redundancy** - Denormalized dimensions duplicate data
- **More storage space** - Redundant attribute values
- **Update anomalies** - Changes must be made in multiple places
- **Not fully normalized** - Violates normalization rules

### When to Use

- **Simple reporting needs**
- **Performance is critical**
- **Dimensions have few hierarchies**
- **Storage space is not a concern**

---

## 2. Snowflake Schema

### Description

The **Snowflake Schema** is a normalized version of the star schema where:
- **Dimension tables are normalized** into multiple related tables
- Creates a **snowflake-like structure** with branches
- **Reduces data redundancy** through normalization

### Structure Diagram

```
                ┌─────────────┐
                │  DIM_TIME   │
                │ (date_key)  │
                │  year_key FK│
                │  quarter_key│
                │  month      │
                │  day        │
                └──────┬──────┘
                       │
           ┌───────────┴────┬──────────────────┐
           │                │                  │
    ┌──────┴────┐    ┌──────┴──────┐    ┌─────┴──────┐
    │ DIM_YEAR  │    │ FACT_SALES  │    │DIM_QUARTER │
    │           │    │             │    │            │
    └───────────┘    │ time_key FK │    └────────────┘
                     │ prod_key FK │
┌──────────┐         │ cust_key FK │         ┌────────────┐
│DIM_BRAND │         │ loc_key  FK │         │DIM_CITY    │
│(brand_key│----┐    │             │    ┌────│(city_key)  │
└──────────┘    │    │ quantity    │    │    │  city_name │
                │    │ amount      │    │    │  state_key │
    ┌───────────┴──┐ │ discount    │ ┌──┴────┴────┐      │
    │DIM_PRODUCT   │-│             │-│DIM_CUSTOMER│      │
    │(prod_key)    │ └─────────────┘ │(cust_key)  │      │
    │product_name  │                 │customer_   │      │
    │category_key  │                 │  name      │      │
    │brand_key FK  │                 │city_key FK │------┘
    └──────┬───────┘                 └────────────┘
           │                                │
    ┌──────┴────────┐              ┌────────┴────┐
    │DIM_CATEGORY   │              │ DIM_STATE   │
    │(category_key) │              │(state_key)  │
    │category_name  │              │  state_name │
    └───────────────┘              │  country_key│
                                   └──────┬──────┘
                                          │
                                   ┌──────┴───────┐
                                   │ DIM_COUNTRY  │
                                   │(country_key) │
                                   │ country_name │
                                   └──────────────┘
```

### Characteristics

✅ **Advantages:**
- **Less storage space** - Eliminates redundancy
- **Data integrity** - Easier to maintain consistency
- **Better for complex hierarchies** - Natural representation
- **Normalized structure** - Follows database design best practices

❌ **Disadvantages:**
- **Complex queries** - More joins required
- **Slower performance** - Multiple table joins impact speed
- **Harder to understand** - More tables to navigate
- **Complex ETL** - More transformations needed

### When to Use

- **Storage space is limited**
- **Data has deep hierarchies**
- **Data integrity is critical**
- **Update frequency is high**

---

## 3. Fact Constellation (Galaxy Schema)

### Description

The **Fact Constellation** (also called Galaxy Schema or Multi-Fact Schema) consists of:
- **Multiple fact tables** sharing dimension tables
- **Shared dimensions** used across different business processes
- Most **complex schema** for enterprise data warehouses

### Structure Diagram

```
                    ┌─────────────┐
                    │  DIM_TIME   │
                    └──────┬──────┘
                           │
            ┌──────────────┼──────────────┐
            │              │              │
    ┌───────┴────┐  ┌──────┴──────┐  ┌───┴────────┐
    │DIM_PRODUCT │  │ FACT_SALES  │  │DIM_CUSTOMER│
    │            │--│             │--│            │
    └──────┬─────┘  └─────────────┘  └─────┬──────┘
           │                               │
           │        ┌─────────────┐        │
           │        │   DIM_      │        │
           │--------│  LOCATION   │--------│
           │        └──────┬──────┘        │
           │               │               │
           │        ┌──────┴──────┐        │
           │        │FACT_        │        │
           └--------│INVENTORY    │--------┘
                    └─────────────┘
                           │
                    ┌──────┴──────┐
                    │ DIM_        │
                    │ WAREHOUSE   │
                    └─────────────┘
```

**Detailed Example:**

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   DIM_TIME   │     │ DIM_PRODUCT  │     │DIM_CUSTOMER  │
│  (shared)    │     │  (shared)    │     │  (shared)    │
└───┬────┬─────┘     └───┬────┬─────┘     └───┬────┬─────┘
    │    │               │    │               │    │
    │    └───────┬───────┘    └───────┬───────┘    │
    │            │                    │            │
┌───┴────────────┴───┐            ┌───┴────────────┴────┐
│   FACT_SALES       │            │  FACT_INVENTORY     │
│                    │            │                     │
│ time_key      FK   │            │ time_key       FK   │
│ product_key   FK   │            │ product_key    FK   │
│ customer_key  FK   │            │ warehouse_key  FK   │
│ location_key  FK   │            │ location_key   FK   │
│                    │            │                     │
│ quantity_sold      │            │ quantity_in_stock   │
│ revenue            │            │ reorder_level       │
│ discount           │            │ stock_value         │
└────────────────────┘            └─────────────────────┘
         │                                    │
         │         ┌──────────────┐           │
         └─────────│DIM_LOCATION  │───────────┘
                   │  (shared)    │
                   └──────────────┘

                        ┌──────────────┐
                        │DIM_WAREHOUSE │
                        │ (specific to │
                        │  inventory)  │
                        └──────┬───────┘
                               │
                        ┌──────┴──────┐
                        │FACT_        │
                        │INVENTORY    │
                        └─────────────┘
```

### Characteristics

✅ **Advantages:**
- **Supports multiple business processes** - Sales, inventory, shipping, etc.
- **Dimension reuse** - Shared dimensions across facts
- **Enterprise-wide view** - Comprehensive data analysis
- **Flexible** - Easy to add new fact tables

❌ **Disadvantages:**
- **Most complex** - Hardest to design and understand
- **Complex queries** - Joins across multiple facts
- **Maintenance challenges** - Coordinating shared dimensions
- **Performance overhead** - Multiple fact tables to query

### When to Use

- **Enterprise data warehouse**
- **Multiple business processes** need analysis
- **Shared dimensions** across departments
- **Comprehensive reporting** required

---

## Detailed Comparison

### 1. Complexity and Structure

| Schema | Complexity Level | Diagram Shape |
|--------|------------------|---------------|
| **Star** | Low | ⭐ Star-shaped |
| **Snowflake** | Medium | ❄️ Snowflake-shaped |
| **Constellation** | High | 🌌 Galaxy/constellation |

---

### 2. Normalization Level

| Schema | Dimension Normalization | Fact Normalization |
|--------|------------------------|-------------------|
| **Star** | Denormalized (flat tables) | Single fact table |
| **Snowflake** | Normalized (multiple levels) | Single fact table |
| **Constellation** | Varies | Multiple fact tables |

---

### 3. Query Performance

**Number of joins for typical query:**

| Schema | Joins Required | Query Speed |
|--------|----------------|-------------|
| **Star** | 1-4 joins | ⚡⚡⚡ Fastest |
| **Snowflake** | 5-10+ joins | ⚡⚡ Moderate |
| **Constellation** | Varies (3-15+) | ⚡ Varies |

---

### 4. Storage Requirements

| Schema | Storage Space | Redundancy |
|--------|---------------|------------|
| **Star** | 🔴 High | Significant |
| **Snowflake** | 🟢 Low | Minimal |
| **Constellation** | 🟡 Medium-High | Varies |

---

### 5. Use Cases

| Schema | Best Use Case | Industry Examples |
|--------|---------------|-------------------|
| **Star** | Simple OLAP, departmental DW | Retail sales, single-dept reporting |
| **Snowflake** | Complex hierarchies, limited storage | HR systems, product catalogs |
| **Constellation** | Enterprise DW, cross-process analysis | Supply chain, multi-dept analytics |

---

## Example Scenario Comparison

**Scenario:** Retail company wants to analyze sales data

### Star Schema Approach
```sql
-- Simple query: Total sales by product category in 2023
SELECT 
    p.category,
    SUM(s.amount) as total_sales
FROM FACT_SALES s
JOIN DIM_PRODUCT p ON s.product_key = p.product_key
JOIN DIM_TIME t ON s.time_key = t.time_key
WHERE t.year = 2023
GROUP BY p.category;

-- Only 2 joins required! ⚡
```

### Snowflake Schema Approach
```sql
-- Same query with normalized dimensions
SELECT 
    cat.category_name,
    SUM(s.amount) as total_sales
FROM FACT_SALES s
JOIN DIM_PRODUCT p ON s.product_key = p.product_key
JOIN DIM_CATEGORY cat ON p.category_key = cat.category_key
JOIN DIM_TIME t ON s.time_key = t.time_key
JOIN DIM_YEAR y ON t.year_key = y.year_key
WHERE y.year = 2023
GROUP BY cat.category_name;

-- 4 joins required
```

### Fact Constellation Approach
```sql
-- Cross-process query: Sales vs Inventory levels
SELECT 
    p.product_name,
    SUM(s.quantity_sold) as sold,
    AVG(i.quantity_in_stock) as avg_stock
FROM FACT_SALES s
JOIN FACT_INVENTORY i ON s.product_key = i.product_key 
    AND s.time_key = i.time_key
JOIN DIM_PRODUCT p ON s.product_key = p.product_key
JOIN DIM_TIME t ON s.time_key = t.time_key
WHERE t.year = 2023
GROUP BY p.product_name;

-- Joins across multiple facts
```

---

## Summary and Recommendations

### Quick Decision Guide

**Choose Star Schema if:**
- ✅ Query performance is top priority
- ✅ Simple dimensional hierarchies
- ✅ Storage space is available
- ✅ Ease of use is important

**Choose Snowflake Schema if:**
- ✅ Storage space is limited
- ✅ Complex dimensional hierarchies
- ✅ Data integrity is critical
- ✅ Dimensions change frequently

**Choose Fact Constellation if:**
- ✅ Enterprise-wide data warehouse
- ✅ Multiple business processes
- ✅ Need cross-process analysis
- ✅ Shared dimensions are beneficial

---

### Hybrid Approaches

In practice, many data warehouses use **hybrid approaches**:
- Star schema for most dimensions
- Snowflake schema for complex hierarchies (e.g., geography)
- Multiple fact tables (constellation) when needed

---

## Key Takeaways

| Concept | Star | Snowflake | Constellation |
|---------|------|-----------|---------------|
| **Ease of use** | 🟢 Easy | 🟡 Moderate | 🔴 Complex |
| **Query speed** | 🟢 Fast | 🟡 Moderate | 🟡 Varies |
| **Storage efficiency** | 🔴 Low | 🟢 High | 🟡 Medium |
| **Scalability** | 🟡 Moderate | 🟢 Good | 🟢 Excellent |
| **Flexibility** | 🔴 Limited | 🟡 Moderate | 🟢 High |

**Most Common:** Star Schema (70% of implementations)  
**Most Storage-Efficient:** Snowflake Schema  
**Most Comprehensive:** Fact Constellation

---

**End of Question 1**
