#!/usr/bin/env python3
"""
Spell checker for technical documentation
Checks spelling in markdown and text files while handling technical content appropriately
"""

import os
import re
import subprocess
import sys
from pathlib import Path
from typing import List, Dict, Set, Tuple

class TechnicalSpellChecker:
    def __init__(self, repo_path: str = "."):
        self.repo_path = Path(repo_path)
        self.report_file = self.repo_path / "SPELLING_REPORT.md"
        
        # Technical terms and proper nouns to ignore
        self.technical_words = {
            # Programming languages and technologies
            'aspell', 'cspell', 'nodejs', 'npm', 'javascript', 'java', 'python', 'groovy',
            'junit', 'jenkins', 'gradle', 'maven', 'docker', 'kubernetes', 'kafka',
            'openssl', 'rsa', 'crypto', 'cryptographic', 'ssl', 'tls',
            'markdown', 'html', 'css', 'json', 'xml', 'yaml', 'yml',
            'github', 'gitlab', 'bitbucket', 'stackoverflow', 'baeldung',
            
            # Operating systems and tools
            'linux', 'ubuntu', 'windows', 'macos', 'powershell', 'bash', 'cmd',
            'eclipse', 'intellij', 'vscode', 'notepad', 'vim', 'emacs',
            'git', 'svn', 'mercurial', 'cvs', 'linuxcnc', 'pronterface', 'gcode',
            
            # Technical abbreviations
            'api', 'rest', 'http', 'https', 'tcp', 'udp', 'ip', 'dns', 'url', 'uri',
            'cpu', 'gpu', 'ram', 'ssd', 'hdd', 'usb', 'pci', 'ide', 'sata',
            'adtf', 'uds', 'can', 'someip', 'automotive', 'obd', 'iso',
            
            # File extensions and formats
            'md', 'txt', 'pdf', 'docx', 'xlsx', 'pptx', 'csv',
            'java', 'py', 'js', 'ts', 'cpp', 'hpp', 'h', 'c',
            'jar', 'war', 'ear', 'zip', 'tar', 'gz',
            
            # Common technical words
            'config', 'configs', 'param', 'params', 'args', 'argv',
            'stdin', 'stdout', 'stderr', 'filesystem', 'namespace',
            'regex', 'regexp', 'xpath', 'json', 'serialization',
            'deserialization', 'marshalling', 'unmarshalling',
            'errorlevel', 'errorlevels', 'classpath', 'localhost',
            'workflow', 'workflows', 'dockerfile', 'makefile',
            'testcase', 'testcases', 'username', 'hostname', 'filepath',
            'filename', 'filenames', 'codebase', 'codebases',
            'plugin', 'plugins', 'addon', 'addons', 'app', 'apps',
            'repo', 'repos', 'cli', 'gui', 'tui', 'ui', 'ux',
            'changelog', 'readme', 'checkstyle', 'sonarlint', 'spotbugs', 'pmd',
            'appender', 'appenders', 'loggers', 'slf', 'logback',
            'boolean', 'varchar', 'nullable', 'nullable', 'autowired',
            'autowiring', 'singleton', 'singletons', 'junit', 'mockito',
            'powermock', 'hamcrest', 'assertj', 'testng',
            
            # Hardware and automotive specific
            'bluetooth', 'wifi', 'ethernet', 'bluetooth', 'endstop', 'endstops',
            'ctrl', 'alt', 'esc', 'del', 'backspace', 'pageup', 'pagedown',
            'checkbox', 'dropdown', 'textarea', 'tooltip', 'tooltips',
            
            # Specific to this repo  
            'senthil', 'geogebra', 'diya', 'yocto', 'bitbake',
            'cmake', 'uboot', 'grub', 'systemd', 'systemctl',
            'grep', 'sed', 'awk', 'wget', 'curl', 'rsync', 'scp', 'ssh',
            'vim', 'nano', 'emacs', 'gedit', 'notepad',
        }
        
        # Common misspellings to flag (even if they might be technical terms)
        self.likely_misspellings = {
            'usefule': 'useful',
            'comparision': 'comparison', 
            'keyvboard': 'keyboard',
            'bluethooth': 'bluetooth',
            'implmentation': 'implementation',
            'appenderstream': 'appender stream',
            'recieve': 'receive',
            'seperate': 'separate',
            'occured': 'occurred',
            'occurance': 'occurrence',
            'definately': 'definitely',
            'neccessary': 'necessary',
            'accomodate': 'accommodate',
            'begining': 'beginning',
            'wierd': 'weird',
            'thier': 'their',
            'publically': 'publicly',
        }
        
        # URL and email patterns to ignore
        self.url_pattern = re.compile(r'https?://[^\s\]]+')
        self.email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        self.code_block_pattern = re.compile(r'```[\s\S]*?```', re.MULTILINE)
        self.inline_code_pattern = re.compile(r'`[^`]+`')
        self.markdown_link_pattern = re.compile(r'\[([^\]]+)\]\([^\)]+\)')
        self.file_path_pattern = re.compile(r'[/\\][\w\-/.\\]+')
        
    def is_valid_file(self, file_path: Path) -> bool:
        """Check if file should be spell checked"""
        if file_path.suffix.lower() not in ['.md', '.txt']:
            return False
        if file_path.name.startswith('.'):
            return False
        if file_path.name == 'SPELLING_REPORT.md':  # Don't check our own report
            return False
        if 'node_modules' in str(file_path) or '.git' in str(file_path):
            return False
        return True
    
    def clean_text_for_spell_check(self, content: str) -> str:
        """Remove URLs, code blocks, and other technical content that shouldn't be spell checked"""
        # Remove code blocks
        content = self.code_block_pattern.sub('', content)
        # Remove inline code
        content = self.inline_code_pattern.sub('', content)
        # Remove URLs
        content = self.url_pattern.sub('', content)
        # Remove email addresses
        content = self.email_pattern.sub('', content)
        # Remove markdown links but keep the text
        content = self.markdown_link_pattern.sub(r'\1', content)
        # Remove file paths
        content = self.file_path_pattern.sub('', content)
        # Remove markdown formatting
        content = re.sub(r'[*_#>-]', ' ', content)
        # Remove numbers and version strings
        content = re.sub(r'\b\d+[\d.]*\b', '', content)
        return content
    
    def check_file_spelling(self, file_path: Path) -> List[Tuple[int, str, List[str]]]:
        """Check spelling in a single file and return errors with line numbers"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return []
        
        errors = []
        for line_num, line in enumerate(lines, 1):
            cleaned_line = self.clean_text_for_spell_check(line)
            if not cleaned_line.strip():
                continue
                
            # Use aspell to check the line
            try:
                result = subprocess.run(
                    ['aspell', 'list'],
                    input=cleaned_line,
                    capture_output=True,
                    text=True,
                    check=False
                )
                
                if result.returncode == 0 and result.stdout.strip():
                    misspelled_words = []
                    priority_errors = []  # High priority misspellings
                    
                    for word in result.stdout.strip().split('\n'):
                        word = word.strip().lower()
                        if word and len(word) > 1:
                            # Check if it's a known misspelling
                            if word in self.likely_misspellings:
                                priority_errors.append(f"{word} → {self.likely_misspellings[word]}")
                            # Check if it's not in technical words and not a common pattern
                            elif (word not in self.technical_words and 
                                  not re.match(r'^[a-z]+\d+$', word) and  # like log4j2, java8
                                  not re.match(r'^\w{1,3}$', word)):      # very short words
                                misspelled_words.append(word)
                    
                    # Prioritize likely misspellings
                    all_errors = priority_errors + misspelled_words
                    if all_errors:
                        errors.append((line_num, line.strip(), all_errors))
                        
            except Exception as e:
                print(f"Error checking line {line_num} in {file_path}: {e}")
                continue
                
        return errors
    
    def generate_report(self) -> Dict[str, List]:
        """Generate comprehensive spelling report"""
        print("🔍 Scanning repository for spelling errors...")
        
        all_errors = {}
        total_files = 0
        files_with_errors = 0
        
        for file_path in self.repo_path.rglob('*'):
            if self.is_valid_file(file_path):
                total_files += 1
                print(f"Checking: {file_path.relative_to(self.repo_path)}")
                
                errors = self.check_file_spelling(file_path)
                if errors:
                    files_with_errors += 1
                    all_errors[str(file_path.relative_to(self.repo_path))] = errors
        
        print(f"\n✅ Completed spell check:")
        print(f"   📁 Files checked: {total_files}")
        print(f"   ⚠️  Files with errors: {files_with_errors}")
        print(f"   📝 Total errors: {sum(len(errors) for errors in all_errors.values())}")
        
        return all_errors
    
    def write_report(self, errors: Dict[str, List]):
        """Write spelling report to markdown file"""
        with open(self.report_file, 'w', encoding='utf-8') as f:
            f.write("# Spelling Error Report\n\n")
            f.write(f"Generated on: {subprocess.run(['date'], capture_output=True, text=True).stdout.strip()}\n\n")
            
            if not errors:
                f.write("✅ **No spelling errors found!**\n\n")
                f.write("All files passed the spell check.\n")
                return
            
            # Collect likely misspellings for summary
            likely_misspellings_found = {}
            for file_path, file_errors in errors.items():
                for line_num, line_content, misspelled in file_errors:
                    for word in misspelled:
                        if '→' in word:  # This is a priority error
                            if word not in likely_misspellings_found:
                                likely_misspellings_found[word] = []
                            likely_misspellings_found[word].append((file_path, line_num))
            
            f.write("## Summary\n\n")
            f.write(f"- **Files with errors:** {len(errors)}\n")
            f.write(f"- **Total errors:** {sum(len(file_errors) for file_errors in errors.values())}\n")
            f.write(f"- **Likely misspellings:** {len(likely_misspellings_found)}\n\n")
            
            if likely_misspellings_found:
                f.write("## 🚨 Priority: Likely Misspellings\n\n")
                f.write("These are high-confidence spelling errors that should be fixed:\n\n")
                
                for misspelling, locations in sorted(likely_misspellings_found.items()):
                    f.write(f"### `{misspelling}`\n\n")
                    f.write("Found in:\n")
                    for file_path, line_num in locations:
                        f.write(f"- `{file_path}` line {line_num}\n")
                    f.write("\n")
            
            f.write("## Errors by File\n\n")
            
            for file_path, file_errors in sorted(errors.items()):
                f.write(f"### 📄 `{file_path}`\n\n")
                f.write(f"**{len(file_errors)} error(s) found:**\n\n")
                
                for line_num, line_content, misspelled in file_errors:
                    f.write(f"**Line {line_num}:**\n")
                    f.write(f"```\n{line_content}\n```\n")
                    f.write(f"**Potential issues:** {', '.join(f'`{word}`' for word in misspelled)}\n\n")
                
            f.write("## How to Fix\n\n")
            f.write("1. **Start with Priority items** - These are likely genuine spelling errors\n")
            f.write("2. Review each error in context\n")
            f.write("3. Fix genuine spelling mistakes\n")
            f.write("4. Add legitimate technical terms to the spell checker's dictionary\n")
            f.write("5. Re-run the spell checker to verify fixes\n\n")
            
            f.write("## Running the Spell Checker\n\n")
            f.write("```bash\n")
            f.write("python3 spell_check.py\n")
            f.write("```\n\n")
            
            f.write("---\n")
            f.write("*Report generated by Technical Spell Checker*\n")

def main():
    """Main function to run spell checker"""
    checker = TechnicalSpellChecker()
    errors = checker.generate_report()
    checker.write_report(errors)
    
    print(f"\n📋 Report written to: {checker.report_file}")
    
    if errors:
        print("❌ Spelling errors found. See report for details.")
        sys.exit(1)
    else:
        print("✅ No spelling errors found!")
        sys.exit(0)

if __name__ == "__main__":
    main()