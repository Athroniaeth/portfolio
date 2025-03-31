<script lang="ts">
    import {CardHeader, CardTitle} from "$lib/components/ui/card";
    import {Button} from "$lib/components/ui/button";
    import {ExternalLink, Github} from "lucide-svelte";
    import {Badge} from "$lib/components/ui/badge";
   import * as Card from "$lib/components/ui/card";
    import * as Carousel from "$lib/components/ui/carousel";
      import * as Avatar from "$lib/components/ui/avatar";
    export let projects: Array<{
        title: string;
        description: string;
        githubUrl: string;
        liveUrl?: string;
        technologies: string[];
        image?: string;
    }> = [];
</script>

<Carousel.Root opts={{ align: "start", loop: true }} class="w-full max-w-4xl mx-auto">
    <Carousel.Content>
        {#each projects as project (project.title)}
            <Carousel.Item class="md:basis-1/2 lg:basis-1/3">
                <div class="p-2">
                    <Card.Root class="h-full flex flex-col">

                        <CardHeader class="p-0">
                            <img
                                    src={project.image || "/src/assets/github-logo.png"}
                                    alt={project.title}
                                    class="w-full h-40 object-cover rounded-t-lg"
                            />
                        </CardHeader>

                        <Card.Content class="flex-1 p-6">
                            <CardTitle class="mb-2">{project.title}</CardTitle>
                            <p class="text-sm text-muted-foreground mb-4">{project.description}</p>
                            <div class="flex flex-wrap gap-1 mb-4">
                                {#each project.technologies as tech}
                                    <Badge variant="secondary">{tech}</Badge>
                                {/each}
                            </div>
                        </Card.Content>
                        <Card.Footer class="flex justify-between p-6 pt-0">
                            <Button> <!--variant="ghost"-->
                                <Github class="mr-2 h-4 w-4" />
                                <a href={project.githubUrl} target="_blank" rel="noopener noreferrer">

                              Code
                                </a>
                            </Button>

                            {#if project.liveUrl}
                                                                                            <Button>
                                <ExternalLink class="mr-2 h-4 w-4" />
                                <a href={project.liveUrl} target="_blank" rel="noopener noreferrer">

                              Voir projet
                                </a>
                            </Button>
                            {/if}
                        </Card.Footer>
                    </Card.Root>
                </div>
            </Carousel.Item>
        {/each}
    </Carousel.Content>
    <Carousel.Previous class="hidden md:flex"/>
    <Carousel.Next class="hidden md:flex"/>
</Carousel.Root>