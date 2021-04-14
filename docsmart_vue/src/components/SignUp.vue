<template>
  <div id="signup">
      <!-- Testing Testing -->
    <form action="">
        <input type="email">
        <input type="password">
        <button>Submit</button>
    </form>
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
