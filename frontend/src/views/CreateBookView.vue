<template>
  <div class="create-book">
    <h1>New Book</h1>
    <v-form class="mt-4">
      <v-text-field
        v-model="title"
        label="Book Title"
        required
      />
      <v-text-field
        v-model="author"
        label="Book Author"
        required
      />
      <v-select
        v-model="rating"
        :items="ratingDropdownData"
        :rules="[v => !!v || 'Item is required']"
        required
      />
      <v-btn :disabled="!isValid" @click="handleCreateBook">Create</v-btn>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'CreateBookView',
  data() {
    return {
      title: '',
      author: '',
      rating: 1,
    };
  },
  computed: {
    ratingDropdownData() {
      return [1, 2, 3, 4, 5];
    },
    isValid() {
      return !!this.title && !!this.author;
    },
  },
  methods: {
    async handleCreateBook() {
      this.$router.push('/books');
    },
  },
};
</script>
