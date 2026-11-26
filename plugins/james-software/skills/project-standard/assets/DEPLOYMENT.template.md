# Deployment

- Contract: domain-directory/v1; production root mirrors one hosting domain directory and MUST contain public_html/.
- Source branch: main; source and AI context never deployed directly.
- Public web root: public_html; other private directory names follow the actual app, not a fixed app/storage example.
- FTP home: own domain directory (actual host/domain Not confirmed).
- Git Manager Remote Root: /; FTP-only Local Path: .
- Release: tools/release.sh (preview); tools/release.sh --push (artifact publication only, no live deploy).
- Mapping and server files to preserve: .release-layout.json; configure real mappings before release.
- Auto-deploy/rebuild: remain OFF until destination, checkout, preservation, migration and rollback accepted; actual live state Not confirmed.
- Credentials: owner fills DA and paired GWM forms; a DA password rotation requires matching GWM update. No passwords in source/chat.
- Server paths, backup/restore and packaged application acceptance: Not confirmed.
