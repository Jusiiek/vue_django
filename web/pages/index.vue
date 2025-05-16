<script setup lang="ts">
import { getStoreName } from "~/constant/config";
</script>

<template>
  <NuxtLayout name="custom">
    <template #body>
      <div class="flex-1 p-8">
        <h1 class="text-2xl text-blue-500">Welcome to {{ getStoreName() }} store</h1>
      </div>
    </template>
  </NuxtLayout>
</template>

<style scoped>
/* optional */
</style>
