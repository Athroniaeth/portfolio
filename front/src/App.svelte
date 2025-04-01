<script lang="ts">
    import "./app.css";
    import * as Card from "$lib/components/ui/card/index.js";
    import * as Avatar from "$lib/components/ui/avatar";
    import * as Button from "$lib/components/ui/button";
    import Projects from "./Projects.svelte";
    import Timeline from "./Timeline.svelte";

    import * as Carousel from "$lib/components/ui/carousel/index.js";
    import {
        Briefcase,
        GraduationCap,
        Github,
        Linkedin,
        LoaderPinwheel,
        Mail,
        Menu,
        X,
        Code,
        Lightbulb,
        Globe,
        Download,
        BrainCog,
        Container,
        FolderCode,
    } from "lucide-svelte";
    import { onMount } from "svelte";
    import { config, loadConfig } from "./config";
    
    // État pour le menu mobile
    let isMobileMenuOpen = false;
    
    // État pour suivre la section active
    let activeSection = "home";
    
    // Compétences mapping pour les icônes
    const skillIcons = {
        'frontend': Code,
        'backend': Lightbulb,
        'tools': Globe,
        'ML': BrainCog,
        'devops':Container,
        'python':FolderCode,
    };
    
    // Rechargement de la configuration au montage du composant
    onMount(async () => {
        await loadConfig();
    
        const handleScroll = () => {
            const sections = document.querySelectorAll('section');
            const scrollPosition = window.scrollY;
    
            sections.forEach(section => {
                const sectionTop = section.offsetTop - 100;
                const sectionHeight = section.offsetHeight;
                const sectionId = section.getAttribute('id');
    
                if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                    activeSection = sectionId;
                }
            });
        };
    
        window.addEventListener('scroll', handleScroll);
        return () => window.removeEventListener('scroll', handleScroll);
    });
    
    // Fonction pour fermer le menu mobile après avoir cliqué sur un lien
    const closeMenu = () => {
        isMobileMenuOpen = false;
    };
</script>

<div class="page-wrapper">
    <div class="dot-pattern"></div>

    <!-- Header -->
    <header class="fixed top-0 left-0 right-0 backdrop-blur-md bg-white/90 dark:bg-slate-900/90 z-50 py-4 shadow-sm border-b border-slate-200 dark:border-slate-800">
        <div class="container max-w-5xl mx-auto px-6 flex justify-between items-center">
            <a href="#home" class="text-xl font-bold tracking-tight text-slate-800 dark:text-white">{$config.personal.name}</a>

            <!-- Navigation desktop -->
            <nav class="hidden md:flex gap-8">
                <a href="#home" class={`hover:text-primary transition-colors ${activeSection === 'home' ? 'text-primary font-medium' : 'text-slate-700 dark:text-slate-300'}`}>Accueil</a>
                <a href="#about" class={`hover:text-primary transition-colors ${activeSection === 'about' ? 'text-primary font-medium' : 'text-slate-700 dark:text-slate-300'}`}>À propos</a>
                <a href="#skills" class={`hover:text-primary transition-colors ${activeSection === 'skills' ? 'text-primary font-medium' : 'text-slate-700 dark:text-slate-300'}`}>Compétences</a>
                <a href="#projects" class={`hover:text-primary transition-colors ${activeSection === 'projects' ? 'text-primary font-medium' : 'text-slate-700 dark:text-slate-300'}`}>Projets</a>
                <a href="#experience" class={`hover:text-primary transition-colors ${activeSection === 'experience' ? 'text-primary font-medium' : 'text-slate-700 dark:text-slate-300'}`}>Parcours</a>
                <a href="#contact" class={`hover:text-primary transition-colors ${activeSection === 'contact' ? 'text-primary font-medium' : 'text-slate-700 dark:text-slate-300'}`}>Contact</a>
            </nav>

            <!-- Menu mobile -->
            <button class="md:hidden text-slate-800 dark:text-white" on:click={() => isMobileMenuOpen = !isMobileMenuOpen}>
                {#if isMobileMenuOpen}
                    <X size={24} />
                {:else}
                    <Menu size={24} />
                {/if}
            </button>
        </div>

        <!-- Menu mobile déroulant -->
        {#if isMobileMenuOpen}
            <div class="md:hidden absolute top-full left-0 right-0 bg-white dark:bg-slate-900 shadow-lg border-b border-slate-200 dark:border-slate-800">
                <nav class="container max-w-5xl mx-auto px-6 py-4 flex flex-col gap-4">
                    <a href="#home" on:click={closeMenu} class={`py-2 hover:text-primary ${activeSection === 'home' ? 'text-primary font-medium' : 'text-slate-700 dark:text-slate-300'}`}>Accueil</a>
                    <a href="#about" on:click={closeMenu} class={`py-2 hover:text-primary ${activeSection === 'about' ? 'text-primary font-medium' : 'text-slate-700 dark:text-slate-300'}`}>À propos</a>
                    <a href="#skills" on:click={closeMenu} class={`py-2 hover:text-primary ${activeSection === 'skills' ? 'text-primary font-medium' : 'text-slate-700 dark:text-slate-300'}`}>Compétences</a>
                    <a href="#projects" on:click={closeMenu} class={`py-2 hover:text-primary ${activeSection === 'projects' ? 'text-primary font-medium' : 'text-slate-700 dark:text-slate-300'}`}>Projets</a>
                    <a href="#experience" on:click={closeMenu} class={`py-2 hover:text-primary ${activeSection === 'experience' ? 'text-primary font-medium' : 'text-slate-700 dark:text-slate-300'}`}>Parcours</a>
                    <a href="#contact" on:click={closeMenu} class={`py-2 hover:text-primary ${activeSection === 'contact' ? 'text-primary font-medium' : 'text-slate-700 dark:text-slate-300'}`}>Contact</a>
                </nav>
            </div>
        {/if}
    </header>

    <main class="min-h-screen flex flex-col relative z-10" style="padding-top: 3rem">
        <!-- Hero Section -->
        <section id="home" class="min-h-[90vh] flex items-center justify-center py-10">
            <div class="content-container bg-white dark:bg-slate-900 rounded-2xl shadow-md">
                <div class="container max-w-5xl px-8 py-16 flex flex-col md:flex-row items-center gap-12">
                    <div class="md:w-1/2 flex flex-col gap-6">
                        <div class="space-y-2">
                            <h1 class="text-5xl font-bold text-slate-800 dark:text-white">{$config.personal.name}</h1>
                            <h2 class="uppercase text-4xl font-bold text-primary-light">{$config.personal.title}</h2>
                        </div>

                        <p class="text-lg text-slate-600 dark:text-slate-400 max-w-lg">
                            {$config.personal.description}
                        </p>

                        <div class="flex gap-4 pt-2">
                            <Button.Root class="bg-primary hover:bg-primary-dark text-white">
                                <a href="#contact" class="flex items-center gap-2">
                                    <Mail size={18} />
                                    Me contacter
                                </a>
                            </Button.Root>

                            <Button.Root variant="outline" class="border-primary text-primary hover:bg-primary/10">
                                <a href={$config.personal.cv_url} download class="flex items-center gap-2">
                                    <Download size={18} />
                                    Télécharger CV
                                </a>
                            </Button.Root>
                        </div>

                        <div class="flex gap-4 pt-4">

                            <a href={$config.social.github} target="_blank" rel="noopener noreferrer"
                               class="text-slate-600 dark:text-slate-400 hover:text-primary transition-colors">
                                <Github size={22} />
                            </a>
                                                        <a href={$config.social.malt} target="_blank" rel="noopener noreferrer"
                               class="text-slate-600 dark:text-slate-400 hover:text-primary transition-colors">
                                <LoaderPinwheel size={22} />
                            </a>
                            <a href={$config.social.linkedin} target="_blank" rel="noopener noreferrer"
                               class="text-slate-600 dark:text-slate-400 hover:text-primary transition-colors">
                                <Linkedin size={22} />
                            </a>
                        </div>
                    </div>

                    <div class="md:w-1/2 flex justify-center">
                        <Avatar.Root class="w-64 h-64 lg:w-80 lg:h-80 rounded-full border-4 border-primary/20">
                            <Avatar.Image src={$config.personal.avatar_url} alt={$config.personal.name} />
                            <Avatar.Fallback>
                                {$config.personal.name.split(' ').map(part => part[0]).join('')}
                            </Avatar.Fallback>
                        </Avatar.Root>
                    </div>
                </div>
            </div>
        </section>

        <!-- About Me Section -->
        <section id="about" class="py-10">
            <div class="content-container bg-white dark:bg-slate-900 rounded-2xl shadow-md">
                <div class="container max-w-5xl px-8 py-16 mx-auto">
                    <div class="max-w-2xl mx-auto text-center mb-16">
                        <h2 class="text-3xl font-bold mb-4 text-slate-800 dark:text-white">À propos de moi</h2>
                        <div class="h-1 w-20 bg-primary mx-auto mb-6"></div>
                    </div>

                    <div class="grid md:grid-cols-2 gap-10 items-center">
                        <div>
                            <Card.Root class="overflow-hidden border-slate-200 dark:border-slate-800">
                                <div class="relative aspect-[10/9]">
                                    <img src="https://images.unsplash.com/photo-1573497620053-ea5300f94f21?q=80&w=1740&auto=format&fit=crop"
                                         alt="Workplace"
                                         class="object-cover w-full h-full" />
                                </div>
                            </Card.Root>
                        </div>

                        <div class="space-y-6">
                            <h3 class="text-2xl font-semibold text-slate-800 dark:text-white">Développeur passionné & créatif</h3>

                            <p class="text-slate-600 dark:text-slate-400 whitespace-pre-line">
                                {$config.personal.about_description}
                            </p>

                            <div class="grid grid-cols-2 gap-4 pt-4">
                                <div>
                                    <h4 class="font-medium text-slate-800 dark:text-white">Nom:</h4>
                                    <p class="text-slate-600 dark:text-slate-400">{$config.personal.name}</p>
                                </div>
                                <div>
                                    <h4 class="font-medium text-slate-800 dark:text-white">Email:</h4>
                                    <p class="text-slate-600 dark:text-slate-400">{$config.personal.email}</p>
                                </div>
                                <div>
                                    <h4 class="font-medium text-slate-800 dark:text-white">Disponibilité:</h4>
                                    <p class="text-slate-600 dark:text-slate-400">{$config.personal.availability}</p>
                                </div>
                                <div>
                                    <h4 class="font-medium text-slate-800 dark:text-white">Localisation:</h4>
                                    <p class="text-slate-600 dark:text-slate-400">{$config.personal.location}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Skills Section -->
        <section id="skills" class="py-10">
            <div class="content-container bg-white dark:bg-slate-900 rounded-2xl shadow-md">
                <div class="container max-w-5xl px-8 py-16 mx-auto">
                    <div class="max-w-2xl mx-auto text-center mb-16">
                        <h2 class="text-3xl font-bold mb-4 text-slate-800 dark:text-white">Mes Compétences</h2>
                        <div class="h-1 w-20 bg-primary mx-auto mb-6"></div>
                    </div>

                    <div class="grid md:grid-cols-3 gap-8">
                        {#each Object.entries($config.skills) as [type, items]}
                            <Card.Root class="border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-800 transition-transform hover:scale-105">
                                <Card.Header>
                                    <div class="flex items-center gap-3">
                                        <div class="p-3 rounded-lg bg-primary-light/20 text-primary">
                                            <svelte:component this={skillIcons[type]} size={24} />
                                        </div>
                                        <Card.Title class="text-slate-800 dark:text-white">
                                            {type.charAt(0).toUpperCase() + type.slice(1)}
                                        </Card.Title>
                                    </div>
                                </Card.Header>
                                <Card.Content>
                                    <ul class="space-y-2">
                                        {#each items as item}
                                            <li class="flex items-center gap-2 text-slate-600 dark:text-slate-400">
                                                <div class="h-2 w-2 rounded-full bg-primary"></div>
                                                {item}
                                            </li>
                                        {/each}
                                    </ul>
                                </Card.Content>
                            </Card.Root>
                        {/each}
                    </div>
                </div>
            </div>
        </section>

        <!-- Projects Section -->
        <section id="projects" class="py-10">
            <div class="content-container bg-white dark:bg-slate-900 rounded-2xl shadow-md">
                <div class="container max-w-5xl px-8 py-16 mx-auto">
                    <div class="max-w-2xl mx-auto text-center mb-16">
                        <h2 class="text-3xl font-bold mb-4 text-slate-800 dark:text-white">Mes Projets</h2>
                        <div class="h-1 w-20 bg-primary mx-auto mb-6"></div>
                    </div>

                    <Projects projects={$config.projects.map(project => ({
                        title: project.title,
                        image: project.image,
                        description: project.description,
                        githubUrl: project.github_url,
                        liveUrl: project.live_url,
                        technologies: project.technologies,
                    }))} />
                </div>
            </div>
        </section>

        <!-- Experience Section -->
        <section id="experience" class="py-10">
            <div class="content-container bg-gray-50 dark:bg-slate-900 rounded-2xl shadow-md">
                <div class="container max-w-5xl px-8 py-16 mx-auto">
                    <div class="max-w-2xl mx-auto text-center mb-16">
                        <h2 class="text-3xl font-bold mb-4 text-slate-800 dark:text-white">Parcours Professionnel</h2>
                        <div class="h-1 w-20 bg-primary mx-auto mb-6"></div>
                    </div>

                    <Timeline
                        items={$config.experience.map(exp => ({
                            title: exp.title,
                            subtitle: exp.subtitle,
                            date: exp.date,
                            location: exp.location,
                            description: exp.description,
                            icon: exp.type === 'work' ? Briefcase : GraduationCap
                        }))}
                    />
                </div>
            </div>
        </section>

        <!-- Contact Section -->
        <section id="contact" class="py-10">
            <div class="content-container bg-white dark:bg-slate-900 rounded-2xl shadow-md">
                <div class="container max-w-5xl px-8 py-16 mx-auto">
                    <div class="max-w-2xl mx-auto text-center mb-16">
                        <h2 class="text-3xl font-bold mb-4 text-slate-800 dark:text-white">Me Contacter</h2>
                        <div class="h-1 w-20 bg-primary mx-auto mb-6"></div>
                    </div>

                    <div class="grid md:grid-cols-2 gap-12">
                        <Card.Root class="border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-800">
                            <Card.Header>
                                <Card.Title class="text-slate-800 dark:text-white">Envoyez-moi un message</Card.Title>
                                <Card.Description class="text-slate-600 dark:text-slate-400">Complétez le formulaire ci-dessous pour me contacter.</Card.Description>
                            </Card.Header>
                            <Card.Content>
                                <form class="space-y-6">
                                    <div class="grid md:grid-cols-2 gap-4">
                                        <div class="space-y-2">
                                            <label for="name" class="text-sm font-medium text-slate-800 dark:text-white">Nom</label>
                                            <input type="text" id="name" placeholder="Votre nom"
                                                   class="w-full p-3 border border-slate-200 dark:border-slate-700 rounded-md bg-white dark:bg-slate-800 focus:border-primary focus:ring-1 focus:ring-primary" />
                                        </div>
                                        <div class="space-y-2">
                                            <label for="email" class="text-sm font-medium text-slate-800 dark:text-white">Email</label>
                                            <input type="email" id="email" placeholder="votre@email.com"
                                                   class="w-full p-3 border border-slate-200 dark:border-slate-700 rounded-md bg-white dark:bg-slate-800 focus:border-primary focus:ring-1 focus:ring-primary" />
                                        </div>
                                    </div>

                                    <div class="space-y-2">
                                        <label for="subject" class="text-sm font-medium text-slate-800 dark:text-white">Sujet</label>
                                        <input type="text" id="subject" placeholder="Sujet du message"
                                               class="w-full p-3 border border-slate-200 dark:border-slate-700 rounded-md bg-white dark:bg-slate-800 focus:border-primary focus:ring-1 focus:ring-primary" />
                                    </div>

                                    <div class="space-y-2">
                                        <label for="message" class="text-sm font-medium text-slate-800 dark:text-white">Message</label>
                                        <textarea id="message" placeholder="Votre message..." rows="5"
                                                  class="w-full p-3 border border-slate-200 dark:border-slate-700 rounded-md bg-white dark:bg-slate-800 resize-none focus:border-primary focus:ring-1 focus:ring-primary"></textarea>
                                    </div>

                                    <Button.Root disabled type="submit" class="w-full bg-primary hover:bg-primary-dark text-white">Envoyer le message</Button.Root>
                                </form>
                            </Card.Content>
                        </Card.Root>

                        <div class="space-y-8">
                            <div>
                                <h3 class="text-2xl font-semibold mb-6 text-slate-800 dark:text-white">Informations de contact</h3>
                                <p class="text-slate-600 dark:text-slate-400 mb-8">
                                    N'hésitez pas à me contacter pour discuter de vos projets ou simplement échanger sur les technologies web.
                                </p>

                                <div class="space-y-4">
                                    <div class="flex items-center gap-4">
                                        <div class="p-3 bg-primary-light/20 dark:bg-primary/20 rounded-lg text-primary">
                                            <Mail size={20} />
                                        </div>
                                        <div>
                                            <p class="font-medium text-slate-800 dark:text-white">Email</p>
                                            <p class="text-slate-600 dark:text-slate-400">{$config.personal.email}</p>
                                        </div>
                                    </div>

                                    <div class="flex items-center gap-4">
                                        <div class="p-3 bg-primary-light/20 dark:bg-primary/20 rounded-lg text-primary">
                                            <Globe size={20} />
                                        </div>
                                        <div>
                                            <p class="font-medium text-slate-800 dark:text-white">Localisation</p>
                                            <p class="text-slate-600 dark:text-slate-400">{$config.personal.location}</p>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div>
                                <h3 class="text-xl font-semibold mb-4 text-slate-800 dark:text-white">Retrouvez-moi sur les réseaux</h3>
                                <div class="flex gap-4">
                                    <a href={$config.social.github} target="_blank" rel="noopener noreferrer"
                                       class="p-3 bg-primary-light/20 dark:bg-primary/20 rounded-lg text-primary hover:bg-primary/20 transition-colors">
                                        <Github size={20} />
                                    </a>
                                    <a href={$config.social.linkedin} target="_blank" rel="noopener noreferrer"
                                       class="p-3 bg-primary-light/20 dark:bg-primary/20 rounded-lg text-primary hover:bg-primary/20 transition-colors">
                                        <Linkedin size={20} />
                                    </a>
                                    <a href={$config.social.malt} target="_blank" rel="noopener noreferrer"
                                       class="p-3 bg-primary-light/20 dark:bg-primary/20 rounded-lg text-primary hover:bg-primary/20 transition-colors">
                                        <LoaderPinwheel size={20} />
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

    </main>

    <!-- Footer -->
    <footer class="bg-white py-8 dark:bg-slate-900 border-t border-slate-200 dark:border-slate-800 mt-12">
        <div class="container max-w-5xl px-6 mx-auto">
            <div class="flex flex-col md:flex-row justify-between items-center gap-4">
                <div>
                    <p class="font-medium text-slate-800 dark:text-white">{$config.personal.name}</p>
                    <p class="text-slate-600 dark:text-slate-400 text-sm">{$config.personal.title}</p>
                </div>

                <nav class="flex gap-6">
                    <a href="#home" class="text-sm text-slate-600 dark:text-slate-400 hover:text-primary transition-colors">Accueil</a>
                    <a href="#about" class="text-sm text-slate-600 dark:text-slate-400 hover:text-primary transition-colors">À propos</a>
                    <a href="#skills" class="text-sm text-slate-600 dark:text-slate-400 hover:text-primary transition-colors">Compétences</a>
                    <a href="#projects" class="text-sm text-slate-600 dark:text-slate-400 hover:text-primary transition-colors">Projets</a>
                    <a href="#experience" class="text-sm text-slate-600 dark:text-slate-400 hover:text-primary transition-colors">Parcours</a>
                    <a href="#contact" class="text-sm text-slate-600 dark:text-slate-400 hover:text-primary transition-colors">Contact</a>
                </nav>

                <div class="flex gap-4">
                    <a href={$config.social.github} target="_blank" rel="noopener noreferrer"
                       class="text-slate-600 dark:text-slate-400 hover:text-primary transition-colors">
                        <Github size={18} />
                    </a>
                    <a href={$config.social.linkedin} target="_blank" rel="noopener noreferrer"
                       class="text-slate-600 dark:text-slate-400 hover:text-primary transition-colors">
                        <Linkedin size={18} />
                    </a>
                    <a href={$config.social.malt} target="_blank" rel="noopener noreferrer"
                       class="text-slate-600 dark:text-slate-400 hover:text-primary transition-colors">
                        <LoaderPinwheel size={18} />
                    </a>
                </div>
            </div>

            <div class="mt-6 text-center text-sm text-slate-600 dark:text-slate-400">
                <p>© {new Date().getFullYear()} {$config.personal.name}. Tous droits réservés.</p>
            </div>
        </div>
    </footer>
</div>


<style>
    /* Conteneur principal avec positionnement relatif */
    .page-wrapper {
        position: relative;
        min-height: 100vh;
        /* Gradiant background color */
        background-image:
                linear-gradient(to right, rgba(34, 0, 155, 0.05), rgba(230, 0, 255, 0.05));
    }

    /* Conteneurs de contenu */
    .content-container {
        margin: 0 auto;
        max-width: 1100px;
        width: 90%;
    }

    /* Motif de points */
    .dot-pattern {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image:
            radial-gradient(circle, rgba(114, 60, 216, 0.4) 1.25px, transparent 1px); /* Points violets plus clairs */
        background-size: 20px 20px, 25px 25px;
        background-position: 0 0, 10px 10px;
        z-index: 1;
        pointer-events: none;
    }

    /* Ajout d'une légère transition aux éléments interactifs */
    a, button {
        transition: all 0.2s ease;
    }

    /* Animation subtile pour les cartes au survol */
    :global(.card) {
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    :global(.card:hover) {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px -5px rgba(114, 60, 216, 0.2);
    }

    /* Définition des couleurs personnalisées */
    :global(:root) {
        --primary: #723CD8; /* Violet - couleur principale */
        --primary-dark: #5F2EC3; /* Version plus foncée du violet */
        --primary-light: #8552E8; /* Version plus claire du violet */
        --secondary: #F0F1F5; /* Gris très clair */
        --slate-700: #334155;
        --slate-800: #1e293b;
        --slate-900: #0f172a;
    }

    /* Classes de couleurs personnalisées */
    :global(.text-primary) { color: var(--primary); }
    :global(.text-primary-dark) { color: var(--primary-dark); }
    :global(.text-primary-light) { color: var(--primary-light); }

    :global(.bg-primary) { background-color: var(--primary); }
    :global(.bg-primary-dark) { background-color: var(--primary-dark); }
    :global(.bg-primary-light) { background-color: var(--primary-light); }
    :global(.bg-secondary) { background-color: var(--secondary); }

    :global(.border-primary) { border-color: var(--primary); }

    /* Ajuster l'espacement entre les sections */
    section {
        scroll-margin-top: 80px;
    }
</style>
