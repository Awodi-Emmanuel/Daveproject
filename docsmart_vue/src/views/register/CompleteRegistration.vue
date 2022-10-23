<template>
    <div>
        <h2>Register</h2>
        <form @submit.prevent="handleSubmit">
            <div class="form-group">
                <label for="firstName">First Name</label>
                <input type="text" v-model="user.firstName" name="firstName" class="form-control" :class="{ 'is-invalid': submitted && !user.firstName }" />
                <div v-show="submitted && !user.firstName" class="invalid-feedback">First Name is invalid</div>
            </div>
            <div class="form-group">
                <label for="lastName">Last Name</label>
                <input type="text" v-model="user.lastName" name="lastName" class="form-control" :class="{ 'is-invalid': submitted && !user.lastName }" />
                <div v-show="submitted && !user.lastName" class="invalid-feedback">Last name is invalid</div>
            </div>
            <div class="form-group">
                <label for="companyname">Company Name</label>
                <input type="text" v-model="user.companyname" name="username" class="form-control" :class="{ 'is-invalid': submitted && !user.companyname }" />
                <div v-show="submitted && !user.companyname" class="invalid-feedback">Company Name is invalid</div>
            </div>
            <div class="form-group">
                <label for="comoanyemail">Company Name</label>
                <input type="text" v-model="user.comoanyemail" name="comoanyemail" class="form-control" :class="{ 'is-invalid': submitted && !user.comoanyemail }" />
                <div v-show="submitted && !user.comoanyemail" class="invalid-feedback">Company Email is invalid</div>
            </div>
            <div class="form-group">
                <label htmlFor="password">Password</label>
                <input type="password" v-model="user.password" class="form-control" :class="{ 'is-invalid': submitted && !user.password }" />
                <div v-show="submitted && !user.password" class="invalid-feedback">Password is invalid</div>
            </div>
            <div class="form-group">
                <label htmlFor="confirmpassword">Confirm Password</label>
                <input type="password" v-model="user.confirmpassword" class="form-control" :class="{ 'is-invalid': submitted && !user.confirmpassword }" />
                <div v-show="submitted && !user.confirmpassword" class="invalid-feedback">Password does not match</div>
            </div>
            <div class="form-group">
                <button class="btn btn-primary" :disabled="status.registering">Register</button>
                <img v-show="status.registering" src="data:image/gif;base64,R0lGODlhEAAQAPIAAP///wAAAMLCwkJCQgAAAGJiYoKCgpKSkiH/C05FVFNDQVBFMi4wAwEAAAAh/hpDcmVhdGVkIHdpdGggYWpheGxvYWQuaW5mbwAh+QQJCgAAACwAAAAAEAAQAAADMwi63P4wyklrE2MIOggZnAdOmGYJRbExwroUmcG2LmDEwnHQLVsYOd2mBzkYDAdKa+dIAAAh+QQJCgAAACwAAAAAEAAQAAADNAi63P5OjCEgG4QMu7DmikRxQlFUYDEZIGBMRVsaqHwctXXf7WEYB4Ag1xjihkMZsiUkKhIAIfkECQoAAAAsAAAAABAAEAAAAzYIujIjK8pByJDMlFYvBoVjHA70GU7xSUJhmKtwHPAKzLO9HMaoKwJZ7Rf8AYPDDzKpZBqfvwQAIfkECQoAAAAsAAAAABAAEAAAAzMIumIlK8oyhpHsnFZfhYumCYUhDAQxRIdhHBGqRoKw0R8DYlJd8z0fMDgsGo/IpHI5TAAAIfkECQoAAAAsAAAAABAAEAAAAzIIunInK0rnZBTwGPNMgQwmdsNgXGJUlIWEuR5oWUIpz8pAEAMe6TwfwyYsGo/IpFKSAAAh+QQJCgAAACwAAAAAEAAQAAADMwi6IMKQORfjdOe82p4wGccc4CEuQradylesojEMBgsUc2G7sDX3lQGBMLAJibufbSlKAAAh+QQJCgAAACwAAAAAEAAQAAADMgi63P7wCRHZnFVdmgHu2nFwlWCI3WGc3TSWhUFGxTAUkGCbtgENBMJAEJsxgMLWzpEAACH5BAkKAAAALAAAAAAQABAAAAMyCLrc/jDKSatlQtScKdceCAjDII7HcQ4EMTCpyrCuUBjCYRgHVtqlAiB1YhiCnlsRkAAAOwAAAAAAAAAAAA==" />
                <router-link to="/login" class="btn btn-link">Cancel</router-link>
            </div>
        </form>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  data () {
    return {
      user: {
        firstName: '',
        lastName: '',
        companyname: '',
        companyemail: '',
        password: ''
      },
      submitted: false
    }
  },
  computed: {
    ...mapState('account', ['status'])
  },
  methods: {
    ...mapActions('account', ['register']),
    handleSubmit (e) {
      this.submitted = true
      if (this.user.firstName && this.user.lastName && this.user.companyname && this.user.companyname && this.user.password) {
        this.register(this.user)
      }
    }
  }
}
</script>
