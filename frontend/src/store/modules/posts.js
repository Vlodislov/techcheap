import axios from 'axios';

const state = {
    posts: null,
    note: null
};

const getters = {
    statePosts: state => state.posts,
    statePost: state => state.post,
};

const actions = {
    async createPost({dispatch}, post) {
        await axios.post('posts', post);
        await dispatch('getPosts');
    },
    async getPosts({commit}) {
        let {data} = await axios.get('posts');
        commit('setPosts', data);
    },
    async viewPost({commit}, id) {
        let {data} = await axios.get(`post/${id}`);
        commit('setPost', data);
    },
    // eslint-disable-next-line no-empty-pattern
    async updatePost({}, post) {
        console.log(post.form);
        await axios.post(`post/${post.id}`, post.form);
    },
    // eslint-disable-next-line no-empty-pattern
    async deletePost({}, id) {
        await axios.delete(`post/${id}`);
    }
};

const mutations = {
    setPosts(state, posts) {
        state.posts = posts;
    },
    setPost(state, post) {
        state.post = post;
    },
};

export default {
    state,
    getters,
    actions,
    mutations
};
