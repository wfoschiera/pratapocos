<template>
  <v-card>
    <v-card-text>
      <div>#{{ cadastro.id }}</div>
      <p class="ma-0 pa-0 text-h5 text--primary">
        {{ cadastro.description }}
      </p>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "CadastrosModel",
  props: {
    cadastro: {
      type: Object,
      default: null,
      roger: "usalinter",
    },
  },
  data: () => ({}),
}
</script>
