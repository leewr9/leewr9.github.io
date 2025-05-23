import os
import yaml

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def get_post_files(posts_folder):
    post_files = []
    for root, dirs, files in os.walk(posts_folder):
        for file in files:
            if file.endswith('.md'):
                post_files.append(os.path.join(root, file))
    return post_files

def extract_metadata_from_post(post_file):
    tags_set = set()
    categories_set = set()

    with open(post_file, 'r', encoding='utf-8') as file:
        content = file.read()
        if content.startswith('---'):
            header_end = content.find('---', 3)

            if header_end != -1:
                header_content = content[3:header_end].strip()
                try:
                    metadata = yaml.safe_load(header_content)
                    if metadata:
                        tags = metadata.get('tag', [])
                        categories = metadata.get('category', [])

                        tags_set.update(tags)
                        if isinstance(categories, list):
                            categories_set.update(categories)
                        else:
                            categories_set.add(categories)
                except yaml.YAMLError:
                    print(f'YAML parsing error in {post_file}')
    
    return tags_set, categories_set

def create_tag_file(tag, tags_folder):
    tag_filename = os.path.join(tags_folder, f'{tag.lower().replace(" ", "_")}.md')

    if not os.path.exists(tag_filename):
        with open(tag_filename, 'w', encoding='utf-8') as tag_file:
            tag_file.write(f'---\n')
            tag_file.write(f'layout: label\n')
            tag_file.write(f'title: {tag}\n')
            tag_file.write(f'tag: {tag}\n')
            tag_file.write(f'permalink: /tags/{tag.lower().replace("#", "sharp")}/\n')
            tag_file.write(f'search_omit: true\n')
            tag_file.write(f'---\n')
        print(f'Tag file created: {tag_filename}')
    else:
        print(f"Tag file already exists: {tag_filename}")

def create_category_file(category, categories_folder):
    category_filename = os.path.join(categories_folder, f'{category.lower().replace(" ", "_")}.md')

    if not os.path.exists(category_filename):
        with open(category_filename, 'w', encoding='utf-8') as category_file:
            category_file.write(f'---\n')
            category_file.write(f'layout: label\n')
            category_file.write(f'title: {category}\n')
            category_file.write(f'category: {category}\n')
            category_file.write(f'permalink: /categories/{category.lower()}/\n')
            category_file.write(f'search_omit: true\n')
            category_file.write(f'---\n')
        print(f'Category file created: {category_filename}')
    else:
        print(f"Category file already exists: {category_filename}")

def main():
    posts_folder = '_posts'
    tags_folder = 'tags'
    categories_folder = 'categories'

    create_folder(tags_folder)
    create_folder(categories_folder)

    post_files = get_post_files(posts_folder)

    tags_set = set()
    categories_set = set()

    for post_file in post_files:
        post_tags, post_categories = extract_metadata_from_post(post_file)
        tags_set.update(post_tags)
        categories_set.update(post_categories)

    for tag in tags_set:
        create_tag_file(tag, tags_folder)

    for category in categories_set:
        create_category_file(category, categories_folder)

if __name__ == '__main__':
    main()
