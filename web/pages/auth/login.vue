<template>
  <div class="flex min-h-screen items-center justify-center bg-gray-900">
    <UCard class="w-full max-w-md">
      <template #header>
        <h1 class="text-2xl font-bold text-center">Login</h1>
      </template>

      <UForm :state="form" @submit="onSubmit" class="space-y-6 text-center">
        <UInput
            v-model="form.email"
            type="email"
            placeholder="you@example.com"
            required
            class="w-full"
            size="xl"
        />

        <UButton type="submit" color="primary" class="max-w-[100px] ml-auto mr-auto" block :loading="loading">
          Sign In
        </UButton>
      </UForm>

      <template #footer>
        <div class="text-center text-sm text-gray-500">
          Don't have an account? <h2 class="text-primary">Register</h2>
        </div>
      </template>
    </UCard>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { navigateTo } from 'nuxt/app'
import { useRoute } from '#imports'
import { ActiveUser } from "~/instance/user"
import { AuthService } from "~/services/auth";
import { UserService } from "~/services/user";

const route = useRoute()

const form = ref({
  email: '',
})

const loading = ref(false)
const isGlobal = route.query.global === 'true';

const onSubmit = async () => {
  loading.value = true

  let { res, data } = await AuthService.login(form.value.email, isGlobal);
  if (res.status === 200 && data) {
    console.log("data", data)
    ActiveUser.setToken(data)
    let { res, data } = await UserService.getUser("me", isGlobal);
    if (res.status === 200 && data) {
      ActiveUser.set(data);
      navigateTo('/')
    }
  }

  loading.value = false
  form.value.email = ''
}
</script>

<style scoped>
</style>
