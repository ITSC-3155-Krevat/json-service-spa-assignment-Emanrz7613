<template>
  <div class="edit-book">
    <h1>Edit Book</h1>
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
      <v-btn :disabled="!isValid" @click="handleUpdateBook">Create</v-btn>
      <v-btn @click="handleCancelClick">Cancel</v-btn>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'EditBooksView',
  data() {
    return {
      title: '',
      author: '',
      rating: 1,
    };
  },
  computed: {
    bookId() {
      return this.$route.params.bookId;
    },
    ratingDropdownData() {
      return [1, 2, 3, 4, 5];
    },
    isValid() {
      return !!this.title && !!this.author;
    },
  },
  methods: {
    handleUpdateBook() {
      this.$router.push(`/books/${this.bookId}`);
    },
    handleCancelClick() {
      this.$router.push(`/books/${this.bookId}`);
    },
  },
};
</script>
