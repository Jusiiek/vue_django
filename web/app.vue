<script setup lang="ts">
const router = useRouter()

const nav = [
  { label: 'Home', to: '/' },
  { label: 'Login', to: '/auth/about' },
]
</script>

<template>
  <NuxtExample
    dir="routing/pages"
    :nav="nav"
    current-route
  >
    <NuxtLoadingIndicator />
    <NuxtPage />
  </NuxtExample>
</template>
