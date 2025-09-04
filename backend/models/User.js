const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const userSchema = new mongoose.Schema({
    email: { type: String, unique: true},
    hash: String,
});
userSchema.methods.setPassword = function(password) {
    this.hash = bcrypt.hashSync(password, 10);
}
userSchema.methods.validatePassword = function(password) {
    return bcrypt.compareSync(password, this.hash);
}