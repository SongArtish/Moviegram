<template>
  <div class="overflow-auto">
    <h2>Write your review here :)</h2>
    <br>
    <b-button @click="toCreateArticle" variant="primary">Review</b-button>
    <br>
    <br>
    <br>
    <b-list-group v-for="article in updateArticles" :key="article.id">
      <b-list-group-item href="#"  class="flex-column align-items-start bg-dark text-white" @click="toDetail(article)"> <!-- active -->
        <div class="d-flex w-100 justify-content-between">
          <p class="mb-1 font-weight-bold"></p>
          <!-- <small>3 days ago</small> -->
          <small>{{ article.genre }}</small>
        </div>

        <h3 class="mb-1 font-weight-bold">{{ article.title}}</h3>
        <br>
        <div class="d-flex w-100 justify-content-between">
          <small></small>
          <small class="mb-1">{{ article.content }}</small>
          <!-- <small>3 days ago</small> -->
          <small class="font-weight-bold">평점 : {{ article.rate }}점</small>
        

        <!-- 수정, 삭제 버튼!!! -->
        <!-- <div v-if="user.pk === article.user">
        {{ user.pk }}
        {{ article.user }}
        <b-button pill variant="info" @click="updateArticle(article)">Update</b-button>
        <b-button pill variant="danger" @click="deleteArticle(article)">Delete</b-button>
        </div> -->
        </div>

      </b-list-group-item>
    </b-list-group>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Articles',
  data: function () {
    return {
      articles: [],
      user: ''
    }
  },
  methods: {
    getToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    getArticles: function () {
      const config = this.getToken()
      axios.get(`${SERVER_URL}/articles/`, config)
        .then((res) => {
          // console.log(res.data)
          this.articles = res.data
          this.articles.reverse()
        })
        .catch((error) => {
          console.log(error)
        })
    },
    deleteArticle: function (article) {
      const config = this.getToken()
      // console.log(article)
      axios.delete(`${SERVER_URL}/articles/${article.id}/`, config)
        .then(res => {
          const idx = this.articles.findIndex(article => {
            return article.id === res.data.id
          })
          this.articles.splice(idx, 1)
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateArticle: function (article) {
      const config = this.getToken()
      const articleItem = {
        title: article.title,
        rate: article.rate,
        content: article.content
      }
      axios.put(`${SERVER_URL}/articles/${article.id}/`, articleItem, config)
        .then((res) => {
          console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    toCreateArticle: function () {
      this.$router.push({ name: 'CreateArticle' })
    },
    toDetail: function (article) {
     this.$router.push({name: 'ArticleDetail', query: {article: article}})
    },
    getUser: function () {
        const config = this.getToken()
        axios.get(`${SERVER_URL}/profile/`, config)
          .then((res) => {
            this.user = res.data
          })
          .catch((error) => {
            console.log(error)
          })
    },
  },
  created: function () {
    // this.getUser()
    this.getArticles()
  },
  computed: {
    updateArticles: function () {
      return this.articles
    }
  }
}
</script>

<style>

</style>