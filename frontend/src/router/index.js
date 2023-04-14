import { createRouter, createWebHistory } from 'vue-router'
import ViewContainer from '../views/ViewContainer.vue';
import HomeView from '../views/HomeView.vue'
import AllBooksView from '../views/AllBooksView.vue';
import CreateBookView from '../views/CreateBookView.vue';
import SingleBookView from '../views/SingleBookView.vue';
import EditBookView from '../views/EditBookView.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/books',
    component: ViewContainer,
    children: [
      {
        path: '',
        component: AllBooksView,
        name: 'all-books',
      },
      {
        path: 'new',
        component: CreateBookView,
        name: 'create-book',
      },
      {
        path: ':bookId',
        component: ViewContainer,
        children: [
          {
            path: '',
            component: SingleBookView,
          },
          {
            path: 'edit',
            component: EditBookView,
          },
        ],
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
