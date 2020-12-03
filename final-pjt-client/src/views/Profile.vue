<template>
  <div class="mx-5 px-5">
    <h2>Profile</h2>
    <br>
    <br>
    <div class="mx-5 px-5">
      <div class="mx-5 px-5">
        <div class="mx-5 px-5">
          <b-jumbotron class="text-dark">
            <template #header>{{ user.username }}</template>

            <template #lead>
              This is a simple hero unit, a simple jumbotron-style component for calling extra attention to
              featured content or information.
            </template>

            <hr class="my-4">

            <p>
              It uses utility classes for typography and spacing to space content out within the larger
              container.
            </p>

            <b-button variant="primary" href="#">Do Something</b-button>
            <b-button variant="success" href="#">Do Something Else</b-button>
          </b-jumbotron>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Profile',
  data: function () {
    return {
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
    this.getUser()
  }
}
</script>

<style>

</style>