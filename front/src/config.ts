// src/lib/config.ts
import type {Writable} from 'svelte/store';
import {writable} from 'svelte/store';
import {BrainCog, Container, FolderCode} from "lucide-svelte";

export interface Config {
    personal: {
        name: string;
        title: string;
        email: string;
        location: string;
        availability: string;
        about_description: string;
        cv_url: string;
        avatar_url: string;
    };
    social: {
        github: string;
        linkedin: string;
        twitter: string;
    };
    skills: {
        frontend: string[];
        backend: string[];
        tools: string[];
        ML: string[];
        devops:string[];
        python:string[];
    };
    projects: {
        title: string;
        image: string;
        description: string;
        github_url: string;
        live_url?: string;
        technologies: string[];
    }[];
    experience: {
        title: string;
        subtitle: string;
        date: string;
        location: string;
        description?: string;
        type: 'work' | 'education';
    }[];
}

// Configuration par défaut (fallback)
const defaultConfig: Config = {
    personal: {
        name: 'John Doe',
        title: 'Développeur Full Stack',
        email: 'contact@johndoe.dev',
        location: 'Paris, France',
        availability: 'Freelance / CDI',
        about_description: 'Développeur full stack passionné...',
        cv_url: '/cv.pdf',
        avatar_url: 'https://github.com/shadcn.png',
    },
    social: {
        github: 'https://github.com/votre-user',
        linkedin: 'https://linkedin.com/in/votre-user',
        twitter: 'https://twitter.com/votre-user',
    },
    skills: {
        frontend: [],
        backend: [],
        tools: [],
        ML: [],
        devops: [],
        python: [],
    },
    projects: [],
    experience: [],
};

// Créer un store pour la configuration
export const config: Writable<Config> = writable(defaultConfig);

// Fonction pour charger la configuration depuis l'API
export async function loadConfig() {
    try {
        const response = await fetch('http://localhost:8000/api/v1/config');
        if (!response.ok) throw new Error('Erreur lors du chargement de la configuration');
        const data = await response.json();
        config.set(data as Config);
        return data;
    } catch (error) {
        console.error('Erreur lors du chargement de la configuration:', error);
        // En cas d'erreur, on garde la configuration par défaut
        return defaultConfig;
    }
}

// Charger automatiquement la configuration si on est côté navigateur
if (typeof window !== 'undefined') {
    loadConfig();
}
