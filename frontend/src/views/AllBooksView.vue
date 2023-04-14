<template>
  <div class="all-books">
    <h1>All Books</h1>
    <v-table class="mt-10">
      <thead>
        <th class="text-left">Title</th>
        <th class="text-left">Author</th>
        <th class="text-left">Rating</th>
      </thead>
      <tbody>
        <tr v-for="book of books" :key="book.bookId">
          <td><router-link :to="`/books/${book.bookId}`">{{ book.title }}</router-link></td>
          <td>{{ book.author }}</td>
          <td>{{ book.rating }}</td>
        </tr>
      </tbody>
    </v-table>
  </div>
</template>

<script>
export default {
  name: 'AllBooksView',
  data() {
    return {
      books: [{ bookId: 1, title: 'Harry Potter', author: 'JK Rowling', rating: 4 }]
    };
  },
};
</script>
