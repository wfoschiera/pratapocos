<template>
  <div>
    <v-card>
      <v-card-text>
        <v-text-field
          v-model="title"
          :label="formLabel"
          required
          outlined
          append-icon="fa-pen"
          @keyup.enter="addNewCadastro" />
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  props: {
    formLabel: {
      type: String,
      default: "",
    },
  },
  emits: ["newCadastro"],
  data: () => {
    return {
      title: "",
    }
  },
  methods: {
    addNewCadastro() {
      this.$emit("newCadastro", {
        title: this.title,
      })
      this.title = ""
    },
  },
}
</script>

<style scoped></style>
