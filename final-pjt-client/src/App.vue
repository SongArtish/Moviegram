<template>
  <div id="app" class="text-white">
    <div v-if="isLogin">
      <!-- <audio autoplay="autoplay">
        <source src="@/assets/music.mp3" type="audio/mp3">
      </audio> -->
      <!-- Navbar (if 로그인) -->
      <div id="nav">
        <b-navbar toggleable="lg" type="dark" variant="dark" class="ml-5 mr-5">
          <b-icon variant="warning" icon="star-fill" animation="fade" font-scale="2" class="mr-3"></b-icon>
          <b-navbar-brand href="#"><router-link :to="{ name: 'Home' }" class="text-white font-weight-bold" style="font-family: cursive;">Moviegram</router-link></b-navbar-brand>
          <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
          <b-collapse id="nav-collapse" is-nav>
            <!-- 검색창 -->
            <b-nav-form class="ml-auto">
              <!-- Using slots -->
              <b-form-input autocomplete @keypress.enter="search(keyword)" size="sm" class="mr-sm-2" placeholder="Search" v-model="keyword" autofocus></b-form-input>
              <!-- required -->
              <b-form-input hidden></b-form-input>
              <!-- <b-button size="sm" class="my-2 my-sm-0">Search</b-button> -->
            </b-nav-form>
            <!-- Right aligned nav items -->
            <!-- 1. 로그인 했을 경우 -->
            <b-navbar-nav class="ml-auto" v-if="isLogin">
              <b-navbar-nav>
                <b-nav-item href="#"><router-link :to="{ name: 'MovieList' }" class="text-white"><p class="h5 mt-4" @mouseover="iconOn1" @mouseout="iconOff1"><b-icon v-if="icon1" icon="camera-reels-fill" variant="primary" aria-hidden="true"></b-icon><b-icon v-else icon="camera-reels" variant="primary" aria-hidden="true"></b-icon></p></router-link></b-nav-item>
                <b-nav-item href="#"><router-link :to="{ name: 'MovieRecommend' }" class="text-white"><p class="h5 mt-4" @mouseover="iconOn2" @mouseout="iconOff2"><b-icon v-if="icon2" icon="heart-fill" variant="danger" aria-hidden="true"></b-icon><b-icon v-else icon="heart" variant="danger" aria-hidden="true"></b-icon></p></router-link></b-nav-item>
                <b-nav-item href="#"><router-link :to="{ name: 'Articles' }" class="text-white"><p class="h5 mt-4" @mouseover="iconOn3" @mouseout="iconOff3"><b-icon v-if="icon3" icon="chat-dots-fill" variant="warning" aria-hidden="true"></b-icon><b-icon v-else icon="chat-dots" variant="warning" aria-hidden="true"></b-icon></p></router-link></b-nav-item>
                <b-nav-item href="#"><router-link :to="{ name: 'Entertainment' }" class="text-white"><p class="h5 mt-4" @mouseover="iconOn4" @mouseout="iconOff4"><b-icon v-if="icon4" icon="collection-play-fill" variant="info" aria-hidden="true"></b-icon><b-icon v-else icon="collection-play" variant="info" aria-hidden="true"></b-icon></p></router-link></b-nav-item>
                <!-- <b-nav-item href="#" disabled>Disabled</b-nav-item> -->
              </b-navbar-nav>
              <b-nav-item-dropdown right id="dropdown">
                <!-- Using 'button-content' slot -->
                <template #button-content>
                  <em class="text-white"><p class="h5 mt-4" @mouseover="iconOn5" @mouseout="iconOff5"><b-icon v-if="icon5" icon="person-circle" variant="secondary" aria-hidden="true"></b-icon><b-icon v-else icon="person-circle" variant="white" aria-hidden="true"></b-icon></p></em>
                </template>
                <b-dropdown-item @click.native="toProfile" href="#">Profile</b-dropdown-item> <!-- 클릭했을 때 라우터 함수 -->
                <b-dropdown-item href="#">Settings</b-dropdown-item>
                <b-dropdown-item @click.native="logout" href="#">Logout</b-dropdown-item>
                <!-- <b-dropdown-item @click.native="logout" href="#">Logout</b-dropdown-item> -->
              </b-nav-item-dropdown>
            </b-navbar-nav>
            <!-- 2. 로그인 하지 않았을 경우 -->
            <b-navbar-nav class="ml-auto" v-else>
              <b-navbar-nav>
                <b-nav-item href="#"><router-link :to="{ name: 'MovieList' }" class="text-white"><p class="h5 mt-4" @mouseover="iconOn1" @mouseout="iconOff1"><b-icon v-if="icon1" icon="camera-reels-fill" variant="primary" aria-hidden="true"></b-icon><b-icon v-else icon="camera-reels" variant="primary" aria-hidden="true"></b-icon></p></router-link></b-nav-item>
                <b-nav-item href="#"><router-link :to="{ name: 'MovieRecommend' }" class="text-white"><p class="h5 mt-4" @mouseover="iconOn2" @mouseout="iconOff2"><b-icon v-if="icon2" icon="heart-fill" variant="danger" aria-hidden="true"></b-icon><b-icon v-else icon="heart" variant="danger" aria-hidden="true"></b-icon></p></router-link></b-nav-item>
                <b-nav-item href="#"><router-link :to="{ name: 'Articles' }" class="text-white"><p class="h5 mt-4" @mouseover="iconOn3" @mouseout="iconOff3"><b-icon v-if="icon3" icon="chat-dots-fill" variant="warning" aria-hidden="true"></b-icon><b-icon v-else icon="chat-dots" variant="warning" aria-hidden="true"></b-icon></p></router-link></b-nav-item>
                <b-nav-item href="#"><router-link :to="{ name: 'Entertainment' }" class="text-white"><p class="h5 mt-4" @mouseover="iconOn4" @mouseout="iconOff4"><b-icon v-if="icon4" icon="collection-play-fill" variant="info" aria-hidden="true"></b-icon><b-icon v-else icon="collection-play" variant="info" aria-hidden="true"></b-icon></p></router-link></b-nav-item>
                <!-- <b-nav-item href="#" disabled>Disabled</b-nav-item> -->
              </b-navbar-nav>
              <b-nav-item-dropdown right id="dropdown">
                <!-- Using 'button-content' slot -->
                <template #button-content>
                  <em class="text-white"><p class="h5 mt-4" @mouseover="iconOn5" @mouseout="iconOff5"><b-icon v-if="icon5" icon="person-circle" variant="secondary" aria-hidden="true"></b-icon><b-icon v-else icon="person-circle" variant="white" aria-hidden="true"></b-icon></p></em>
                </template>
                <b-dropdown-item href="#"><router-link :to="{ name: 'Login' }">Login</router-link></b-dropdown-item>
                <b-dropdown-item href="#"><router-link :to="{ name: 'SignUp' }">SignUp</router-link></b-dropdown-item>
              </b-nav-item-dropdown>
            </b-navbar-nav>
          </b-collapse>
        </b-navbar>
      </div>
      <router-view/>
    </div>
    <div v-else>
      <Login @login-ed="logined" />
    </div>
  </div>
</template>

<script>
import Login from '@/components/Login'
import { Glide, GlideSlide } from 'vue-glide-js'

export default {
  name: 'App',
  components: {
    Login,
    [Glide.name]: Glide,
    [GlideSlide.name]: GlideSlide
  },
  data: function () {
    return {
      isLoading: false,
      keyword: '',
      icons: {
        icon1: false,
        icon2: false,
        icon3: false,
        icon4: false,
        icon5: true
      }
    }
  },
  computed: {
    isLogin: function () {
      return this.$store.state.isLogin
    },
    icon1: function () {
      return this.icons.icon1
    },
    icon2: function () {
      return this.icons.icon2
    },
    icon3: function () {
      return this.icons.icon3
    },
    icon4: function () {
      return this.icons.icon4
    },
    icon5: function () {
      return this.icons.icon5
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
    toSignup: function () {
      this.$router.push({ name:'SingUp' })
    },
    logout: function () {
      localStorage.removeItem('jwt')
      this.$store.state.isLogin = false
    },
    toProfile: function () {
      this.$router.push({ name:'Profile' })
    },
    logined: function () {
      this.$store.state.isLogin=true
    },
    search: function (keyword) {
      this.$router.push({name: 'SearchMovieList', query: {keyword: keyword}})
      this.keyword = ''
    },
    iconOn1: function () {
      this.icons.icon1 = true
    },
    iconOff1: function () {
      this.icons.icon1 = false
    },
    iconOn2: function () {
      this.icons.icon2 = true
    },
    iconOff2: function () {
      this.icons.icon2 = false
    },
    iconOn3: function () {
      this.icons.icon3 = true
    },
    iconOff3: function () {
      this.icons.icon3 = false
    },
    iconOn4: function () {
      this.icons.icon4 = true
    },
    iconOff4: function () {
      this.icons.icon4 = false
    },
    iconOn5: function () {
      this.icons.icon5 = false
    },
    iconOff5: function () {
      this.icons.icon5 = true
    },
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.$store.state.isLogin = true
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#img {
  width: 35px;
  height: 35px;
}

#nav {
  padding: 30px;
  position: sticky;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

/* #dropdown {
  position: relative;
  z-index: 1;
} */
</style>
