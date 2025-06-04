<template>
  <UCard class="p-4 shadow rounded-2xl bg-gray-900">
    <div class="border-2 border-dashed border-gray-300 rounded-xl p-6 flex flex-col gap-4 items-center">

      <div class="text-center">
        <h2 class="text-lg font-semibold">{{ domain }}</h2>
        <div :class="['w-4 h-4 rounded-full ml-auto mr-auto mt-3', stateColor]" />
      </div>

      <UButton color="error" @click="onDelete">
        Delete Store
      </UButton>
    </div>
  </UCard>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{
  domain: string
  state: 'running' | 'closed' | 'crashed'
}>()

const stateColor = computed(() => {
  switch (props.state) {
    case 'running':
      return 'bg-green-500'
    case 'closed':
      return 'bg-gray-400'
    case 'crashed':
      return 'bg-red-500'
    default:
      return 'bg-gray-400'
  }
})

const emit = defineEmits<{
  (e: 'delete'): void
}>()

const onDelete = () => {
  emit('delete')
}
</script>

<style scoped>
</style>
