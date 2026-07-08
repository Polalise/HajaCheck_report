import os
import glob
from jinja2 import Environment, FileSystemLoader

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(HERE, "html", "templates")
HTML_DIR = os.path.join(HERE, "html")


def compile_all():
    if not os.path.exists(TEMPLATE_DIR):
        print(f"오류: 템플릿 디렉터리가 존재하지 않습니다: {TEMPLATE_DIR}")
        return False

    print("Jinja2 템플릿 컴파일을 시작합니다...")
    # FileSystemLoader로 html/templates/ 디렉터리 지정
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

    # templates/ 아래의 모든 slide-*.html 파일 검색
    search_pattern = os.path.join(TEMPLATE_DIR, "slide-*.html")
    templates = glob.glob(search_pattern)

    if not templates:
        print("경고: 컴파일할 템플릿 파일(slide-*.html)이 존재하지 않습니다.")
        return True

    for t_path in templates:
        name = os.path.basename(t_path)
        output_path = os.path.join(HTML_DIR, name)
        
        try:
            template = env.get_template(name)
            rendered = template.render()
            
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(rendered)
            print(f"  - 컴파일 완료: {name} -> html/{name}")
        except Exception as e:
            print(f"  - 오류 발생 ({name}): {e}")
            return False
            
    print("모든 템플릿 컴파일 완료.")
    return True


if __name__ == "__main__":
    compile_all()
