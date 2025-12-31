import os
import random

# ================= 配置区 =================

# 1. 图片文件夹路径
IMAGE_FOLDER_PATH = r"D:\普朗达\网线产品图\八类圆形网线压缩图片"

# 2. SEO 关键词库 (注意：结尾必须有 ] 闭合)
SEO_KEYWORDS = [
    "cat8-patch-cord",
]  # <--- 之前可能就是这里少了右中括号

# 3. 起始编号
START_NUMBER = 1

# ================= 主程序 =================

def batch_rename_images():
    if not os.path.exists(IMAGE_FOLDER_PATH):
        print(f"❌ 错误：找不到文件夹路径: {IMAGE_FOLDER_PATH}")
        return

    files = os.listdir(IMAGE_FOLDER_PATH)
    # 过滤图片文件 (排除脚本本身)
    image_files = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]
    
    if not image_files:
        print(f"⚠️ 在文件夹中没有找到图片文件。")
        return

    print(f"📂 找到 {len(image_files)} 张图片，准备重命名...")
    
    count = 0
    total_keywords = len(SEO_KEYWORDS)

    for index, filename in enumerate(image_files):
        file_ext = os.path.splitext(filename)[1].lower()
        keyword = SEO_KEYWORDS[index % total_keywords]
        
        # 生成新名字: 关键词-001.jpg
        new_name = f"{keyword}-{str(index + START_NUMBER).zfill(3)}{file_ext}"
        
        old_path = os.path.join(IMAGE_FOLDER_PATH, filename)
        new_path = os.path.join(IMAGE_FOLDER_PATH, new_name)
        
        try:
            if os.path.exists(new_path):
                print(f"⚠️ 跳过: {new_name} 已存在")
                continue
            
            os.rename(old_path, new_path)
            print(f"✅: {filename} -> {new_name}")
            count += 1
        except Exception as e:
            print(f"❌: {filename} - {e}")

    print(f"\n🎉 完成！共重命名了 {count} 张图片。")

if __name__ == "__main__":
    batch_rename_images()
    input("按回车键退出...")