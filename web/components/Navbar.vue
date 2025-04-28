<script setup lang="ts">
import {ref} from 'vue'
import {navigateTo} from 'nuxt/app'
import type {DropdownMenuItem} from '@nuxt/ui'

const logout = async() => {
  console.log("LOGOUT")
  // if (process.client) {
  //   localStorage.removeItem('user')
  // }
  // navigateTo('/auth/login')
}

const items = ref<DropdownMenuItem[]>([
  {
    label: 'Logout',
    icon: 'i-heroicons-arrow-left-on-rectangle',
    onSelect() {
      logout();
    },
  }
])
</script>

<template>
  <div class="flex items-center justify-between px-6 py-4 bg-gray-900 shadow">
    <div class="text-xl font-bold">My App</div>

    <div>
      <UDropdownMenu
          :items="items"
          :content="{
            align: 'start',
            side: 'bottom',
            sideOffset: 8
          }"
          :ui="{
            content: 'w-48'
          }"
      >
        <UAvatar
              size="md"
              src="https://i.pravatar.cc/150?img=3"
              alt="User Avatar"
              class="cursor-pointer"
              label="open"
          />

      </UDropdownMenu>
    </div>
  </div>
</template>

<style scoped>
/* optional */
</style>
