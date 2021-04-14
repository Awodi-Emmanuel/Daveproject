<template>
    <div class="signup">
        <SignUp msg="Welcome to Your Vue.js App"/>
    </div>
</template>

<script>
// @ is an alias to /src
import SignUp from '@/components/SignUp.vue'

export default {
  name: 'Join',
  components: {
    SignUp
  }
}
</script>
