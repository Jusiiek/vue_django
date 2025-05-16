import { useRuntimeConfig, useRoute } from '#imports'

export const useBaseUrl = (is_global=false) => {
  const config = useRuntimeConfig()
  const route = useRoute()

  if (is_global) return config.public.GLOBAL_API

  return route.path.includes('global')
    ? config.public.GLOBAL_API
    : config.public.STORE_API
}
