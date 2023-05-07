import api from "./config.js"

export default {
  getCadastros: async () => {
    const response = await api.get("/api/core/cadastros/list")
    return response.data
  },
  addNewCadastro: async (description) => {
    const json = JSON.stringify({ description })
    const response = await api.post(
      "/api/core/cadastros/add",
      json
    )
    return response.data
  },
}
