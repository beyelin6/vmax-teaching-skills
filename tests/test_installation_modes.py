import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class InstallationModeDocs(unittest.TestCase):
    def read(self, name):
        return (ROOT / name).read_text(encoding='utf-8')

    def test_readme_declares_exclusive_codex_modes(self):
        text = self.read('README.md')
        self.assertIn('兩種互斥的安裝模式', text)
        self.assertIn('不要同時啟用兩種模式', text)

    def test_sync_docs_repeat_guard(self):
        agents = self.read('AGENTS.md')
        self.assertIn('同時使用', agents)
        self.assertIn('擇一', agents)
        docs = self.read('docs/codex-skill-sync.md')
        self.assertIn('不要再執行同步腳本', docs)
        self.assertIn('Plugin', docs)

    def test_sources_are_distinct(self):
        self.assertIn('.codex\\skills', self.read('scripts/sync_codex_skills.ps1'))
        self.assertIn('"skills": "./skills/"', self.read('.codex-plugin/plugin.json'))

if __name__ == '__main__':
    unittest.main()
