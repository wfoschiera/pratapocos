<template>
  <v-container class="fill-height">
    <v-row justify="center" align="center">
      <v-col cols="12">
        <v-card>
          <v-card-title class="headline"> Cadastros </v-card-title>
        </v-card>
      </v-col>

      <v-col cols="12">
        <cadastro-form :form-label="'New Cadastro'" @new-cadastro="addNewCadastro" />
      </v-col>

      <v-col v-for="item in cadastros" :key="item.id" cols="12">
        <cadastro :cadastro="item" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapState } from "pinia"
import { useBaseStore } from "@/stores/baseStore"
import { usecoreStore } from "@/stores/coreStore"
import Cadastro from "@/components/Cadastro.vue"
import CadastroForm from "@/components/CadastroForm.vue"

export default {
  name: "CadastrosList",
  components: { Cadastro, CadastroForm },
  setup() {
    const baseStore = useBaseStore()
    const coreStore = usecoreStore()
    return { baseStore, coreStore }
  },
  computed: {
    ...mapState(usecoreStore, ["cadastros", "cadastrosLoading"]),
  },
  mounted() {
    this.getCadastros()
  },
  methods: {
    getCadastros() {
      this.coreStore.getCadastros()
    },
    async addNewCadastro(cadastro) {
      const newCadastro = await this.coreStore.addNewCadastro(cadastro)
      this.baseStore.showSnackbar(`New cadastro added #${ newCadastro.id }`)
      this.getCadastros()
    },
  },
}
</script>

<style scoped>
.done {
  text-decoration: line-through;
}
</style>
