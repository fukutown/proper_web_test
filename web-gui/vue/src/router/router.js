import Vue from 'vue'
import Router from 'vue-router'

// import component
import TestList from '@/components/pages/settings/tests/TestList'
import CreateTest from '@/components/pages/settings/tests/create/CreateTest'

Vue.use(Router)

const routes = [
    // tmp
    { path: '/', component: TestList },
    // テスト一覧ページ
    { path: '/settings/tests', component: TestList },
    // テスト作成ページ
    { path: '/settings/tests/create', component: CreateTest },
]

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: routes
})