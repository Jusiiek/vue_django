<script setup lang="ts">
import {ref, onMounted} from 'vue'
import {useRoute} from 'vue-router'
import {UserService} from '~/services/user'
import type {UserInterface} from '~/interfaces'

const route = useRoute()
const isGlobal = route.query.global === 'true'

const userList = ref<UserInterface[]>([])
const loading = ref(false)

onMounted(async () => {
  loading.value = true
  try {
    const {res, data} = await UserService.getUserList(isGlobal)
    if (res.ok && data) {
      userList.value = data
    }
  } catch (error) {
    console.error('Failed to fetch user list:', error)
  } finally {
    loading.value = false
  }
})

const formatBoolean = (val: boolean) => (val ? 'Yes' : 'No')
</script>

<template>
  <NuxtLayout name="custom">
    <template #body>
      <div class="flex-1 p-8">
        <h1 class="text-2xl text-blue-500" v-if="loading">
          Loading users...
        </h1>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4" v-else>
          <div
              v-for="user in userList"
              :key="user.id"
              class="max-w-[420px] p-4 rounded-xl shadow-2xl dark:bg-gray-900 dark:text-white bg-white text-gray-900"
          >
            <h3 class="text-lg font-bold mb-2 text-center">{{ user.email }}</h3>
            <ul class="text-sm space-y-1">
              <li><strong>ID:</strong> {{ user.id }}</li>
              <li><strong>Staff:</strong> {{ formatBoolean(user.is_staff) }}</li>
              <li><strong>Active:</strong> {{ formatBoolean(user.is_active) }}</li>
              <li><strong>Verified:</strong> {{ formatBoolean(user.is_verified) }}</li>
              <li><strong>Superuser:</strong> {{ formatBoolean(user.is_superuser) }}</li>
              <li><strong>Global User:</strong> {{ formatBoolean(user.is_global_user) }}</li>
              <li><strong>Created:</strong> {{ user.created }}</li>
            </ul>
          </div>
        </div>
      </div>
    </template>
  </NuxtLayout>
</template>

<style scoped>

</style>