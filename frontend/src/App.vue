<template>
  <v-app>
    <v-main>
      <v-app-bar>
        <v-app-bar-title><router-link class="nav-link" to="/">Home</router-link></v-app-bar-title>
        <v-app-bar-title><router-link class="nav-link" to="/books">All Books</router-link></v-app-bar-title>
        <v-app-bar-title><router-link class="nav-link" to="/books/new">Create Book</router-link></v-app-bar-title>
      </v-app-bar>
      <v-container>
        <router-view class="mt-6" />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',
}
</script>

<style scoped>
.nav-link {
  text-decoration: none;
  color: blue;
}
</style>
