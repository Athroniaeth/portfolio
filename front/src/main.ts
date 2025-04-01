import { mount } from 'svelte'
import './app.css'
import App from './App.svelte'
export const images = import.meta.glob('/src/assets/**/*.{png,jpg,jpeg,svg,gif,webp}', { eager: true });

const app = mount(App, {
  target: document.getElementById('app')!,
})

export default app
