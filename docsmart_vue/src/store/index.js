import { createStore } from 'vuex'

import { alert } from './alert.module'
import { account } from './account.module'
import { users } from './users.module'

export default createStore({
  state: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    alert,
    account,
    users
  }
})
