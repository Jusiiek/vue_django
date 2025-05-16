<template>
  <NuxtLayout name="custom">
    <template #body>
      <div class="flex-1 p-8">
        <div class="p-8 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <PodCard
              v-for="pod in samplePods"
              :key="pod.domain"
              :domain="pod.domain"
              :state="pod.state"
              @delete="handleDelete(pod.domain)"
          />
        </div>
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
    </template>
  </NuxtLayout>
</template>

<script setup lang="ts">
import {ref} from "vue";
import {navigateTo} from "nuxt/app";

type Pod = {
  domain: string
  state: 'running' | 'closed' | 'crashed'
}

const samplePods: Pod[] = [
  {domain: "Running", state: "running"},
  {domain: "Closed", state: "closed"},
  {domain: "Crashed", state: "crashed"}
]

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

const handleDelete = async (domain: string) => {
  console.log(`Deleting ${domain}`);
}
</script>

<style scoped>
/* optional */
</style>
