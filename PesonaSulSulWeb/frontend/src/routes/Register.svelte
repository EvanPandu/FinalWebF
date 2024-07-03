<script>
  import { navigate } from 'svelte-routing';

  let username = '';
  let password = '';
  let role = 'User';

  async function handleRegister() {
    const response = await fetch('http://localhost:5000/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ username, password, role })
    });

    const data = await response.json();
    if (data.success) {
      navigate('/');
    } else {
      alert('Registration failed');
    }
  }
</script>

<div class="container">
  <h2>Register</h2>
  <input type="text" placeholder="Username" bind:value={username} />
  <input type="password" placeholder="Password" bind:value={password} />
  <select bind:value={role}>
    <option>User</option>
    <option>Admin</option>
  </select>
  <button class="register" on:click={handleRegister}>Register</button>
</div>
