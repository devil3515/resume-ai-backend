import os
import django
import asyncio
import traceback
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "resume_ai_backend.settings")
django.setup()

try:
    from interview.views import interview_system

    async def main():
        print("Starting interview...", flush=True)
        result = await interview_system.start_interview(
            job_title='Software Engineer',
            company='TechCorp',
            job_description='Test description',
            interview_type='mixed',
            experience_level='mid',
            duration=30,
            voice_analysis=False
        )
        print("Success!", result, flush=True)

    asyncio.run(main())
except Exception as e:
    print("Caught Exception:", flush=True)
    traceback.print_exc()
    sys.exit(1)
