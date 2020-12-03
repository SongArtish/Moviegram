import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Articles from '../views/Articles.vue'
import ArticleDetail from '@/components/ArticleDetail.vue'
import ArticleUpdate from '@/components/ArticleUpdate.vue'
import CreateArticle from '../components/CreateArticle.vue'
import Entertainment from '../views/Entertainment.vue'
import Login from '../components/Login.vue'
import MovieDetail from '../components/MovieDetail.vue'
import MovieList from '../views/MovieList.vue'
import MovieRecommend from '../views/MovieRecommend.vue'
import Profile from '../views/Profile.vue'
import SearchMovieList from '../components/SearchMovieList.vue'
import SlideToUnlock from '../components/SlideToUnlock.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/movielist',
    name: 'MovieList',
    component: MovieList
  },
  {
    path: '/movierecommend',
    name: 'MovieRecommend',
    component: MovieRecommend
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/articles',
    name: 'Articles',
    component: Articles
  },
  // 여기서부터는 하위 component
  {
    path: '/createarticle',
    name: 'CreateArticle',
    component: CreateArticle
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/moviedetail',
    name: 'MovieDetail',
    component: MovieDetail,
  },
  {
    path: '/entertainment',
    name: 'Entertainment',
    component: Entertainment
  },
  {
    path: '/slidetounlock',
    name: 'SlideToUnlock',
    component: SlideToUnlock
  },
  {
    path: '/articledetail',
    name: 'ArticleDetail',
    component: ArticleDetail
  },
  {
    path: '/searchmovielist',
    name: 'SearchMovieList',
    component: SearchMovieList
  },
  {
    path: '/articleupdate',
    name: 'ArticleUpdate',
    component: ArticleUpdate
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
