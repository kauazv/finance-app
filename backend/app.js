require('dotenv').config();
const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');

const app = express();
app.use(express.json(), cors());

moongoose.connect(process.env.MONGO_URI || 'mongodb://localhost:27017/finance-app', {
  useNewUrlParser: true,
});

const User = require('./models/User');
const Transaction = require('./models/Transaction');
const authMiddleware = require('./utils/auth');
