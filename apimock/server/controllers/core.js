const data = require("../data");
const accounts = require("./accounts");

function getMaxId(items) {
  return Math.max(...items.map((item) => item.id));
}

module.exports = {
  find: (req, res) => {
    const loggedUser = accounts.loginRequired(req, res);
    if (!loggedUser) {
      return;
    }
    const { id } = req.params;
    if (id != undefined) {
      const cadastro = data.cadastros.find((t) => t.id == id);
      if (!cadastro || cadastro.userId != loggedUser.id) {
        res.status(404).end();
        return;
      }
      res.send(cadastro);
      return;
    }
    const response = {
      cadastros: data.cadastros.filter((t) => t.userId == loggedUser.id),
    };
    res.send(response);
  },
  add: (req, res) => {
    const loggedUser = accounts.loginRequired(req, res);
    if (!loggedUser) {
      return;
    }
    const { description } = req.body;
    const id = getMaxId(data.cadastros) + 1;
    const newCadastro = {
      id,
      description,
      userId: loggedUser.id,
    };
    data.cadastros.push(newCadastro);
    res.send(newCadastro);
  },
};
