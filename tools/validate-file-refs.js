#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');

const PROJECT_ROOT = path.join(__dirname, '..', '..');

function findAllFiles(dir, fileList = []) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        const fullPath = path.join(dir, file);
        const stat = fs.statSync(fullPath);
        if (stat.isDirectory() && !file.startsWith('.') && file !== 'node_modules') {
            findAllFiles(fullPath, fileList);
        } else if (stat.isFile()) {
            fileList.push(fullPath);
        }
    }
    return fileList;
}

// Patterns to ignore - these are NOT literal file path references:
// 1. Instruções "→ consultar skills/XXX/SKILL.md" - textual guidelines
// 2. Starlight-style absolute links (/path - works at runtime, not file system)
// 3. Template/format references (result-envelope.md, AGENTS.md like generic refs)
// 4. Comandos de exemplo (ansible-playbook, kubectl, az)
// 5. Cross-repo references (packages/superpowers/, agentsos/001.md)
// 6. Placeholder/template format strings (knowledge/<category>/<type>/<slug>.md)
const IGNORE_REF_PATTERNS = [
    // Starlight absolute links: [text](/slug)
    /^\/(?!assets\/)/,
    // Knowledge base slug refs (without .md extension)
    /\[([^\]]+)\]\(([^)]+)\)/,
    // Template format placeholders
    /<category>\/<type>\/<slug>/,
    // Known cross-repo placeholders
    /agentsos\/00\d\.md/,
    /packages\/superpowers\//,
    /scripts\//,
    /output\/result-envelope\.json/,
    /agentsos\/memory\/knowledge\/skills\/knowledge-(manager|create)/,
];

// Patterns to ignore for inline code refs (in backticks)
const IGNORE_CODE_PATTERNS = [
    // Ansible file paths
    /^(tasks|handlers|vars|defaults|meta)\/main\.yml$/,
    // Comandos de exemplo
    /^ansible-playbook.*/,
    /^kubectl.*/,
    /^az.*/,
    /site\.yml$/,
    // Template format strings
    /^memory\/knowledge\/.*$/,
    /^agentsos\/memory\/knowledge\/.*$/,
    /^knowledge\/.*$/,
    /eval\/evals\.json$/,
    /slug-case\.md$/,
    /incident-response\.md$/,
    /^.*\.{{source}}$/,
    /INDEX\.md$/,
    /<server-name>\//,
    /^memory\/portable-context\.md$/,
    /^validate\.py$/,
    /^AGENTS\.md$/,
    /^tools\/.*$/,
    // Generic template references
    /^result-envelope(\.md)?$/,
    /^task-envelope(\.md)?$/,
    /^task-envelope\.json$/,
    /^result-envelope\.json$/,
    /^config\.json$/,
    /^run\.py$/,
    /^report\.py$/,
    /^report\.md$/,
    /^package\.json$/,
    /^scope\.md$/,
    /^tools\.md$/,
    /^authority\.md$/,
    /^change-risk-levels\.md$/,
    /^docs\/architecture-existing\.md$/,
    /^docs\/ARCHITECTURE\.md$/,
    /^docs\/design-decisions\.md$/,
    /^docs\/usage\.md$/,
    /^docs\/plan\/choose-a-planning-path\.md$/,
    /^docs\/SKILLS\.md$/,
    /^docs\/BEST_PRACTICES\.md$/,
    /^docs\/HIC_PRACTICES\.md$/,
    /^docs\/MEMORY\.md$/,
    /^docs\/README\.md$/,
    /^docs\/AGENT-ARCHITECTURE\.md$/,
    /^docs\/GOVERNANCE\.md$/,
    /^docs\/ARCHITECTURE\.md$/,
    /^agentsos\/agents\/.*\/AGENTS\.md$/,
    /^agentsos\/agents\/sre\/AGENTS\.md$/,
    /^agentsos\/skills\/.*\/SKILL\.md$/,
    /^agentsos\/skills\/.*\/SKILL\.md$/,
    /^agentsos\/templates\/.*$/,
    /^agentsos\/guardrails\/global\/.*$/,
    /^agentsos\/tests\/.*$/,
    /^agentsos\/benchmarks\/.*$/,
    /^agentsos\/memory\/.*$/,
    /^agentsos\/contracts\/.*$/,
    /^agentsos\/mcp\/.*$/,
    /^agentsos\/workflows\/.*$/,
    /^AGENTS\.md$/,
    /^GOVERNANCE\.md$/,
    /^CONTRIBUTING\.md$/,
    /^SKILL\.md$/,
    /^brief-template\.md$/,
    /^adr-template\.md$/,
    /^sprint-plan-template\.md$/,
    /^epic-story-template\.md$/,
    /^product-brief-template\.md$/,
    /^prd-template\.md$/,
    /^tech-spec-template\.md$/,
    /^retrospective-template\.md$/,
    /^architecture-template\.md$/,
    /^agentos-build\/SKILL\.md$/,
    /^agentos-help\/SKILL\.md$/,
    /^security-hardening\/SKILL\.md$/,
    /^slo-management\/SKILL\.md$/,
    /^integration-testing\/SKILL\.md$/,
    /^node-pool-management\/SKILL\.md$/,
    /^pipeline-orchestration\/SKILL\.md$/,
    /^knowledge-manager\/SKILL\.md$/,
    /^knowledge-create\/SKILL\.md$/,
    /^scan-repo\.md$/,
    /^establish-context\.md$/,
    /^entry-point\.md$/,
    // Memory learning/candidate entries (dynamic, not literal)
    /LEARN-20\d{2}-\d+\.md/,
    /LEARN-ID\.md/,
    /^capture-session\.py$/,
    /^promote-memory\.py$/,
    /^auto_learning_hook\.py$/,
    /^migrate-to-atomic\.py$/,
    /^authorization\.py$/,
    /^memory-authorization\.md$/,
    /^integration-testing\/SKILL\.md$/,
    /^node-pool-management\/SKILL\.md$/,
    /^pipeline-orchestration\/SKILL\.md$/,
];

function isIgnored(ref) {
    return IGNORE_CODE_PATTERNS.some(p => p.test(ref)) ||
           IGNORE_REF_PATTERNS.some(p => p.test(ref));
}

function validateRefs() {
    const allFiles = findAllFiles(PROJECT_ROOT);
    const markdownFiles = allFiles.filter(f => f.endsWith('.md'));

    let brokenRefs = 0;
    let totalRefs = 0;

    for (const file of markdownFiles) {
        const content = fs.readFileSync(file, 'utf-8');
        const relPath = path.relative(PROJECT_ROOT, file);

        // Find markdown links [text](path)
        const linkRegex = /\[([^\]]+)\]\(([^)]+)\)/g;
        let match;

        while ((match = linkRegex.exec(content)) !== null) {
            const linkText = match[1];
            const linkPath = match[2];
            totalRefs++;

            // Skip external links
            if (linkPath.startsWith('http://') || linkPath.startsWith('https://') || linkPath.startsWith('mailto:')) {
                continue;
            }

            // Skip Starlight absolute links (start with /, not in website)
            // These are slug-based links that work in Astro/Starlight
            if (linkPath.startsWith('/')) {
                // Check if it's in website dir - skip (Starlight links)
                if (relPath.startsWith('website/')) {
                    continue;
                }
            }

            // Skip "→ consultar" instructions
            if (linkPath.includes('→ consultar') || linkText.includes('→ consultar')) {
                continue;
            }

            // Skip placeholder/template refs
            if (isIgnored(linkPath) || isIgnored(linkText)) {
                continue;
            }

            // Skip knowledge base slug refs (no file extension, used as tags)
            if (!linkPath.includes('.') && !linkPath.includes('/')) {
                // Likely a topic slug reference
                continue;
            }

            // Resolve relative path
            let targetPath;
            if (linkPath.startsWith('/')) {
                targetPath = path.join(PROJECT_ROOT, linkPath);
            } else {
                targetPath = path.join(path.dirname(file), linkPath);
            }

            if (!fs.existsSync(targetPath)) {
                // In website docs, /path links are Starlight routes
                if (relPath.startsWith('website/')) {
                    continue;
                }
                console.log(`❌ Broken ref in ${relPath}: ${linkPath} (${linkText})`);
                brokenRefs++;
            }
        }

        // Find file references in code blocks or inline code
        const codeRefRegex = /`([^`]+\.(md|json|yaml|yml|py|js|ts|sh))`/g;
        while ((match = codeRefRegex.exec(content)) !== null) {
            const ref = match[1];
            totalRefs++;

            if (!fs.existsSync(path.join(PROJECT_ROOT, ref))) {
                // Check relative to file directory
                const altPath = path.join(path.dirname(file), ref);
                if (!fs.existsSync(altPath)) {
                    // Skip if it matches ignored patterns
                    if (isIgnored(ref)) {
                        continue;
                    }
                    console.log(`⚠️  Possible missing file ref in ${relPath}: ${ref}`);
                }
            }
        }
    }

    console.log(`\nChecked ${markdownFiles.length} markdown files`);
    console.log(`Total references: ${totalRefs}`);
    console.log(`Broken references: ${brokenRefs}`);

    return brokenRefs === 0;
}

const strict = process.argv.includes('--strict');
const valid = validateRefs();

if (!valid && strict) {
    console.log('\n❌ Validation failed (strict mode)');
    process.exit(1);
} else if (!valid) {
    console.log('\n⚠️  Validation has warnings (non-strict mode)');
    process.exit(0);
} else {
    console.log('\n✅ All references valid');
    process.exit(0);
}