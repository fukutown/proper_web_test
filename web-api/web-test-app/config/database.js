const Sequelize = require('sequelize');
const sequelize = new Sequelize('webtest_database', 'root', 'root', {
  host: 'localhost',
  dialect: 'mysql'
});
const db = {
  sequelize: sequelize,
  Sequelize: Sequelize
};

module.exports = db;