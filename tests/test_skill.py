"""Checks that the skill file and the plugin manifests agree, so a bad edit cannot ship: python3 -m unittest discover -s tests"""
import json
import os
import re
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(*p):
    with open(os.path.join(ROOT, *p), encoding="utf-8") as f:
        return f.read()


class SkillTests(unittest.TestCase):
    def test_skill_has_frontmatter_and_name(self):
        s = read("skills", "linkedin-roast", "SKILL.md")
        self.assertTrue(s.startswith("---\n"))
        head = s.split("---", 2)[1]
        self.assertRegex(head, r"(?m)^name: linkedin-roast$")
        self.assertRegex(head, r"(?m)^description: .{40,}")

    def test_skill_keeps_its_promises(self):
        s = read("skills", "linkedin-roast", "SKILL.md")
        for needle in ("220", "2,600", "1584", "[ADD YOUR NUMBER"):
            self.assertIn(needle, s)

    def test_plugin_manifests(self):
        plugin = json.loads(read(".claude-plugin", "plugin.json"))
        market = json.loads(read(".claude-plugin", "marketplace.json"))
        self.assertEqual(plugin["name"], "linkedin-roast-skill")
        self.assertEqual(market["plugins"][0]["name"], plugin["name"])
        self.assertEqual(plugin["license"], "MIT")

    def test_readme_install_paths_exist(self):
        r = read("README.md")
        self.assertIn("skills/linkedin-roast", r)
        self.assertTrue(os.path.exists(os.path.join(ROOT, "skills", "linkedin-roast", "SKILL.md")))
        self.assertIsNotNone(re.search(r"/plugin marketplace add alexyc9381/linkedin-roast-skill", r))


if __name__ == "__main__":
    unittest.main()
