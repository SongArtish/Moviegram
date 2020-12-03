<template>
  <div>
    <b-row>
      <b-col cols="2"></b-col>
      <b-col cols="8">
        <b-card no-body class="overflow-hidden text-dark">
          <b-row no-gutters>
              <b-col md="6">
                <b-card-img src="https://picsum.photos/400/400/?image=20" alt="Image" class="rounded-0"></b-card-img>
              </b-col>
              <b-col md="6">
                <b-card-body title="">
                  <b-card-text>
                    <h2>{{ $route.query.article.title }}</h2>
                    <h3>평점 : {{$route.query.article.rate}}</h3>
                    {{$route.query.article.content}}
                    <br>
                    {{$route.query.article.genre}}
                    <br>
                    <!-- <p>created_at : {{ $route.query.article.created_at }}</p> -->
                    <!-- <p>updated_at : {{ $route.query.article.updated_at }}</p> -->
                  </b-card-text>
                </b-card-body>
              </b-col>
          </b-row>
        </b-card>
        <br>
        <b-button pill variant="primary" @click="toArticles">Back</b-button>
        <b-button v-if="user.pk === $route.query.article.user" pill variant="info" @click="toUpdate($route.query.article)">Update</b-button>
        <b-button v-if="user.pk === $route.query.article.user" pill variant="danger" @click="deleteArticle($route.query.article)">Delete</b-button>
      </b-col>
      <b-col cols="2">
      </b-col>
    </b-row>
    <br>
    <br>
    <div>
  <b-card title="" body-class="text-center" header-tag="nav">
    <template #header>
      <b-nav card-header tabs>
        <b-nav-item active>Active</b-nav-item>
        <b-nav-item>Inactive</b-nav-item>
        <b-nav-item disabled>Disabled</b-nav-item>
      </b-nav>
    </template>

    <b-card-text class="text-dark">
      <h3>Comments</h3>
      <div v-if="!hiComments.length">
        <p>No Comments</p>
      </div>
      <div v-else v-for="(comment, idx) in hiComments" :key="idx" class="justify-content-between">
        <span class="mr-5">{{comment.user}} : {{ comment.content }}</span>
        <!-- <span class="mr-5">created_at : {{comment.created_at}}  updated_at : {{ comment.updated_at }}</span> -->
        <span v-if="user.pk === comment.user">
          <b-button pill variant="info" @click="updateComment(comment.content)">Update</b-button>
          <b-button pill variant="danger" @click="deleteComment(comment)">Delete</b-button>
        </span>
      </div>
    </b-card-text>
    <div>
      <input type="text" v-model="comment.content" @keypress.enter="commentCreate">
      <b-button variant="warning" class="ml-4" @click="commentCreate">comment</b-button>
    </div>
  </b-card>
</div>
  <br>
  <br>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ArticleDetail',
  data: function () {
    return {
      user: '',
      comments: [],
      comment: {
        content: ''
      },
    }
  },
  computed: {
    hiComments: function () {
      return this.comments
    }
  },
  methods: {
    toArticles: function () {
      this.$router.push({name:'Articles'})
    },
    getToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    deleteArticle: function (article) {
      const config = this.getToken()
      // console.log(article)
      axios.delete(`${SERVER_URL}/articles/${article.id}/`, config)
        .then(res => {
          console.log(res)
          console.log(article.pk)
          this.$router.push({name:'Articles'})
        })
        .catch(err => {
          console.log(err)
        })
    },
    // updateArticle: function (article) {
    //   const config = this.getToken()
    //   const articleItem = {
    //     title: article.title,
    //     rate: article.rate,
    //     content: article.content
    //   }
    //   axios.put(`${SERVER_URL}/articles/${article.id}/`, articleItem, config)
    //     .then((res) => {
    //       console.log(res)
    //     })
    //     .catch((err) => {
    //       console.log(err)
    //     })
    // },
    toUpdate: function (article) {
      this.$router.push({name: 'ArticleUpdate', query: {article: article}})
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
    getComments: function () {
      const config = this.getToken()
      const id = this.$route.query.article.id
      // console.log(id)
      axios.get(`${SERVER_URL}/articles/${id}/comment_list_create/`, config)
        .then((res) => {
          console.log(res)
          this.comments = res.data
          // console.log(this.comments)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    commentCreate: function() {
      const config = this.getToken()
      const id = this.$route.query.article.id
      axios.post(`${SERVER_URL}/articles/${id}/comment_list_create/`, this.comment, config)
        .then((res) => {
          this.getComments()
          console.log(res)
          // this.$router.push({ name:'Articles' })
        })
        .catch((err) => {
          console.log(err)
        })
    },
    updateComment: function (content) {
      this.comment.content = content
    },
    deleteComment: function (comment) {
      const config = this.getToken()
      axios.delete(`${SERVER_URL}/articles/${comment.id}/comment_delete/`, config)
        .then(res => {
          console.log(res)
          this.getComments()
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created: function () {
    this.getUser()
    this.getComments()
    // console.log(this.$route.query.article.id)
  }
}
</script>

<style>

</style>