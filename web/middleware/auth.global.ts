import { navigateTo } from 'nuxt/app'
import { ActiveUser } from '@/instance/user'

export default defineNuxtRouteMiddleware((to) => {
  const user = ActiveUser.getUser()
  const isAuthPage = to.path.includes('/auth')

  // if (!user && !isAuthPage) {
  //   return navigateTo('/')
  // }
  //
  // if (user && isAuthPage) {
  //   return navigateTo('/')
  // }
})
