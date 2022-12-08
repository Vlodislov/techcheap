import createPersistedState from "vuex-persistedstate";
import Vue from 'vue';
import Vuex from 'vuex';

import posts from './modules/posts';
import users from './modules/users';
import comments from "./modules/comments";

Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        comments,
        posts,
        users,
    },
    plugins: [createPersistedState()]
});
