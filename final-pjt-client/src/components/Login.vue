<template>
 <div class="bg-white">
    <br>
    <br>
    <br>
    <div class="row" style='height : 600px; justify-content: space-between; align-items: center;'>
      <div class="box col-3"></div>
      <div class="box col-3">
        <img src="../assets/iPhoneX.png" alt="iPhone Logo" style='width: 90%; height: 90%;'>
      </div>

    <!-- Login -->
    <div class="col-3" v-if="!dummy">
      <div class="card" style="width: 18rem;" >
        <!-- 로그인 박스-->
        <div class="card-body">
          <!-- Insta 로고 -->
          <h2 id="logo" class='text-center'>Moviegram</h2>
          <br>
          <!-- 로그인 form -->
          <input style='width: 250px' type="text" v-model="credentials.username" id="username" placeholder='Phone number, username, or email' autofocus>
          <input style='width: 250px' type="password" v-model="credentials.password" id="password" placeholder='Password' @keypress.enter='login'>
          <br>
          <br>
          <b-button @click="login" variant="primary" class="font-weight-bold btn-sm btn-block">Log in</b-button>
          <br>
          <h6 class="card-subtitle mb-2 text-muted text-center">-------------- or --------------</h6>
          <br>
          <p class='text-center font-weight-bold small'><a href="https://www.facebook.com/" class="card-link">
            <img src="../assets/facebook_logo.png" alt="Facebook Logo" style='width: 10%; height: 10%;'> 
          Log in with Facebook</a></p>
          <p class='text-center small'><a href="#" class="card-link">Forgot Password?</a></p>
        </div>
      </div>
      <br>
      <div class="card" style="width: 18rem;">
          <h6 class="my-2 text-center card-subtitle mb-2 text-muted">No accounts yet?  <a @click="toSignup" href="#">Signup</a></h6>
      </div>
    </div>

    <!-- Signup -->
    <div class="col-3" v-else>
      <div class="card" style="width: 18rem;" >
        <!-- 로그인 박스-->
        <div class="card-body">
          <!-- Insta 로고 -->
          <h2 id="logo" class='text-center'>Moviegram</h2>
          <br>
          <!-- 로그인 form -->
          <input style='width: 250px' type="text" v-model="credentials.username" id="username" placeholder='Phone number, username, or email' autofocus>
          <input style='width: 250px' type="password" v-model="credentials.password" id="password" placeholder='Password'>
          <input style='width: 250px' type="password" v-model="credentials.passwordConfirmation" id="passwordConfirmation" placeholder='Password Confirmation' @keypress.enter='signup'>
          <br>
          <br>
          <b-button @click="signup" variant="primary" class="font-weight-bold btn-sm btn-block">Sign up</b-button>
          <br>
          <h6 class="card-subtitle mb-2 text-muted text-center">-------------- or --------------</h6>
          <br>
          <p class='text-center font-weight-bold small'><a href="https://www.facebook.com/" class="card-link">
            <img src="../assets/facebook_logo.png" alt="Facebook Logo" style='width: 10%; height: 10%;'> 
          Signup with Facebook</a></p>
        </div>
      </div>
      <br>
      <div class="card" style="width: 18rem;">
          <h6 class="my-2 text-center card-subtitle mb-2 text-muted">Go to  <a @click="toLogin" href="#">Login</a></h6>
      </div>
    </div>


      <div class="box col-2"></div>
  </div>
    </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL= process.env.VUE_APP_SERVER_URL

export default {
  name: 'Login',
  data: function(){
  return {
    credentials:{
      username:'',
      password:'',
      passwordConfirmation: ''
    },
    dummy: false
    }
  },
  computed: {
    hiSignup: function () {
      return this.dummy
    }
  },
methods: {
  login: function () {
    axios.post(`${SERVER_URL}/api-token-auth/`, this.credentials)
      .then((res)=>{
        localStorage.setItem('jwt', res.data.token)
        this.$emit('login-ed')
      })
      .catch((err) => {
        console.log(err)
      })
  },
  toSignup: function () {
    this.dummy = true
    this.credentials.user = ''
    this.credentials.password = ''
    this.credentials.passwordConfirmation = ''
  },
  toLogin: function () {
    this.credentials.user = ''
    this.credentials.password = ''
    this.credentials.passwordConfirmation = ''
    this.dummy = false
  },
  signup: function () {
    axios.post(`${SERVER_URL}/signup/`, this.credentials)
      .then(() => {
        this.dummy = false
      })
      .catch((err) => {
        console.log(err)
      })
  }
  },
  created: function () {
    this.dummy = false
    this.credentials.user = ''
    this.credentials.password = ''
    this.credentials.passwordConfirmation = ''
  }
}

</script>

<style>
#logo {
  color: black;
  font-family : cursive;
}
</style>