# core/management/commands/load_services.py
from django.core.management.base import BaseCommand
from core.models import Service

class Command(BaseCommand):
    help = 'Load predefined services into the database'

    def handle(self, *args, **kwargs):
        services = [
            {
                "title": "Networking Solutions",
                "description": "We provide comprehensive networking solutions, including installation, configuration, and maintenance for businesses of all sizes.",
                "icon": "bi bi-router",
            },
            {
                "title": "Hardware Sales",
                "description": "We sell high-quality hardware products, from routers to workstations, to ensure your business runs smoothly and efficiently.",
                "icon": "bi bi-laptop",
            },
            {
                "title": "IT Support",
                "description": "Our team offers 24/7 IT support, troubleshooting, and maintenance to keep your systems up and running.",
                "icon": "bi bi-headset",
            },
            {
                "title": "Cybersecurity Services",
                "description": "Protect your business with our advanced cybersecurity solutions, ensuring data safety and system integrity.",
                "icon": "bi bi-shield-lock",
            },
            {
                "title": "Cloud Integration",
                "description": "Leverage the power of the cloud with our integration services, tailored to enhance scalability and efficiency.",
                "icon": "bi bi-cloud-arrow-up",
            },
            {
                "title": "Custom Solutions",
                "description": "If you need a specific hardware or networking solution, we can provide custom-tailored services to meet your unique needs.",
                "icon": "bi bi-tools",
            },
        ]

        for service in services:
            obj, created = Service.objects.get_or_create(
                title=service["title"],
                defaults={
                    "description": service["description"],
                    "icon": service["icon"],
                },
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Service '{obj.title}' created."))
            else:
                self.stdout.write(self.style.WARNING(f"Service '{obj.title}' already exists."))
