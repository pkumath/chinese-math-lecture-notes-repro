.PHONY: validate-skill validate-current audit-all

validate-skill:
	python3 scripts/validate_lecture_note.py --skill-dir skill

validate-current:
	python3 scripts/audit_examples.py --current-only

audit-all:
	python3 scripts/audit_examples.py --all
