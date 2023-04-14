<template>
  <div class="single-book">
    <template v-if="book">
      <h1>{{ book.title }}</h1>
      <v-btn flat @click="handleEditClick">Edit</v-btn>
      <v-btn flat @click="handleDeleteClick">Delete</v-btn>
      <h2 class="mt-2">Written by {{ book.author }}</h2>
      <p class="mt-3">Rated {{ book.rating }} out of 5</p>
    </template>
  </div>
</template>

<script>
export default {
  name: 'SingleBooksView',
  data() {
    return {
      book: { bookId: 1, title: 'Harry Potter', author: 'JK Rowling', rating: 4 }
    };
  },
  computed: {
    bookId() {
      return this.$route.params.bookId;
    },
  },
  methods: {
    handleEditClick() {
      this.$router.push(`/books/${this.book.bookId}/edit`);
    },
    handleDeleteClick() {
      this.$router.push('/books');
    },
  },
};
</script>
