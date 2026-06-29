.PHONY: validate-skill validate-skill-zh validate-skill-en validate-all-skills validate-current audit-all

validate-skill: validate-skill-zh

validate-skill-zh:
	python3 scripts/validate_lecture_note.py --skill-dir skill

validate-skill-en:
	python3 scripts/validate_lecture_note.py --language en --skill-dir skill-en

validate-all-skills: validate-skill-zh validate-skill-en

validate-current:
	python3 scripts/audit_examples.py --current-only

audit-all:
	python3 scripts/audit_examples.py --all
