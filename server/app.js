var express = require('express')
  , app = express()
  , port = 5555

  , fs = require('fs');

app.use(express.bodyParser());
app.use(express.static(__dirname + '/public'));

// incoming msg
app.post('/', function(req,res){
  fs.writeFile('public/msg.txt', req.body.msg.toString());
  res.redirect('/');
})

app.get('/hasIncoming', function(req,res){
  fs.readFile('public/msg.txt', 'utf-8', function(err,ok){
    if(ok){
      res.end("TRUE")
    }
    else res.end("FALSE")
  })
})

app.get('/lookup', function(req,res){
  fs.readFile('public/msg.txt', 'utf-8', function(err, ok){
    if(!ok){
      var msg = {
        none: true
      }
      res.send(JSON.stringify(msg));
    }
    else {   
      var msg = {
        msg: ok.toString()
      }
      res.send(JSON.stringify(msg));
      fs.unlink('public/msg.txt', function(){

      });
    }
  });
})

console.log("Up @ " + port);
app.listen(port);