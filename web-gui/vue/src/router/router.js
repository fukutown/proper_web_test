import Vue from 'vue'
import Router from 'vue-router'

// import component
import SubjectsList from '@/components/pages/settings/subjects/SubjectsList'
import CreateSubject from '@/components/pages/settings/subjects/create/CreateSubject'

Vue.use(Router)

const routes = [
    // tmp
    { path: '/', component: SubjectsList },
    // テスト一覧ページ
    { path: '/settings/subjects', component: SubjectsList },
    // テスト作成ページ
    { path: '/settings/subjects/create', component: CreateSubject },
]

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: routes
})