<template>
  <div id="signup">
      <!-- Testing Testing -->
    <section>
    <form action="">
        <label for="email">Email:</label>
        <input type="email"><br>
         <label for="password">Password:</label>
        <input type="password"><br>
        <button>Submit</button>
    </form>
    </section>
  </div>
</template>

<script>
export default {
  name: 'SignUp',
  props: {
    msg: String
  }
}
</script>

<style>
.margin-bottom {
  margin-bottom: 15px;
}

.fade-enter,
.fade-leave-active {
  opacity: 0;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
</style>
