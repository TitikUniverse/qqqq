import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router);

import vContactList from '../components/contacts/v-contact-list'
import vContactUserInfo from '../components/contacts/v-contact-user-info'
import vUsersList from '../components/users/v-users-list'
import vUserChat from '../components/users/chat/v-user-chat'
import vLogin from '../components/contacts/userLogin'
import vReg from '../components/contacts/userRegister'
import vSer from '../components/contacts/userSearch'

let router = new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [{
            path: '/register',
            name: 'Register',
            component: vReg,
            props: true
        },
        {
            path: '/',
            name: 'contacts',
            component: vContactList
        },
        {
            path: '/contact',
            name: 'contact',
            component: vContactUserInfo,
            props: true
        },
        {
            path: '/chats',
            name: 'chats',
            component: vUsersList
        },
        {
            path: '/user',
            name: 'user',
            component: vUserChat,
            props: true
        },
        {
            path: '/login',
            name: 'login',
            component: vLogin,
            props: true
        },
        {
            path: '/search',
            name: 'search',
            component: vSer,
            props: true
        }
    ]
})

export default router;