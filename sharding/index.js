const express = require("express");
const { Client } = require("pg");
require("dotenv").config();
// const ConsistentHash = require("consistent-hash");
const HashRing = require("hashring")
const crypto = require("crypto");

const port = process.env.PORT || 5000;

const hashRing = new HashRing();
hashRing.add("shard1");
hashRing.add("shard2");
hashRing.add("shard3");

const clients = {
  shard1: new Client({
    host: "localhost",
    port: "5432",
    user: "postgres",
    password: process.env.DB_PASSWORD,
    database: process.env.DB_NAME,
  }),
  shard2: new Client({
    host: "localhost",
    port: "5432",
    user: "postgres",
    password: process.env.DB_PASSWORD,
    database: process.env.DB_NAME,
  }),
  shard3: new Client({
    host: "localhost",
    port: "5432",
    user: "postgres",
    password: process.env.DB_PASSWORD,
    database: process.env.DB_NAME,
  }),
};

const app = express();

const connect = async () => {
  for (let shard in clients) {
    await clients[shard].connect();
    console.log(`Connected to ${shard}`);
  }
};

app.get("/", (req, res) => {
  res.send("Hello from Charles's Node.js server!");
})

app.get("/:urlid", async (req, res) => {
  // res.send("Hello from Charles's Node.js server!");
  const urlId = req.params.urlid;
  const server = hashRing.get(urlId)
  const result = await clients[server].query("SELECT * FROM URL_TABLE WHERE URL_ID = $1", [urlId]);
  // res.send(result);
  if (result.rowCount > 0){
    res.send({
      "id":result.rows[0].id,
      "urlId": urlId,
      "url":result.rows[0].url,
      "server":server
    });
  }else{
    res.send("The server returned nothing. Please try again")
  }
});

app.post("/", async (req, res) => {
  const url = req.query.url;

  // consistency check to get the port
  const hash = crypto.createHash("sha256").update(url).digest("base64");
  const urlId = hash.substring(0, 5)

  const server = hashRing.get(urlId)

  await clients[server].query("insert into url_table (URL, URL_ID) values($1,$2)", [url,urlId]);

  res.send({
    "urlId": urlId,
    "url":url,
    "server":server
  });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}....`);
  connect();
});
