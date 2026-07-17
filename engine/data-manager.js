import * as data from "../data/index.js";

const DataManager = Object.freeze({

    getPurposes() {
        return data.purposes;
    },

    getCategories() {
        return data.categories;
    },

    getTopics() {
        return data.topics;
    },

    getGoals() {
        return data.goals;
    },

    getContentStyles() {
        return data.contentStyles;
    },

    getAudiences() {
        return data.audiences;
    },

    getLengths() {
        return data.lengths;
    },

    getPlatforms() {
        return data.platforms;
    },

    getLanguages() {
        return data.languages;
    },

    getCreativityLevels() {
        return data.creativity;
    },

    getEmojiOptions() {
        return data.emojis;
    },

    getCTAOptions() {
        return data.ctas;
    },


    getCategoriesByPurpose(purpose) {

        return data.categories.filter(

            item => item.purpose === purpose

        );

    },


    getTopicsByCategory(category) {

        return data.topics.filter(

            item => item.category === category

        );

    },


    getCategory(id) {
        return data.categories.find(item => item.id === id) || null;
    },

    getTopic(id) {
        return data.topics.find(item => item.id === id) || null;
    },

    getPurpose(id) {
        return data.purposes.find(item => item.id === id) || null;
    }

});

export default DataManager;
