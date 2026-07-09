"""Build paper-ams.docx from paper-ams.md in AMS style (numbered [n] citations, all-author references)."""
import os
import re
from pathlib import Path
import pypandoc

HERE = Path(__file__).resolve().parent
RESOURCE_PATH = os.pathsep.join([str(HERE), str(HERE.parent)])

# AMS reference style: initials + surname, all authors, full journal, volume, year, pages.
REFS = {
    "simard2012mycorrhizal": "S. W. Simard, K. J. Beiler, M. A. Bingham, J. R. Deslippe, L. J. Philip and F. P. Teste, Mycorrhizal networks: mechanisms, ecology and modelling, Fungal Biology Reviews, 26, 2012, 39-60.",
    "terhoeven2025mesa": "E. ter Hoeven, J. Kwakkel, V. Hess, T. Pike, B. Wang, rht and J. Kazil, Mesa 3: agent-based modeling with Python in 2025, Journal of Open Source Software, 10, 2025, 7668.",
    "grasso2025tradecoevolution": "S. V. Grasso, M. H. Ryan, F. E. Albornoz and M. Renton, A simple plant-mycorrhizal fungal resource trade co-evolution model explains mutualism stability, extinction and transitory parasitism via fitness feedback, New Phytologist, 248, 2025, 1429-1441.",
    "vantpadje2021phosphorus": "A. van 't Padje, G. D. A. Werner and E. T. Kiers, Mycorrhizal fungi control phosphorus value in trade symbiosis with host roots when exposed to abrupt 'crashes' and 'booms' of resource availability, New Phytologist, 229, 2021, 2933-2944.",
    "masad2015mesa": "D. Masad and J. Kazil, Mesa: an agent-based modeling framework, Proceedings of the 14th Python in Science Conference, 2015, 51-58.",
    "grimm2020odd": "V. Grimm, S. F. Railsback, C. E. Vincenot, U. Berger, C. Gallagher, D. L. DeAngelis, B. Edmonds, J. Ge, J. Giske, J. Groeneveld, A. S. A. Johnston, A. Milles, J. Nabe-Nielsen, J. G. Polhill, V. Radchuk, M. Rohwader, R. A. Stillman, J. C. Thiele and D. Ayllon, The ODD protocol for describing agent-based and other simulation models: a second update to improve clarity, replication, and structural realism, Journal of Artificial Societies and Social Simulation, 23, 2020, 7.",
}


def main():
    src = (HERE / "paper-ams.md").read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", src, re.S)
    front, body = m.group(1), m.group(2)
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)

    order = []
    for key in re.findall(r"@([A-Za-z0-9]+)", body):
        if key not in order:
            order.append(key)
    num = {k: i + 1 for i, k in enumerate(order)}

    def repl(match):
        keys = re.findall(r"@([A-Za-z0-9]+)", match.group(0))
        return "[" + ", ".join(str(num[k]) for k in keys) + "]"

    body = re.sub(r"\[@[^\]]+\]", repl, body)
    body = re.sub(r"\n#+\s*References\s*$", "", body.rstrip())
    refs = "\n".join(f"[{num[k]}] {REFS[k]}\n" for k in order)
    body += "\n\n## References\n\n" + refs + "\n"

    tmp = HERE / "_ams_build.md"
    tmp.write_text(f"---\n{front}\n---\n\n{body}", encoding="utf-8")
    pypandoc.convert_file(str(tmp), "docx", outputfile=str(HERE / "paper-ams.docx"),
                          extra_args=["--resource-path", RESOURCE_PATH])
    print(f"wrote {HERE / 'paper-ams.docx'}  ({len(order)} references, {len(num)} cited)")
    try:
        pypandoc.convert_file(str(tmp), "pdf", outputfile=str(HERE / "paper-ams.pdf"),
                              extra_args=["--resource-path", RESOURCE_PATH, "--pdf-engine=xelatex"])
        print(f"wrote {HERE / 'paper-ams.pdf'}")
    except Exception as e:
        print(f"PDF build skipped ({type(e).__name__}); docx is ready. Detail: {str(e)[:200]}")
    tmp.unlink()


if __name__ == "__main__":
    main()
