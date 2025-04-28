<template>
  <div class="min-h-screen flex flex-col bg-gray-800">
    <!-- Navbar -->
    <Navbar/>

    <!-- Main Content -->
    <div class="flex-1 p-8">
      <h1 class="text-2xl font-semibold">Home Page</h1>
      <p class="text-gray-500 mt-2">Welcome to your dashboard!</p>
    </div>
    <div class="flex-1 p-8 flex flex-col items-center justify-center text-center">
      <UForm :state="form" @submit="onSubmit" class="space-y-6 w-full max-w-xs">

        <UFormGroup>
          <UInput
              v-model="form.domain"
              type="text"
              placeholder="Some domain"
              required
              size="xl"
              class="w-full max-w-[300px]"
          />
        </UFormGroup>

        <UButton
            type="submit"
            color="primary"
            block
            :loading="loading"
            class="w-full max-w-[200px] mt-4"
        >
          Create a pod
        </UButton>

      </UForm>
    </div>
  </div>
</template>

<script setup lang="ts">
import {ref} from "vue";
import {navigateTo} from "nuxt/app";

const form = ref({
  domain: '',
})

const loading = ref(false)

const onSubmit = async () => {
  loading.value = true

  try {
    await new Promise((resolve) => setTimeout(resolve, 1000))
    const userData = {domain: form.value.domain}
    if (process.client) {
      localStorage.setItem('user', JSON.stringify(userData))
    }
    navigateTo('/')
  } catch (error) {
    console.error(error)
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
/* optional */
</style>
