import axios from 'axios';

const state = {
    user: null,
};

const getters = {
    isAuthenticated: state => !!state.user,
    stateUser: state => state.user,
};

const actions = {
    async register({dispatch}, form) {
        await axios.post('register', form);
        const UserForm = new FormData();
        UserForm.append('username', form.login);
        UserForm.append('password', form.password);
        await dispatch('logIn', UserForm);
    },
    async logIn({dispatch}, user) {
        await axios.post('login', user, {headers: {"Access-Control-Allow-Origin": "*"}});
        await dispatch('viewMe');
    },
    async viewMe({commit}) {
        let {data} = await axios.get('users/iam');
        await commit('setUser', data);
    },
    // eslint-disable-next-line no-empty-pattern
    async deleteUser({}, id) {
        await axios.delete(`user/${id}`, {headers: {"Access-Control-Allow-Origin": "*"}});
    },
    async logOut({commit}) {
        let user = null;
        commit('logout', user);
    }
};

const mutations = {
    setUser(state, login) {
        state.user = login;
    },
    logout(state, user) {
        state.user = user;
    },
};

export default {
    state,
    getters,
    actions,
    mutations
};
