import unittest

from scripts.render_mintlify_releases import parse_releases, render


RELEASE = """
## 2026-07-17 21:45:13
### Changes
Based on:
- OpenAPI Doc
- Speakeasy CLI 1.790.2 (2.918.3) https://github.com/speakeasy-api/speakeasy
### Generated
- [python v1.0.0] .
### Releases
- [PyPI v1.0.0] https://pypi.org/project/textql-sdk/1.0.0 - .
"""


class RenderMintlifyReleasesTest(unittest.TestCase):
    def test_parses_speakeasy_release_format(self) -> None:
        release = parse_releases(RELEASE)[0]
        self.assertEqual(release.version, "1.0.0")
        self.assertEqual(
            release.pypi_url, "https://pypi.org/project/textql-sdk/1.0.0"
        )
        self.assertEqual(release.speakeasy_cli, "1.790.2")
        self.assertEqual(release.generator_version, "2.918.3")

    def test_accepts_standard_markdown_pypi_link(self) -> None:
        markdown = RELEASE.replace(
            "[PyPI v1.0.0] https://pypi.org/project/textql-sdk/1.0.0 - .",
            "[PyPI v1.0.0](https://pypi.org/project/textql-sdk/1.0.0)",
        )
        self.assertEqual(parse_releases(markdown)[0].version, "1.0.0")

    def test_renders_mintlify_updates(self) -> None:
        output = render(RELEASE)
        self.assertIn('title: "Python SDK release log"', output)
        self.assertIn(
            '<Update label="v1.0.0" description="July 17, 2026">', output
        )
        self.assertIn("pip install textql-sdk==1.0.0", output)
        self.assertIn("[Speakeasy CLI 1.790.2 (generator 2.918.3)]", output)

    def test_rejects_release_without_pypi_link(self) -> None:
        with self.assertRaisesRegex(ValueError, "no PyPI link"):
            parse_releases(RELEASE.replace("PyPI", "Package"))


if __name__ == "__main__":
    unittest.main()
