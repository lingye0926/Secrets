//jshint esversion:6
require("dotenv").config();//must be in the top line
const express = require("express");
const ejs = require("ejs");
const bodyParser = require("body-parser");
const mongoose = require("mongoose");
const encrypt = require("mongoose-encryption");


const app = express();
console.log(process.env.API_KEY);
app.use(express.static("public"));
app.set("view engine","ejs");
app.use(bodyParser.urlencoded({
    extended:true
}));

mongoose.connect("mongodb://localhost:27017/userDB");

const userSchema = new mongoose.Schema({
    email: String,
    password: String
});

userSchema.plugin( encrypt, {secret: process.env.SECRET,  encryptedFeilds:  ['password']});

const User = new mongoose.model("User",userSchema);

app.get("/",function(req,res){
    res.render("home.ejs");
})

app.get("/register",function(req,res){
    res.render("register.ejs");
})

app.get("/login",function(req,res){
    res.render("login.ejs")
})


app.post("/register",function(req,res){
    const newUser = new User({
        email: req.body.username,
        password: req.body.password
    });

    newUser.save(function(err){
        if(err){
            console.log(err);
        }else{
            res.render("secrets.ejs")
        }
    })
});

app.post("/login",function(req,res){
    const username = req.body.username;
    const password = req.body.password;

    User.findOne({email: username},function(err,foundUser){
        if(err){
            console.log(err);
        }else{
            if(foundUser){
                if(foundUser.password === password){
                    res.render("secrets.ejs")
                }
            }
        }
    })
});



app.listen(3000,function(){
    console.log("The server is listening on port 3000...")
})
