<template>
  <div class="min-h-screen flex flex-col bg-gray-800">
    <Navbar />
    <slot name="body" />
  </div>
</template>

<script setup>
import Navbar from '~/components/Navbar.vue'
</script>
