<script>
  import { Router, Link, Route } from 'svelte-routing';
  import Login from './routes/Login.svelte';
  import Register from './routes/Register.svelte';
</script>

<main>
  <nav>
    <Link to="/">Login</Link>
    <Link to="/register">Register</Link>
  </nav>

  <Router>
    <Route path="/" component={Login} />
    <Route path="register" component={Register} />
  </Router>
</main>

<style>
  nav {
    display: flex;
    justify-content: center;
    margin-bottom: 20px;
  }

  nav a {
    margin: 0 10px;
    text-decoration: none;
    color: #000;
  }
</style>
