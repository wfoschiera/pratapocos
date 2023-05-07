// Composables
import DefaultLayout from "@/layouts/default/DefaultLayout.vue"
import CadastroListView from "@/pages/core/CadastroListView.vue"

export default [
  {
    path: "/cadastros",
    component: DefaultLayout,
    children: [
      {
        path: "list",
        name: "cadastros-list",
        component: CadastroListView,
      },
    ],
  },
]
