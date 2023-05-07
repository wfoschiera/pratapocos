const utils = require('../utils')

module.exports = {
  users: utils.parseJson('./data/users.json'),
  cadastros: utils.parseJson('./data/cadastros.json'),
}
