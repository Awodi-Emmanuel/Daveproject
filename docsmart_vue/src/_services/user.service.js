
import { authHeader } from '../_helpers'

const AUTH_BASE_URL = 'http://127.0.0.1:8000/api/auth'

export const userService = {
  login,
  logout,
  register,
  completesRegistration,
  getAll,
  getById,
  update,
  delete: _delete
}

function login (username, password) {
  var User = new FormData()
  User.append('email', username)
  User.append('password', password)
  console.log(User.get('email'))
  const requestOptions = {
    method: 'POST',
    body: User
  }

  const response = fetch(AUTH_BASE_URL + '/login', requestOptions)
  const user = handleResponse(response)
  // login successful if there's a jwt token in the response
  if (user.token) {
    // store user details and jwt token in local storage to keep user logged in between page refreshes
    localStorage.setItem('user', JSON.stringify(user))
  }
  return user
}

function logout () {
  // remove user from local storage to log user out
  localStorage.removeItem('user')
}

function register (user) {
  var User = new FormData()
  User.append('email', user.email)

  const requestOptions = {
    method: 'POST',
    // headers: { 'Content-Type': 'application/json' },
    body: User
  }

  const response = fetch(AUTH_BASE_URL + '/signup', requestOptions)
  return handleResponse(response)
}

function completesRegistration (user) {
  var User = new FormData()
  User.append('email', user.email)
  User.append('first_name', user.email)
  User.append('last_name', user.email)
  User.append('phone', user.email)
  User.append('password', user.email)
  User.append('last_name', user.email)
  User.append('company_name', user.email)
  User.append('company_email', user.email)

  const requestOptions = {
    method: 'POST',
    body: User
  }

  const response = fetch(AUTH_BASE_URL + '/complete-signup', requestOptions)
  return handleResponse(response)
}

async function getAll () {
  const requestOptions = {
    method: 'GET',
    headers: authHeader()
  }

  const response = await fetch('/users/register', requestOptions)
  return handleResponse(response)
}

async function getById (id) {
  const requestOptions = {
    method: 'GET',
    headers: authHeader()
  }

  const response = await fetch('/users/', requestOptions)
  return handleResponse(response)
}

async function update (user) {
  const requestOptions = {
    method: 'PUT',
    headers: { ...authHeader(), 'Content-Type': 'application/json' },
    body: JSON.stringify(user)
  }

  const response = await fetch('`/users/', requestOptions)
  return handleResponse(response)
}

// prefixed function name with underscore because delete is a reserved word in javascript
async function _delete (id) {
  const requestOptions = {
    method: 'DELETE',
    headers: authHeader()
  }

  const response = await fetch('/users/', requestOptions)
  return handleResponse(response)
}

function handleResponse (response) {
  return response.then(text => {
    const data = text.data && JSON.parse(text.data)
    if (!text.ok) {
      if (text.status === 401) {
        // auto logout if 401 response returned from api
        logout()
      }

      const error = (text && text.message) || text.statusText
      return Promise.reject(error)
    }

    return data
  })
}
