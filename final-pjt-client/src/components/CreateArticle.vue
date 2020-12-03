<template>
  <div class="mx-5 px-5">
    <div class="mx-5 px-5">
      <div class="mx-5 px-5">
        <div class="mx-5 px-5">
          <b-form @submit="onSubmit" @reset="onReset" v-if="show">
            <b-form-group
              id="input-group-1"
              label="Movie Title"
              label-for="input-1"
              description="솔직한 리뷰는 환영입니다!!!"
            >
              <b-form-input
                id ="input-1"
                v-model="article.title"
                type="text"
                required
                placeholder="Please write title"
                autofocus
              ></b-form-input>
            </b-form-group>

            <b-form-group id="input-group-2" label="Rate" label-for="input-2">
              <b-form-select
                id="input-2"
                v-model="article.rate"
                :options="rates"
                required
              ></b-form-select>
            </b-form-group>


            <b-form-group id="input-group-3" label="Content" label-for="input-3">
              <b-form-textarea
                id="input-3"
                v-model="article.content"
                placeholder="Please write review"
                required
                rows="3"
                max-rows="6"
              ></b-form-textarea>
            </b-form-group>

            <b-form-group id="input-group-4" label="Genre" label-for="input-4">
              <b-form-select
                id="input-4"
                v-model="article.genre"
                :options="genres"
                required
              ></b-form-select>
            </b-form-group>

            <b-button variant="primary" @click="createArticle">Submit</b-button>
            <b-button type="reset" variant="danger">Reset</b-button>
          </b-form>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  data() {
    return {
      article: {
        title: '',
        rate: '',
        content: '',
        genre: '',
      },
      genres: [{ text: 'Select One', value: null }, 'Horror', 'Romance', 'Comedy', 'Adventure', 'Fantasy', 'Animation','Drama','Action','History','Western','Thriller','Crime','Documentary','SF','Mystery','Music','Family','War','TVmovie'],
      rates: [{ text: 'Rate for it!!', value: null }, '1', '2', '3', '4', '5', '6','7','8','9','10'],
      show: true,
      user: ''
    }
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault()
      alert(JSON.stringify(this.article))
    },
    onReset(evt) {
      evt.preventDefault()
      // Reset our form values
      this.article.title = ''
      this.article.rate = ''
      this.article.content = null
      
      // Trick to reset/clear native browser form validation state
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
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
    createArticle: function () {
      const config = this.getToken()
      axios.post(`${SERVER_URL}/articles/`, this.article, config)
        .then(() => {
          this.$router.push({ name:'Articles' })
        })
        .catch((err) => {
          console.log(err)
        })
        }
    }
  }
</script>

<style>

</style>