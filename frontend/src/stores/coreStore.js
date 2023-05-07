import { defineStore } from "pinia"
import coreApi from "@/api/core.api.js"

export const usecoreStore = defineStore("coreStore", {
  state: () => ({
    cadastros: [],
    cadastrosLoading: false,
  }),
  actions: {
    async getCadastros() {
      this.cadastrosLoading = true
      const response = await coreApi.getCadastros()
      this.cadastros = response.cadastros
      this.cadastrosLoading = false
    },
    async addNewCadastro(tarefa) {
      const newCadastro = await coreApi.addNewCadastro(tarefa.title)
      return newCadastro
    },
  },
})
