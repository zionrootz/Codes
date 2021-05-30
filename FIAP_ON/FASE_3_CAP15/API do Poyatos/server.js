// server.js
// where your node app starts

// init project
const express = require("express");
const bodyParser = require("body-parser");
const app = express();
const fs = require("fs");
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// we've started you off with Express,
// but feel free to use whatever libs or frameworks you'd like through `package.json`.

// http://expressjs.com/en/starter/static-files.html
app.use(express.static("public"));

// init sqlite db
const dbFile = "./.data/dc1-2021b.db";
const exists = fs.existsSync(dbFile);
const sqlite3 = require("sqlite3").verbose();
const db = new sqlite3.Database(dbFile);

// if ./.data/sqlite.db does not exist, create it, otherwise print records to console
db.serialize(() => {
  if (!exists) {
    /*db.run(
      "CREATE TABLE alunos (rm INTEGER, nome text, senha text, hash text)"
    );
    console.log("Nova tabela alunos criada!");

    db.run(
      "CREATE TABLE acessos (id INTEGER PRIMARY KEY AUTOINCREMENT, rm INTEGER, acesso INTEGER)"
    );
    console.log("Nova tabela acessos criada!");
    */
    db.serialize(() => {
  });
  } else {
    console.log('Database "dc1-2021" ready to go!');
  }
});

// http://expressjs.com/en/starter/basic-routing.html
app.get("/", (request, response) => {
  response.sendFile(`${__dirname}/views/index.html`);
});

app.post("/getHash", (request, response) => {
  let sql="SELECT nome, hash from alunos WHERE rm=? AND senha=?"
  var inserts = [request.body.rm, request.body.senha]
  //console.log(sql);
  db.all(sql, inserts, (err, rows) => {
    db.run("INSERT INTO acessos (rm, acesso) VALUES ("+request.body.rm+", strftime('%s','now'))"); 
    
    if (rows.length == 1){
      response.send(JSON.stringify(rows[0]));  
    } else {
      response.send(JSON.stringify({'erro': 'RM/senha inválidos'}));
    }
    
    //console.log(err);
    //console.log(rows.length)
  });
});

// endpoint to add a dream to the database
app.get("/getAcessos", (request, response) => {
  db.all("SELECT rm, datetime(acesso-10800, 'unixepoch') as acesso FROM acessos", (err, rows) => {
    response.send(JSON.stringify(rows));
  });// 'unixepoch')
});

// helper function that prevents html/css/script malice
const cleanseString = function(string) {
  return string.replace(/</g, "&lt;").replace(/>/g, "&gt;");
};

// listen for requests :)
var listener = app.listen(process.env.PORT, () => {
  console.log(`Your app is listening on port ${listener.address().port}`);
});