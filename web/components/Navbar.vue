<script setup lang="ts">
import {ref} from 'vue'
import {navigateTo} from 'nuxt/app'
import type {DropdownMenuItem} from '@nuxt/ui'
import {ActiveUser} from "~/instance/user";

const logout = async () => {
  ActiveUser.clear()
  navigateTo('/auth/login')
}

const isUserGlobal = ActiveUser.isGlobalUser() || false;

const items = ref<DropdownMenuItem[]>([
  {
    label: 'Logout',
    color: 'error',
    icon: 'i-heroicons-arrow-left-on-rectangle',
    onSelect() {
      logout();
    },
  }
])
</script>

<template>
  <div class="flex items-center justify-between px-6 py-4 bg-gray-900 shadow">
    <div class="text-xl font-bold">
      <ULink to="/">My App</ULink>
    </div>

    <div>
      <ULink
          :to="isUserGlobal ? '/users?global=true' : '/users'"
          class="mr-3"
      >
        User List
      </ULink>
      <ULink to="/global" v-if="isUserGlobal" class="mr-3">Create a store</ULink>
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
