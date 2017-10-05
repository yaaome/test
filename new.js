var express=require('express');
var app=express();
var querystring = require('querystring');
var goData = '';
var bodyParser = require('body-parser');

app.set('view engine','jade');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static('images'));
app.use(express.static('/'));
app.post('/',function(req,res)
{
	var goData = req.body.model;
	var formData = '';
	
	res.render('as',
{mysrc: goData + '.jpg'})
	
});
	


app.get('/',function(req,res)
{
res.render('as',
{title:'Guru99',message:'Welcome'})
});
var server=app.listen(3000,function() {});