const Sequelize = require('sequelize')
const db = require('../config/database.js')

module.exports = db.sequelize.define(
  'm_user',
  {
    id: {
      type: Sequelize.INTEGER,
      primaryKey: true,
      autoIncrement: true
    }
  }
)
