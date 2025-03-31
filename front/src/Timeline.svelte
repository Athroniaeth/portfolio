<script lang="ts">
  import { Card, CardContent, CardHeader, CardTitle } from "$lib/components/ui/card";
  import { Separator } from "$lib/components/ui/separator";
  import { Calendar, MapPin } from "lucide-svelte";

  export let items: Array<{
    title: string;
    subtitle: string;
    date: string;
    location?: string;
    description?: string;
    icon?: ConstructorOfATypedSvelteComponent;
  }> = [];
</script>

<div class="relative">
  <!-- Ligne verticale de la timeline -->
  <div class="absolute left-4 top-0 h-full w-0.5 bg-primary/10 md:left-1/2" style="background-color:blueviolet"></div>

  <div class="space-y-8">
    {#each items as item, i (i)}
      <div class="relative flex gap-6" >
        <!-- Point de la timeline -->
        <div
          class="absolute left-0 top-1.5 z-10 flex h-8 w-8 items-center justify-center rounded-full bg-primary text-primary-foreground shadow-md md:left-1/2 md:-translate-x-1/2"
        style="top:40%">
          {#if item.icon}
            <svelte:component this={item.icon} class="h-4 w-4"/>
          {:else}
            {i + 1}
          {/if}
        </div>

        <!-- Carte de l'événement -->
        <Card
          class="ml-12 flex-1 md:ml-0 md:max-w-[calc(50%-32px)] {i % 2 === 0 ? 'md:mr-auto md:pr-8' : 'md:ml-auto md:pl-8'}"
        >
          <CardHeader>
            <p class="text-sm font-medium text-muted-foreground">{item.subtitle}</p>


            <CardTitle class="text-lg">{item.title}</CardTitle>
<div class="flex items-center gap-2 text-sm text-muted-foreground">
              <Calendar class="h-4 w-4" />

              <span>{item.date}</span>
              {#if item.location}
                <span class="flex items-center gap-2">
                  <Separator orientation="vertical" class="h-4" />
                  <MapPin class="h-4 w-4" />
                  <span>{item.location}</span>
                </span>
              {/if}
            </div>
          </CardHeader>

          <CardContent class="space-y-2 p-3 px-6">


            {#if item.description}
              <p class="text-sm text-muted-foreground pb-3">{item.description}</p>
            {/if}
          </CardContent>
        </Card>
      </div>
    {/each}
  </div>
</div>