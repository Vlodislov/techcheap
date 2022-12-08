import axios from 'axios';

const state = {
    comments: null,
    posts: null,
    note: null
};

const getters = {
    stateComments: state => state.comments,
    stateComment: state => state.comment,
};

const actions = {
    async createComment({dispatch}, comment) {
        let  com = {
            content: comment.content
        }
        console.log(com);
        await axios.post(`comments?${comment.post_id}`, com);
        await dispatch('getComments');
    },
    async getComments({commit}) {
        let {data} = await axios.get('comments');
        commit('setComments', data);
    },
    // eslint-disable-next-line no-empty-pattern
    async updateComment({}, comment) {
        console.log(comment.form);
        await axios.post(`comments/${comment.id}`, comment.form);
    },
    // eslint-disable-next-line no-empty-pattern
    async deleteComment({}, id) {
        await axios.delete(`comments/${id}`);
    }
};

const mutations = {
    setComments(state, comments) {
        state.comments = comments;
    },
    setComment(state, comment) {
        state.comment = comment;
    },
};

export default {
    state,
    getters,
    actions,
    mutations
};
