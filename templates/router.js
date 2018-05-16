/*jshint esversion: 6 */

import Vue from 'vue';
import VueRouter from 'vue-router';


import indexPage from './main/index.vue';

Vue.use(VueRouter);

const routes = [
    { path: '/', name: 'HomeRouter', component: indexPage ,alias:'/paper'},
    { path: '/home', name: 'Home1', component: indexPage,alias:'/paper/home' },
   /* { path: '/search', name: 'Search', component: searchPage },
    { path: '/profile', name: 'Profile', component: profilePage },
    { path: '/showProfile', name: 'ShowProfile', component: showProfilePage }*/
];



var router = new VueRouter ({
    routes: routes,
    //mode: 'history'
    mode: 'history',
    linkActiveClass: 'active'
});

export default router;
