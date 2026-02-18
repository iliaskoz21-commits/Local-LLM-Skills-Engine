import os

def test_skills_folder_exists():
    """Ελέγχει αν υπάρχει ο φάκελος με τα skills"""
    assert os.path.exists("skills") is True

def test_markdown_files_in_skills():
    """Ελέγχει αν υπάρχουν αρχεία .md μέσα στο skills"""
    skills = [f for f in os.listdir("skills") if f.endswith(".md")]
    assert len(skills) > 0

def test_env_example_exists():
    """Ελέγχει αν ξέχασες να φτιάξεις το .env.example για το GitHub"""
    assert os.path.exists(".env.example") is True