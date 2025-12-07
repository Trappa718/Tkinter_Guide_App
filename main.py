import flet as ft
import sys
import os

class TkinterGuideApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.current_page = "library"
        self.is_light_theme = False
        self.search_pending = False  # По умолчанию темная тема
        
        # Данные видео уроков (15 видео)
        self.videos = [
            {
                "title": "Модуль tkinter python",
                "video_file": "lesson_1.mp4",
            },
            {
                "title": "Кнопки в tkinter python",
                "video_file": "lesson_2.mp4",
            },
            {
                "title": "Виджет Label в tkinter python",
                "video_file": "lesson_3.mp4",
            },
            {
                "title": "Текстовое поле для ввода Entry в tkinter python",
                "video_file": "lesson_4.mp4",
            },
            {
                "title": "Метод pack в tkinter python",
                "video_file": "lesson_5.mp4",
            },
            {
                "title": "Метод place в tkinter python",
                "video_file": "lesson_6.mp4",
            },
            {
                "title": "Виджет Toplevel в tkinter python",
                "video_file": "lesson_7.mp4",
            },
            {
                "title": "Стили в tkinter ttk python",
                "video_file": "lesson_8.mp4",
            },
            {
                "title": "Рисование в tkinter python",
                "video_file": "lesson_9.mp4",
            },
            {
                "title": "Добавление фона окна tkinter python",
                "video_file": "lesson_10.mp4",
            },
            {
                "title": "Добавление вкладок в tkinter python",
                "video_file": "lesson_11.mp4",
            },
            {
                "title": "Как использовать HTML в tkinter python",
                "video_file": "lesson_12.mp4",
            },
            {
                "title": "Создание виджетов при нажатии на кнопку tkinter python",
                "video_file": "lesson_13.mp4",
            },
            {
                "title": "Делаем картинку кнопкой в tkinter python",
                "video_file": "lesson_14.mp4",
            },
            {
                "title": "Создание контекстного меню в tkinter python",
                "video_file": "lesson_15.mp4",
            },
        ]


        self.library_chapters = [
            {
                "title": "Глава 1. Основы Tkinter",
                "topics": [
                    {"title": "Введение в Tkinter. Первая программа"},
                    {"title": "Окно приложения"}
                ]
            },
            {
                "title": "Глава 2. Виджеты", 
                "topics": [
                    {"title": "Введение в виджеты. Tk и ttk"},
                    {"title": "Кнопки"},
                    {"title": "Позиционирование. Pack"},
                    {"title": "Позиционирование. Place"},
                    {"title": "Позиционирование. Grid"},
                    {"title": "Обработка событий"},
                    {"title": "Текстовая метка Label"},
                    {"title": "Поле ввода Entry"},
                    {"title": "Привязка виджетов к переменным"},
                    {"title": "Checkbutton"},
                    {"title": "Radiobutton"},
                    {"title": "Установка родительского контейнера. Frame"},
                    {"title": "Listbox"},
                    {"title": "Scrollbar и прокрутка виджета"},
                    {"title": "Combobox"},
                    {"title": "Scale"},
                    {"title": "Spinbox"},
                    {"title": "Progressbar"},
                    {"title": "Меню"},
                    {"title": "Notebook. Создание вкладок"}
                ]
            },
            {
                "title": "Глава 3. Виджет Text",
                "topics": [
                    {"title": "Создание многострочного текстового поля"},
                    {"title": "Основные операции с виджетом Text"},
                    {"title": "Стилизация и добавление виджетов в Text"}
                ]
            },
            {
                "title": "Глава 4. Виджет Treeview. Создание таблиц и деревьев",
                "topics": [
                    {"title": "Управление данными в Treeview"},
                    {"title": "Создание таблиц"},
                    {"title": "Нажатие на заголовок столбца и сортировка"},
                    {"title": "Выделение строк таблицы"},
                    {"title": "Создание дерева"}
                ]
            },
            {
                "title": "Глава 5. Окна",
                "topics": [
                    {"title": "Создание окон"},
                    {"title": "MessageBox"},
                    {"title": "Диалоговые окна"}
                ]
            },
            {
                "title": "Глава 6. Стилизация",
                "topics": [
                    {"title": "Шрифты"},
                    {"title": "Установка цвета"},
                    {"title": "Курсоры"},
                    {"title": "Установка стилей"},
                    {"title": "Темы"}
                ]
            },
            {
                "title": "Глава 7. Canvas",
                "topics": [
                    {"title": "Добавление элементов на Canvas"},
                    {"title": "Управление элементами в Canvas"},
                    {"title": "Установка тегов"},
                    {"title": "Привязка событий"}
                ]
            }
        ]
        self.setup_page()
        self.create_app_layout()
        self.show_library_page()

    def get_theme_colors(self):
        """Получение цветов в зависимости от текущей темы"""
        if self.is_light_theme:
            return {
                "bg_primary": "#E0E0E0",      # Задний фон
                "bg_container": "#FFFFFF",   # Контейнеры
                "bg_sidebar": "#FFFFFF",     # Боковая панель
                "bg_active": "#E0E0E0",      # Активная кнопка
                "bg_tertiary": "#F5F5F5",    # Третичный фон (для переключателя)
                "text_primary": "#000000",   # Основной текст (черный)
                "text_secondary": "#333333", # Вторичный текст
                "text_active": "#000000",    # Активный текст
                "divider": "#CCCCCC",        # Разделитель
                "border": "#CCCCCC",         # Границы
            }
        else:
            return {
                "bg_primary": "#0f0f0f",     # Задний фон
                "bg_container": "#1a1a1a",   # Контейнеры
                "bg_sidebar": "#1a1a1a",     # Боковая панель
                "bg_active": "#3a3f3e",      # Активная кнопка
                "bg_tertiary": "#2c302f",     # Третичный фон (для переключателя)
                "text_primary": "#FFFFFF",   # Основной текст (белый)
                "text_secondary": "#FFFFFF", # Вторичный текст
                "text_active": "#FFFFFF",    # Активный текст
                "divider": "#3a3f3e",        # Разделитель
                "border": "#3a3f3e",         # Границы
            }
            
    def exit_app(self, e):  
        self.page.window.close()

    def toggle_theme(self, e):
        """Переключение между светлой и темной темой"""
        # Если событие пришло от Switch, значение уже изменено автоматически
        if hasattr(e, 'control') and isinstance(e.control, ft.Switch):
            self.is_light_theme = e.control.value
        else:
            self.is_light_theme = not self.is_light_theme
        self.apply_theme()
        self.update_sidebar()
        # Обновляем текущую страницу, чтобы применить новые цвета
        if self.current_page == "library":
            self.show_library_page()
        elif self.current_page == "videos":
            self.show_videos_page()
        elif self.current_page == "functions":
            self.show_functions_page()
        elif self.current_page == "trainer":
            self.show_trainer_page()
        elif self.current_page == "about":
            self.show_about_page()

    def apply_theme(self):
        """Применение текущей темы к странице"""
        colors = self.get_theme_colors()
        self.page.bgcolor = colors["bg_primary"]
        self.page.theme_mode = ft.ThemeMode.LIGHT if self.is_light_theme else ft.ThemeMode.DARK
        self.sidebar_container.bgcolor = colors["bg_sidebar"]
        self.content_area.bgcolor = colors["bg_primary"]

    def setup_page(self):
        """Настройка основной страницы"""
        self.page.title = "Tkinter Учебное Пособие"
        colors = self.get_theme_colors()
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.bgcolor = colors["bg_primary"]
        self.page.padding = 0
        self.page.theme = ft.Theme(font_family="Play")
        self.page.dark_theme = ft.Theme(font_family="Play")

    def create_app_layout(self):
        """Создание основной структуры приложения"""
        colors = self.get_theme_colors()
        self.sidebar_container = ft.Container(
            width=280,
            padding=15,
            bgcolor=colors["bg_sidebar"],
            border_radius=15,
            margin=ft.margin.only(left=10, top=10, bottom=10)
        )
        
        self.content_area = ft.Container(expand=True, bgcolor=colors["bg_primary"], padding=20)
        
        self.page.add(
            ft.Row([
                self.sidebar_container,
                self.content_area,
            ], expand=True)
        )
        
        self.update_sidebar()

    def update_sidebar(self):
        """Обновление боковой панели с текущей подсветкой"""
        self.sidebar_container.content = self.create_sidebar()
        self.page.update()

    def create_nav_button(self, text, icon, page_name, click_handler):
        """Создание кнопки навигации с серой подсветкой активной страницы"""
        colors = self.get_theme_colors()
        is_active = self.current_page == page_name
        text_color = colors["text_active"] if is_active else colors["text_secondary"]
        icon_color = colors["text_active"] if is_active else colors["text_secondary"]
        return ft.Container(
            content=ft.TextButton(
                content=ft.Row([
                    ft.Icon(icon, 
                           color=icon_color, 
                           size=22),
                    ft.Text(text, 
                           color=text_color, 
                           size=16,
                           weight=ft.FontWeight.BOLD if is_active else ft.FontWeight.NORMAL),
                ]),
                on_click=click_handler,
            ),
            height=45,
            border_radius=8,
            padding=ft.padding.only(left=10),
            bgcolor=colors["bg_active"] if is_active else "transparent",
        )

    def create_sidebar(self):
        """Создание боковой панели навигации"""
        colors = self.get_theme_colors()
        return ft.Column([
            # Заголовок
            ft.Container(
                content=ft.Column([
                    ft.Text("Tkinter Guide", size=25, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                    ft.Text("Учебное пособие по Tkinter", size=14, color=colors["text_secondary"]),
                ]),
                padding=15,
                margin=ft.margin.only(bottom=20)
            ),
            
            ft.Divider(color=colors["divider"], height=1),
            ft.Container(height=10),
            
            # Навигационные кнопки
            ft.Container(
                content=ft.Column([
                    self.create_nav_button("Библиотека", ft.Icons.BOOK, "library", lambda e: self.show_library_page()),
                    self.create_nav_button("Видео уроки", ft.Icons.VIDEO_LIBRARY, "videos", lambda e: self.show_videos_page()),
                    self.create_nav_button("Функции", ft.Icons.CODE, "functions", lambda e: self.show_functions_page()),
                    self.create_nav_button("Тренажер", ft.Icons.FITNESS_CENTER, "trainer", lambda e: self.show_trainer_page()),
                    self.create_nav_button("О программе", ft.Icons.INFO, "about", lambda e: self.show_about_page()),
                ], spacing=5),
            ),
            
            ft.Container(expand=True),
            
            ft.Divider(color=colors["divider"], height=1),
            ft.Container(height=10),
            
            # Переключатель темы
            ft.Container(
                content=ft.Row([
                    ft.Icon(ft.Icons.WB_SUNNY if not self.is_light_theme else ft.Icons.NIGHTLIGHT, 
                           color=colors["text_secondary"], size=20),
                    ft.Text("Светлая тема" if not self.is_light_theme else "Темная тема", 
                           color=colors["text_secondary"], size=14),
                    ft.Switch(
                        value=self.is_light_theme,
                        on_change=self.toggle_theme,
                        active_color="#2196F3",
                    )
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                padding=15,
                bgcolor=colors["bg_tertiary"],
                border_radius=10,
                margin=ft.margin.only(bottom=10)
            ),
            
            ft.Divider(color=colors["divider"], height=1),
            ft.Container(height=10),
            
            # Кнопка выхода
            ft.Container(
                content=ft.ElevatedButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.EXIT_TO_APP, color=ft.Colors.WHITE, size=20),
                        ft.Text("Выйти", color=ft.Colors.WHITE, size=16, weight=ft.FontWeight.BOLD),
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    on_click=self.exit_app,
                    bgcolor="#d32f2f",
                    color=ft.Colors.WHITE,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                        padding=ft.padding.symmetric(horizontal=20, vertical=15),
                    ),
                ),
                padding=10,
            ),
        ])

    def update_content(self, content, page_name):
        """Обновление содержимого основной области"""
        self.current_page = page_name
        self.content_area.content = content
        self.update_sidebar()

    def get_video_path(self, video_file):
        """Получение пути к видеофайлу"""
        video_dir = "Video_Tkinter"
        if not os.path.exists(video_dir):
            os.makedirs(video_dir)
            print(f"Создана папка {video_dir}. Добавьте в неё видеофайлы.")
        
        return os.path.join(video_dir, video_file)

    def get_image_path(self, lesson_number):
        """Получение пути к изображению урока"""
        images_dir = "lesson_images"
        if not os.path.exists(images_dir):
            os.makedirs(images_dir)
            print(f"Создана папка {images_dir}. Добавьте в неё изображения уроков.")
        
        image_file = f"lesson_{lesson_number}.jpg"
        return os.path.join(images_dir, image_file)

    def get_library_image_path(self, image_file):
        """Получение пути к изображению для библиотеки"""
        Library_Images_dir = "Library_Images"
        if not os.path.exists(Library_Images_dir):
            os.makedirs(Library_Images_dir)
            print(f"Создана папка {Library_Images_dir}. Добавьте в неё изображения для библиотеки.")
        
        return os.path.join(Library_Images_dir, image_file)

    def open_video_external(self, video_path):
        """Открытие видео во внешнем плеере"""
        try:
            if os.path.exists(video_path):
                if sys.platform == "win32":
                    os.startfile(video_path)
                elif sys.platform == "darwin":  # macOS
                    os.system(f'open "{video_path}"')
                else:  # linux
                    os.system(f'xdg-open "{video_path}"')
            else:
                print(f"Файл не найден: {video_path}")
        except Exception as e:
            print(f"Ошибка при открытии видео: {e}")

    def create_search_field(self, hint_text, on_change_handler=None, value=""):
        """Создание поля поиска с кнопкой очистки"""
        colors = self.get_theme_colors()
        hint_color = "#666666" if self.is_light_theme else ft.Colors.WHITE54
        
        search_field = ft.TextField(
            hint_text=hint_text,
            hint_style=ft.TextStyle(color=hint_color),
            text_style=ft.TextStyle(color=colors["text_primary"]),
            bgcolor=colors["bg_container"],
            border_color=colors["border"],
            border_radius=10,
            width=250,
            height=40,
            prefix_icon=ft.Icons.SEARCH,
            value=value,
        )
        
        # Кнопка очистки
        clear_button = ft.IconButton(
            icon=ft.Icons.CLOSE,
            icon_size=18,
            icon_color=colors["text_secondary"],
            tooltip="Очистить поиск",
            visible=bool(value),
        )
        
        # Функция очистки
        def clear_search_handler(e):
            search_field.value = ""
            clear_button.visible = False
            clear_button.update()
            search_field.update()
            self.search_pending = False
            self.show_library_page()
        
        clear_button.on_click = clear_search_handler
        
        # Обновляем видимость кнопки при изменении текста
        def on_change_wrapper(e):
            has_text = bool(e.control.value and e.control.value.strip())
            clear_button.visible = has_text
            clear_button.update()
            
            # Если поле пустое, сразу показываем все темы
            if not has_text:
                self.search_pending = False
                self.show_library_page()
            else:
                # Помечаем, что поиск ожидает выполнения
                self.search_pending = True
        
        # Поиск по нажатию Enter или кнопки поиска
        def on_submit_handler(e):
            query = search_field.value
            self.search_pending = False
            # Выполняем поиск сразу
            if query and query.strip():
                self.search_library(query)
            else:
                self.show_library_page()
        
        search_field.on_change = on_change_wrapper
        search_field.on_submit = on_submit_handler
        
        # Кнопка поиска
        search_button = ft.IconButton(
            icon=ft.Icons.SEARCH,
            icon_size=20,
            icon_color=colors["text_primary"],
            tooltip="Найти",
            on_click=on_submit_handler,
        )
        
        return ft.Row([
            search_field,
            search_button,
            clear_button
        ], spacing=5, tight=True)

    def create_page_header(self, title, subtitle, search_hint=None, search_on_change=None):
        """Создание заголовка страницы с поиском"""
        colors = self.get_theme_colors()
        header_content = [
            ft.Column([
                ft.Text(title, size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Text(subtitle, size=16, color=colors["text_secondary"]),
            ], expand=True)
        ]
        
        if search_hint:
            header_content.append(self.create_search_field(search_hint, search_on_change))
        
        colors = self.get_theme_colors()
        return ft.Container(
            content=ft.Row(header_content),
            bgcolor=colors["bg_container"],
            padding=20,
            border_radius=15,
        )

    def create_code_block(self, code):
        """Создание блока кода без подсветки синтаксиса"""
        colors = self.get_theme_colors()
        code_color = colors["text_secondary"] if not self.is_light_theme else "#333333"
        return ft.Container(
            content=ft.Text(code, size=12, color=code_color, font_family="Courier New"),
            padding=15,
            bgcolor=colors["bg_container"],
            border_radius=10,
        )

    def create_function_card(self, title, description, code):
        """Создание карточки функции с кодом"""
        colors = self.get_theme_colors()
        return ft.Container(
            content=ft.Column([
                ft.Text(title, size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=5),
                ft.Text(description, size=14, color=colors["text_secondary"]),
                ft.Container(height=10),
                ft.Container(
                    content=ft.Column([
                        ft.Text("Код:", size=14, color=colors["text_primary"], weight=ft.FontWeight.BOLD),
                        ft.Container(height=5),
                        ft.Container(
                            content=ft.Column([
                                self.create_code_block(code)
                            ], scroll=ft.ScrollMode.ADAPTIVE),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                            height=200,
                        )
                    ]),
                )
            ]),
            padding=20,
            bgcolor=colors["bg_container"],
            border_radius=15,
            margin=ft.margin.only(bottom=15),
        )
    
    def highlight_syntax(self, code):
        """Подсветка синтаксиса Python кода"""
        colors = self.get_theme_colors()
        # Цвета для обычного текста кода
        text_color = colors["text_secondary"] if not self.is_light_theme else "#333333"
        # Цвета для подсветки синтаксиса (оставляем яркими для контраста)
        keyword_color = "#64B5F6" if self.is_light_theme else ft.Colors.BLUE_200
        builtin_color = "#FF9800" if self.is_light_theme else ft.Colors.ORANGE_300
        string_color = "#4CAF50" if self.is_light_theme else ft.Colors.GREEN_400
        comment_color = "#757575" if self.is_light_theme else ft.Colors.GREY_500
        
        # Простая подсветка ключевых слов Python
        keywords = ['def ', 'import ', 'from ', 'class ', 'if ', 'else ', 'elif ', 'for ', 'while ', 
                   'return ', 'try ', 'except ', 'finally ', 'with ', 'as ', 'global ', 'nonlocal ',
                   'lambda ', 'yield ', 'assert ', 'break ', 'continue ', 'pass ', 'raise ']
        
        builtins = ['print', 'len', 'range', 'str', 'int', 'float', 'list', 'dict', 'tuple', 'set']
        
        # Разбиваем код на строки и обрабатываем каждую
        lines = code.split('\n')
        highlighted_lines = []
        
        for line in lines:
            if not line.strip():
                highlighted_lines.append(ft.Text("", size=12))
                continue
                
            # Проверяем отступы
            indent = len(line) - len(line.lstrip())
            indent_text = " " * indent
            
            content = line.lstrip()
            spans = []
            
            # Проверяем на ключевые слова
            found_keyword = False
            for keyword in keywords:
                if content.startswith(keyword):
                    spans.append(ft.TextSpan(indent_text, style=ft.TextStyle(color=text_color)))
                    spans.append(ft.TextSpan(keyword, style=ft.TextStyle(color=keyword_color, weight=ft.FontWeight.BOLD)))
                    remaining = content[len(keyword):]
                    if remaining:
                        spans.append(ft.TextSpan(remaining, style=ft.TextStyle(color=text_color)))
                    found_keyword = True
                    break
            
            if not found_keyword:
                # Проверяем на встроенные функции
                found_builtin = False
                for builtin in builtins:
                    if builtin + '(' in content:
                        parts = content.split(builtin + '(', 1)
                        spans.append(ft.TextSpan(indent_text + parts[0], style=ft.TextStyle(color=text_color)))
                        spans.append(ft.TextSpan(builtin, style=ft.TextStyle(color=builtin_color, weight=ft.FontWeight.BOLD)))
                        spans.append(ft.TextSpan('(', style=ft.TextStyle(color=text_color)))
                        if parts[1]:
                            spans.append(ft.TextSpan(parts[1], style=ft.TextStyle(color=text_color)))
                        found_builtin = True
                        break
                
                if not found_builtin:
                    # Проверяем на строки (в кавычках)
                    if ('"' in content or "'" in content) and ('#' not in content or content.find('"') < content.find('#') or content.find("'") < content.find('#')):
                        # Простая обработка строк - выделяем все между кавычек
                        if '"' in content:
                            parts = content.split('"', 2)
                            if len(parts) >= 3:
                                spans.append(ft.TextSpan(indent_text + parts[0], style=ft.TextStyle(color=text_color)))
                                spans.append(ft.TextSpan('"' + parts[1] + '"', style=ft.TextStyle(color=string_color)))
                                if parts[2]:
                                    spans.append(ft.TextSpan(parts[2], style=ft.TextStyle(color=text_color)))
                            else:
                                spans.append(ft.TextSpan(indent_text + content, style=ft.TextStyle(color=text_color)))
                        elif "'" in content:
                            parts = content.split("'", 2)
                            if len(parts) >= 3:
                                spans.append(ft.TextSpan(indent_text + parts[0], style=ft.TextStyle(color=text_color)))
                                spans.append(ft.TextSpan("'" + parts[1] + "'", style=ft.TextStyle(color=string_color)))
                                if parts[2]:
                                    spans.append(ft.TextSpan(parts[2], style=ft.TextStyle(color=text_color)))
                            else:
                                spans.append(ft.TextSpan(indent_text + content, style=ft.TextStyle(color=text_color)))
                        else:
                            spans.append(ft.TextSpan(indent_text + content, style=ft.TextStyle(color=text_color)))
                    else:
                        # Проверяем на комментарии
                        if '#' in content:
                            comment_index = content.find('#')
                            code_part = content[:comment_index]
                            comment_part = content[comment_index:]
                            spans.append(ft.TextSpan(indent_text + code_part, style=ft.TextStyle(color=text_color)))
                            spans.append(ft.TextSpan(comment_part, style=ft.TextStyle(color=comment_color)))
                        else:
                            spans.append(ft.TextSpan(indent_text + content, style=ft.TextStyle(color=text_color)))
            
            highlighted_lines.append(ft.Text(spans=spans, size=12, font_family="Courier New"))
        
        return ft.Column(highlighted_lines, spacing=2)

    def create_function_card(self, title, description, code):
        """Создание карточки функции с кодом и подсветкой синтаксиса"""
        colors = self.get_theme_colors()
        return ft.Container(
            content=ft.Column([
                ft.Text(title, size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=5),
                ft.Text(description, size=14, color=colors["text_secondary"]),
                ft.Container(height=10),
                ft.Container(
                    content=ft.Column([
                        ft.Text("Код:", size=14, color=colors["text_primary"], weight=ft.FontWeight.BOLD),
                        ft.Container(height=5),
                        ft.Container(
                            content=ft.Column([
                                self.highlight_syntax(code)
                            ], scroll=ft.ScrollMode.ADAPTIVE),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                            height=200,  # Фиксированная высота с прокруткой
                        )
                    ]),
                )
            ]),
            padding=20,
            bgcolor=colors["bg_container"],
            border_radius=15,
            margin=ft.margin.only(bottom=15),
        )

    def create_video_lesson_card(self, video_data, video_index):
        """Создание карточки видеоурока"""
        video_path = self.get_video_path(video_data["video_file"])
        image_path = self.get_image_path(video_index + 1)
        
        # Проверяем существует ли изображение
        if os.path.exists(image_path):
            lesson_image = ft.Image(
                src=image_path,
                width=120,
                height=90,
                fit=ft.ImageFit.COVER,
                border_radius=10
            )
        else:
            colors = self.get_theme_colors()
            lesson_image = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.VIDEO_LIBRARY, size=40, color=colors["text_secondary"]),
                    ft.Text(f"Урок {video_index + 1}", size=12, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=120,
                height=80,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
        
        colors = self.get_theme_colors()
        return ft.Container(
            content=ft.Row([
                # Изображение урока
                lesson_image,
                
                # Текстовая информация
                ft.Column([
                    ft.Text(f"УРОК {video_index + 1}", 
                           size=12, 
                           color="#2196F3" if self.is_light_theme else ft.Colors.BLUE_200,
                           weight=ft.FontWeight.BOLD),
                    ft.Text(video_data["title"], 
                           size=16, 
                           color=colors["text_primary"],
                           weight=ft.FontWeight.BOLD),
                ], expand=True, spacing=5),
                
                # Кнопка воспроизведения
                ft.ElevatedButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.PLAY_ARROW, size=20),
                        ft.Text("Воспроизвести"),
                    ]),
                    on_click=lambda e, path=video_path: self.open_video_external(path),
                    bgcolor="#2196F3",
                    color=ft.Colors.WHITE,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                        padding=ft.padding.symmetric(horizontal=15, vertical=10),
                    ),
                ),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            padding=20,
            bgcolor=colors["bg_container"],
            border_radius=15,
        )


    def extract_text_from_content(self, topic_title):
        """Извлечение текста из контента темы для поиска"""
        try:
            # Используем тот же маппинг что и в show_topic_content
            content = None
            if topic_title == "Введение в Tkinter. Первая программа":
                content = self.create_introduction_content()
            elif topic_title == "Окно приложения":
                content = self.create_window_content()
            elif topic_title == "Введение в виджеты. Tk и ttk":
                content = self.create_widgets_introduction_content()
            elif topic_title == "Кнопки":
                content = self.create_buttons_content()
            elif topic_title == "Позиционирование. Pack":
                content = self.create_pack_positioning_content()
            elif topic_title == "Позиционирование. Place":
                content = self.create_place_positioning_content()
            elif topic_title == "Позиционирование. Grid":
                content = self.create_grid_positioning_content()
            elif topic_title == "Обработка событий":
                content = self.create_events_content()
            elif topic_title == "Текстовая метка Label":
                content = self.create_label_content()
            elif topic_title == "Поле ввода Entry":
                content = self.create_entry_content()
            elif topic_title == "Привязка виджетов к переменным":
                content = self.create_variable_binding_content()
            elif topic_title == "Checkbutton":
                content = self.create_checkbutton_content()
            elif topic_title == "Radiobutton":
                content = self.create_radiobutton_content()
            elif topic_title == "Установка родительского контейнера. Frame":
                content = self.create_frame_content()
            elif topic_title == "Listbox":
                content = self.create_listbox_content()
            elif topic_title == "Scrollbar и прокрутка виджета":
                content = self.create_scrollbar_content()
            elif topic_title == "Combobox":
                content = self.create_combobox_content()
            elif topic_title == "Scale":
                content = self.create_scale_content()
            elif topic_title == "Spinbox":
                content = self.create_spinbox_content()
            elif topic_title == "Progressbar":
                content = self.create_progressbar_content()
            elif topic_title == "Меню":
                content = self.create_menu_content()
            elif topic_title == "Notebook. Создание вкладок":
                content = self.create_notebook_content()
            elif topic_title == "Создание многострочного текстового поля":
                content = self.create_text_widget_content()
            elif topic_title == "Основные операции с виджетом Text":
                content = self.create_text_operations_content()
            elif topic_title == "Стилизация и добавление виджетов в Text":
                content = self.create_text_styling_content()
            elif topic_title == "Управление данными в Treeview":
                content = self.create_treeview_data_content()
            elif topic_title == "Создание таблиц":
                content = self.create_treeview_table_content()
            elif topic_title == "Нажатие на заголовок столбца и сортировка":
                content = self.create_treeview_sorting_content()
            elif topic_title == "Выделение строк таблицы":
                content = self.create_treeview_selection_content()
            elif topic_title == "Создание дерева":
                content = self.create_treeview_tree_content()
            elif topic_title == "Создание окон":
                content = self.create_windows_content()
            elif topic_title == "MessageBox":
                content = self.create_messagebox_content()
            elif topic_title == "Диалоговые окна":
                content = self.create_dialogs_content()
            elif topic_title == "Шрифты":
                content = self.create_fonts_content()
            elif topic_title == "Установка цвета":
                content = self.create_colors_content()
            elif topic_title == "Курсоры":
                content = self.create_cursors_content()
            elif topic_title == "Установка стилей":
                content = self.create_styles_content()
            elif topic_title == "Темы":
                content = self.create_themes_content()
            elif topic_title == "Добавление элементов на Canvas":
                content = self.create_canvas_elements_content()
            elif topic_title == "Управление элементами в Canvas":
                content = self.create_canvas_management_content()
            elif topic_title == "Установка тегов":
                content = self.create_canvas_tags_content()
            elif topic_title == "Привязка событий":
                content = self.create_canvas_events_content()
            
            if content:
                # Извлекаем текст из виджетов рекурсивно
                text_parts = []
                self._extract_text_recursive(content, text_parts)
                return " ".join(text_parts).lower()
        except Exception as e:
            print(f"Ошибка при извлечении текста для '{topic_title}': {e}")
        return ""
    
    def _extract_text_recursive(self, widget, text_parts):
        """Рекурсивное извлечение текста из виджетов"""
        try:
            # Обрабатываем ft.Text виджеты
            if isinstance(widget, ft.Text):
                if hasattr(widget, 'value') and widget.value:
                    text_parts.append(str(widget.value))
                elif hasattr(widget, 'data') and widget.data:
                    text_parts.append(str(widget.data))
                return
            
            # Обрабатываем виджеты с content
            if hasattr(widget, 'content'):
                content = widget.content
                if isinstance(content, str):
                    text_parts.append(content)
                elif isinstance(content, (list, tuple)):
                    for item in content:
                        self._extract_text_recursive(item, text_parts)
                elif content is not None:
                    self._extract_text_recursive(content, text_parts)
            
            # Обрабатываем виджеты с controls (Column, Row и т.д.)
            if hasattr(widget, 'controls'):
                for control in widget.controls:
                    self._extract_text_recursive(control, text_parts)
            
            # Обрабатываем виджеты с actions
            if hasattr(widget, 'actions'):
                for action in widget.actions:
                    self._extract_text_recursive(action, text_parts)
            
            # Обрабатываем итерируемые объекты
            if isinstance(widget, (list, tuple)):
                for item in widget:
                    self._extract_text_recursive(item, text_parts)
        except Exception:
            # Игнорируем ошибки при извлечении текста
            pass

    def search_library(self, search_query):
        """Поиск по библиотеке"""
        if not search_query or search_query.strip() == "":
            # Если поиск пустой, показываем все темы
            self.show_library_page()
            return
        
        search_query = search_query.lower().strip()
        colors = self.get_theme_colors()
        
        # Фильтруем главы и темы по поисковому запросу
        filtered_chapters = []
        for chapter in self.library_chapters:
            # Проверяем название главы
            chapter_matches = search_query in chapter["title"].lower()
            
            # Фильтруем темы
            filtered_topics = []
            for topic in chapter["topics"]:
                topic_matches = search_query in topic["title"].lower()
                
                # Ищем в тексте контента темы
                content_text = self.extract_text_from_content(topic["title"])
                content_matches = search_query in content_text if content_text else False
                
                if topic_matches or chapter_matches or content_matches:
                    filtered_topics.append(topic)
            
            # Если есть совпадения, добавляем главу
            if filtered_topics or chapter_matches:
                filtered_chapters.append({
                    "title": chapter["title"],
                    "topics": filtered_topics if filtered_topics else chapter["topics"]
                })
        
        # Создаем контент с результатами поиска
        if not filtered_chapters:
            # Нет результатов - занимает всю страницу
            results_content = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.SEARCH_OFF, size=80, color=colors["text_secondary"]),
                    ft.Container(height=20),
                    ft.Text("Ничего не найдено", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                    ft.Container(height=10),
                    ft.Text(f"По запросу '{search_query}' ничего не найдено", size=16, color=colors["text_secondary"]),
                    ft.Container(height=10),
                    ft.Text("Попробуйте изменить поисковый запрос или использовать другие ключевые слова", 
                           size=14, color=colors["text_secondary"], italic=True),
                ], 
                horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=0),
                padding=50,
                expand=True,
                alignment=ft.alignment.center,
            )
        else:
            results_content = ft.Container(
                content=ft.Column([
                    ft.Text(f"Найдено результатов: {sum(len(ch['topics']) for ch in filtered_chapters)}", 
                           size=14, color=colors["text_secondary"], weight=ft.FontWeight.BOLD),
                    ft.Container(height=10),
                    *[self.create_chapter_section(chapter, chapter_index) 
                      for chapter_index, chapter in enumerate(filtered_chapters)]
                ], scroll=ft.ScrollMode.ADAPTIVE),
                padding=25,
            )
        
        # Создаем поле поиска с текущим значением
        search_field_container = self.create_search_field(
            "Поиск по библиотеке...",
            lambda e: self.search_library(e.control.value),
            search_query
        )
        
        content = ft.Container(
            content=ft.Column([
                self.create_page_header_with_search(
                    "Библиотека Tkinter", 
                    "Полное руководство по созданию GUI приложений", 
                    search_field_container
                ),
                ft.Container(height=20),
                ft.Container(
                    content=results_content,
                    bgcolor=colors["bg_container"],
                    border_radius=15,
                    expand=True,
                )
            ]),
            expand=True
        )
        self.update_content(content, "library")


    def show_library_page(self, search_query=""):
        """Страница библиотеки"""
        if search_query:
            self.search_library(search_query)
            return
            
        colors = self.get_theme_colors()
        
        # Создаем поле поиска с возможностью очистки
        search_field_container = self.create_search_field(
            "Поиск по библиотеке...",
            lambda e: self.search_library(e.control.value),
            ""
        )
        
        content = ft.Container(
            content=ft.Column([
                self.create_page_header_with_search(
                    "Библиотека Tkinter", 
                    "Полное руководство по созданию GUI приложений", 
                    search_field_container
                ),
                ft.Container(height=20),
                
                ft.Container(
                    content=ft.Column([
                        *[self.create_chapter_section(chapter, chapter_index) 
                          for chapter_index, chapter in enumerate(self.library_chapters)]
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    bgcolor=colors["bg_container"],
                    border_radius=15,
                    padding=25,
                    expand=True,
                )
            ]),
            expand=True
        )
        self.update_content(content, "library")
    
    def create_page_header_with_search(self, title, subtitle, search_widget):
        """Создание заголовка страницы с виджетом поиска"""
        colors = self.get_theme_colors()
        header_content = [
            ft.Column([
                ft.Text(title, size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Text(subtitle, size=16, color=colors["text_secondary"]),
            ], expand=True)
        ]
        
        if search_widget:
            header_content.append(search_widget)
        
        return ft.Container(
            content=ft.Row(header_content),
            bgcolor=colors["bg_container"],
            padding=20,
            border_radius=15,
        )

    def create_chapter_section(self, chapter, chapter_index):
        """Создание раздела главы с темами"""
        colors = self.get_theme_colors()
        return ft.Container(
            content=ft.Column([
                # Заголовок главы
                ft.Container(
                    content=ft.Text(chapter["title"], size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                    padding=10,
                ),
                
                # Список тем
                ft.Column([
                    *[self.create_topic_item(topic, chapter_index, topic_index) 
                      for topic_index, topic in enumerate(chapter["topics"])]
                ]),
                
                ft.Divider(color=colors["divider"], height=1, thickness=1),
                ft.Container(height=20),
            ]),
        )

    def create_topic_item(self, topic, chapter_index, topic_index):
        """Создание элемента темы"""
        colors = self.get_theme_colors()
        return ft.Container(
            content=ft.Row([
                ft.Icon(ft.Icons.CHEVRON_RIGHT, size=16, color=colors["text_secondary"]),
                ft.Text(topic["title"], color=colors["text_secondary"], size=14, expand=True),
            ]),
            padding=ft.padding.only(left=20, top=8, bottom=8),
            on_click=lambda e, t=topic["title"]: self.show_topic_content(t),
        )

    def show_topic_content(self, topic_title):
        """Содержание темы"""
        # Определяем какой контент показывать в зависимости от темы
        if topic_title == "Введение в Tkinter. Первая программа":
            content = self.create_introduction_content()
        elif topic_title == "Окно приложения":
            content = self.create_window_content()
        elif topic_title == "Введение в виджеты. Tk и ttk":
            content = self.create_widgets_introduction_content()
        elif topic_title == "Кнопки":
            content = self.create_buttons_content()
        elif topic_title == "Позиционирование. Pack":
            content = self.create_pack_positioning_content()
        elif topic_title == "Позиционирование. Place":
            content = self.create_place_positioning_content()
        elif topic_title == "Позиционирование. Grid":
            content = self.create_grid_positioning_content()
        elif topic_title == "Обработка событий":
            content = self.create_events_content()
        elif topic_title == "Текстовая метка Label":
            content = self.create_label_content()
        elif topic_title == "Поле ввода Entry":
            content = self.create_entry_content()
        elif topic_title == "Привязка виджетов к переменным":
            content = self.create_variable_binding_content()
        elif topic_title == "Checkbutton":
            content = self.create_checkbutton_content()
        elif topic_title == "Radiobutton":
            content = self.create_radiobutton_content()
        elif topic_title == "Установка родительского контейнера. Frame":
            content = self.create_frame_content()
        elif topic_title == "Listbox":
            content = self.create_listbox_content()
        elif topic_title == "Scrollbar и прокрутка виджета":
            content = self.create_scrollbar_content()
        elif topic_title == "Combobox":
            content = self.create_combobox_content()
        elif topic_title == "Scale":
            content = self.create_scale_content()
        elif topic_title == "Spinbox":
            content = self.create_spinbox_content()
        elif topic_title == "Progressbar":
            content = self.create_progressbar_content()
        elif topic_title == "Меню":
            content = self.create_menu_content()
        elif topic_title == "Notebook. Создание вкладок":
            content = self.create_notebook_content()
        elif topic_title == "Создание многострочного текстового поля":
            content = self.create_text_widget_content()
        elif topic_title == "Основные операции с виджетом Text":
            content = self.create_text_operations_content()
        elif topic_title == "Стилизация и добавление виджетов в Text":
            content = self.create_text_styling_content()
        elif topic_title == "Управление данными в Treeview":
            content = self.create_treeview_data_content()
        elif topic_title == "Создание таблиц":
            content = self.create_treeview_table_content()
        elif topic_title == "Нажатие на заголовок столбца и сортировка":
            content = self.create_treeview_sorting_content()
        elif topic_title == "Выделение строк таблицы":
            content = self.create_treeview_selection_content()
        elif topic_title == "Создание дерева":
            content = self.create_treeview_tree_content()
        elif topic_title == "Создание окон":
            content = self.create_windows_content()
        elif topic_title == "MessageBox":
            content = self.create_messagebox_content()
        elif topic_title == "Диалоговые окна":
            content = self.create_dialogs_content()
        elif topic_title == "Шрифты":
            content = self.create_fonts_content()
        elif topic_title == "Установка цвета":
            content = self.create_colors_content()
        elif topic_title == "Курсоры":
            content = self.create_cursors_content()
        elif topic_title == "Установка стилей":
            content = self.create_styles_content()
        elif topic_title == "Темы":
            content = self.create_themes_content()
        elif topic_title == "Добавление элементов на Canvas":
            content = self.create_canvas_elements_content()
        elif topic_title == "Управление элементами в Canvas":
            content = self.create_canvas_management_content()
        elif topic_title == "Установка тегов":
            content = self.create_canvas_tags_content()
        elif topic_title == "Привязка событий":
            content = self.create_canvas_events_content()
        else:
            content = self.create_default_topic_content(topic_title)
        
        self.update_content(content, "library")

    def create_introduction_content(self):
        """Создание контента для темы 'Введение в Tkinter. Первая программа'"""
        colors = self.get_theme_colors()
        image_path = self.get_library_image_path("t1.png")
        
        # Проверяем существует ли изображение
        if os.path.exists(image_path):
            program_image = ft.Image(
                src=image_path,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            program_image = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение программы", size=12, color=colors["text_secondary"]),
                    ft.Text("first_program.jpg", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Введение в Tkinter. Первая программа", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Многие программы на сегодняшний день используют графический интерфейс, который более интуитивен и удобен для пользователя, чем консоль. И с помощью языка программирования Python также можно создавать графические программы. Для этого в Python по умолчанию применяется специальный тулкит - набор компонентов, который называется tkinter.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Тулкит tkinter доступен в виде отдельного встроенного модуля, который содержит все необходимые графические компоненты - кнопки, текстовые поля и т.д.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "По сути Tkinter представляет интерфейс в Python для графической библиотеки Tk (Собственно само название 'Tkinter' является сокращением 'Tk interface'). Первоначально данная библиотека разрабатывалась для языка Tcl - ее создал в 1988 году Джон Остерхаут (John Ousterhout), профессор computer science из Беркли для создания графических приложений для своего языка Tcl. Но впоследствии Tk была адаптирована для широкого ряда динамических языков, в частности, для Ruby, Perl и естественно для языка Python (в 1994 году). И на сегодняшний день и библиотека Tk, и сам тулкит tkinter доступны для большинства операционных систем, в том числе для Mac OS, Linux и Windows.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Преимущества Tkinter:", size=16, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text("• Данный тулкит по умолчанию включен в стандартную библиотеку языка Python в виде отдельного модуля, поэтому не потребуется что-то дополнительно устанавливать", size=14, color=colors["text_secondary"]),
                        ft.Text("• Tkinter - кроссплатформенный, один и тот же код будет работать одинаково на разных платформах (Mac OS, Linux и Windows)", size=14, color=colors["text_secondary"]),
                        ft.Text("• Tkinter легко изучать. Сам тулкит, хотя и содержит некоторый готовый код, виджеты и графические элементы, но при этом довольно лаконичен и прост.", size=14, color=colors["text_secondary"]),
                        ft.Text("• Tk распространяется по BSD-лицензии, поэтому библиотека может быть использована как в опенсорсных проектах, так и в коммерческих наработках.", size=14, color=colors["text_secondary"]),
                        ft.Container(height=20),
                        
                        ft.Text("Если необходимо или интересно узнать версию библиотеки Tk, которая будет использоваться, в интерпертаторе Python можно выполнить следующую инструкцию:", size=14, color=colors["text_secondary"]),
                        ft.Container(height=10),
                        
                        # Блок кода
                        ft.Container(
                            content=self.highlight_syntax("tkinter.Tcl().eval(\"info patchlevel\")"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text("Пример выполнения:", size=14, color=colors["text_secondary"]),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''C:\\Users\\eugen>python\nPython 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32\nType "help", "copyright", "credits" or "license" for more information.\n>>> import tkinter\n>>>\n>>> tkinter.Tcl().eval("info patchlevel")\n'8.6.12'\n>>>'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text("В некоторых ОС на базе Linux иногда при установке python не устанавливается пакет tkinter. В этом случае мы можем доустановить thinkter командой", size=14, color=colors["text_secondary"]),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("sudo apt-get install python3-tk"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Первая программа", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text("Создадим первую программу с использованием Tkinter. Для этого определим следующий скрипт:", size=14, color=colors["text_secondary"]),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n\nroot = Tk()     # создаем корневой объект - окно\nroot.title("Приложение на Tkinter")     # устанавливаем заголовок окна\nroot.geometry("300x250")    # устанавливаем размеры окна\n\nlabel = Label(text="Hello METANIT.COM") # создаем текстовую метку\nlabel.pack()    # размещаем метку в окне\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text("Для создания графического окна применяется конструктор Tk(), который определен в модуле tkinter. Создаваемое окно присваивается переменной root, и через эту переменную мы можем управлять атрибутами окна. В частности, с помощью метода title() можно установить заголовок окна.", size=14, color=colors["text_secondary"]),
                        ft.Container(height=10),
                        
                        ft.Text("С помощью метода geometry() - размер окна. Для установки размера в метод geometry() передается строка в формате 'Ширина x Высота'. Если при создании окна приложения метод geometry() не вызывается, то окно занимает то пространство, которое необходимо для размещения внутреннего содержимого.", size=14, color=colors["text_secondary"]),
                        ft.Container(height=10),
                        
                        ft.Text("Создав окно, мы можем разместить в нем другие графические элементы. Эти элементы еще называются виджетами. В данном случае мы размещаем в окне текстовую метку. Для это создаем объект класса Label, которые хранит некоторый текст. Затем для размещения элемента label в окне вызываем у него метод pack()", size=14, color=colors["text_secondary"]),
                        ft.Container(height=10),
                        
                        ft.Text("Для отображения окна надо вызвать у него метод mainloop(), который запускает цикл обработки событий окна для взаимодействия с пользователем.", size=14, color=colors["text_secondary"]),
                        ft.Container(height=10),
                        
                        ft.Text("В результате при запуске скрипта мы увидим такое пустое окошко:", size=14, color=colors["text_secondary"]),
                        ft.Container(height=10),
                        
                        # Изображение программы
                        ft.Container(
                            content=program_image,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Графическая программа на Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=10),
                        
                        ft.Text("На скриншоте выше определено окно, создаваемое в ОС Windows, на каждой конкретной системе отдельные визуальные моменты, отрисовка графических компонентов может несколько отличаться.", size=14, color=colors["text_secondary"]),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_window_content(self):
        """Создание контента для темы 'Окно приложения'"""
        colors = self.get_theme_colors()
        image_path1 = self.get_library_image_path("t2.png")
        image_path2 = self.get_library_image_path("t3.png")
        
        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            window_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            window_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение окна", size=12, color=colors["text_secondary"]),
                    ft.Text("t2.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            window_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            window_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение иконки", size=12, color=colors["text_secondary"]),
                    ft.Text("t3.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Окно приложения", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Основным компонентом графических программ является окно. Затем в окно добавляются все остальные компоненты графического интерфейса. В Tkinter окно представлено классом Tk. Например, создание окна:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("root = Tk()"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Для отображения окна и взаимодействия с пользователем у окна вызывается метод mainloop()",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n\nroot = Tk() \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Класс Tk обладает рядом методов и атрибутов, которые позволяют установить различные аспекты окна. Некоторые из них.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Размеры и начальная позиция окна", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "По умолчанию окно имеет некоторые стандартные размеры. Для установки размеров используется метод geometry(). Например, определение окна с шириной в 300 единиц и высотой 250 единиц:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n\nroot = Tk()\nroot.geometry("300x250")\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "По умолчанию окно позиционируется в верхний левый угол экрана с небольшим смещением. Но мы можем изменить его положение, передав нужные значения в метод geometry():",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n\nroot = Tk()\nroot.geometry("300x250+400+200")\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Теперь строка в методе geometry имеет следующий формат: 'Ширина x Высота + координатаX + координатаY'. То есть при запуске окно шириной в 300 единиц и высотой 250 единиц будет находиться на 400 пикселей вправо и на 200 пикселей вниз от верхнего левого угла экрана.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Для получения данных о размере и позиции также можно использовать метод geometry(), который возвращает данные значения в виде строки в формате 'widthxheight+x+y':",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n\nroot = Tk()\nroot.geometry("300x250+400+200")\n\nroot.update_idletasks()\nprint(root.geometry())    # "300x250+400+200"\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Чтобы приложение еще до метода mainloop() приминенило для окна переданные ему значения по ширине, высоте и позиции, вызывается метод root.update_idletasks(). В итоге вызов root.geometry() возвратить строку '300x250+400+200'",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "По умолчанию мы можем изменять размеры окна. Тем не менее иногда может потребоваться сделать размер окна фиксированным. В этом случае мы можем использовать метод resizable(). Его первый параметр указывает, может ли пользователь растягивать окно по ширине, а второй параметр - можно ли растягивать по высоте. Чтобы запретить растягивание по какой-либо стороне, необходимо для соответствующего параметра передать значение False. Например, запретим какое-либо изменение размеров:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n\nroot = Tk()\nroot.geometry("300x250")\n\nroot.resizable(False, False)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Также можно установить минимальные и максимальные размеры окна:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''root.minsize(200,150)   # минимальные размеры: ширина - 200, высота - 150\nroot.maxsize(400,300)   # максимальные размеры: ширина - 400, высота - 300'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Установка заголовка", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "По умолчанию заголовок окна - 'tk'. Для установки заголовка применяется метод title(), в который передается текст заголовка:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n\nroot = Tk()\nroot.title("Hello METANIT.COM")\nroot.geometry("300x250") \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 1
                        ft.Container(
                            content=window_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Заголовок и размеры окна в thinkter в Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Установка иконки", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Перед заголовком отображается иконка. По умолчанию это иконка пера. С помощью метода iconbitmap() можно задать любую другую иконку. Например, определим в одной папке с файлом приложения какой-нибудь файл с иконкой, допустип, он называется 'favicon.ico' и используем его для установки иконки:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n\nroot = Tk()\nroot.title("Hello METANIT.COM")\nroot.iconbitmap(default="favicon.ico")\nroot.geometry("300x250") \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "через параметр default в метод iconbitmap передается путь к иконки. В данном случае файл иконки располагается с файлом приложения в одной папке, поэтому в качестве пути указывается просто имя файла.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 2
                        ft.Container(
                            content=window_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Иконка окна в thinkter в Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В качестве альтернативы для установки иконки также можно было бы использовать метод iconphoto()",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n\nroot = Tk()\nroot.geometry("250x200")\n\nroot.title("Hello METANIT.COM")\nicon = PhotoImage(file = "icon2.png")\nroot.iconphoto(False, icon)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Первый параметр метода iconphoto() указывает, надо ли использовать иконку по умолчанию для всех окон приложения. Второй параметр - объект PhotoImage, который собственно и устанавливает файл изображения (здесь файл 'icon2.png')",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Однако что, если мы хотим, чтобы окно вообще не имело иконки? В этом случае можно определить прозрачную иконку и также ее подключать. Можно это сделать также динамически без наличия реального файла:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nimport tempfile, base64, zlib\n\nICON = zlib.decompress(base64.b64decode("eJxjYGAEQgEBBiDJwZDBysAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc="))\n\n_, ICON_PATH = tempfile.mkstemp()\nwith open(ICON_PATH, "wb") as icon_file:\n    icon_file.write(ICON)\n\nroot = Tk()\nroot.title("Hello METANIT.COM")\nroot.geometry("300x250")\n\nroot.iconbitmap(default=ICON_PATH)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае создается временный файл иконки в памяти.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Перехват закрытия окна", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n\ndef finish():\n    root.destroy()  # ручное закрытие окна и всего приложения\n    print("Закрытие приложения")\n\nroot = Tk()\nroot.geometry("250x200")\n\nroot.title("Hello METANIT.COM")\nroot.protocol("WM_DELETE_WINDOW", finish)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Первый параметр метода protocol() представляет имя события, в данном случае это 'WM_DELETE_WINDO'. Второй параметр представляет функцию, которая вызывается при возникновении события. Здесь эта функция finish(), в котором с помощью метода destroy() вручную вызываем закрытие окна (а с ним и всего приложения), а затем выводим на консоль некоторое сообщение.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Атрибуты окна", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "С помощью специального метода attributes() можно установать отдельные атрибуты окна, для которых нет специальных методов. В качестве первого параметра метод принимает название атрибута, которое предваряется дефисом. А второй параметр - значение для этого атрибута. Например, растяжение окна на весь экран:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("root.attributes(\"-fullscreen\", True)"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь атрибуту fullscreen передается значение True, благодаря чему устанавливается полноэкранный режим.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Другой пример - установка прозрачности с помощью атрибута alpha:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("root.attributes(\"-alpha\", 0.5)"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Значение 0.5 указывает на полупрозрачность.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Третий пример - отключение верхней панели окна (за исключением заголовка и крестика для закрытия):",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("root.attributes(\"-toolwindow\", True)"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_widgets_introduction_content(self):
        """Создание контента для темы 'Введение в виджеты. Tk и ttk'"""
        colors = self.get_theme_colors()
        image_path1 = self.get_library_image_path("t4.png")
        image_path2 = self.get_library_image_path("t5.png")
        image_path3 = self.get_library_image_path("t6.png")
        
        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            widget_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            widget_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение виджетов tkinter", size=12, color=colors["text_secondary"]),
                    ft.Text("t4.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            widget_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            widget_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение виджетов ttk", size=12, color=colors["text_secondary"]),
                    ft.Text("t5.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 3
        if os.path.exists(image_path3):
            widget_image3 = ft.Image(
                src=image_path3,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            widget_image3 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение параметров виджета", size=12, color=colors["text_secondary"]),
                    ft.Text("t6.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Введение в виджеты. Tk и ttk", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Ключевым строительным блоком в графическом приложении являются различные элементов управления, с которыми взаимодействует пользователь, как кнопки, метки, поля ввода. В Tkinter имеется богатая палитра различных элементов управления, которые называются виджетами. Основные из них:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text("Button: кнопка", size=14, color=colors["text_secondary"]),
                        ft.Text("Label: текстовая метка", size=14, color=colors["text_secondary"]),
                        ft.Text("Entry: однострочное текстовое поле", size=14, color=colors["text_secondary"]),
                        ft.Text("Text: многострочное текстовое поле", size=14, color=colors["text_secondary"]),
                        ft.Text("Checkbutton: флажок", size=14, color=colors["text_secondary"]),
                        ft.Text("Radiobutton: переключатель или радиокнопка", size=14, color=colors["text_secondary"]),
                        ft.Text("Frame: фрейм, который организует виджеты в группы", size=14, color=colors["text_secondary"]),
                        ft.Text("Listbox: список", size=14, color=colors["text_secondary"]),
                        ft.Text("Combobox: выпадающий список", size=14, color=colors["text_secondary"]),
                        ft.Text("Menu: элемент меню", size=14, color=colors["text_secondary"]),
                        ft.Text("Scrollbar: полоса прокрутки", size=14, color=colors["text_secondary"]),
                        ft.Text("Treeview: позволяет создавать древовидные и табличные элементы", size=14, color=colors["text_secondary"]),
                        ft.Text("Scale: текстовая метка", size=14, color=colors["text_secondary"]),
                        ft.Text("Spinbox: список значений со стрелками для перемещения по элементам", size=14, color=colors["text_secondary"]),
                        ft.Text("Progressbar: текстовая метка", size=14, color=colors["text_secondary"]),
                        ft.Text("Canvas: текстовая метка", size=14, color=colors["text_secondary"]),
                        ft.Text("Notebook: панель вкладок", size=14, color=colors["text_secondary"]),
                        ft.Container(height=20),
                        
                        ft.Text(
                            "Tkinter предоставляет виджеты в двух вариантах: виджеты, которые располагаются непосредственно в пакете tkinter, и виджеты из пакета tkinter.ttk. С одной стороны, оба пакета предоставляют практически одни и те же виджеты, например, виджет Button есть в обоих пакетах. Но с другой стороны, ttk предоставляет чуть больше функциональности по настройке виджетов, в частности, по их стилизации. И считается, что виджеты из ttk несколько современнее, чем стандартные, в то же время с ttk, возможно, чуть сложнее работать. Что именно использовать остается на выбор разработчика.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Рассмотрим разницу на примере виджета Button. Сначала посмотрим на стандартный виджет Button из общего пакета tkinter:", size=14, color=colors["text_secondary"]),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nbtn = Button(text="Click") # создаем кнопку из пакета tkinter\nbtn.pack()    # размещаем кнопку в окне\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 1
                        ft.Container(
                            content=widget_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Виджеты в графическом приложении tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Теперь посмотрим на примере кнопки из пакета ttk:", size=14, color=colors["text_secondary"]),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk     # подключаем пакет ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nbtn = ttk.Button(text="Click") # создаем кнопку из пакета ttk\nbtn.pack()    # размещаем кнопку в окне\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text("По сути мы создаем ту же самую кнопку с той же надписью, однако ее внешний вид будет несколько иной:", size=14, color=colors["text_secondary"]),
                        ft.Container(height=10),
                        
                        # Изображение 2
                        ft.Container(
                            content=widget_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Виджеты ttk в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("В дальнейшем я буду ориентироваться прежде всего на виджеты из пакета ttk, но перейти на стандартные виджеты не составит особого труда.", size=14, color=colors["text_secondary"]),
                        ft.Container(height=20),
                        
                        ft.Text("Параметры виджета", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Виджет обладает набором параметров, которые позволяют настроить его внешний вид и поведение. У каждого виджета свой набор параметров. Обычно параметры задаются через конструктор. Например, в примере выше у кнопки устанавливался параметр text, который задает текст на кнопке:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('ttk.Button(text="Click") # устанавливаем параметр text'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Но обращаться к параметрам можно и вне конструктора, используя имя переменной виджета и синтаксис словарей:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x150")\n\nbtn = ttk.Button()\nbtn.pack()\n# устанавливаем параметр text\nbtn["text"]="Send"\n# получаем значение параметра text\nbtnText = btn["text"]\nprint(btnText)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 3
                        ft.Container(
                            content=widget_image3,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Получение и установка параметров виджета в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Для изменения параметров виджета также можно использовать метод config(), в который передаются параметры и их значения:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''btn = ttk.Button()\nbtn.pack()\n# устанавливаем параметр text\nbtn.config(text="Send Email")'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Получение информации о виджете", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для получения информации о виджете можно использовать ряд его атрибутов. Рассмотрим некоторые из них:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text("• winfo_class: возвращает класс виджета, например, для кнопки это класс TButton", size=14, color=colors["text_secondary"]),
                        ft.Text("• winfo_children: возвращает для текущего виджета список вложенных виджетов", size=14, color=colors["text_secondary"]),
                        ft.Text("• winfo_parent: возвращает родительский виджет", size=14, color=colors["text_secondary"]),
                        ft.Text("• winfo_toplevel: возвращает окно, которое содержит данный виджет", size=14, color=colors["text_secondary"]),
                        ft.Text("• winfo_width и winfo_height: текущая ширина и высота виджета", size=14, color=colors["text_secondary"]),
                        ft.Text("• winfo_reqwidth и winfo_reqheight: запрошенная виджетом ширина и высота", size=14, color=colors["text_secondary"]),
                        ft.Text("• winfo_x и winfo_y: x и y координаты верхнего левого угла виджета относительно родительского элемента", size=14, color=colors["text_secondary"]),
                        ft.Text("• winfo_rootx и winfo_rooty: x и y координаты верхнего левого угла виджета относительно экрана", size=14, color=colors["text_secondary"]),
                        ft.Text("• winfo_viewable: указывает, отображается ли виджет или скрыт", size=14, color=colors["text_secondary"]),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Например, получим информацию о всех виджетах в окне:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nbtn = Button(text="Hello")\nbtn.pack()\n\n\ndef print_info(widget, depth=0):\n    widget_class=widget.winfo_class()\n    widget_width = widget.winfo_width()\n    widget_height = widget.winfo_height()\n    widget_x = widget.winfo_x()\n    widget_y = widget.winfo_y()\n    print("   "*depth + f"{widget_class} width={widget_width} height={widget_height}  x={widget_x} y={widget_y}")\n    for child in widget.winfo_children():\n        print_info(child, depth+1)\n\nroot.update()     # обновляем информацию о виджетах\n\nprint_info(root)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь определена функция print_info(), которая в качестве параметров получает виджет, информацию о котором надо вывести на консоль, и уровень в визуальной иерархии элементов (depth).",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "В самой функции для виджета выводим информацию о классе, ширине, высоте и координатах Х и Y, а также для каждого вложенного виджета рекурсивно вызываем эту же функцию.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Чтобы установленные размеры и позиции были применены к виджетам до вызыва root.mainloop(), вызываем метод root.update()",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "В данном случае визуальная иерархия виджетов не такая глубокая - всего два элемента - окно (Tk) и кнопка (Button), соответственно консольный вывод будет следуюшим:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''Tk width=250 height=200  x=104 y=104\n   Button width=39 height=26  x=105 y=0'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_buttons_content(self):
        """Создание контента для темы 'Кнопки'"""
        colors = self.get_theme_colors()
        image_path1 = self.get_library_image_path("t7.png")
        image_path2 = self.get_library_image_path("t8.png")
        image_path3 = self.get_library_image_path("t9.png")
        
        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            button_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            button_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение кнопки tkinter", size=12, color=colors["text_secondary"]),
                    ft.Text("t7.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            button_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            button_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение обработки нажатия", size=12, color=colors["text_secondary"]),
                    ft.Text("t8.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 3
        if os.path.exists(image_path3):
            button_image3 = ft.Image(
                src=image_path3,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            button_image3 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение отключенной кнопки", size=12, color=colors["text_secondary"]),
                    ft.Text("t9.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Кнопки", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Одним из наиболее используемых компонентов в графических программах является кнопка. В tkinter кнопки представлены классом Button. Основные параметры виджета Button:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text("• command: функция, которая вызывается при нажатии на кнопку", size=14, color=colors["text_secondary"]),
                        ft.Text("• compund: устанавливает расположение картинки и текста относительно друг друга", size=14, color=colors["text_secondary"]),
                        ft.Text("• cursor: курсор указателя мыши при наведении на метку", size=14, color=colors["text_secondary"]),
                        ft.Text("• image: ссылка на изображение, которое отображается на метке", size=14, color=colors["text_secondary"]),
                        ft.Text("• pading: отступы от границ вилжета до его текста", size=14, color=colors["text_secondary"]),
                        ft.Text("• state: состояние кнопки", size=14, color=colors["text_secondary"]),
                        ft.Text("• text: устанавливает текст метки", size=14, color=colors["text_secondary"]),
                        ft.Text("• textvariable: устанавливает привязку к элементу StringVar", size=14, color=colors["text_secondary"]),
                        ft.Text("• underline: указывает на номер символа в тексте кнопки, который подчеркивается. По умолчанию значение -1, то есть никакой символ не подчеркивается", size=14, color=colors["text_secondary"]),
                        ft.Text("• width: ширина виджета", size=14, color=colors["text_secondary"]),
                        ft.Container(height=20),
                        
                        ft.Text("Добавим в окно обычную кнопку из пакета ttk:", size=14, color=colors["text_secondary"]),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\n# стандартная кнопка\nbtn = ttk.Button(text="Button")\nbtn.pack()\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Для создания кнопки используется конструктор Button(). В этом конструкторе с помощью параметра text можно установить текст кнопки.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Чтобы разместить виджет в контейнере (главном окне), у него вызывается метод pack(). На ОС Windows мы получим следующую кнопку:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 1
                        ft.Container(
                            content=button_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Кнопка в tkinter в Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Конструктор Button определяет различные параметры, которые позволяют настроить поведение и внешний вид кнопки. Однако конкретный набор параметров зависит от того, используем ли мы кнопки из пакета tkinter или из пакета tkinter.ttk.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Обработка нажатия на кнопку", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для обработки нажатия на кнопку необходимо установить в конструкторе параметр command, присвоив ему ссылку на функцию, которая будет срабатывать при нажатии:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n\nclicks = 0\n\ndef click_button():\n    global clicks\n    clicks += 1\n    # изменяем текст на кнопке\n    btn["text"] = f"Clicks {clicks}"   \n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x150")\n\nbtn = ttk.Button(text="Click Me", command=click_button)\nbtn.pack()\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь в качестве обработчика нажатия устанавливается функция click_button. В этой функции изменяется глобальная переменная clicks, которая хранит число кликов. Кроме того, изменяем текст кнопки, чтобы визуально было видно сколько нажатий произведено. Таким образом, при каждом нажатии кнопки будет срабатывать функция click_button, и количество кликов будет увеличиваться:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 2
                        ft.Container(
                            content=button_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Обработка нажатия кнопки в tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Отключение кнопки", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для ttk-кнопки мы можем установить отключенное состояние с помощью метода state(), передав ему значение 'disabled'. С такой кнопкой пользователь не сможет взаимодействовать:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nbtn = ttk.Button(text="Click Me", state=["disabled"])\nbtn.pack()\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "При этом в метод state мы можем передать набор состояний, поэтому значение 'disabled' передается внутри списка.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 3
                        ft.Container(
                            content=button_image3,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("отключение кнопки в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_pack_positioning_content(self):
        """Создание контента для темы 'Позиционирование. Pack'"""
        colors = self.get_theme_colors()
        image_path1 = self.get_library_image_path("t10.png")
        image_path2 = self.get_library_image_path("t11.png")
        image_path3 = self.get_library_image_path("t12.png")
        image_path4 = self.get_library_image_path("t13.png")
        image_path5 = self.get_library_image_path("t14.png")
        image_path6 = self.get_library_image_path("t15.png")
        image_path7 = self.get_library_image_path("t16.png")
        image_path8 = self.get_library_image_path("t17.png")
    
    # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            pack_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            pack_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение позиционирования", size=12, color=colors["text_secondary"]),
                    ft.Text("t10.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
        
    # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            pack_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            pack_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Схема anchor", size=12, color=colors["text_secondary"]),
                    ft.Text("t11.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
        
    # Проверяем существует ли изображение 3
        if os.path.exists(image_path3):
            pack_image3 = ft.Image(
                src=image_path3,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            pack_image3 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Позиционирование в углу", size=12, color=colors["text_secondary"]),
                    ft.Text("t12.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
        
    # Проверяем существует ли изображение 4
        if os.path.exists(image_path4):
            pack_image4 = ft.Image(
                src=image_path4,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            pack_image4 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Заполнение по горизонтали", size=12, color=colors["text_secondary"]),
                    ft.Text("t13.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
        
    # Проверяем существует ли изображение 5
        if os.path.exists(image_path5):
            pack_image5 = ft.Image(
                src=image_path5,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            pack_image5 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Внешние отступы", size=12, color=colors["text_secondary"]),
                    ft.Text("t14.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
        
    # Проверяем существует ли изображение 6
        if os.path.exists(image_path6):
            pack_image6 = ft.Image(
                src=image_path6,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            pack_image6 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Разные отступы", size=12, color=colors["text_secondary"]),
                    ft.Text("t15.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
        
    # Проверяем существует ли изображение 7
        if os.path.exists(image_path7):
            pack_image7 = ft.Image(
                src=image_path7,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            pack_image7 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Внутренние отступы", size=12, color=colors["text_secondary"]),
                    ft.Text("t16.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
        
        # Проверяем существует ли изображение 8
        if os.path.exists(image_path8):
            pack_image8 = ft.Image(
                src=image_path8,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            pack_image8 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Позиционирование по сторонам", size=12, color=colors["text_secondary"]),
                    ft.Text("t17.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Позиционирование. Pack", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Для позиционирования виджетов в контейнере применяются различные способы. Один из них представляет вызов у виджета метода pack(). Этот метод принимает следующие параметры:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text("• expand: если равно True, то виджет заполняет все пространство контейнера.", size=14, color=colors["text_secondary"]),
                        ft.Text("• fill: определяет, будет ли виджет растягиваться, чтобы заполнить свободное пространство вокруг. Этот параметр может принимать следующие значения: NONE (по умолчанию, элемент не растягивается), X (элемент растягивается только по горизонтали), Y (элемент растягивается только по вертикали) и BOTH (элемент растягивается по вертикали и горизонтали).", size=14, color=colors["text_secondary"]),
                        ft.Text("• anchor: помещает виджет в определенной части контейнера. Может принимать значения n, e, s, w, ne, nw, se, sw, c, которые являются сокращениями от Noth(север - вверх), South (юг - низ), East (восток - правая сторона), West (запад - левая сторона) и Center (по центру). Например, значение nw указывает на верхний левый угол", size=14, color=colors["text_secondary"]),
                        ft.Text("• side: выравнивает виджет по одной из сторон контейнера. Может принимать значения: TOP (по умолчанию, выравнивается по верхней стороне контейнера), BOTTOM (выравнивание по нижней стороне), LEFT (выравнивание по левой стороне), RIGHT (выравнивание по правой стороне).", size=14, color=colors["text_secondary"]),
                        ft.Text("• ipadx: устанавливает отступ содержимого виджета от его границы по горизонтали.", size=14, color=colors["text_secondary"]),
                        ft.Text("• ipady: устанавливают отступ содержимого виджета от его границы по вертикали.", size=14, color=colors["text_secondary"]),
                        ft.Text("• padx: устанавливает отступ виджета от границ контейнера по горизонтали.", size=14, color=colors["text_secondary"]),
                        ft.Text("• pady: устанавливает отступ виджета от границ контейнера по вертикали.", size=14, color=colors["text_secondary"]),
                        ft.Container(height=20),
                        
                        ft.Text("Растяжение виджета", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для растяжения виджета применяется параметру expand передается значение True (или соответствующее число). Причем при отсутствии других параметров позиционирования значение expand=True позволяет поместить виджет по центру:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('''from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nbtn = ttk.Button(text="Click me")\nbtn.pack(expand=True)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 1
                        ft.Container(
                            content=pack_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text(
                            "позиционирование виджета по центру в tkinter и python",
                            size=14,
                            color=colors["text_secondary"],
                            italic=True,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Anchor", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Параметр anchor помещает виджет в определенной части контейнера. Может принимать следующие значения:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text("• n: положение вверху по центру", size=14, color=colors["text_secondary"]),
                        ft.Text("• e: положение в правой части контейнера по центру", size=14, color=colors["text_secondary"]),
                        ft.Text("• s: положение внизу по центру", size=14, color=colors["text_secondary"]),
                        ft.Text("• w: положение в левой части контейнера по центру", size=14, color=colors["text_secondary"]),
                        ft.Text("• nw: положение в верхнем левом углу", size=14, color=colors["text_secondary"]),
                        ft.Text("• ne: положение в верхнем правом углу", size=14, color=colors["text_secondary"]),
                        ft.Text("• se: положение в нижнем правом углу", size=14, color=colors["text_secondary"]),
                        ft.Text("• sw: положение в нижнем левом углу", size=14, color=colors["text_secondary"]),
                        ft.Text("• center: положение центру", size=14, color=colors["text_secondary"]),
                        ft.Container(height=15),
                        
                        ft.Text("Схематически это выглядит следующим образом:", size=14, color=colors["text_secondary"]),
                        ft.Container(height=10),
                        
                        # Изображение 2
                        ft.Container(
                            content=pack_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text(
                            "позиционирование виджета в tkinter и python",
                            size=14,
                            color=colors["text_secondary"],
                            italic=True,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Стоит отметить, что значение в кавычках для параметра anchor передается в нижнем регистре, без кавычек - в верхнем регистре",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('''btn.pack(anchor="nw")\nbtn.pack(anchor=NW)'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Также стоит отметить, что для некоторых сценариев (например, помещение в нижней части контейнера) может потребоваться указать для параметра expand значение True. Например, поместим кнопку в верхнем левом углу:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('''from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nbtn = ttk.Button(text="Click me")\nbtn.pack(anchor="nw")\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 3
                        ft.Container(
                            content=pack_image3,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text(
                            "позиционирование виджета в контейнере в tkinter и python",
                            size=14,
                            color=colors["text_secondary"],
                            italic=True,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Заполнение контейнера", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Параметр fill позволяет заполнить пространство контейнер по горизонтали (значение X), по вертикали (значение Y) или по обеим сторонам (значение BOTH). По умолчанию значение NONE, при котором заполнение контейнера отсутствует. Например, заполним все пространство контейнера по горизонтали",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('''from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nbtn = ttk.Button(text="Click me")\nbtn.pack(fill=X)\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 4
                        ft.Container(
                            content=pack_image4,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text(
                            "Метод pack и fill в tkinter Python",
                            size=14,
                            color=colors["text_secondary"],
                            italic=True,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Для заполнения контейнера по всем сторонам также требуется установить параметр expand = True",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('btn.pack(fill=BOTH, expand=True)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Отступы", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Параметры padx и pady позволяют указать отступы виджета от границ контейнера:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('''from tkinter import *\nfrom tkinter import ttk\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nbtn = ttk.Button(text="Click me")\nbtn.pack(anchor="nw", padx=20, pady=30)\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь кнопка смещена относительно верхнего левого угла на 20 единиц вправо и на 30 единиц вниз",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 5
                        ft.Container(
                            content=pack_image5,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text(
                            "Метод pack и внешние отступы виджета в tkinter Python",
                            size=14,
                            color=colors["text_secondary"],
                            italic=True,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Выше устанавливался общий отступ от левой и правой стороны и общий отступ от верхней и нижней кромки контейнера. Поскольку кнопка позиционировалась в верхнем левом углу и имеела небольшие размеры, отступ от нижней и правой кромки контейнера нас не особо интересовали. Однако при желании мы можем задать отдельно два отступа от правой и левой границы и отдельно два отступа от верхней и нижней границ:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('''from tkinter import *\nfrom tkinter import ttk\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nbtn = ttk.Button(text="Click me")\nbtn.pack(fill=X, padx=[20, 60], pady=30)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае отступ слева - 20 единиц, а справа - 60 единиц",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 6
                        ft.Container(
                            content=pack_image6,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text(
                            " внешние отступы виджета в tkinter Python",
                            size=14,
                            color=colors["text_secondary"],
                            italic=True,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Параметры ipadx и ipady позволяют указать отступы содержимого виджета от границ виджета по горизонтали и вертикали соответственно:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('''from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nbtn = ttk.Button(text="Click me")\nbtn.pack(expand=True, ipadx=10, ipady=10)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 7
                        ft.Container(
                            content=pack_image7,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text(
                            " внутренние отступы виджета в tkinter Python",
                            size=14,
                            color=colors["text_secondary"],
                            italic=True,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Позиционирование по стороне", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Используем параметр side:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('''from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nbtn1 = ttk.Button(text="BOTTOM")\nbtn1.pack(side=BOTTOM)\n\nbtn2 = ttk.Button(text="RIGHT")\nbtn2.pack(side=RIGHT)\n\nbtn3 = ttk.Button(text="LEFT")\nbtn3.pack(side=LEFT)\n\nbtn4 = ttk.Button(text="TOP")\nbtn4.pack(side=TOP)\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 8
                        ft.Container(
                            content=pack_image8,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text(
                            "Параметр side в методе pack в Python",
                            size=14,
                            color=colors["text_secondary"],
                            italic=True,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Комбинируя параметры side и fill, можно растянуть элемент по вертикали:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('''btn1 = ttk.Button(text="CLICK ME")\nbtn1.pack(side=LEFT, fill=Y)'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_place_positioning_content(self):
        """Создание контента для темы 'Позиционирование. Place'"""
        image_path1 = self.get_library_image_path("t18.png")
        image_path2 = self.get_library_image_path("t19.png")
        image_path3 = self.get_library_image_path("t20.png")
        image_path4 = self.get_library_image_path("t21.png")
        image_path5 = self.get_library_image_path("t22.png")
        image_path6 = self.get_library_image_path("t23.png")
        colors = self.get_theme_colors()
        
        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            place_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            place_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Абсолютные координаты", size=12, color=colors["text_secondary"]),
                    ft.Text("t18.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            place_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            place_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Относительные координаты", size=12, color=colors["text_secondary"]),
                    ft.Text("t19.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 3
        if os.path.exists(image_path3):
            place_image3 = ft.Image(
                src=image_path3,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            place_image3 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Схема anchor", size=12, color=colors["text_secondary"]),
                    ft.Text("t20.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 4
        if os.path.exists(image_path4):
            place_image4 = ft.Image(
                src=image_path4,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            place_image4 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Позиционирование по центру", size=12, color=colors["text_secondary"]),
                    ft.Text("t21.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 5
        if os.path.exists(image_path5):
            place_image5 = ft.Image(
                src=image_path5,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            place_image5 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Размеры виджета", size=12, color=colors["text_secondary"]),
                    ft.Text("t22.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 6
        if os.path.exists(image_path6):
            place_image6 = ft.Image(
                src=image_path6,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            place_image6 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Относительные размеры", size=12, color=colors["text_secondary"]),
                    ft.Text("t23.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Позиционирование. Place", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Метод place() позволяет более точно настроить координаты и размеры виджета. Он принимает следующие параметры:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text("• height и width: устанавливают соответственно высоту и ширину элемента в пикселях", size=14, color=colors["text_secondary"]),
                        ft.Text("• relheight и relwidth: также задают соответственно высоту и ширину элемента, но в качестве значения используется число float в промежутке между 0.0 и 1.0, которое указывает на долю от высоты и ширины родительского контейнера", size=14, color=colors["text_secondary"]),
                        ft.Text("• x и y: устанавливают смещение элемента по горизонтали и вертикали в пикселях соответственно относительно верхнего левого угла контейнера", size=14, color=colors["text_secondary"]),
                        ft.Text("• relx и rely: также задают смещение элемента по горизонтали и вертикали, но в качестве значения используется число float в промежутке между 0.0 и 1.0, которое указывает на долю от высоты и ширины родительского контейнера", size=14, color=colors["text_secondary"]),
                        ft.Text("• bordermode: задает формат границы элемента. Может принимать значение INSIDE (по умолчанию) и OUTSIDE", size=14, color=colors["text_secondary"]),
                        ft.Text("• anchor: устанавливает опции растяжения элемента. Может принимать значения n, e, s, w, ne, nw, se, sw, c, которые являются сокращениями от North(север - вверх), South (юг - низ), East (восток - правая сторона), West (запад - левая сторона) и Center (по центру). Например, значение nw указывает на верхний левый угол", size=14, color=colors["text_secondary"]),
                        ft.Container(height=20),
                        
                        ft.Text("Установка расположения", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Параметры x и y позволяют задать точные параметры расположения относительно верхнего левого угла контейнера:",
                            size=14, color=colors["text_secondary"]),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nbtn = ttk.Button(text="Click me")\nbtn.place(x=20, y=30)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае кнопка относительно верхнего левого угла контейнера спещена на 20 единиц по оси X и на 30 единиц по оси Y:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 1
                        ft.Container(
                            content=place_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("установка расположения виджета с помощью метода place в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text(
                            "Параметры relx и rely также позволяют сместить виджет, но в качестве значения используется число float в промежутке между 0.0 и 1.0, которое указывает на долю от высоты и ширины родительского контейнера:",
                            size=14, color=colors["text_secondary"]),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nbtn = ttk.Button(text="Click me")\nbtn.place(relx=0.4, rely=0.25)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае кнопка смещена относительно верхнего левого угла контейнера на 40% ширины контейнера по оси Х и на 25% высоты контейнера по оси Y.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 2
                        ft.Container(
                            content=place_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("установка относительных координат виджета с помощью метода place в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Anchor", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Параметр anchor помещает виджет в определенной части контейнера. Может принимать следующие значения:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text("• n: положение вверху по центру", size=14, color=colors["text_secondary"]),
                        ft.Text("• e: положение в правой части контейнера по центру", size=14, color=colors["text_secondary"]),
                        ft.Text("• s: положение внизу по центру", size=14, color=colors["text_secondary"]),
                        ft.Text("• w: положение в левой части контейнера по центру", size=14, color=colors["text_secondary"]),
                        ft.Text("• nw: положение в верхнем левом углу", size=14, color=colors["text_secondary"]),
                        ft.Text("• ne: положение в верхнем правом углу", size=14, color=colors["text_secondary"]),
                        ft.Text("• se: положение в нижнем правом углу", size=14, color=colors["text_secondary"]),
                        ft.Text("• sw: положение в нижнем левом углу", size=14, color=colors["text_secondary"]),
                        ft.Text("• center: положение центру", size=14, color=colors["text_secondary"]),
                        ft.Container(height=15),
                        
                        ft.Text("Схематически это выглядит следующим образом:", size=14, color=colors["text_secondary"]),
                        ft.Container(height=10),
                        
                        # Изображение 3
                        ft.Container(
                            content=place_image3,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("позиционирование виджета в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Стоит отметить, что значение в кавычках для параметра anchor передается в нижнем регистре, без кавычек - в верхнем регистре",
                            size=14, color=colors["text_secondary"]),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('btn.pack(anchor=NW)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Например, разместим кнопку в центре окна:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nbtn = ttk.Button(text="Click me")\nbtn.place(relx=.5, rely=.5, anchor="c")\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "При этом все равно устанавливаются относительные координаты, которые примерно соответствуют центру окна, однако сам виджет все позиционируется по центру",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 4
                        ft.Container(
                            content=place_image4,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Позиционирование элементов  с помощью place в tkinter в Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Размеры", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Параметры height и width устанавливают соответственно высоту и ширину элемента в пикселях:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nbtn = ttk.Button(text="Click me")\nbtn.place(relx=0.5, rely=0.5, anchor="c", width=80, height=40)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь кнопка имеет ширину в 80 единиц и высоту в 40 единиц.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 5
                        ft.Container(
                            content=place_image5,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("установка размеров виджета с помощью метода place в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text(
                            "Параметры relheight и relwidth также задают соответственно высоту и ширину элемента, но в качестве значения используется число float в промежутке между 0.0 и 1.0, которое указывает на долю от высоты и ширины родительского контейнера:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nbtn = ttk.Button(text="Click me")\nbtn.place(relx=0.5, rely=0.5, anchor="c", relwidth=0.33, relheight=0.25)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь ширина кнопки составляет треть ширины контейнера, а высота кнопки - четверть высоты контейнера. И по мере изменения размеров контейнера размеры кнопки тоже будут изменяться.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 6
                        ft.Container(
                            content=place_image6,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("установка относительных размеров виджета с помощью метода place в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_grid_positioning_content(self):
        """Создание контента для темы 'Позиционирование. Grid'"""
        image_path1 = self.get_library_image_path("t24.png")
        image_path2 = self.get_library_image_path("t25.png")
        image_path3 = self.get_library_image_path("t26.png")
        image_path4 = self.get_library_image_path("t27.png")
        image_path5 = self.get_library_image_path("t28.png")
        image_path6 = self.get_library_image_path("t29.png")
        image_path7 = self.get_library_image_path("t30.png")
        image_path8 = self.get_library_image_path("t31.png")
        colors = self.get_theme_colors()
        
        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            grid_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            grid_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Базовый grid", size=12, color=colors["text_secondary"]),
                    ft.Text("t24.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            grid_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            grid_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Настроенный grid", size=12, color=colors["text_secondary"]),
                    ft.Text("t25.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 3
        if os.path.exists(image_path3):
            grid_image3 = ft.Image(
                src=image_path3,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            grid_image3 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Отступы в grid", size=12, color=colors["text_secondary"]),
                    ft.Text("t26.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 4
        if os.path.exists(image_path4):
            grid_image4 = ft.Image(
                src=image_path4,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            grid_image4 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Columnspan", size=12, color=colors["text_secondary"]),
                    ft.Text("t27.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 5
        if os.path.exists(image_path5):
            grid_image5 = ft.Image(
                src=image_path5,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            grid_image5 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Rowspan", size=12, color=colors["text_secondary"]),
                    ft.Text("t28.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 6
        if os.path.exists(image_path6):
            grid_image6 = ft.Image(
                src=image_path6,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            grid_image6 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Выравнивание sticky", size=12, color=colors["text_secondary"]),
                    ft.Text("t29.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 7
        if os.path.exists(image_path7):
            grid_image7 = ft.Image(
                src=image_path7,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            grid_image7 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Растяжение виджета", size=12, color=colors["text_secondary"]),
                    ft.Text("t30.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 8
        if os.path.exists(image_path8):
            grid_image8 = ft.Image(
                src=image_path8,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            grid_image8 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Выравнивание NSEW", size=12, color=colors["text_secondary"]),
                    ft.Text("t31.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Позиционирование. Grid", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Метод grid() позволяет поместить виджет в определенную ячейку условной сетки или грида.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text("Метод grid применяет следующие параметры:", size=14, color=colors["text_secondary"]),
                        ft.Container(height=10),
                        
                        ft.Text("• column: номер столбца, отсчет начинается с нуля", size=14, color=colors["text_secondary"]),
                        ft.Text("• row: номер строки, отсчет начинается с нуля", size=14, color=colors["text_secondary"]),
                        ft.Text("• columnspan: сколько столбцов должен занимать элемент", size=14, color=colors["text_secondary"]),
                        ft.Text("• rowspan: сколько строк должен занимать элемент", size=14, color=colors["text_secondary"]),
                        ft.Text("• ipadx и ipady: отступы по горизонтали и вертикали соответственно от границ элемента до его содержимого", size=14, color=colors["text_secondary"]),
                        ft.Text("• padx и pady: отступы по горизонтали и вертикали соответственно от границ ячейки грида до границ элемента", size=14, color=colors["text_secondary"]),
                        ft.Text("• sticky: выравнивание элемента в ячейке, если ячейка больше элемента. Может принимать значения n, e, s, w, ne, nw, se, sw, которые указывают соответствующее направление выравнивания", size=14, color=colors["text_secondary"]),
                        ft.Container(height=20),
                        
                        ft.Text("Установка ячейки виджета", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Например, определим грид из 9 кнопок:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nfor r in range(3):\n    for c in range(3):\n        btn = ttk.Button(text=f"({r},{c})")\n        btn.grid(row=r, column=c)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь в цикле создается девять кнопок, каждая из которых помещается в свою ячейку. В итоге у нас получится следующий грид",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 1
                        ft.Container(
                            content=grid_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Grid в tkinter в Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "По умолчанию для каждой ячейки выделяется столько места, сколько необходимо для виджета в ней. Соответственно мы получаем небольшую таблицу и много пустого места вне грида, что, возможно, смотрится не лучшим образом. И ситуация усугубляется, если мы попробуем растянуть окно - появится еще больше пустого пространства. Чтоюбы решить эту проблему, надо сконфигурировать грид у контейнера.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Конфигурация грида", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для конфигурации грида в контейнере применяются два метода:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('container.columnconfigure(index, weight)\ncontainer.rowconfigure(index, weight)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Метод columnconfigure() настраивает столбец. В качестве параметра index метод получает индекс столбца, а через параметр weight устанавливает его вес. Столбцы распределяются по всей ширине контейнера в соответствии со своим весом.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Метод rowconfigure() настраивает строку аналогичным образом. В качестве параметра index метод получает индекс строки, а через параметр weight устанавливает ее вес. Строки распределяются по всей длине контейнера в соответствии со своим весом.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Например, изменим код выше, добавив конфигурацию строк и столбцов:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nfor c in range(3): root.columnconfigure(index=c, weight=1)\nfor r in range(3): root.rowconfigure(index=r, weight=1)\n\nfor r in range(3):\n    for c in range(3):\n        btn = ttk.Button(text=f"({r},{c})")\n        btn.grid(row=r, column=c)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Поскольку у нас три строки, для упрощения в цикле для каждой строки устанавливаем вес 1. То есть в итоге каждая из трех строк будет занимать треть высоты контейнера (пространство_контейнера / сумму всех весов строк).",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Аналогично в цикле для каждого столбца устанавливаем вес 1. То есть в итоге каждый из трех столбец будет занимать треть ширины контейнера.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 2
                        ft.Container(
                            content=grid_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Настройка столбцов и строк в гриде в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Отступы", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Параметры padx и pady повзвозяют установить отступы по горизонтали и вертикали соответственно от границ ячейки грида до границ виджета, а ipadx и ipady - отступы по горизонтали и вертикали соответственно от границ виджета до его содержимого",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nfor c in range(3): root.columnconfigure(index=c, weight=1)\nfor r in range(3): root.rowconfigure(index=r, weight=1)\n\nfor r in range(3):\n    for c in range(3):\n        btn = ttk.Button(text=f"({r},{c})")\n        btn.grid(row=r, column=c, ipadx=6, ipady=6, padx=4, pady=4)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае внешние отсуты равны 4 единиц, а внутренние - 6 единицам.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 3
                        ft.Container(
                            content=grid_image3,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Отступы в гриде в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Для параметров padx и pady можно установить отступы с двух сторон в виде списка:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('btn.grid(row=r, column=c, ipadx=6, ipady=6, padx=[15, 4], pady=4)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь внешний отступ слева равен 10, а справа - 4 единицам.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Объединение ячеек", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Параметр columnspan указывает, столько столбцов, а параметр rowspan сколько строк должен занимать виджет. То есть с помощью подобных параметров мы можем объединить ячейки.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text("Растяжение на два столбца:", size=14, color=colors["text_secondary"]),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nfor c in range(2): root.columnconfigure(index=c, weight=1)\nfor r in range(2): root.rowconfigure(index=r, weight=1)\n\nbtn1 = ttk.Button(text="button 1")\n# columnspan=2 - растягиваем на два столбца\nbtn1.grid(row=0, column=0, columnspan=2, ipadx=70, ipady=6, padx=5, pady=5)\n\nbtn3 = ttk.Button(text="button 3")\nbtn3.grid(row=1, column=0, ipadx=6, ipady=6, padx=5, pady=5)\n\nbtn4 = ttk.Button(text="button 4")\nbtn4.grid(row=1, column=1, ipadx=6,  ipady=6, padx=5, pady=5)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 4
                        ft.Container(
                            content=grid_image4,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("columnspan в grid в Tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Растяжение на две строки:", size=14, color=colors["text_secondary"]),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nfor c in range(2): root.columnconfigure(index=c, weight=1)\nfor r in range(2): root.rowconfigure(index=r, weight=1)\n\nbtn2 = ttk.Button(text="button 2")\n# rowspan=2 - растягиваем на две строки\nbtn2.grid(row=0, column=1, rowspan=2, ipadx=6, ipady=55, padx=5, pady=5)\n\nbtn1 = ttk.Button(text="button 1")\nbtn1.grid(row=0, column=0, ipadx=6, ipady=6, padx=5, pady=5)\n\nbtn3 = ttk.Button(text="button 3")\nbtn3.grid(row=1, column=0, ipadx=6,  ipady=6, padx=5, pady=5)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 5
                        ft.Container(
                            content=grid_image5,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("rowspan в grid в Tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Выравнивание", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Параметр sticky задает выравнивание виджета в ячейке, если размер ячейки больше размера этого виджета. Этот параметр может принимать следующие значения:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text("• n: положение вверху по центру", size=14, color=colors["text_secondary"]),
                        ft.Text("• e: положение в правой части контейнера по центру", size=14, color=colors["text_secondary"]),
                        ft.Text("• s: положение внизу по центру", size=14, color=colors["text_secondary"]),
                        ft.Text("• w: положение в левой части контейнера по центру", size=14, color=colors["text_secondary"]),
                        ft.Text("• nw: положение в верхнем левом углу", size=14, color=colors["text_secondary"]),
                        ft.Text("• ne: положение в верхнем правом углу", size=14, color=colors["text_secondary"]),
                        ft.Text("• se: положение в нижнем правом углу", size=14, color=colors["text_secondary"]),
                        ft.Text("• sw: положение в нижнем левом углу", size=14, color=colors["text_secondary"]),
                        ft.Text("• ns: растяжение по вертикали", size=14, color=colors["text_secondary"]),
                        ft.Text("• ew: растяжение по горизонтали", size=14, color=colors["text_secondary"]),
                        ft.Text("• nsew: растяжение по горизонтали и вертикали", size=14, color=colors["text_secondary"]),
                        ft.Container(height=15),
                        
                        ft.Text("По умолчанию виджет позиционируется по центру ячейки", size=14, color=colors["text_secondary"]),
                        ft.Container(height=10),
                        
                        # Изображение 6
                        ft.Container(
                            content=grid_image6,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("sticky и выравнивание в grid в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text("Наглядно растяжение по вертикали и горизонтали", size=14, color=colors["text_secondary"]),
                        ft.Container(height=10),
                        
                        # Изображение 7
                        ft.Container(
                            content=grid_image7,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("sticky и растяжение виджета в grid в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Стоит отметить, что значение в кавычках для параметра anchor передается в нижнем регистре, без кавычек - в верхнем регистре",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('sticky=NW\nsticky="nw"'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Например, растянем виджет по всему пространству ячейки (значение NSEW):",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nfor c in range(3): root.columnconfigure(index=c, weight=1)\nfor r in range(3): root.rowconfigure(index=r, weight=1)\n\nfor r in range(3):\n    for c in range(3):\n        btn = ttk.Button(text=f"({r},{c})")\n        btn.grid(row=r, column=c, ipadx=6, ipady=6, padx=4, pady=4, sticky=NSEW)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 8
                        ft.Container(
                            content=grid_image8,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("sticky и выравнивание виджета в grid в приложении на tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_events_content(self):
        """Создание контента для темы 'Обработка событий'"""
        image_path1 = self.get_library_image_path("t32.png")
        colors = self.get_theme_colors()
        
        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            events_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            events_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Привязка событий", size=12, color=colors["text_secondary"]),
                    ft.Text("t32.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Обработка событий", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Tkinter позволяет обрабатывать события виджетов. Для обработки распространенных и наболее используемых событий Tkinter предоставляет интерфейс команд. Например, для обработки нажатия на кнопку ее параметру command надо передать функцию, которая будет вызываться при нажатии на кнопку",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('def click(): \n    print("Hello")\n \nbtn = ttk.Button(text="Click", command=click)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Ряд виджетов также позволяют с помощью параметра command задать обработчик для одного из событий данного виджета.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Однако что, если мы хотим обрабатывать другие события виджета. Например, для кнопки обработать получение фокуса, или обработать нажатие клавиши клавиатуры? Для подобных ситуаций Tkinter предоставляет ряд встроенных событий. Наиболее распространенные из них:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text("• Activate: окно становится активным.", size=14, color=colors["text_secondary"]),
                        ft.Text("• Deactivate: окно становится неактивным.", size=14, color=colors["text_secondary"]),
                        ft.Text("• MouseWheel: прокрутка колеса мыши.", size=14, color=colors["text_secondary"]),
                        ft.Text("• KeyPress: нажатие клавиши на клавиатуре.", size=14, color=colors["text_secondary"]),
                        ft.Text("• KeyRelease: освобождение нажатой клавиши", size=14, color=colors["text_secondary"]),
                        ft.Text("• ButtonPress: нажатие кнопки мыши.", size=14, color=colors["text_secondary"]),
                        ft.Text("• ButtonRelease: освобождение кнопки мыши.", size=14, color=colors["text_secondary"]),
                        ft.Text("• Motion: движение мыши.", size=14, color=colors["text_secondary"]),
                        ft.Text("• Configure: изменение размера и положения виджета", size=14, color=colors["text_secondary"]),
                        ft.Text("• Destroy: удаление виджета", size=14, color=colors["text_secondary"]),
                        ft.Text("• FocusIn: получение фокуса", size=14, color=colors["text_secondary"]),
                        ft.Text("• FocusOut: потеря фокуса.", size=14, color=colors["text_secondary"]),
                        ft.Text("• Enter: указатель мыши вошел в пределы виджета.", size=14, color=colors["text_secondary"]),
                        ft.Text("• Leave: указатель мыши покинул виджет.", size=14, color=colors["text_secondary"]),
                        ft.Container(height=20),
                        
                        ft.Text("Привязка событий", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для привязки события к виджету применяется метод bind():",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('bind(событие, функция)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В качестве первого параметра указывается обрабатываемое событие, а в качестве второго - функция, которая обрабатывает событие.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Например, обработаем события получения и потери фокуса для кнопки:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n \n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n \ndef entered(event): \n    btn["text"] ="Entered"\n \ndef left(event): \n    btn["text"] ="Left"\n \nbtn = ttk.Button(text="Click")\nbtn.pack(anchor=CENTER, expand=1)\n \nbtn.bind("<Enter>", entered)\nbtn.bind("<Leave>", left)\n \nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Название событие передается в угловных скобках, например, \"<Enter>\" или \"<Leave>\". Для события Enter (получение фокуса) определен обработчик-функция entered, которая изменяет текст кнопки:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('def entered(event): \n    btn["text"] ="Entered"'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Стоит обратить внимание, что функция обработки события должна принимать в качестве параметра объект события - в примере выше параметр event, даже если он в самой функции не используется.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Событие потери фокуса связывывается с функцией left:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('btn.bind("<Leave>", left)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 1
                        ft.Container(
                            content=events_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Привязка событий в виджетах к функциям в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Кроме обычных событий некоторые виджеты Tkinter могут использовать виртуальные события или высокоуровневые события (выше были описаны низкоуровневые события), которые помещаются в двойные угловые скобки, например, событие выделения списка \"<<ListboxSelect>>\". Наиболее используемые виртуальные события будут рассмотрены в соответствующих темах про виджеты.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Шаблон события", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "В примере выше при привязке события указывалось только имя события например, \"<Enter>\" или \"<Leave>\". Но в реальности в угловных скобках указывается не просто имя события, а его шаблон. Шаблон события имеет следующую форму:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('<модификатор-имя_события-клавиша>'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Модификаторы события", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text("Часто используемые модификаторы:", size=14, color=colors["text_secondary"]),
                        ft.Container(height=10),
                        
                        ft.Text("• Alt: нажата клавиша Alt", size=14, color=colors["text_secondary"]),
                        ft.Text("• Control: нажата клавиша Ctrl", size=14, color=colors["text_secondary"]),
                        ft.Text("• Shift: нажата клавиша Shift", size=14, color=colors["text_secondary"]),
                        ft.Text("• Any: нажата любая клавиша", size=14, color=colors["text_secondary"]),
                        ft.Container(height=20),
                        
                        ft.Text("Клавиши", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text("Также в шаблоне можно указать конкретные клавиши или комбинации. Некоторые из них:", size=14, color=colors["text_secondary"]),
                        ft.Container(height=10),
                        
                        ft.Text("• Alt_L: левая клавиша alt", size=14, color=colors["text_secondary"]),
                        ft.Text("• Alt_R: правая клавиша alt", size=14, color=colors["text_secondary"]),
                        ft.Text("• BackSpace: клавиша backspace", size=14, color=colors["text_secondary"]),
                        ft.Text("• Cancel: клавиша break", size=14, color=colors["text_secondary"]),
                        ft.Text("• Caps_Lock: клавиша CapsLock", size=14, color=colors["text_secondary"]),
                        ft.Text("• Control_L: левая клавиша control", size=14, color=colors["text_secondary"]),
                        ft.Text("• Control_R: правая клавиша control", size=14, color=colors["text_secondary"]),
                        ft.Text("• Delete: клавиша Delete", size=14, color=colors["text_secondary"]),
                        ft.Text("• Down: клавиша ↓", size=14, color=colors["text_secondary"]),
                        ft.Text("• End: клавиша end", size=14, color=colors["text_secondary"]),
                        ft.Text("• Escape: клавиша esc", size=14, color=colors["text_secondary"]),
                        ft.Text("• Execute: клавиша SysReq", size=14, color=colors["text_secondary"]),
                        ft.Text("• F1: клавиша F1", size=14, color=colors["text_secondary"]),
                        ft.Text("• F2: клавиша F2", size=14, color=colors["text_secondary"]),
                        ft.Text("• Fi: функциональная клавиша Fi", size=14, color=colors["text_secondary"]),
                        ft.Text("• F12: клавиша F12", size=14, color=colors["text_secondary"]),
                        ft.Text("• Home: клавиша home", size=14, color=colors["text_secondary"]),
                        ft.Text("• Insert: клавиша insert", size=14, color=colors["text_secondary"]),
                        ft.Text("• Left: клавиша ←", size=14, color=colors["text_secondary"]),
                        ft.Text("• Linefeed: клавиша Linefeed (control-J)", size=14, color=colors["text_secondary"]),
                        ft.Text("• KP_0: клавиша 0", size=14, color=colors["text_secondary"]),
                        ft.Text("• KP_1: клавиша 1", size=14, color=colors["text_secondary"]),
                        ft.Text("• KP_2: клавиша 2", size=14, color=colors["text_secondary"]),
                        ft.Text("• KP_3: клавиша 3", size=14, color=colors["text_secondary"]),
                        ft.Text("• KP_4: клавиша 4", size=14, color=colors["text_secondary"]),
                        ft.Text("• KP_5: клавиша 5", size=14, color=colors["text_secondary"]),
                        ft.Text("• KP_6: клавиша 6", size=14, color=colors["text_secondary"]),
                        ft.Text("• KP_7: клавиша 7", size=14, color=colors["text_secondary"]),
                        ft.Text("• KP_8: клавиша 8", size=14, color=colors["text_secondary"]),
                        ft.Text("• KP_9: клавиша 9", size=14, color=colors["text_secondary"]),
                        ft.Text("• KP_Add: клавиша +", size=14, color=colors["text_secondary"]),
                        ft.Text("• KP_Begin: центральная клавиша (5)", size=14, color=colors["text_secondary"]),
                        ft.Text("• KP_Decimal: клавиша точка (.)", size=14, color=colors["text_secondary"]),
                        ft.Text("• KP_Delete: клавиша delete", size=14, color=colors["text_secondary"]),
                        ft.Text("• KP_Divide: клавиша /", size=14, color=colors["text_secondary"]),
                        ft.Text("• KP_Down: клавиша ↓", size=14, color=colors["text_secondary"]),
                        ft.Text("• KP_End: клавиша end", size=14, color=colors["text_secondary"]),
                        ft.Text("• KP_Enter: клавиша enter", size=14, color=colors["text_secondary"]),
                        ft.Text("• KP_Home: клавиша home", size=14, color=colors["text_secondary"]),
                        ft.Text("• KP_Insert: клавиша insert", size=14, color=colors["text_secondary"]),
                        ft.Text("• KP_Left: клавиша ←", size=14, color=colors["text_secondary"]),
                        ft.Text("• KP_Multiply: клавиша ×", size=14, color=colors["text_secondary"]),
                        ft.Text("• KP_Next: клавиша PageDown", size=14, color=colors["text_secondary"]),
                        ft.Text("• KP_Prior: клавиша PageUp", size=14, color=colors["text_secondary"]),
                        ft.Text("• KP_Right: клавиша →", size=14, color=colors["text_secondary"]),
                        ft.Text("• KP_Subtract: клавиша -", size=14, color=colors["text_secondary"]),
                        ft.Text("• KP_Up: клавиша ↑", size=14, color=colors["text_secondary"]),
                        ft.Text("• Next: клавиша PageDown", size=14, color=colors["text_secondary"]),
                        ft.Text("• Num_Lock: клавиша NumLock", size=14, color=colors["text_secondary"]),
                        ft.Text("• Pause: клавиша pause", size=14, color=colors["text_secondary"]),
                        ft.Text("• Print: клавиша PrintScrn", size=14, color=colors["text_secondary"]),
                        ft.Text("• Prior: клавиша PageUp", size=14, color=colors["text_secondary"]),
                        ft.Text("• Return: клавиша Enter", size=14, color=colors["text_secondary"]),
                        ft.Text("• Right: клавиша →", size=14, color=colors["text_secondary"]),
                        ft.Text("• Scroll_Lock: клавиша ScrollLock", size=14, color=colors["text_secondary"]),
                        ft.Text("• Shift_L: левая клавиша shift", size=14, color=colors["text_secondary"]),
                        ft.Text("• Shift_R: правая клавиша shift", size=14, color=colors["text_secondary"]),
                        ft.Text("• Tab: клавиша tab", size=14, color=colors["text_secondary"]),
                        ft.Container(height=15),
                        
                        ft.Text("Например", size=14, color=colors["text_secondary"]),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n \ndef single_click(event): \n    btn["text"] ="Single Click"\n \ndef double_click(event): \n    btn["text"] ="Double Click"\n \nbtn = ttk.Button(text="Click")\nbtn.pack(anchor=CENTER, expand=1)\n \nbtn.bind("<ButtonPress-1>", single_click)\nbtn.bind("<Double-ButtonPress-1>", double_click)\n \nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь в шаблоне \"<ButtonPress-1>\" ButtonPress - название события - нажатие кнопки мыши, а \"1\" указывает на конкретную кнопку - левую кнопку мыши (например, 3 - представляет правую кнопку)",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "А в шаблоне \"<Double-ButtonPress-1>\" добавляется модификатор Doubles, который указывает на двойное нажатие.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Глобальная регистрация события", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "В примерах выше обработка события устанавливалась для одного конкретного объекта - для одной кнопки. Но что, если у нас много кнопок и мы хотим, чтобы для всех была установлена привязка одного и тоже события с одной и той же функцией_обработчиком? В этом случае мы можем установить привязку события глобально ко всем объектам класса с помощью метода bind_class класса Tk:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n \nclicks = 0\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n \ndef clicked(event): \n    global clicks\n    clicks = clicks + 1\n    btn["text"] =f"{clicks} Clicks"\n \nbtn = ttk.Button(text="Click")\nbtn.pack(anchor=CENTER, expand=1)\n \n# привязка события к кнопкам ttk.Button\nroot.bind_class("TButton", "<Double-ButtonPress-1>", clicked)\n \nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае для кнопок для обработки двойного нажатия установаливается обработчик - функция clicked. Причем события привязывается к кнопкам из пакета tkinter.ttk, поэтому в качестве типа виджетов используется \"TButton\" (а не просто Button).",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Удаление события", size=18, weight=ft.FontWeight.BOLD,color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для открепления события от виджета вызывается метод unbind(), в который передается шаблон события:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('widget.unbind(event)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_label_content(self):
        """Создание контента для темы 'Текстовая метка Label'"""
        image_path1 = self.get_library_image_path("t33.png")
        image_path2 = self.get_library_image_path("t34.png")
        image_path3 = self.get_library_image_path("t35.png")
        image_path4 = self.get_library_image_path("t36.png")
        image_path5 = self.get_library_image_path("t37.png")
        colors = self.get_theme_colors()
        
        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            label_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            label_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Базовый Label", size=12, color=colors["text_secondary"]),
                    ft.Text("t33.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            label_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            label_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Шрифт Label", size=12, color=colors["text_secondary"]),
                    ft.Text("t34.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 3
        if os.path.exists(image_path3):
            label_image3 = ft.Image(
                src=image_path3,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            label_image3 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение в Label", size=12, color=colors["text_secondary"]),
                    ft.Text("t35.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 4
        if os.path.exists(image_path4):
            label_image4 = ft.Image(
                src=image_path4,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            label_image4 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Текст с изображением", size=12, color=colors["text_secondary"]),
                    ft.Text("t36.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 5
        if os.path.exists(image_path5):
            label_image5 = ft.Image(
                src=image_path5,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            label_image5 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Стилизация Label", size=12, color=colors["text_secondary"]),
                    ft.Text("t37.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Текстовая метка Label", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Виджет Label представляет текстовую метку. Этот элемент позволяет выводить статический текст без возможности редактирования.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Для создания элемента Label применяется конструктор, который принимает два параметра:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('Label(master, options)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Параметр master представляет ссылку на родительский контейнер, а параметр options представляет следующие именованные параметры",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text("• anchor: устанавливает позиционирование текста", size=14, color=colors["text_secondary"]),
                        ft.Text("• background: фоновый цвет", size=14, color=colors["text_secondary"]),
                        ft.Text("• borderwidth: толщина границы метки", size=14, color=colors["text_secondary"]),
                        ft.Text("• cursor: курсор указателя мыши при наведении на метку", size=14, color=colors["text_secondary"]),
                        ft.Text("• font: шрифт текста", size=14, color=colors["text_secondary"]),
                        ft.Text("• foreground: цвет текста", size=14, color=colors["text_secondary"]),
                        ft.Text("• height: высота виджета", size=14, color=colors["text_secondary"]),
                        ft.Text("• image: ссылка на изображение, которое отображается на метке", size=14, color=colors["text_secondary"]),
                        ft.Text("• justify: устанавливает выравнивание текста. Значение LEFT выравнивает текст по левому краю, CENTER - по центру, RIGHT - по правому краю", size=14, color=colors["text_secondary"]),
                        ft.Text("• pading: отступы от границ вилжета до его текста", size=14, color=colors["text_secondary"]),
                        ft.Text("• relief: определяет тип границы, по умолчанию значение FLAT", size=14, color=colors["text_secondary"]),
                        ft.Text("• text: устанавливает текст метки", size=14, color=colors["text_secondary"]),
                        ft.Text("• textvariable: устанавливает привязку к элементу StringVar", size=14, color=colors["text_secondary"]),
                        ft.Text("• underline: указывает на номер символа в тексте метки, который подчеркивается. По умолчанию значение -1, то есть никакой символ не подчеркивается", size=14, color=colors["text_secondary"]),
                        ft.Text("• width: ширина виджета", size=14, color=colors["text_secondary"]),
                        ft.Text("• wraplength: при положительном значении строки текста будут переносится для вмещения в пространство виджета", size=14, color=colors["text_secondary"]),
                        ft.Container(height=20),
                        
                        ft.Text(
                            "Выведем в окне приложения простейший текст:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nlabel = ttk.Label(text="Hello METANIT.COM")\nlabel.pack()\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 1
                        ft.Container(
                            content=label_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Label в tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Установка шрифта", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Параметр font принимает определение шрифта в виде:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('font = ("имя шрифта", размер_шрифта)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Первое значение передает имя шрифта в кавычках, а второе - числовой размер шрифта. Например, установим шрифт Arial высотой в 14 единиц:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nlabel = ttk.Label(text="Hello METANIT.COM", font=("Arial", 14))\nlabel.pack()\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 2
                        ft.Container(
                            content=label_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Шрифт текста в Label в tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Установка изображения", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "За установку изображения на метке отвечает параметр image. Самый простой способ определения изображения представляет создание объекта PhotoImage, в конструктор которого передается путь к изображению:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\npython_logo = PhotoImage(file="./python_logo.png")\n\nlabel = ttk.Label(image=python_logo)\nlabel.pack()\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В моем случае изображение представляет файл python_logo.png, которое находится в одной папке с файлом приложения и которое изображает логотип python:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 3
                        ft.Container(
                            content=label_image3,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("изображение в Label в tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Если необходимо также отображать и текст, то для этого можно установить параметр compound, который определяет положение текста по отношению к изображению с помощью одного из следующих значений:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text("• top: изображение поверх текста", size=14, color=colors["text_secondary"]),
                        ft.Text("• bottom: изображение под текстом", size=14, color=colors["text_secondary"]),
                        ft.Text("• left: изображение слева от текста", size=14, color=colors["text_secondary"]),
                        ft.Text("• right: изображение справа от текста", size=14, color=colors["text_secondary"]),
                        ft.Text("• none: при наличии изображения отображается только изображение", size=14, color=colors["text_secondary"]),
                        ft.Text("• text: отображается только текст", size=14, color=colors["text_secondary"]),
                        ft.Text("• image: отображается только изображение", size=14, color=colors["text_secondary"]),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Например, отобразим картинку поверх текста:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\npython_logo = PhotoImage(file="./python_logo.png")\n\nlabel = ttk.Label(image=python_logo, text="Python", compound="top")\nlabel.pack()\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 4
                        ft.Container(
                            content=label_image4,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Картинка с текстов в label в tkinter в Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Стилизация", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "По умолчанию метка не имеет границы. Для установки толщины границы используется параметр borderwidth, при этом нам также надо установить тип границы с помощью параметра releaf, который может принимать значения: \"flat\", \"raised\", \"sunken\", \"ridge\", \"solid\" и \"groove\":",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\n\nlabel = ttk.Label(text="Hello Tkinter", borderwidth=2, relief="ridge", padding=8)\nlabel.pack(expand=True)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Установка цвета фона и текста:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\n\nlabel = ttk.Label(text="Hello Tkinter", background="#FFCDD2", foreground="#B71C1C", padding=8)\nlabel.pack(expand=True)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 5
                        ft.Container(
                            content=label_image5,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("стилизация label в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_entry_content(self):
        """Создание контента для темы 'Поле ввода Entry'"""
        image_path1 = self.get_library_image_path("t38.png")
        image_path2 = self.get_library_image_path("t39.png")
        image_path3 = self.get_library_image_path("t40.png")
        image_path4 = self.get_library_image_path("t41.png")
        colors = self.get_theme_colors()
        
        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            entry_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            entry_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Базовый Entry", size=12, color=colors["text_secondary"]),
                    ft.Text("t38.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            entry_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            entry_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Получение текста", size=12, color=colors["text_secondary"]),
                    ft.Text("t39.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 3
        if os.path.exists(image_path3):
            entry_image3 = ft.Image(
                src=image_path3,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            entry_image3 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Валидация ввода", size=12, color=colors["text_secondary"]),
                    ft.Text("t40.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 4
        if os.path.exists(image_path4):
            entry_image4 = ft.Image(
                src=image_path4,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            entry_image4 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Вывод ошибок валидации", size=12, color=colors["text_secondary"]),
                    ft.Text("t41.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Поле ввода Entry", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Элемент Entry представляет поле для ввода текста. С помощью конструктора Entry можно установить ряд параметров, основные из них:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text("• background: фоновый цвет", size=14, color=colors["text_secondary"]),
                        ft.Text("• cursor: курсор указателя мыши при наведении на текстовое поле", size=14, color=colors["text_secondary"]),
                        ft.Text("• foreground: цвет текста", size=14, color=colors["text_secondary"]),
                        ft.Text("• font: шрифт текста", size=14, color=colors["text_secondary"]),
                        ft.Text("• justify: устанавливает выравнивание текста. Значение LEFT выравнивает текст по левому краю, CENTER - по центру, RIGHT - по правому краю", size=14, color=colors["text_secondary"]),
                        ft.Text("• show: задает маску для вводимых символов", size=14, color=colors["text_secondary"]),
                        ft.Text("• state: состояние элемента, может принимать значения NORMAL (по умолчанию) и DISABLED", size=14, color=colors["text_secondary"]),
                        ft.Text("• textvariable: устанавливает привязку к элементу StringVar", size=14, color=colors["text_secondary"]),
                        ft.Text("• width: ширина элемента", size=14, color=colors["text_secondary"]),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Элемент Entry имеет ряд методов. Основные из них:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text("• insert(index, str): вставляет в текстовое поле строку по определенному индексу", size=14, color=colors["text_secondary"]),
                        ft.Text("• get(): возвращает введенный в текстовое поле текст", size=14, color=colors["text_secondary"]),
                        ft.Text("• delete(first, last=None): удаляет символ по индексу first. Если указан параметр last, то удаление производится до индекса last. Чтобы удалить до конца, в качестве второго параметра можно использовать значение END.", size=14, color=colors["text_secondary"]),
                        ft.Text("• focus(): установить фокус на текстовое поле", size=14, color=colors["text_secondary"]),
                        ft.Container(height=20),
                        
                        ft.Text(
                            "Простейшее текстовое поле:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nttk.Entry().pack(anchor=NW, padx=8, pady= 8)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 1
                        ft.Container(
                            content=entry_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("текстовое поле ввода Entry в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Получение введенного текста", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для получения текста из Entry, можно использовать его метод get(). Так, определим элемент Entry и по нажатию на кнопку выведем введенный текст на текстовую метку:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\ndef show_message():\n    label["text"] = entry.get()     # получаем введенный текст\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200") \n\nentry = ttk.Entry()\nentry.pack(anchor=NW, padx=6, pady=6)\n  \nbtn = ttk.Button(text="Click", command=show_message)\nbtn.pack(anchor=NW, padx=6, pady=6)\n\nlabel = ttk.Label()\nlabel.pack(anchor=NW, padx=6, pady=6)\n  \nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 2
                        ft.Container(
                            content=entry_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("получение текста из текстового поля Entry в tkinter в Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Вставка и удаление текста", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Рассмотрим вставку и удаление текста в Entry:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\ndef clear():\n    entry.delete(0, END)   # удаление введенного текста\n\ndef display():\n    label["text"] = entry.get()   # получение введенного текста\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x150")\n\nlabel = ttk.Label()\nlabel.pack(anchor=NW, padx=6, pady=6)\n\nentry = ttk.Entry()\nentry.pack(anchor=NW, padx=6, pady=6)\n\n# вставка начальных данных\nentry.insert(0, "Hello World")\n\ndisplay_button = ttk.Button(text="Display", command=display)\ndisplay_button.pack(side=LEFT, anchor=N, padx=6, pady=6)\n\nclear_button = ttk.Button(text="Clear", command=clear)\nclear_button.pack(side=LEFT, anchor=N, padx=6, pady=6)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "При запуске программы в текстовое поле сразу же добавляется текст по умолчанию:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('entry.insert(0, "Hello World")'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Кнопка Clear очищает оба поля, вызывая метод delete:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('def clear():\n    entry.delete(0, END)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Вторая кнопка, используя метод get, получает введенный текст:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('def display():\n    label["text"] = entry.get()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Валидация", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "С помощью параметра validate конструктора Entry можно задать, когда проводить валидацию введенного значения. Этот параметр может принимать следующие значения:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text("• none: отсутствие валидации, значение по умолчанию", size=14, color=colors["text_secondary"]),
                        ft.Text("• focus: валидация при получении фокуса", size=14, color=colors["text_secondary"]),
                        ft.Text("• focusin: валидация при изменении фокуса", size=14, color=colors["text_secondary"]),
                        ft.Text("• focusout: валидация при потере фокуса", size=14, color=colors["text_secondary"]),
                        ft.Text("• key: валидация при каждом вводе нового символа", size=14, color=colors["text_secondary"]),
                        ft.Text("• all: валидация при измении фокуса и вводе символов в поле", size=14, color=colors["text_secondary"]),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Параметр validatecommand позволяет установить команду валидации.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Рассмотрим небольшой пример. Допустим, пользовтаель должен ввести номер телефона в формете +xxxxxxxxxxx. То есть сначала должен идти знак +, а затем 11 цифр, например, +12345678901:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\nimport re\n\ndef is_valid(newval):\n    return re.match("^\\+\\d{0,11}$", newval) is not None\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\ncheck = (root.register(is_valid), "%P")\n\nphone_entry = ttk.Entry(validate="key", validatecommand=check) \nphone_entry.pack(padx=5, pady=5, anchor=NW)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Итак, параметр validate=\"key\" указывает, что мы будем валидировать ввод при каждом нажати на клавиатуру. Параметр validatecommand=check говорит, что валидировать ввод будет команда \"check\". Эта команда представляет кортеж из двух элементов:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('check = (root.register(is_valid), "%P")'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Первый элемент - вызов метода root.register(is_valid) регистрирует функцию, которая собственно будет производить валидацию - это функция is_valid(). Второй элемент - подстановка \"%P\" представляет новое значение, которое передается в функцию валидации.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Собственно саму валидацию выполняет функция is_valid(). Она принимает один параметр - текущее значение Entry, которое надо валидировать. Она возвращает True, если значение прошло валидацию, и False, если не прошло. Сама логика валидации представляет проверку строки на регулярное выражение \"^\\+\\d*$\". Если новое значение соответствует этому выражению, и в нем не больше 12 символов, то оно прошло валидацию.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "В итоге мы сможем ввести в текстовое поле только символ + и затем только 11 цифр.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 3
                        ft.Container(
                            content=entry_image3,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Валидация ввода  в entry на tkinter в Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text(
                            "Теперь немного изменим код и добавим вывод ошибок валидации:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\nimport re\n\ndef is_valid(newval):\n    result=  re.match("^\\+{0,1}\\d{0,11}$", newval) is not None\n    if not result and len(newval) <= 12:\n        errmsg.set("Номер телефона должен быть в формате +xxxxxxxxxxx, где x представляет цифру")\n    else:\n        errmsg.set("")\n    return result\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\ncheck = (root.register(is_valid), "%P")\n\nerrmsg = StringVar()\n\nphone_entry = ttk.Entry(validate="key", validatecommand=check) \nphone_entry.pack(padx=5, pady=5, anchor=NW)\n\nerror_label = ttk.Label(foreground="red", textvariable=errmsg, wraplength=250)\nerror_label.pack(padx=5, pady=5, anchor=NW)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь для вывода ошибок валидации добавлен виджет Label. Если введенное значение не соответствует регулярному выражению (например, пользователь попытался ввести нецифровой символ), и длина ввода меньше и равно 12 символов (проверять ввод больше 12 символов нет смысла, так как номер телефона содержит только 12 символов), то в метке выводим сообщение об ошибке",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 4
                        ft.Container(
                            content=entry_image4,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Валидация ввода в entry и вывод сообщения об ошибке в tkinter в Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Также мы можем передать значение параметра validate, чтобы в функции валидации в зависимости от того, нажал пользователь на клавишу или убрал фокус с поля, производить те или иные действия. В этом случае необходимо передать команде валидации дополнительный аргумент:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('check = (root.register(is_valid), "%P", "%V")'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь значение \"%V\" представляет событие, которое вызывает валидацию (focus/focusin/focusout/key). Тогда в функции валидации с помощью второго параметра мы сможем получить это значение:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('def is_valid(newval, op):\n    result=  re.match("^\\+\\d{0,11}$", newval) is not None\n    if op=="key":\n        # некоторые действия\n    elif op=="focus":\n        # некоторые действия\n    return result'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_variable_binding_content(self):
        """Создание контента для темы 'Привязка виджетов к переменным'"""
        image_path1 = self.get_library_image_path("t42.png")
        image_path2 = self.get_library_image_path("t43.png")
        image_path3 = self.get_library_image_path("t44.png")
        colors = self.get_theme_colors()
        
        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            binding_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            binding_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Привязка StringVar", size=12, color=colors["text_secondary"]),
                    ft.Text("t42.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            binding_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            binding_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изменение IntVar", size=12, color=colors["text_secondary"]),
                    ft.Text("t43.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 3
        if os.path.exists(image_path3):
            binding_image3 = ft.Image(
                src=image_path3,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            binding_image3 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Отслеживание изменений", size=12, color=colors["text_secondary"]),
                    ft.Text("t44.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Привязка виджетов к переменным", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Одной из примечательных особенностей Tkinter является то, что он позволяет привязать к ряду виджетов переменные определенных типов. При изменении значения виджета автоматически будет изменяться и значение привязанной переменной. Для привязки может использоваться переменная следующих типов:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text("• StringVar", size=14, color=colors["text_secondary"]),
                        ft.Text("• IntVar", size=14, color=colors["text_secondary"]),
                        ft.Text("• BooleanVar", size=14, color=colors["text_secondary"]),
                        ft.Text("• DoubleVar", size=14, color=colors["text_secondary"]),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Простейший пример:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x150")\n\nmessage = StringVar()\n\nlabel = ttk.Label(textvariable=message)\nlabel.pack(anchor=NW, padx=6, pady=6)\n\nentry = ttk.Entry(textvariable=message)\nentry.pack(anchor=NW, padx=6, pady=6)\n\nbutton = ttk.Button(textvariable=message)\nbutton.pack(side=LEFT, anchor=N, padx=6, pady=6)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае определяется переменная message, которая представляет класс StringVar, то есть такая переменная, которая хранит некоторую строку.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "С помощью параметра textvariable эта переменная привязана к тексту поля Entry, а также к тексту кнопки и метки:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('ttk.Label(textvariable=message)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "И если мы изменим текст в поле Entry, автоматически синхронно изменится и значение привязанной переменной message. а поскольку к этой переменной также привязаны кнопка и метка, то автоматически также изменится текст метки и кнопки.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 1
                        ft.Container(
                            content=binding_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Привязка переменной StringVar к виджету в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text(
                            "Типы имеют параметр value, который позволяет установить значение по умолчанию. Кроме того, они имеют два метода:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text("• get(): возвращает значение", size=14, color=colors["text_secondary"]),
                        ft.Text("• set(value): устанавливает значение, которое передано через параметр", size=14, color=colors["text_secondary"]),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Применим эти методы. Например, мы могли бы установить привязку к переменной IntVar и выводить количество кликов:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\ndef click_button():\n    value = clicks.get()    # получаем значение\n    clicks.set(value + 1)   # устанавливаем новое значение\n\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x150")\n\nclicks = IntVar(value=0)    # значение по умолчанию\n\nbtn = ttk.Button(textvariable=clicks, command=click_button)\nbtn.pack(anchor=CENTER, expand=1)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 2
                        ft.Container(
                            content=binding_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Изменение текста кнопки в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Отслеживание изменения переменной", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Класс Stringvar позволяет отслеживать чтение и изменение своего значения. Для отслеживания у объекта StringVar вызывается метод trace_add()",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('trace_add(trace_mode, function)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Первый параметр представляет отслеживаемое событие и может принимать следующие значения:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text("• write: изменение значения", size=14, color=colors["text_secondary"]),
                        ft.Text("• read: чтение значения", size=14, color=colors["text_secondary"]),
                        ft.Text("• unset: удаление значения", size=14, color=colors["text_secondary"]),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Также можно передать список из этих значений, если нам надо отслеживать несколько событий.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Второй параметр представляет функцию, которая будет вызываться при возникновении события из первого параметра. Эта функция должна принимать один параметр.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Посмотрим на примере:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\ndef check(*args):\n    print(name)\n    if name.get()=="admin":\n        result.set("запрещенное имя")\n    else: \n        result.set("норм")\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nname = StringVar()\nresult = StringVar()\n\nname_entry = ttk.Entry(textvariable=name) \nname_entry.pack(padx=5, pady=5, anchor=NW)\n\ncheck_label = ttk.Label(textvariable=result)\ncheck_label.pack(padx=5, pady=5, anchor=NW) \n\n# отслеживаем изменение значения переменной name\nname.trace_add("write", check)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае текстовое поле name_entry привязано к переменной name, а метка check_label - к переменной result.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Здесь мы отлеживаем изменение значения переменной name - при изменении срабатывает функция check, в которой изменяем переменную result в зависимости от значения name. Условимся, что name представляет имя пользователя, но имя \"admin\" запрещено.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 3
                        ft.Container(
                            content=binding_image3,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Отслеживание изменение переменной StringVar в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_checkbutton_content(self):
        """Создание контента для темы 'Checkbutton'"""
        image_path1 = self.get_library_image_path("t45.png")
        image_path2 = self.get_library_image_path("t46.png")
        image_path3 = self.get_library_image_path("t47.png")
        image_path4 = self.get_library_image_path("t48.png")
        colors = self.get_theme_colors()
        
        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            checkbutton_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            checkbutton_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Базовый Checkbutton", size=12, color=colors["text_secondary"]),
                    ft.Text("t45.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            checkbutton_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            checkbutton_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Обработка изменения", size=12, color=colors["text_secondary"]),
                    ft.Text("t46.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 3
        if os.path.exists(image_path3):
            checkbutton_image3 = ft.Image(
                src=image_path3,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            checkbutton_image3 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Текст флажка", size=12, color=colors["text_secondary"]),
                    ft.Text("t47.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 4
        if os.path.exists(image_path4):
            checkbutton_image4 = ft.Image(
                src=image_path4,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            checkbutton_image4 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Несколько флажков", size=12, color=colors["text_secondary"]),
                    ft.Text("t48.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Checkbutton", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Элемент Checkbutton представляет собой флажок, который может находиться в двух состояниях: отмеченном и неотмеченном.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Конструктор Checkbutton принимает ряд параметров, отметим основные из них:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text("• command: ссылка на функцию, которая вызывается при нажатии на флажок", size=14, color=colors["text_secondary"]),
                        ft.Text("• cursor: курсор при наведении на элемент", size=14, color=colors["text_secondary"]),
                        ft.Text("• image: графическое изображение, отображаемое на элементе", size=14, color=colors["text_secondary"]),
                        ft.Text("• offvalue: значение флажка в неотмеченном состоянии, по умолчанию равно 0", size=14, color=colors["text_secondary"]),
                        ft.Text("• onvalue: значение флажка в отмеченном состоянии, по умолчанию равно 1", size=14, color=colors["text_secondary"]),
                        ft.Text("• padding: отступы от текста до границы флажка", size=14, color=colors["text_secondary"]),
                        ft.Text("• state: состояние элемента, может принимать значения NORMAL (по умолчанию), DISABLED и ACTIVE", size=14, color=colors["text_secondary"]),
                        ft.Text("• text: текст элемента", size=14, color=colors["text_secondary"]),
                        ft.Text("• textvariable: привязанный к тексту объект StringVar", size=14, color=colors["text_secondary"]),
                        ft.Text("• underline: индекс подчеркнутого символа в тексте флажка", size=14, color=colors["text_secondary"]),
                        ft.Text("• variable: ссылка на переменную, как правило, типа IntVar, которая хранит состояние флажка", size=14, color=colors["text_secondary"]),
                        ft.Text("• width: ширина элемента", size=14, color=colors["text_secondary"]),
                        ft.Container(height=20),
                        
                        ft.Text(
                            "Создадим простейший флажок:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nenabled = IntVar()\n  \nenabled_checkbutton = ttk.Checkbutton(text="Включить", variable=enabled)\nenabled_checkbutton.pack(padx=6, pady=6, anchor=NW)\n  \nenabled_label = ttk.Label(textvariable=enabled)\nenabled_label.pack(padx=6, pady=6, anchor=NW)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Отличительной чертой Checkbutton является возможность привязки к переменной через параметр variable, который представляет значение флажка. Здесь данный параметр привязан к переменной enabled типа IntVar. В отмеченном состоянии привязанный объект IntVar имеет значение 1, а в неотмеченном - 0. В итоге через IntVar мы можем получать значение, указанное пользователем.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 1
                        ft.Container(
                            content=checkbutton_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Checkbutton в tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Обработка изменения флажка", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "С помощью параметра command можно установить функцию, которая будет вызываться при изменении состояния флажка:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\nfrom tkinter.messagebox import showinfo\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\ndef checkbutton_changed():\n    if enabled.get() == 1:\n        showinfo(title="Info", message="Включено")\n    else:\n        showinfo(title="Info", message="Отключено")\n\nenabled = IntVar()\n  \nenabled_checkbutton = ttk.Checkbutton(text="Включить", variable=enabled, command=checkbutton_changed)\nenabled_checkbutton.pack(padx=6, pady=6, anchor=NW)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь при изменении состояния флажка срабатывает функция checkbutton_changed. В ней в зависимости от состояния флажка (а точнее в зависимости от значения переменной enabled) с помощью встроенной функции showinfo() отображаем сообщение о состоянии флажка:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 2
                        ft.Container(
                            content=checkbutton_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("изменение состояния флажка Checkbutton в tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("onvalue и offvalue", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Параметры onvalue и offvalue позволяют задать значение флажка в отмеченном и неотмеченном состоянии. По умолчанию они равны 1 и 0 соответственно. Однако мы можем передать им и другие, более удобные для нас значения.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\nfrom tkinter.messagebox import showinfo\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\ndef checkbutton_changed():\n    showinfo(title="Info", message=enabled.get())\n\nenabled = StringVar()\n  \nenabled_checkbutton = ttk.Checkbutton(text="Включить", variable=enabled, offvalue="Отключено", onvalue="Включено", command=checkbutton_changed)\nenabled_checkbutton.pack(padx=6, pady=6, anchor=NW)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Теперь переменная enabled представляет StringVar, то есть хранит строку. Соответственно параметры offvalue и onvalue тоже представляют строку",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Текст флажка", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для установки текста флажка можно использовать параметры text и textvariable. Причем мы можем привязать текст флажка к его значению с помощью textvariable:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nenabled_on = "Включено"\nenabled_off = "Отключено"\nenabled = StringVar(value=enabled_on)\n  \nenabled_checkbutton = ttk.Checkbutton(textvariable=enabled, variable=enabled, offvalue=enabled_off, onvalue=enabled_on)\nenabled_checkbutton.pack(padx=6, pady=6, anchor=NW)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае для хранения текста в отмеченном и неотмеченном состояниях определены две переменные: enabled_on и enabled_off. Переменная enabled инициализируется тем же значением (enabled_on), что и параметр onvalue, поэтому по умолчанию флажок будет отмечен. А поскольку его параметры textvariable и variable привязаны к одной и той же переменной enabled, то они будет изменяться синхронно",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 3
                        ft.Container(
                            content=checkbutton_image3,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("привязка текста флажка Checkbutton к его состоянию в tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Обработка нескольких флажков", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Аналогичным образом можно использовать наборы флажков:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\ndef select():\n    result = "Выбрано: "\n    if python.get() == 1: result = f"{result} Python"\n    if javascript.get() == 1: result = f"{result} JavaScript"\n    if java.get() == 1: result = f"{result} Java"\n    languages.set(result)\n\nposition = {"padx":6, "pady":6, "anchor":NW}\n\nlanguages = StringVar()\nlanguages_label = ttk.Label(textvariable=languages)\nlanguages_label.pack(**position)\n\npython = IntVar()\npython_checkbutton = ttk.Checkbutton(text="Python", variable=python, command=select)\npython_checkbutton.pack(**position)\n\njavascript = IntVar()\njavascript_checkbutton = ttk.Checkbutton(text="JavaScript", variable=javascript, command=select)\njavascript_checkbutton.pack(**position)\n\njava = IntVar()\njava_checkbutton = ttk.Checkbutton(text="Java", variable=java, command=select)\njava_checkbutton.pack(**position)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае языки, которые соответствуют выбранным чекбоксам, будут отображаться на текстовой метке:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 4
                        ft.Container(
                            content=checkbutton_image4,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("checkbox in tkinter and Python", size=14, color=colors["text_secondary"], italic=True),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_radiobutton_content(self):
        """Создание контента для темы 'Radiobutton'"""
        image_path1 = self.get_library_image_path("t49.png")
        image_path2 = self.get_library_image_path("t50.png")
        image_path3 = self.get_library_image_path("t51.png")
        image_path4 = self.get_library_image_path("t52.png")
        colors = self.get_theme_colors()
        
        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            radiobutton_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            radiobutton_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Базовые Radiobutton", size=12, color=colors["text_secondary"]),
                    ft.Text("t49.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            radiobutton_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            radiobutton_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Обработка выбора", size=12, color=colors["text_secondary"]),
                    ft.Text("t50.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 3
        if os.path.exists(image_path3):
            radiobutton_image3 = ft.Image(
                src=image_path3,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            radiobutton_image3 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображения Radiobutton", size=12, color=colors["text_secondary"]),
                    ft.Text("t51.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 4
        if os.path.exists(image_path4):
            radiobutton_image4 = ft.Image(
                src=image_path4,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            radiobutton_image4 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Текст и изображения", size=12, color=colors["text_secondary"]),
                    ft.Text("t52.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Radiobutton", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Виджет Radiobutton представляет переключатель, который может находиться в двух состояниях: отмеченном или неотмеченном. Но в отличие от Checkbutton переключатели могут создавать группу, из которой одномоментно мы можем выбрать только один переключатель.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Среди параметров конструктора Radiobutton стоит выделить следующие:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text("• command: ссылка на функцию, которая вызывается при нажатии на переключатель", size=14, color=colors["text_secondary"]),
                        ft.Text("• cursor: курсор при наведении на виджет", size=14, color=colors["text_secondary"]),
                        ft.Text("• image: графическое изображение, отображаемое виджетом", size=14, color=colors["text_secondary"]),
                        ft.Text("• padding: отступы от содержимого до границы переключателя", size=14, color=colors["text_secondary"]),
                        ft.Text("• state: состояние виджета, может принимать значения NORMAL (по умолчанию), DISABLED и ACTIVE", size=14, color=colors["text_secondary"]),
                        ft.Text("• text: текст виджета", size=14, color=colors["text_secondary"]),
                        ft.Text("• textvariable: устанавливает привязку к переменной StringVar, которая задает текст переключателя", size=14, color=colors["text_secondary"]),
                        ft.Text("• underline: индекс подчеркнутого символа в тексте виджета", size=14, color=colors["text_secondary"]),
                        ft.Text("• variable: ссылка на переменную, как правило, типа IntVar, которая хранит состояние переключателя", size=14, color=colors["text_secondary"]),
                        ft.Text("• value: значение переключателя", size=14, color=colors["text_secondary"]),
                        ft.Text("• width: ширина виджета", size=14, color=colors["text_secondary"]),
                        ft.Container(height=20),
                        
                        ft.Text(
                            "Определим группу переключателей:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nposition = {"padx":6, "pady":6, "anchor":NW}\n\npython = "Python"\njava = "Java"\njavascript = "JavaScript"\n\nlang = StringVar(value=java)    # по умолчанию будет выбран элемент с value=java\n\nheader = ttk.Label(textvariable=lang)\nheader.pack(**position)\n  \npython_btn = ttk.Radiobutton(text=python, value=python, variable=lang)\npython_btn.pack(**position)\n  \njavascript_btn = ttk.Radiobutton(text=javascript, value=javascript, variable=lang)\njavascript_btn.pack(**position)\n\njava_btn = ttk.Radiobutton(text=java, value=java, variable=lang)\njava_btn.pack(**position)\n  \nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь определено три переключателя. Все они привязаны к одной переменной lang, которая представляет тип StringVar. При этом они имеют разные значения, устанавливаемые через параметр value. Начальное значение переменной lang (\"java\") соответствует значению value последнего переключателя, поэтому по умолчанию будет выбран последний переключатель.А при выборе одного переключателя, другой автоматически перейдет в неотмеченное состояние.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для вывода выделенного значения над переключателями определена текстовая метка, которая отображает значение переменной lang:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 1
                        ft.Container(
                            content=radiobutton_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Radiobutton в tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В примере выше отображаемый текст (параметр text) и значение (параметр value) совпадают, но это необязательно",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Обработка выбора пользователя", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Параметр command позволяет установить функцию, которая обрабатывает выбор переключателя. Например:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nposition = {"padx":6, "pady":6, "anchor":NW}\nlanguages = ["Python", "JavaScript", "Java", "C#"]\nselected_language = StringVar()    # по умолчанию ничего не выборанно\n\nheader = ttk.Label(text="Выберите язык")\nheader.pack(**position)\n\ndef select():\n    header.config(text=f"Выбран {selected_language.get()}")\n\nfor lang in languages:\n    lang_btn = ttk.Radiobutton(text=lang, value=lang, variable=selected_language, command=select)\n    lang_btn.pack(**position)\n  \nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь для упрощения данные переключателей определены в виде списка languages. В цикле for пробегаемся по всем элементам списка и создаем переключатель. При нажатии на каждый переключатель будет срабатывать функция select(), которая установит для метки header соответствующий текст:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 2
                        ft.Container(
                            content=radiobutton_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Обработка выбора Radiobutton в tkinter Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Установка изображения", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для установки изображения применяется параметр image:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from itertools import chain\nfrom tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nposition = {"padx":6, "pady":6, "anchor":NW}\n\npython = "Python"\njava = "Java"\ncsharp = "C#"\n\nlang = StringVar(value=java)    # по умолчанию будет выбран элемент с value=java\n\nheader = ttk.Label(textvariable=lang)\nheader.pack(**position)\n\npython_img = PhotoImage(file="./python_sm.png")\ncsharp_img = PhotoImage(file="./csharp_sm.png")\njava_img = PhotoImage(file="./java_sm.png")\n  \npython_btn = ttk.Radiobutton( value=python, variable=lang, image=python_img)\npython_btn.pack(**position)\n  \ncsharp_btn = ttk.Radiobutton(value=csharp, variable=lang, image=csharp_img)\ncsharp_btn.pack(**position)\n\njava_btn = ttk.Radiobutton(value=java, variable=lang, image=java_img)\njava_btn.pack(**position)\n  \nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Параметру image передается объект PhotoImage, в конструкторе которого через параметр file устанавливается путь к изображению. Здесь предполагается, что в одной папке с файлом приложения находятся файлы изображений \"python_sm.png\", \"csharp_sm.png\" и \"java_sm.png\".",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 3
                        ft.Container(
                            content=radiobutton_image3,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Установка изображения для Radiobutton в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text(
                            "Если необходимо также отображать и текст, то для этого можно установить параметр compound, который определяет положение текста по отношению к изображению с помощью одного из следующих значений:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text("• top: изображение поверх текста", size=14, color=colors["text_secondary"]),
                        ft.Text("• bottom: изображение под текстом", size=14, color=colors["text_secondary"]),
                        ft.Text("• left: изображение слева от текста", size=14, color=colors["text_secondary"]),
                        ft.Text("• right: изображение справа от текста", size=14, color=colors["text_secondary"]),
                        ft.Text("• none: при наличии изображения отображается только изображение", size=14, color=colors["text_secondary"]),
                        ft.Text("• text: отображается только текст", size=14, color=colors["text_secondary"]),
                        ft.Text("• image: отображается только изображение", size=14, color=colors["text_secondary"]),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Например, отобразим картинку поверх текста:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from itertools import chain\nfrom tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nposition = {"padx":6, "pady":6, "anchor":NW}\n\nlanguages = [\n    {"name": "Python", "img": PhotoImage(file="./python_sm.png")},\n    {"name": "C#", "img": PhotoImage(file="./csharp_sm.png")},\n    {"name": "Java", "img": PhotoImage(file="./java_sm.png")}\n]\n\n\nlang = StringVar(value=languages[0]["name"])    # по умолчанию будет выбран элемент с value=python\n\nheader = ttk.Label(textvariable=lang)\nheader.pack(**position)\n\nfor l in languages:\n    btn = ttk.Radiobutton(value=l["name"], text=l["name"], variable=lang, image=l["img"], compound="top")\n    btn.pack(**position)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 4
                        ft.Container(
                            content=radiobutton_image4,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Установка изображения и текста для Radiobutton в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_frame_content(self):
        """Создание контента для темы 'Установка родительского контейнера. Frame'"""
        image_path1 = self.get_library_image_path("t53.png")
        image_path2 = self.get_library_image_path("t54.png")
        colors = self.get_theme_colors()
        
        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            frame_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            frame_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Базовый Frame", size=12, color=colors["text_secondary"]),
                    ft.Text("t53.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            frame_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            frame_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Несколько Frame", size=12, color=colors["text_secondary"]),
                    ft.Text("t54.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Установка родительского контейнера. Frame", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Каждый виджет, кроме окна, располагается в определенном родительском контейнере. Например:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nlbl = ttk.Label(text="Hello")\nlbl.pack()\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь для метки lbl контейнером выступает главное окно - root. Однако графическое приложение может иметь более сложную структуру со множеством вложенных контейнеров. И для каждого виджета можно явным образом установить контейнер с помощью первого параметра конструктора, который называтся master. Например, в примере выше мы могли бы явным образом прописать для Label родительский контейнер:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('lbl = ttk.Label(master=root, text="Hello")\n# или так \nlbl = ttk.Label(root, text="Hello")'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае это не имеет смысла, кнопка по умолчанию добавляется в окно. Однако также мы можем определять вложенные контейнеры. В частности, для в Tkinter предназначен виджет Frame.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Frame", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Frame отображает прямоугольник и обычно применяется для организации интерфейса в отдельные блоки. Некоторые основные параметры, которые мы можем установить через конструктор класса Frame:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text("• borderwidth: толщина границы фрейма, по умолчанию равно 0", size=14, color=colors["text_secondary"]),
                        ft.Text("• relief: определяет тип границы, может принимать значения SUNKEN, RAISED, GROOVE, RIDGE", size=14, color=colors["text_secondary"]),
                        ft.Text("• cursor: устанавливает курсор при наведении на фрейм", size=14, color=colors["text_secondary"]),
                        ft.Text("• height: высота фрейма", size=14, color=colors["text_secondary"]),
                        ft.Text("• width: ширина фрейма", size=14, color=colors["text_secondary"]),
                        ft.Text("• padding: отступы от вложенного содержимого до границ фрейма", size=14, color=colors["text_secondary"]),
                        ft.Container(height=20),
                        
                        ft.Text(
                            "Используем фреймы:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('import re\nfrom tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nframe = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])\nname_label = ttk.Label(frame, text="Введите имя")\nname_label.pack(anchor=NW)\n\nname_entry = ttk.Entry(frame)\nname_entry.pack(anchor=NW)\n\nframe.pack(anchor=NW, fill=X, padx=5, pady=5)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь фрейм имеет границу толщиной в 1 пиксель. Граница представляет обычную линию (relief=SOLID). Также для фрейма заданы внутренние отступы: 8 по горизонтали и 10 по вертикали. Для установки отступов можно использовать следующие формы:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('padding=10              # устанавливает общий доступ в 10 единиц\npadding=[8, 10]         # отступ по горизонтали - 8, отступ по вертикали - 10\npadding=[8, 10, 6, 5]   # отступ слева 8, сверху - 10, справа - 6 и снизу 5'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В сам фрейм добавляются два других виджета: Label и Entry. Для этого для обоих виджетов указываем фрейм в качестве родительского контейнера.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 1
                        ft.Container(
                            content=frame_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Frame в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text(
                            "При этом мы можем вынести во вне создание фрейма:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\ndef create_frame(label_text):\n    frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])\n    # добавляем на фрейм метку\n    label = ttk.Label(frame, text=label_text)\n    label.pack(anchor=NW)\n    # добавляем на фрейм текстовое поле\n    entry = ttk.Entry(frame)   \n    entry.pack(anchor=NW)\n    # возвращаем фрейм из функции\n    return frame\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nname_frame = create_frame("Введите имя")\nname_frame.pack(anchor=NW, fill=X, padx=5, pady=5)\n\nemail_frame = create_frame("Введите email")\nemail_frame.pack(anchor=NW, fill=X, padx=5, pady=5)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь для создания фрейма определена функция create_frame, которая возвращает фрейм с меткой и текстовым полем. Далее создаем с помощью этой функции два фрейма и добавляем их в окно:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 2
                        ft.Container(
                            content=frame_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Frame как контейнер виджетов в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_listbox_content(self):
        """Создание контента для темы 'Listbox'"""
        image_path1 = self.get_library_image_path("t55.png")
        image_path2 = self.get_library_image_path("t56.png")
        image_path3 = self.get_library_image_path("t57.png")
        image_path4 = self.get_library_image_path("t58.png")
        colors = self.get_theme_colors()
        
        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            listbox_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            listbox_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Базовый Listbox", size=12, color=colors["text_secondary"]),
                    ft.Text("t55.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            listbox_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            listbox_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Управление данными", size=12, color=colors["text_secondary"]),
                    ft.Text("t56.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 3
        if os.path.exists(image_path3):
            listbox_image3 = ft.Image(
                src=image_path3,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            listbox_image3 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Обработка выбора", size=12, color=colors["text_secondary"]),
                    ft.Text("t57.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 4
        if os.path.exists(image_path4):
            listbox_image4 = ft.Image(
                src=image_path4,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            listbox_image4 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Программное выделение", size=12, color=colors["text_secondary"]),
                    ft.Text("t58.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Listbox", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Виджет Listbox в tkinter представляет список объектов. Стоит отметить, что данный виджет присутствует только в пакете tkinter, а в пакете tkinter.ttk для него нет аналогов.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Для настройки Listbox мы можем указать в его конструкторе следующие параметры:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text("• listvariable: список элементов, которые добавляются в ListBox", size=14, color=colors["text_secondary"]),
                        ft.Text("• bg: фоновый цвет", size=14, color=colors["text_secondary"]),
                        ft.Text("• bd: толщина границы вокруг элемента", size=14, color=colors["text_secondary"]),
                        ft.Text("• cursor: курсор при наведении на Listbox", size=14, color=colors["text_secondary"]),
                        ft.Text("• font: настройки шрифта", size=14, color=colors["text_secondary"]),
                        ft.Text("• fg: цвет текста", size=14, color=colors["text_secondary"]),
                        ft.Text("• highlightcolor: цвет элемента, когда он получает фокус", size=14, color=colors["text_secondary"]),
                        ft.Text("• highlightthickness: толщина границы элемента, когда он находится в фокусе", size=14, color=colors["text_secondary"]),
                        ft.Text("• relief: устанавливает стиль элемента, по умолчанию имеет значение SUNKEN", size=14, color=colors["text_secondary"]),
                        ft.Text("• selectbackground: фоновый цвет для выделенного элемента", size=14, color=colors["text_secondary"]),
                        ft.Text("• selectmode: определяет, сколько элементов могут быть выделены. Может принимать следующие значения: BROWSE, SINGLE, MULTIPLE, EXTENDED. Например, если необходимо включить множественное выделение элементов, то можно использовать значения MULTIPLE или EXTENDED.", size=14, color=colors["text_secondary"]),
                        ft.Text("• height: высота элемента в строках. По умолчанию отображает 10 строк", size=14, color=colors["text_secondary"]),
                        ft.Text("• width: устанавливает ширину элемента в символах. По умолчанию ширина - 20 символов", size=14, color=colors["text_secondary"]),
                        ft.Text("• xscrollcommand: задает горизонтальную прокрутку", size=14, color=colors["text_secondary"]),
                        ft.Text("• yscrollcommand: устанавливает вертикальную прокрутку", size=14, color=colors["text_secondary"]),
                        ft.Container(height=20),
                        
                        ft.Text(
                            "Определим простой список:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nlanguages = ["Python", "JavaScript", "C#", "Java"]\nlanguages_var = Variable(value=languages)\n\nlanguages_listbox = Listbox(listvariable=languages_var)\n\nlanguages_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Для наполнения listboxa элементами определяем список languages, затем этот список передаем в переменную типа Variable. Затем привязываем эту переменную к параметру listvariable у Listbox",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 1
                        ft.Container(
                            content=listbox_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Listbox в tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Основные методы Listbox", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Listbox имеет ряд методов для управления поведением элемента и его содержимым. Некоторые из них:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text("• curselection(): возвращает набор индексов выделенных элементов", size=14, color=colors["text_secondary"]),
                        ft.Text("• delete(first, last = None): удаляет элементы с индексами из диапазона [first, last]. Если второй параметр опущен, то удаляет только один элемент по индексу first.", size=14, color=colors["text_secondary"]),
                        ft.Text("• get(first, last = None): возвращает кортеж, который содержит текст элементов с индексами из дипазона [first, last]. Если второй параметр опущен, возвращается только текст элемента с индексом first.", size=14, color=colors["text_secondary"]),
                        ft.Text("• insert(index, element): вставляет элемент по определенному индексу", size=14, color=colors["text_secondary"]),
                        ft.Text("• size(): возвращает количество элементов", size=14, color=colors["text_secondary"]),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Для рассмотрения этих методов напишем небольшой скрипт по управлению данными:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n \n \n# удаление выделенного элемента\ndef delete():\n    selection = languages_listbox.curselection()\n    # мы можем получить удаляемый элемент по индексу\n    # selected_language = languages_listbox.get(selection[0])\n    languages_listbox.delete(selection[0])\n \n \n# добавление нового элемента\ndef add():\n    new_language = language_entry.get()\n    languages_listbox.insert(0, new_language)\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("300x250")\nroot.columnconfigure(index=0, weight=4)\nroot.columnconfigure(index=1, weight=1)\nroot.rowconfigure(index=0, weight=1)\nroot.rowconfigure(index=1, weight=3)\nroot.rowconfigure(index=2, weight=1)\n\n# текстовое поле и кнопка для добавления в список\nlanguage_entry = ttk.Entry()\nlanguage_entry.grid(column=0, row=0, padx=6, pady=6, sticky=EW)\nttk.Button(text="Добавить", command=add).grid(column=1, row=0, padx=6, pady=6)\n\n# создаем список\nlanguages_listbox = Listbox()\nlanguages_listbox.grid(row=1, column=0, columnspan=2, sticky=EW, padx=5, pady=5)\n\n# добавляем в список начальные элементы\nlanguages_listbox.insert(END, "Python")\nlanguages_listbox.insert(END, "C#")\n\nttk.Button(text="Удалить", command=delete).grid(row=2, column=1, padx=5, pady=5)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Для манипулирования элемента списка здесь определено две кнопки. Первая кнопка вызывает функцию add(), которая получает введенное в текстовое поле значение и добавляет его на первое место в списке с помощью метода insert().",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Вторая кнопка по нажатию удаляет выделенный элемент. Для этого мы сначала получаем выделенные индексы через метод curselection(). Так как в нашем случае выделяется только один элемент, то получаем его индекс через выражение selection[0]. И этот индекс передаем в метод delete() для удаления.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 2
                        ft.Container(
                            content=listbox_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Управление данными с помщью методов в Listbox в tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text(
                            "Подобным образом мы можем управлять элементами, если Listbox привязан к переменной типа Var/StringVar:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\n# добавление нового элемента\ndef add():\n    new_language = language_entry.get()\n    languages_listbox.insert(0, new_language)\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("300x250")\nroot.columnconfigure(index=0, weight=4)\nroot.columnconfigure(index=1, weight=1)\nroot.rowconfigure(index=0, weight=1)\nroot.rowconfigure(index=1, weight=3)\n\nlanguages = ["Python", "C#"]\nlanguages_var = StringVar(value=languages)\n\n# текстовое поле и кнопка для добавления в список\nlanguage_entry = ttk.Entry()\nlanguage_entry.grid(column=0, row=0, padx=6, pady=6, sticky=EW)\nttk.Button(text="Добавить", command=add).grid(column=1, row=0, padx=6, pady=6)\n\n# создаем список\nlanguages_listbox = Listbox(listvariable=languages_var)\nlanguages_listbox.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=5, pady=5)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Для упрощения здесь я убрал код для удаления, потому что суть будет та же. А именно: у нас есть стандартный список строк languages и есть переменная languages_var, которая использует этот список и к которой привязан Listbox. Все операции с элементами внутри Listbox, например, добавление с помощью вызова languages_listbox.insert(0, new_language) повлияют на переменную languages_var - она изменит свое значение. Но! изначальный список строк languages останется без изменений.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Что если нам также надо изменить сам изначальный список languages, особенно когда у нас в программе несколько функциональных частей, которые используют этот список и которые должны быть синхронизированы? В этом случае мы можем добавлять и удалять элементы напрямую в списке languages, но тогда необходимо переустанавливать значение переменной languages_var, к которой привязан Listbox:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\n# добавление нового элемента\ndef add():\n    new_language = language_entry.get()\n    # добавляем новый элемент в список languages\n    languages.append(new_language)\n    # переустанавливаем значение переменной languages_var\n    languages_var.set(languages)\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("300x250")\nroot.columnconfigure(index=0, weight=4)\nroot.columnconfigure(index=1, weight=1)\nroot.rowconfigure(index=0, weight=1)\nroot.rowconfigure(index=1, weight=3)\n\n# базовый список\nlanguages = ["Python", "C#"]\nlanguages_var = StringVar(value=languages)\n\n# текстовое поле и кнопка для добавления в список\nlanguage_entry = ttk.Entry()\nlanguage_entry.grid(column=0, row=0, padx=6, pady=6, sticky=EW)\nttk.Button(text="Добавить", command=add).grid(column=1, row=0, padx=6, pady=6)\n\n# создаем список\nlanguages_listbox = Listbox(listvariable=languages_var)\nlanguages_listbox.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=5, pady=5)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Режим и обработка выбора", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "По умолчанию Listbox позволяет выбрать один элемент. Но с помощью параметра selectmode это поведение можно переопределить. Данный параметр принимает одно из следующих значений:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text("• BROWSE: позволяет выбирать один элемент и перетаскивать его мышкой. Режим по умолчанию.", size=14, color=colors["text_secondary"]),
                        ft.Text("• EXTENDED: позволяет выбрать группу элементов, выделив начальный и конечный элементы", size=14, color=colors["text_secondary"]),
                        ft.Text("• SINGLE: позволяет выбрать один элемент, но не позволяет перетаскивать его мышкой", size=14, color=colors["text_secondary"]),
                        ft.Text("• MULTIPLE: позволяет выбрать множество элементов, надимая на строку элемента.", size=14, color=colors["text_secondary"]),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Например, установка выбора нескольких элементов:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('languages_listbox = Listbox(listvariable=languages_var, selectmode=EXTENDED)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Для обработки выбора элементов в Listbox необходимо прикрепить функцию обработки к событию <<ListboxSelect>> с помощью метода bind:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('listbox.bind("<<ListboxSelect>>", функция_обработки)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Например, динамически обработаем выбор в списке:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\ndef selected(event):\n    # получаем индексы выделенных элементов\n    selected_indices = languages_listbox.curselection()\n    # получаем сами выделенные элементы\n    selected_langs = ",".join([languages_listbox.get(i) for i in selected_indices])\n    msg = f"вы выбрали: {selected_langs}"\n    selection_label["text"] = msg\n\nlanguages = ["Python", "JavaScript", "C#", "Java"]\nlanguages_var = Variable(value=languages)\n\nselection_label = ttk.Label()\nselection_label.pack(anchor=NW, fill=X, padx=5, pady=5)\n\nlanguages_listbox = Listbox(listvariable=languages_var, selectmode=EXTENDED)\nlanguages_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)\nlanguages_listbox.bind("<<ListboxSelect>>", selected)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае при изменении выбора в списке срабатывает функция selected. Функция должна принимать один параметр, который несет информацию о событии - здесь это параметр event. Хотя в данном случае он никак не используется.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "В самой функции сначала получаем индексы выделенных элементов с помощью метода curselection(), затем в цикле получаем собственно элементы по этим индексам и создаем общую строку, которая затем выводится в элементе Label.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 3
                        ft.Container(
                            content=listbox_image3,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Обработка выбора элементов в Listbox в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Программное выделение", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Ряд методов Listbox позволяют программно управлять выделением элементов:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text("• select_set(first, last): выделяет с индекса first по индекс last. Если надо выделить только один элемент, то применяется только параметр first", size=14, color=colors["text_secondary"]),
                        ft.Text("• select_includes(index): возвращает True, среди элемент с индексом index выделен", size=14, color=colors["text_secondary"]),
                        ft.Text("• select_clear(first, last): снимает выделение с индекса first по индекс last. Если надо снять выделение только с одного элемента, то применяется только параметр first", size=14, color=colors["text_secondary"]),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Например, выделим элементы с 1 по 2 индексы:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nlanguages = ["Python", "C#", "Java", "JavaScript"]\nlanguages_var = StringVar(value=languages)\n\nlanguages_listbox = Listbox(listvariable=languages_var, selectmode=EXTENDED)\nlanguages_listbox.pack(expand=1, fill=BOTH)\nlanguages_listbox.select_set(first=1, last=2)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 4
                        ft.Container(
                            content=listbox_image4,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Программное выделение элементов в Listbox в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_scrollbar_content(self):
        """Создание контента для темы 'Scrollbar и прокрутка виджета'"""
        image_path1 = self.get_library_image_path("t59.png")
        colors = self.get_theme_colors()
        
        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            scrollbar_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            scrollbar_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Scrollbar с Listbox", size=12, color=colors["text_secondary"]),
                    ft.Text("t59.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Scrollbar и прокрутка виджета", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Виджет Scrollbar прокручивать содержимое контейнера, которое больше размеров этого контейнера.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Основные параметры конструктора Scrollbar:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text("• orient: направление прокрутки. Может принать следующие значения: vertical (вертикальная прокрутка) и horizontal (горизонтальная прокрутка).", size=14, color=colors["text_secondary"]),
                        ft.Text("• command: команда прокрутки", size=14, color=colors["text_secondary"]),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Scrollbar не используется сам по себе, он применяется лишь для прокручиваемого виджета. Не все виджеты в tkinter являются прокручиваемыми. Для прокрутки по вертикали прокручиваемый виджет имеет yview, а для прокрутки по горизонтали - метод xview (виджет может иметь только один из этих методов). Примером прокручиваемого виджета может служить Listbox или Text. Этот метод используется в качестве команды для Scrollbar:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('listbox = Listbox()\n# вертикальная прокрутка\nscrollbar = ttk.Scrollbar(orient="vertical", command = listbox.yview)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Но прокручиваемый виджет должен также взаимодействовать со Scrollbar. Для этого у прокручиваемого виджета имеются параметры yscrollcommand и/или xscrollcommand, которые должны принимать вызов метода set объекта Scrollbar:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n  \nlanguages = ["Python", "JavaScript", "C#", "Java", "C++", "Rust", "Kotlin", "Swift",\n             "PHP", "Visual Basic.NET", "F#", "Ruby", "R", "Go", "C", \n             "T-SQL", "PL-SQL", "Typescript", "Assembly", "Fortran"]\n  \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n \n \nlanguages_var = StringVar(value=languages)\nlistbox = Listbox(listvariable=languages_var)\nlistbox.pack(side=LEFT, fill=BOTH, expand=1)\n  \nscrollbar = ttk.Scrollbar(orient="vertical", command=listbox.yview)\nscrollbar.pack(side=RIGHT, fill=Y)\n  \nlistbox["yscrollcommand"]=scrollbar.set\n  \nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В конструкторе scrollbar ассоциируется с функцией, которую надо выполнять при прокрутке. В данном случае это метод yview элемента listbox. В итоге мы сможем прокручивать элементы по вертикали:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "И так как необходимо прокручивать listbox по вертикали, то у него задается параметр listbox[\"yscrollcommand\"]=scrollbar.set",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 1
                        ft.Container(
                            content=scrollbar_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Scrollbar и Listbox в tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Ручная прокрутка", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "В принципе для прокрутки виджета (который поддерживает прокрутку) использовать Scrollbar необязательно. Для прокрутки виджет может содержать специальные методы:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text("• yview_scroll(number, what): сдвигает текущее положение по вертикали. Параметр number указывает количество, на которое надо сдвигать. А параметр what определяет единицы сдвига и может принимать следующие значения: \"units\" (элемент) и \"pages\" (страницы)", size=14, color=colors["text_secondary"]),
                        ft.Text("• xview_scroll(number, what): сдвигает текущее положение по горизонтали", size=14, color=colors["text_secondary"]),
                        ft.Text("• yview_moveto(fraction): сдвигает область просмотра по вертикали на определенную часть, которая выражается во float от 0 до 1", size=14, color=colors["text_secondary"]),
                        ft.Text("• xview_moveto(fraction): сдвигает область просмотра на определенную часть по горизонтали", size=14, color=colors["text_secondary"]),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Например, сдвиг на два элемента списка вниз:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n  \nlanguages = ["Python", "JavaScript", "C#", "Java", "C++", "Rust", "Kotlin", "Swift",\n             "PHP", "Visual Basic.NET", "F#", "Ruby", "R", "Go",\n             "T-SQL", "PL-SQL", "Typescript"]\n  \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n  \nlanguages_var = StringVar(value=languages)\nlistbox = Listbox(listvariable=languages_var)\nlistbox.pack(expand=1, fill=BOTH)\n# сдвигаем скрол на 1 элемент внизу\nlistbox.yview_scroll(number=1, what="units")\n \nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_combobox_content(self):
        """Создание контента для темы 'Combobox'"""
        image_path1 = self.get_library_image_path("t60.png")
        image_path2 = self.get_library_image_path("t61.png")
        image_path3 = self.get_library_image_path("t62.png")
        colors = self.get_theme_colors()
        
        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            combobox_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            combobox_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Базовый Combobox", size=12, color=colors["text_secondary"]),
                    ft.Text("t60.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            combobox_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            combobox_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Привязка переменной", size=12, color=colors["text_secondary"]),
                    ft.Text("t61.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 3
        if os.path.exists(image_path3):
            combobox_image3 = ft.Image(
                src=image_path3,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            combobox_image3 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Обработка выбора", size=12, color=colors["text_secondary"]),
                    ft.Text("t62.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Combobox", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Виджет Combobox представляет выпадающий список, из которого пользователь может выбрать один элемент. Фактически он представляет комбинацию виджетов Entry и Listbox.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Основные параметры конструктора Combobox:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text("• values: список строк для отображения в Combobox", size=14, color=colors["text_secondary"]),
                        ft.Text("• background: фоновый цвет", size=14, color=colors["text_secondary"]),
                        ft.Text("• cursor: курсор указателя мыши при наведении на текстовое поле", size=14, color=colors["text_secondary"]),
                        ft.Text("• foreground: цвет текста", size=14, color=colors["text_secondary"]),
                        ft.Text("• font: шрифт текста", size=14, color=colors["text_secondary"]),
                        ft.Text("• justify: устанавливает выравнивание текста. Значение LEFT выравнивает текст по левому краю, CENTER - по центру, RIGHT - по правому краю", size=14, color=colors["text_secondary"]),
                        ft.Text("• show: задает маску для вводимых символов", size=14, color=colors["text_secondary"]),
                        ft.Text("• state: состояние элемента, может принимать значения NORMAL (по умолчанию) и DISABLED", size=14, color=colors["text_secondary"]),
                        ft.Text("• textvariable: устанавливает привязку к элементу StringVar", size=14, color=colors["text_secondary"]),
                        ft.Text("• height: высота элемента", size=14, color=colors["text_secondary"]),
                        ft.Text("• width: ширина элемента", size=14, color=colors["text_secondary"]),
                        ft.Container(height=20),
                        
                        ft.Text(
                            "Определим простейший выпадающий список:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nlanguages = ["Python", "C#", "Java", "JavaScript"]\ncombobox = ttk.Combobox(values=languages)\ncombobox.pack(anchor=NW, padx=6, pady=6)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь для элемента combobox в качестве источника значений устанавливается список languages:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 1
                        ft.Container(
                            content=combobox_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Combobox в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text(
                            "С помощью параметра textvariable мы можем установить привязку к выбранному в Combobox значению:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from cProfile import label\nfrom cgitb import text\nfrom tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nlanguages = ["Python", "C#", "Java", "JavaScript"]\n# по умолчанию будет выбран первый элемент из languages\nlanguages_var = StringVar(value=languages[0])   \n\nlabel = ttk.Label(textvariable=languages_var)\nlabel.pack(anchor=NW, padx=6, pady=6)\n\ncombobox = ttk.Combobox(textvariable=languages_var, values=languages)\ncombobox.pack(anchor=NW, padx=6, pady=6)\n\nprint(combobox.get())\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь выбранный в Combobox элемент привязан к переменной languages_var. По умолчанию выбран первый элемент списка languages. Для отслеживания изменения выбора определена метка Label, которая отображает выбранный элемент:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 2
                        ft.Container(
                            content=combobox_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Получение выбранного элемента в Combobox в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "По умолчанию мы можем ввести в текстовое поле в Combobox любое значение, даже то, которого нет в списке. Такое поведение не всегда может быть удобно. В этом случае мы можем установить для виджета состояние только для чтения, передав параметру \"state\" значение \"readonly\":",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('combobox = ttk.Combobox(textvariable=languages_var, values=languages, state="readonly")'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Выбранный элемент можно получить с помощью метода get() класса Combobox",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('selection = combobox.get()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "либо с помощью метода get() привязанной переменной",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('selection = languages_var.get()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Для установки нового значения можно использовать метод set():",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('languages_var.set(new_value)\ncombobox.set(new_value)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Для установки по индексу из привязанного набора значений также можно использовать метод current(newindex), где с помощью параметра newindex задается индекс выбранного значения. Например, выберем второй элемент:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('combobox.current(1)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Отслеживание выбора значения", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для обработки выбора элементов в Combobox необходимо прикрепить функцию обработки к событию <<ComboboxSelect>> с помощью метода bind:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('combobox.bind("<<ComboboxSelected>>", функция_обработки)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Например, динамически обработаем выбор в Combobox:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.create_code_block('from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\ndef selected(event):\n    # получаем выделенный элемент\n    selection = combobox.get()\n    print(selection)\n    label["text"] = f"вы выбрали: {selection}"\n\nlanguages = ["Python", "C#", "Java", "JavaScript"]\nlabel = ttk.Label()\nlabel.pack(anchor=NW, fill=X, padx=5, pady=5)\n\ncombobox = ttk.Combobox(values=languages, state="readonly")\ncombobox.pack(anchor=NW, fill=X, padx=5, pady=5)\ncombobox.bind("<<ComboboxSelected>>", selected)\n\nroot.mainloop()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае при изменении выбора в списке срабатывает функция selected. Функция должна принимать один параметр, который несет информацию о событии - здесь это параметр event. Хотя в данном случае он никак не используется.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "В самой функции получаем выбранный элемент и выводит соответствующую информацию на метку Label.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        # Изображение 3
                        ft.Container(
                            content=combobox_image3,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Обработка выбора элементов в Combobox в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_scale_content(self):
        """Создание контента для темы 'Scale'"""
        image_path1 = self.get_library_image_path("t63.png")
        image_path2 = self.get_library_image_path("t64.png")
        image_path3 = self.get_library_image_path("t65.png")
        colors = self.get_theme_colors()
        
        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            scale_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            scale_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение Scale", size=12, color=colors["text_secondary"]),
                    ft.Text("t63.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            scale_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            scale_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение Scale", size=12, color=colors["text_secondary"]),
                    ft.Text("t64.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        # Проверяем существует ли изображение 3
        if os.path.exists(image_path3):
            scale_image3 = ft.Image(
                src=image_path3,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            scale_image3 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение Scale", size=12, color=colors["text_secondary"]),
                    ft.Text("t65.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Scale - Ползунок со шкалой", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Scale представляет ползунок со шкалой, на которой можно выбрать одно из числовых значений.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text("Основные параметры Scale", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Среди параметров Scale следует отметить следующие:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''orient: направление виджета. Может принимать значения HORIZONTAL/"horizontal" и VERTICAL/"vertical"\n\nfrom_: начальное значение шкалы виджета, представляет тип float\n\nto: конечное значение шкалы виджета, представляет тип float\n\nlength: длина виджета\n\ncommand: функция, которая выполняется при изменении текущего значения\n\nvalue: текущее значение шкалы виджета, представляет тип float\n\nvariable: переменная IntVar или DoubleVar, к которой привязано текущее значение виджета'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Простейший Scale", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Простейший Scale в горизонтальной и вертикальной ориентации:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x250") \n\nverticalScale = ttk.Scale(orient=VERTICAL, length=200, from_=1.0, to=100.0, value=50)\nverticalScale.pack()\n\nhorizontalScale = ttk.Scale(orient=HORIZONTAL, length=200, from_=1.0, to=100.0, value=30)\nhorizontalScale.pack()\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 1
                        ft.Container(
                            content=scale_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Виджет Scale в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Привязка к переменной", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200") \n\nval = IntVar(value=10)\n\nttk.Label(textvariable=val).pack(anchor=NW)\n\nhorizontalScale = ttk.Scale(orient=HORIZONTAL, length=200, from_=1.0, to=100.0, variable=val)\nhorizontalScale.pack(anchor=NW)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае и метка Label, и виджет Scale привязаны к переменной val:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 2
                        ft.Container(
                            content=scale_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Виджет Scale и привязка к переменной IntVar в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Обработка изменения значения", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Параметр command позволяет установить функцию, которая будет выполняться при изменении текущего значения Scale. В качестве параметра в эту функцию передается новое значение:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200") \n\ndef change(newVal):\n    label["text"] = newVal\n    # или так\n    # label["text"] = scale.get()\n\nlabel = ttk.Label()\nlabel.pack(anchor=NW)\n\nscale = ttk.Scale(orient=HORIZONTAL, length=200, from_=1.0, to=100.0, command=change)\nscale.pack(anchor=NW)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае новое значение Scale передается в метку label:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 3
                        ft.Container(
                            content=scale_image3,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Обработка изменения значения в виджете Scale в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Для получения текущего значения Scale можно использовать его метод get():",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('label["text"] = scale.get()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Стоит учитывать, что передаваемое в функцию значение newVal представляет строку, а точнее значение типа float в строковом виде. Но что делать, если мы хотим выводить в метке label не строку или даже float, а целое число? В этом случае необходимо выполнить цепь преобразований:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''def change(newVal):\n    float_value = float(newVal)     # получаем из строки значение float\n    int_value = round(float_value)  # округляем до целочисленного значения\n    label["text"] = int_value'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_spinbox_content(self):
        """Создание контента для темы 'Spinbox'"""
        image_path1 = self.get_library_image_path("t66.png")
        image_path2 = self.get_library_image_path("t67.png")
        image_path3 = self.get_library_image_path("t68.png")
        image_path4 = self.get_library_image_path("t69.png")
        colors = self.get_theme_colors()
        
        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            spinbox_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            spinbox_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение Spinbox", size=12, color=colors["text_secondary"]),
                    ft.Text("t66.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            spinbox_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            spinbox_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение Spinbox", size=12, color=colors["text_secondary"]),
                    ft.Text("t67.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        # Проверяем существует ли изображение 3
        if os.path.exists(image_path3):
            spinbox_image3 = ft.Image(
                src=image_path3,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            spinbox_image3 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение Spinbox", size=12, color=colors["text_secondary"]),
                    ft.Text("t68.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        # Проверяем существует ли изображение 4
        if os.path.exists(image_path4):
            spinbox_image4 = ft.Image(
                src=image_path4,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            spinbox_image4 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение Spinbox", size=12, color=colors["text_secondary"]),
                    ft.Text("t69.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Spinbox - Выбор значения из списка", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Виджет Spinbox позволяет выбрать значение (чаще число) из некоторого списка.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text("Основные параметры Spinbox", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''values: набор значений виджета в виде списка или кортежа\n\nfrom_: минимальное значение (тип float)\n\nto: максимальное значение (тип float)\n\nincrement: приращение значения (тип float)\n\ntextvariable: определяет переменную StringVar, которая хранит текущее значение виджета\n\ncommand: указывает на функцию, которая вызывается при изменении значения виджета\n\nwrap: при значении True создает зацикленный список, при котором после минимального значения идет максимальное\n\nbackground: фоновый цвет\n\nforeground: цвет текста\n\nfont: шрифт виджета\n\njustify: выравнивание текста, принимает значения "left" (по левому краю), "right" (по правому краю) и "center" (по центру)\n\nwidth: ширина виджета\n\nstate: состояние виджета'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Простейший Spinbox", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200") \n\nspinbox = ttk.Spinbox(from_=1.0, to=100.0)\nspinbox.pack(anchor=NW)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае мы можем выбрать одно из чисел от 1 до 100. При нажатии на стрелочки вверх и вниз на виджете значение виджета будет увеличиваться и уменьшаться на единицу:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 1
                        ft.Container(
                            content=spinbox_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Spinbox в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "По умолчанию приращение идет на единицу, но с помощью параметра increment можно установить другое значение, например, приращение на 2:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('ttk.Spinbox(from_=1.0, to=100.0, increment=2)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Также по умолчанию мы можем, не используя стрелочки, ввести в текстовое поле виджета какое-либо значение, даже то, которое не входит в диапазон значений. Если нам надо запретить ввод значений в текстовое поле и оставить доступными для выбора значений только стрелочки, то для этого можно установить для параметра state значение readonly:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('spinbox = ttk.Spinbox(from_=1.0, to=100.0, state="readonly")'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Привязка к переменной", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "С помощью параметра textvariable можно привязать значение Spinbox к переменной StringVar:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x150") \n\nspinbox_var = StringVar(value=22) # начальное значение 22\n\nlabel = ttk.Label(textvariable=spinbox_var)\nlabel.pack(anchor=NW)\n\nspinbox = ttk.Spinbox(from_=1.0, to=100.0, textvariable=spinbox_var)\nspinbox.pack(anchor=NW)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь для наглядности добавлена метка, которая выводит выбранное значение. В качестве начального значения применяется число 22.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 2
                        ft.Container(
                            content=spinbox_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Spinbox и привязка к переменной StringVar в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Получение текущего значения", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для получения текущего значения у Spinbox вызывается метод get():",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('current_value = spinbox.get()'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Обработка изменения значения", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Чтобы обработать изменение значения нужно определить функцию, которая будет срабатывать при изменении значения, и передать ее параметру command:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200") \n\ndef change():\n    label["text"] = spinbox.get()\n\nlabel = ttk.Label()\nlabel.pack(anchor=NW)\n\nspinbox = ttk.Spinbox(from_=1.0, to=100.0, command=change)\nspinbox.pack(anchor=NW)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае при изменении значения срабатывает функция change в которой изменяем текст метки label в соответствии с новым значением:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 3
                        ft.Container(
                            content=spinbox_image3,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Обработка изменения значения в Spinbox в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Установка набора значений", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Данный виджет необязательно должен представлять список из числовых значений. В реальности это может быть любой набор значений в виде списка или кортежа, который можно установить с помощью параметра values:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x150") \n\nspinbox_var = StringVar()\n\nlanguages=["Python", "JavaScript", "C#", "Java", "C++"]\n\nlabel = ttk.Label(textvariable=spinbox_var)\nlabel.pack(anchor=NW)\n\nspinbox = ttk.Spinbox(textvariable=spinbox_var, values=languages)\nspinbox.pack(anchor=NW)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае Spinbox позволяет выбрать одно из значений из списка languages:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 4
                        ft.Container(
                            content=spinbox_image4,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Установка значений в Spinbox в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_progressbar_content(self):
        """Создание контента для темы 'Progressbar'"""
        image_path1 = self.get_library_image_path("t70.png")
        image_path2 = self.get_library_image_path("t71.png")
        image_path3 = self.get_library_image_path("t72.png")
        image_path4 = self.get_library_image_path("t73.png")
        colors = self.get_theme_colors()
        
        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            progressbar_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            progressbar_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение Progressbar", size=12, color=colors["text_secondary"]),
                    ft.Text("t70.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            progressbar_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            progressbar_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение Progressbar", size=12, color=colors["text_secondary"]),
                    ft.Text("t71.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        # Проверяем существует ли изображение 3
        if os.path.exists(image_path3):
            progressbar_image3 = ft.Image(
                src=image_path3,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            progressbar_image3 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение Progressbar", size=12, color=colors["text_secondary"]),
                    ft.Text("t72.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        # Проверяем существует ли изображение 4
        if os.path.exists(image_path4):
            progressbar_image4 = ft.Image(
                src=image_path4,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            progressbar_image4 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение Progressbar", size=12, color=colors["text_secondary"]),
                    ft.Text("t73.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Progressbar - Индикатор выполнения", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Виджет Progressbar предназначен для отображения хода выполнения какого-либо процесса.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text("Основные параметры Progressbar", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''value: текущее значение виджета (тип float)\n\nmaximum: максимальное значение (тип float)\n\nvariable: определяет переменную IntVar/DoublerVar, которая хранит текущее значение виджета\n\nmode: определяет режим, принимает значения "determinate" (конечный) и "indeterminate" (бесконечный)\n\norient: определяет ориентацию виджета, принимает значения "vertical" (вертикальный) и "horizontal" (горизонтальный)\n\nlength: длина виджета'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Простейший Progressbar", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Определим вертикальный и горизонтальный Progressbar:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x150") \n\n# вертикальный Progressbar\nttk.Progressbar(orient="vertical", length=100, value=40).pack(pady=5)\n\n# горизонтальный Progressbar\nttk.Progressbar(orient="horizontal", length=150, value=20).pack(pady=5)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 1
                        ft.Container(
                            content=progressbar_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Progressbar в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Привязка к переменной", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "С помощью параметра variable можно привязать значение прогрессбара к переменной типа IntVar или DoublerVar:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x150") \n\nvalue_var = IntVar(value=30)\n\nprogressbar =  ttk.Progressbar(orient="horizontal", variable=value_var)\nprogressbar.pack(fill=X, padx=6, pady=6)\n\nlabel = ttk.Label(textvariable=value_var)\nlabel.pack(anchor=NW, padx=6, pady=6)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае значение прогрессбара привязано к переменной value_var, значение которой выводит метка label:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 2
                        ft.Container(
                            content=progressbar_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Привязка Progressbar к IntVar в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Методы Progressbar", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Некоторые важные методы виджета:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''start([interval]): запускает перемещение индикатора через определенные интервалы времени. Каждый раз, когда пройдет очередной интервал, индикатор смещается на одно деление вперед. По умолчанию интервал равен 50 миллисекунд\n\nstep([delta]): увеличивает значение индикатора на значение из параметра delta (по умолчанию равен 1.0)\n\nstop(): останавливает перемещение индикатора'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Применим методы:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x150") \n\nvalue_var = IntVar()\n\nprogressbar =  ttk.Progressbar(orient="horizontal", variable=value_var)\nprogressbar.pack(fill=X, padx=6, pady=6)\n\nlabel = ttk.Label(textvariable=value_var)\nlabel.pack(anchor=NW, padx=6, pady=6)\n\ndef start(): progressbar.start(1000) # запускаем progressbar\ndef stop(): progressbar.stop()      # останавливаем progressbar\n\nstart_btn = ttk.Button(text="Start", command=start)\nstart_btn.pack(anchor=SW, side=LEFT, padx=6, pady=6)\nstop_btn = ttk.Button(text="Stop", command=stop)\nstop_btn.pack(anchor=SE, side=RIGHT, padx=6, pady=6)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае по нажатию на кнопку start_btn запускаем перемещение индикатора - через каждые 1000 миллисекунд (1 секунду) индикатор перемещается на одно деление вперед. По нажатию на кнопку stop_btn останавливаем движение индикатора.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 3
                        ft.Container(
                            content=progressbar_image3,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Запуск Progressbar в приложении на Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Режим прогрессбара", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Параметр mode отвечает за установку режима прогрессбара и может принимать два значения:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''"indeterminate": прогрессбар показывает индикатор, который перемещается без остановки между двумя краями виджета, то есть фактически бесконечно продолжает перемещение. Данный режим подходит, когда сложно расчитать, насколько должен перемещаться индикатор при отображении хода некоторой задачи\n\n"determinate": индикатор прогрессбара проходит от начала до конца и затем завершает перемещение. Значение по умолчанию. Подходит для отображения таких процессов, где можно подсчитать перемещение индикатора. Например, копируется 100 файлов, и, если параметр maximum равен 100, при копирования одного файла перемещаем индикатор на одно деление вперед.'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Применение режима 'determinate' по сути уже рассматривалось выше, так как это режим по умолчанию. Посмотрим на пример применения режима 'indeterminate':",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x150") \n\nprogressbar =  ttk.Progressbar(orient="horizontal", mode="indeterminate")\nprogressbar.pack(fill=X, padx=10, pady=10)\n\nstart_btn = ttk.Button(text="Start", command=progressbar.start)\nstart_btn.pack(anchor=SW, side=LEFT, padx=10, pady=10)\n\nstop_btn = ttk.Button(text="Stop", command=progressbar.stop)\nstop_btn.pack(anchor=SE, side=RIGHT, padx=10, pady=10)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "По нажатию на кнопку start_btn также запускается процесс. Когда индикатор дойдет до конца, он начинает обратное движение:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 4
                        ft.Container(
                            content=progressbar_image4,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("indeterminate mode в Progressbar в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_menu_content(self):
        """Создание контента для темы 'Menu'"""
        image_path1 = self.get_library_image_path("t74.png")
        image_path2 = self.get_library_image_path("t75.png")
        image_path3 = self.get_library_image_path("t76.png")
        image_path4 = self.get_library_image_path("t77.png")
        image_path5 = self.get_library_image_path("t78.png")
        colors = self.get_theme_colors()
        
        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            menu_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            menu_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение Menu", size=12, color=colors["text_secondary"]),
                    ft.Text("t74.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            menu_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            menu_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение Menu", size=12, color=colors["text_secondary"]),
                    ft.Text("t75.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        # Проверяем существует ли изображение 3
        if os.path.exists(image_path3):
            menu_image3 = ft.Image(
                src=image_path3,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            menu_image3 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение Menu", size=12, color=colors["text_secondary"]),
                    ft.Text("t76.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        # Проверяем существует ли изображение 4
        if os.path.exists(image_path4):
            menu_image4 = ft.Image(
                src=image_path4,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            menu_image4 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение Menu", size=12, color=colors["text_secondary"]),
                    ft.Text("t77.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        # Проверяем существует ли изображение 5
        if os.path.exists(image_path5):
            menu_image5 = ft.Image(
                src=image_path5,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            menu_image5 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение Menu", size=12, color=colors["text_secondary"]),
                    ft.Text("t78.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Menu - Иерархическое меню", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Для создания иерархического меню в tkinter применяется виджет Menu.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text("Основные параметры Menu", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''activebackground: цвет активного пункта меню\n\nactiveborderwidth: толщина границы активного пункта меню\n\nactiveforeground: цвет текста активного пункта меню\n\nbackground / bg: фоновый цвет\n\nbd: толщина границы\n\ncursor: курсор указателя мыши при наведении на меню\n\ndisabledforeground: цвет, когда меню находится в состоянии DISABLED\n\nfont: шрифт текста\n\nforeground / fg: цвет текста\n\ntearoff: меню может быть отсоединено от графического окна. В частности, при создании подменю а скриншоте можно увидеть прерывающуюся линию в верху подменю, за которую его можно отсоединить. Однако при значении tearoff=0 подменю не сможет быть отсоединено.'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Методы добавления элементов", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Меню может содержать много элементов, причем эти элементы сами могут представлять меню и содержать другие элементы. В зависимости от того, какой тип элементов мы хотим добавить в меню, будет отличаться метод, используемый для их добавления. В частности, нам доступны следующие методы:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''add_command(options): добавляет элемент меню через параметр options\n\nadd_cascade(options): добавляет элемент меню, который в свою очередь может представлять подменю\n\nadd_separator(): добавляет линию-разграничитель\n\nadd_radiobutton(options): добавляет в меню переключатель\n\nadd_checkbutton(options): добавляет в меню флажок'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Простейшее меню", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Создадим простейшее меню:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x150") \n\nmain_menu = Menu()\nmain_menu.add_cascade(label="File")\nmain_menu.add_cascade(label="Edit")\nmain_menu.add_cascade(label="View")\n\nroot.config(menu=main_menu)\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Для добавления пунктов меню у объекта Menu вызывается метод add_cascade(). В этот метод передаются параметры пункта меню, в данном случае они представлены текстовой меткой, устанавливаемой через параметр label.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Но просто создать меню - еще недостаточно. Его надо установить для текущего окна с помощью параметра menu в методе config(). В итоге графическое окно будет иметь следующее меню:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 1
                        ft.Container(
                            content=menu_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Меню в tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Добавление подменю", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Теперь добавим подменю:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x150") \n\nmain_menu = Menu()\n\nfile_menu = Menu()\nfile_menu.add_command(label="New")\nfile_menu.add_command(label="Save")\nfile_menu.add_command(label="Open")\nfile_menu.add_separator()\nfile_menu.add_command(label="Exit")\n\nmain_menu.add_cascade(label="File", menu=file_menu)\nmain_menu.add_cascade(label="Edit")\nmain_menu.add_cascade(label="View")\n\nroot.config(menu=main_menu)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь определяется подменю file_menu, которое добавляется в первый пункт основного меню благодаря установке опции menu=file_menu:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('main_menu.add_cascade(label="File", menu=file_menu)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 2
                        ft.Container(
                            content=menu_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Подменю и сепаратор в tkinter в Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Но обратите внимание на пунктирную линию в подменю, которая совершенно не нужна и непонятно откуда появляется. Чтобы избавиться от этой линии, надо для нужного пункта меню установить параметр tearoff=0:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('file_menu = Menu(tearoff=0)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Однако так как подпунктов меню может быть много, чтобы для каждого не прописывать этот параметр, то проще отключить все это глобально с помощью следующей строки кода:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('root.option_add("*tearOff", FALSE)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Полный код:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x150") \n\nroot.option_add("*tearOff", FALSE)\n\nmain_menu = Menu()\n\nfile_menu = Menu()\nfile_menu.add_command(label="New")\nfile_menu.add_command(label="Save")\nfile_menu.add_command(label="Open")\nfile_menu.add_separator()\nfile_menu.add_command(label="Exit")\n\nmain_menu.add_cascade(label="File", menu=file_menu)\nmain_menu.add_cascade(label="Edit")\nmain_menu.add_cascade(label="View")\n\nroot.config(menu=main_menu)\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 3
                        ft.Container(
                            content=menu_image3,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Подменю и сепаратор в виджете Menu в приложении на tkinter в Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Сложные иерархии меню", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Подобным образом можно создавать и более глубокие иерархии меню:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x150") \n\nroot.option_add("*tearOff", FALSE)\n\nmain_menu = Menu()\nfile_menu = Menu()\nsettings_menu = Menu()\n\nsettings_menu.add_command(label="Save")\nsettings_menu.add_command(label="Open")\n\nfile_menu.add_cascade(label="Settings", menu=settings_menu) \nfile_menu.add_separator()\nfile_menu.add_command(label="Exit")\n\nmain_menu.add_cascade(label="File", menu=file_menu)\n\nroot.config(menu=main_menu)\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 4
                        ft.Container(
                            content=menu_image4,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Сложные подменю в виджете Menu в приложении на tkinter в Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Взаимодействие с меню", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Отличительной особенностью элементов меню является способность реагировать на нажатия пользователя. Для этого у каждого элемента меню можно задать параметр command, который устанавливает ссылку на функцию, выполняемую при нажатии.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import messagebox\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x150") \n\nroot.option_add("*tearOff", FALSE)\n\ndef edit_click():\n    messagebox.showinfo("GUI Python", "Нажата опция Edit")\n\nmain_menu = Menu()\n\nmain_menu.add_cascade(label="File")\nmain_menu.add_cascade(label="Edit", command=edit_click)\nmain_menu.add_cascade(label="View")\n\nroot.config(menu=main_menu)\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 5
                        ft.Container(
                            content=menu_image5,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Обработка нажатия меню в виджете Menu в приложении на tkinter в Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_notebook_content(self):
        """Создание контента для темы 'Notebook'"""
        image_path1 = self.get_library_image_path("t79.png")
        image_path2 = self.get_library_image_path("t80.png")
        colors = self.get_theme_colors()
        
        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            notebook_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            notebook_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение Notebook", size=12, color=colors["text_secondary"]),
                    ft.Text("t79.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            notebook_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            notebook_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение Notebook", size=12, color=colors["text_secondary"]),
                    ft.Text("t80.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Notebook - Набор вкладок", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Виджет Notebook представляет набор вкладок.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text("Основные параметры Notebook", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''width: ширина виджета\n\nheight: высота виджета\n\ncursor: курсор при наведении на виджет\n\npadding: отступы от границ виджета до его содержимого\n\nstyle: стиль виджета'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Методы управления вкладками", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для управления вкладками Notebook предоставляет ряд методов, в частности, для добавления вкладки применяется метод add():",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''add(child, state, sticky, padding, text, image, compound, underline)'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text("Параметры метода add()", size=16, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''child: добавляемый виджет, для которого собственно и создается вкладка. Обычно это Frame, который затем добавляет другие виджеты\n\nstate: состояние вкладки. Возможные значения: "normal", "disabled", "hidden"\n\nsticky: определяет прикрепление виджета к определенной стороне вкладки\n\npadding: отступы от границ вкладки до внутреннего содержимого\n\ntext: заголовок вкладки\n\nimage: изображение в заголовке вкладки\n\ncompound: управляет расположением изображения и текста в заголовке вкладки\n\nunderline: определяет номер подчеркнутого символа в заголовке вкладки'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Другие методы", size=16, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Кроме того, чтобы скрыть временно вкладку, применяется метод hide():",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('hide(tabId)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "В качестве параметра принимает идентификатор вкладки, который по умолчанию представляет числовой индекс вкладки начиная с 0.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Чтобы совсем удалить вкладку, применяется метод forget():",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('forget(child)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "В качестве параметра в метод передается удаляемый виджет.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Простейший пример", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Рассмотрим простейший пример:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200") \n\n# создаем набор вкладок\nnotebook = ttk.Notebook()\nnotebook.pack(expand=True, fill=BOTH)\n\n# создаем пару фреймов\nframe1 = ttk.Frame(notebook)\nframe2 = ttk.Frame(notebook)\n\nframe1.pack(fill=BOTH, expand=True)\nframe2.pack(fill=BOTH, expand=True)\n\n# добавляем фреймы в качестве вкладок\nnotebook.add(frame1, text="Python")\nnotebook.add(frame2, text="Java")\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь определяются два фрейма, для которых создаются отдельные вкладки:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 1
                        ft.Container(
                            content=notebook_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Notebook и создание вкладок в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Добавление изображений", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "За установку изображения в заголовке вкладки отвечает параметр image метода add. Кроме того, с помощью параметра compound можно задать расположение картинки относительно текста. В частности, параметр compound может принимать следующие значения:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''top: изображение поверх текста\n\nbottom: изображение под текстом\n\nleft: изображение слева от текста\n\nright: изображение справа от текста\n\nnone: при наличии изображения отображается только изображение\n\ntext: отображается только текст\n\nimage: отображается только изображение'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Например, отобразим картинку слева от текста:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200") \n\n# создаем набор вкладок\nnotebook = ttk.Notebook()\nnotebook.pack(expand=True, fill=BOTH)\n\n# создаем пару фреймов\nframe1 = ttk.Frame(notebook)\nframe2 = ttk.Frame(notebook)\n\nframe1.pack(fill=BOTH, expand=True)\nframe2.pack(fill=BOTH, expand=True)\n\npython_logo = PhotoImage(file="./python_mc.png")\njava_logo = PhotoImage(file="./java_mc.png")\n# добавляем фреймы в качестве вкладок\nnotebook.add(frame1, text="Python", image=python_logo, compound=LEFT)\nnotebook.add(frame2, text="Java", image=java_logo, compound=LEFT)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Следует отметить, что высота заголовка вкладки устанавливается в соответствии с высотой картинки:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 2
                        ft.Container(
                            content=notebook_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Notebook и добавление изображения на вкладки в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )
    
    def create_text_widget_content(self):
        """Создание контента для темы 'Создание многострочного текстового поля'"""
        image_path1 = self.get_library_image_path("t81.png")
        image_path2 = self.get_library_image_path("t82.png")
        image_path3 = self.get_library_image_path("t83.png")
        colors = self.get_theme_colors()
        
        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            text_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            text_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение Text виджета", size=12, color=colors["text_secondary"]),
                    ft.Text("t81.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            text_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            text_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение переноса текста", size=12, color=colors["text_secondary"]),
                    ft.Text("t82.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        # Проверяем существует ли изображение 3
        if os.path.exists(image_path3):
            text_image3 = ft.Image(
                src=image_path3,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            text_image3 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение прокрутки", size=12, color=colors["text_secondary"]),
                    ft.Text("t83.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Создание многострочного текстового поля", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Text предназначен для отображения и редактирования многострочного текста. Стоит отметить, что данный виджет доступен только в основном пакете tkinter, в пакете tkinter.ttk аналога нет.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Основные параметры конструктора Text:", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "bd / borderwidth: толщина границы\n\nbg/background: фоновый цвет\n\nfg/foreground: цвет текста\n\nfont: шрифт текста, например, font=\"Arial 14\" - шрифт Arial высотой 14px, или font=(\"Verdana\", 13, \"bold\") - шрифт Verdana высотой 13px с выделением жирным\n\nheight: высота в строках\n\npadx: отступ от границ кнопки до ее текста справа и слева\n\npady: отступ от границ кнопки до ее текста сверху и снизу\n\nrelief: определяет тип границы, может принимать значения SUNKEN, RAISED, GROOVE, RIDGE\n\nstate: устанавливает состояние кнопки, может принимать значения DISABLED, ACTIVE, NORMAL (по умолчанию)\n\nwidth: ширина в символах\n\nwrap: указывает, каким образом переносить текст, если он не вмещается в границы виджета",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Простейший Text:", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\neditor = Text()\neditor.pack(fill=BOTH, expand=1)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 1
                        ft.Container(
                            content=text_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("виджет Text в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Перенос текста", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Иногда предложения в текстовом поле могут быть очень большими, что могут не помещаться в отведенное для них пространство виджета. В этом случае большое значение имеет стратегия переноса, которая устанавливается с помощью параметра wrap. Этот параметр может принимать следующие параметры:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "none: переносы отстуствуют, но можно сделать горизонтальную прокрутку\n\nchar: переносы осуществляются по символам\n\nword: переносы осуществляются по словам",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text("Сравнение:", size=16, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\nchar_editor = Text(height=5, wrap="char")\nchar_editor.pack(anchor=N, fill=X)\n\nword_editor = Text(height=5, wrap="word")\nword_editor.pack(anchor=S, fill=X)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 2
                        ft.Container(
                            content=text_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Перенос текста в виджете Text в Tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Прокрутка текста", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Используя Scrollbar, можно добавить в Text прокрутку текста:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\nroot.grid_columnconfigure(0, weight = 1)\nroot.grid_rowconfigure(0, weight = 1)\n\neditor = Text(wrap = "none")\neditor.grid(column = 0, row = 0, sticky = NSEW)\n\nys = ttk.Scrollbar(orient = "vertical", command = editor.yview)\nys.grid(column = 1, row = 0, sticky = NS)\nxs = ttk.Scrollbar(orient = "horizontal", command = editor.xview)\nxs.grid(column = 0, row = 1, sticky = EW)\n\neditor["yscrollcommand"] = ys.set\neditor["xscrollcommand"] = xs.set\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь для виджета определяются две полосы прокрутки - вертикальная и горизонтальная, соответственно, для каждой определяется свой элемент Scrollbar. Один (ys) имеет вертикальную ориентацию, а второй (xs) - горизонтальную. А у Text устанавливаются команды yscrollcommand и xscrollcommand с помощью соответствующих скроллбаров.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 3
                        ft.Container(
                            content=text_image3,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("вертикальная и горизонтальная прокрутка в Text в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Стоит отметить, что поскольку создание прокрутки для виджета Text является довольно распространенной задачей, то в Tkinter также по умолчанию есть аналог виджета Text с готовой вертикальной прокруткой - ScrolledText (в пакете tkinter.scrolledtext):",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter.scrolledtext import ScrolledText\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x150")\n\nst = ScrolledText(root, width=50,  height=10)\nst.pack(fill=BOTH, side=LEFT, expand=True)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_text_operations_content(self):
        """Создание контента для темы 'Основные операции с виджетом Text'"""
        image_path1 = self.get_library_image_path("t84.png")
        image_path2 = self.get_library_image_path("t85.png")
        image_path3 = self.get_library_image_path("t86.png")
        image_path4 = self.get_library_image_path("t87.png")
        image_path5 = self.get_library_image_path("t88.png")
        colors = self.get_theme_colors()
        
        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            text_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            text_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение добавления текста", size=12, color=colors["text_secondary"]),
                    ft.Text("t84.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            text_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            text_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение получения текста", size=12, color=colors["text_secondary"]),
                    ft.Text("t85.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        # Проверяем существует ли изображение 3
        if os.path.exists(image_path3):
            text_image3 = ft.Image(
                src=image_path3,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            text_image3 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение замены текста", size=12, color=colors["text_secondary"]),
                    ft.Text("t86.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        # Проверяем существует ли изображение 4
        if os.path.exists(image_path4):
            text_image4 = ft.Image(
                src=image_path4,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            text_image4 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение обработки ввода", size=12, color=colors["text_secondary"]),
                    ft.Text("t87.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        # Проверяем существует ли изображение 5
        if os.path.exists(image_path5):
            text_image5 = ft.Image(
                src=image_path5,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            text_image5 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение обработки выделения", size=12, color=colors["text_secondary"]),
                    ft.Text("t88.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Основные операции с виджетом Text", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text("Добавление текста", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для добавления текста применяется метод insert():",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('insert(index, chars)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Первый параметр представляет позицию вставки в формате \"line.column\" - сначала идет номер строки, а затем номер символа. Второй параметр - собственно вставляемый текст. Например, вставка в начало:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('editor.insert("1.0", "Hello")'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Для вставки в конец для позиции передается значение END:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\neditor = Text()\neditor.pack(fill=BOTH, expand=1)\n\neditor.insert("1.0", "Hello World")     # вставка в начало\neditor.insert(END, "\\nBye World")       # вставка в конец\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 1
                        ft.Container(
                            content=text_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Добавление строк в виджет Text в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Получение текста", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для получения введенного текста применяется метод get():",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('get(start, end)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Параметр start указывает на начальный символ, а end - на конечный символ, текст между которыми надо получить. Оба параметра в формате \"line.colunm\", где line - номер строки, а \"column\" - номер символа. Для указания последнего символа применяется константа END:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("300x200")\n\neditor = Text(height=5)\neditor.pack(anchor=N, fill=X)\n\nlabel=ttk.Label()\nlabel.pack(anchor=N, fill=BOTH)\n\ndef get_text():\n    label["text"] = editor.get("1.0", "end")\n\nbutton = ttk.Button(text="Click", command=get_text)\nbutton.pack(side=BOTTOM)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае по нажатию на кнопку срабатывает функция get_text(), которая получает текст и передается его для отображения в метку label:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 2
                        ft.Container(
                            content=text_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Получение введенного текста из виджета Text в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Удаление текста", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для удаления текста применяется метод delete()",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('delete(start, end)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Параметр start указывает на начальный символ, а end - на конечный символ, текст между которыми надо удалить. Оба параметра в формате \"line.colunm\", где line - номер строки, а \"column\" - номер символа. Для указания последнего символа применяется константа END. Например, определим кнопку, которая будет удалять весь текст из виджета:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("300x200")\n\neditor = Text(height=10)\neditor.pack(anchor=N, fill=BOTH)\n\ndef delete_text():\n    editor.delete("1.0", END)\n\nbutton = ttk.Button(text="Clear", command=delete_text)\nbutton.pack(side=BOTTOM)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Замена текста", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для замены текста применяется метод replace():",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('replace(start, end, chars)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Параметр start указывает на начальный символ, а end - на конечный символ, текст между которыми надо заменить. Оба параметра в формате \"line.colunm\", где line - номер строки, а \"column\" - номер символа. Для указания последнего символа применяется константа END. Последний параметр - chars - строка, на которую надо заменить. Например, замена первых четырех символов на строку \"дама\":",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("300x200")\n\neditor = Text(height=10)\neditor.pack(anchor=N, fill=BOTH)\neditor.insert("1.0", "мама мыла раму")\n\ndef edit_text():\n    editor.replace("1.0", "1.4", "дама")\n\nbutton = ttk.Button(text="Replace", command=edit_text)\nbutton.pack(side=BOTTOM)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 3
                        ft.Container(
                            content=text_image3,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Замена текста в виджете Text в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Повтор и отмена операций", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Методы edit_undo() и edit_redo() позволяют соответственно отменить и повторить операцию (добавление, изменение, удаление текста). Данные методы применяются, если в виджете Text параметр undo равен True. Стоит отметить, что данные методы оперируют своим стеком операций, в котором сохраняются данные операций. Однако если стек для соответствующего метода пуст, то вызов метода вызывает исключение. Простейший пример, где по нажатию на кнопку вызывается отмена или возврат операции:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\nroot.grid_columnconfigure(0, weight = 1)\nroot.grid_columnconfigure(1, weight = 1)\nroot.grid_rowconfigure(0, weight = 1)\n\neditor = Text(undo=True)\neditor.grid(column = 0, columnspan=2, row = 0, sticky = NSEW)\n\ndef undo():\n    editor.edit_undo()\n\ndef redo():\n    editor.edit_redo()\n\nredo_button = ttk.Button(text="Undo", command=undo)\nredo_button.grid(column=0, row=1)\nclear_button = ttk.Button(text="Redo", command=redo)\nclear_button.grid(column=1, row=1)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Выделение текста", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для управления выделением текста виджет Text обладает следующими методами:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "selection_get(): возвращает выделенный фрагмент\n\nselection_clear(): снимает выделение",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text("Применим данные методы:", size=16, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\ndef get_selection():\n    label["text"]=editor.selection_get()\n\ndef clear_selection():\n    editor.selection_clear()\n\neditor = Text(height=5)\neditor.pack(fill=X)\n\nlabel = ttk.Label()\nlabel.pack(anchor=NW)\n\nget_button = ttk.Button(text="Get selection", command=get_selection)\nget_button.pack(side=LEFT)\nclear_button = ttk.Button(text="Clear", command=clear_selection)\nclear_button.pack(side=RIGHT)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае по нажатию на кнопку get_button срабатывает функция get_selection, которая передает в метку label выделенный текст. При нажатии на кнопку clear_button срабатывает функция clear_selection, которая снимает выделение.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("События", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Достаточно часто встречает необходимость обработки ввода текста. Для виджета Text определено событие <<Modified>>, которое срабатывает при изменении текста в текстовом поле. Однако оно срабатывает один раз. И в этом случае мы можем обработать стандартные события клавиатуры. Например, событие освобождения клавиши <KeyRelease>:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\ndef on_modified(event):\n    label["text"]=editor.get("1.0", END)\n\neditor = Text(height=8)\neditor.pack(fill=X)\neditor.bind("<KeyRelease>", on_modified)\n\nlabel = ttk.Label()\nlabel.pack(anchor=NW)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае при освобождении клавиши будет срабатывать функция on_modified, в которой метке label передается весь введенный текст:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 4
                        ft.Container(
                            content=text_image4,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("обработка ввода текста в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Другую распространенную задачу представляет динамическое получение выделенного текста. В этом случае мы можем обработать событие <<Selection>>. Например, при выделении текста выведем выделенный фрагмент в метку Label:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n\ndef on_modified(event):\n    label["text"]=editor.selection_get()\n\neditor = Text(height=8)\neditor.pack(fill=X)\neditor.bind("<<Selection>>", on_modified)\n\nlabel = ttk.Label()\nlabel.pack(anchor=NW)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 5
                        ft.Container(
                            content=text_image5,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("обработка выделения текста в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_text_styling_content(self):
        """Создание контента для темы 'Стилизация и добавление виджетов в Text'"""
        image_path1 = self.get_library_image_path("t89.png")
        image_path2 = self.get_library_image_path("t90.png")
        image_path3 = self.get_library_image_path("t91.png")
        colors = self.get_theme_colors()

        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            text_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            text_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение тегов", size=12, color=colors["text_secondary"]),
                    ft.Text("t89.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            text_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            text_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение добавления картинки", size=12, color=colors["text_secondary"]),
                    ft.Text("t90.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        # Проверяем существует ли изображение 3
        if os.path.exists(image_path3):
            text_image3 = ft.Image(
                src=image_path3,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            text_image3 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение добавления виджетов", size=12, color=colors["text_secondary"]),
                    ft.Text("t91.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Стилизация и добавление виджетов в Text", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text("Добавление тегов", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Теги позволяют определить форматирование. Тег добавляется с помощью метода add_tag() класса Text:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('tag_add(tagName, index1, index2)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Первый параметр устанавливает имя тега, второй параметр - index1 указывает на начальный символ, с которого начинает применяться тег. Дополнительно (но необязательно) можно указать третий параметр, который устанавливает конечный символ, к которому применяется тег.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Для прикрепления тега к определенному тексту также можно использовать метод insert, который добавляет текст, и в качестве второго параметра передать тег или набор тегов, которые будут применяться к добавляемому тексту:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''insert(index, text, tagName)\n insert(index, text, (tagName1, tagName2,...tagNameN))'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "С помощью метода tag_configure() для тега можно сконфигурировать стили.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('tag_configure(имя_тега, стили)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Стили представляют параметры background, bgstipple, borderwidth, elide, fgstipple, font, foreground, justify, lmargin1, lmargin2, offset, overstrike, relief, rmargin, spacing1, spacing2, spacing3, tabs, tabstyle, underline и wrap, которым передаются некоторые значения.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Посмотрим на примере:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import * \n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200") \n\neditor = Text(wrap = "none")\neditor.pack(expand=1, fill=BOTH)\neditor.insert("1.0","Hello ")\n # создаем тег highlightline и прикрепляем его к символам 1.0 до 1.2\n editor.tag_add("highlightline", "1.0", "1.2")\n# добавляем текст, к которому применяется тег highlightline\neditor.insert("end","World", "highlightline") \neditor.insert("end","\\\\nHello All!") \n# устанавливаем стили тега highlightline \neditor.tag_configure("highlightline", background="#ccc", foreground="red", font="TkFixedFont", relief="raised") \n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь создается тег \"highlightline\", который прикрепляется сначала по 2-й символ в первой строке. Далее добавляется текст \"World\", к которму применяется данный тег. В конце конфигурируем тег, задавая его стилевые параметры:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 1
                        ft.Container(
                            content=text_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Теги в Text в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Если в процессе работы программы тег стал не нужен, его можно удалить. Метод remove_tag() удаляет тег с определенных символов:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('editor.tag_remove("highlightline", "1.0", "1.2")'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "В данном случае удаляем тег \"highlightline\" с символов с 0 по 2-й в первой строке.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Также можно вообще удалить тег со всех символов, к которым он применяется:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('editor.tag_delete("highlightline")'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Добавление изображений и других виджетов", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Виджет Text позволяет добавление изображений и других виджетов.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для добавления изображений применяется метод image_create:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n\nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200") \n\neditor = Text()\neditor.pack(expand=1, fill=BOTH)\n\npython_img = PhotoImage(file="python_sm.png")\neditor.image_create("1.0", image=python_img)\n\nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "В метод image_create в качестве первого параметра передается позиция вставки изображения. В качестве второго параметра - image указывается файл изображения:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 2
                        ft.Container(
                            content=text_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Добавление изображения в виджет Text в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Аналогично можно добавлять другие виджеты в Text с помощью метода window_create()",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import     \nfrom tkinter import ttk   \n\nroot = Tk()    \nroot.title("METANIT.COM")    \nroot.geometry("250x200")     \n\neditor = Text()    \neditor.pack(expand=1, fill=BOTH)    \ndef click():
        editor.insert("2.0", "Click\\\\n")   \n\nbtn = ttk.Button(editor, text="Click", command=click)   \neditor.window_create("1.0", window=btn)    \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Первый параметр метода window_create также позиция создания виджета, а второй параметр - window указывает на добавляемый виджет, в данном случае это кнопка, на которую также можно нажимать и также можно обрабатывать ее нажатия",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 3
                        ft.Container(
                            content=text_image3,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Добавление виджетов в виджет Text в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_treeview_data_content(self):
        colors = self.get_theme_colors()
        """Создание контента для темы 'Управление данными в Treeview'"""
        return ft.Container(
            content=ft.Column([
                ft.Text("Управление данными в Treeview", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Виджет Treeview предназначен для отображения иерархических данных, причем как в виде дерева, так и в виде таблицы. Среди параметров Treeview следует отметить следующие:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Container(
                            content=self.highlight_syntax("columns: столбцы таблицы в виде строки или списка/кортежа строк\n\ndisplaycolumns: отображаемые столбцы таблицы\n\ncursor: курсор при наведении на виджет\n\nheight: высота виджета\n\npadding: отступы от границ виджета до содержимого\n\nselectmode: режим выбора элементов в виджете\n\nshow: формат отображения данных. Может принимать одно из следующих значений:\n\ntree: отображает столбец #0\n\nheading: отображает строку с заголовками\n\ntree headings: отображает столбец #0 и строку с заголовками\n\n\"\": не отображает ни столбец #0, ни строку с заголовками"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Управление данными", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text("Добавление элементов", size=16, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для добавления данных применяется метод insert():",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("insert: (parent, index, iid, values) -> str"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Этот метод создает новый элемент и возвращает его идентификатор, который по умолчанию представляет строку наподобие \"IOO1\". Основные параметры метода:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("parent: представляет идентификатор родительского элемента, в который добавляется элемент. Если создается элемент верхнего уровня, для которого не существует никакого родительского элемента, как, например, в случае с добавлением строки в таблицу, то передается пустая строка.\n\nindex: указывает индекс для вставки элемента. Если элемент добавляется в конец, то используется значение END или \"end\", либо указывается число, которое равно количеству элементов или больше его. Если элемент добавляется в самое начало, то указывается 0 или число меньше нуля.\n\niid: если указан данный параметр, то его значение будет использоваться в качестве идентификатора элемента. При этом подобный в виджете не должно быть элемента с подобным идентификатором, иначе генерируется новый идентификатор, как в обшем случае\n\nvalues: список или кортеж значений, которые и составляют добавляемый элемент"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text("Удаление элементов", size=16, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для удаления данных применяется метод delete():",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("delete(items)"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "В качестве параметра метод принимает удаляемые данные",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text("Перемещение элементов", size=16, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для перемещения элемента на другую позицию применяется метод move():",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("move(item, parent, index)"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Этот метод создает новый элемент и возвращает его идентификатор, который по умолчанию представляет строку наподобие \"IOO1\". Основные параметры метода:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("item: идентификатор элемента, который надо переместить.\n\nparent: представляет родительский элемент перемещаемого элемента .\n\nindex: индекс, на который перемещается элемент"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text("Получение элементов", size=16, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для получения элементов применяется метод get_children():",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("get_children(item)"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Он принимает идентификатор элемента, дочерние элементы которого надо получить, и возвращает набор идентификаторов полученных элементов:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('for k in treeview.get_children(""): print(k)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "В данном случае k представляет идентификатор элемент.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "В качестве параметра в get_children() передается элемент в Treeview, дочерние элементы которого мы хотим получить. Если надо получить элементы верхнего уровня (например, строки таблицы), то передается пустая строка.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Конкретный элемент по ключу с помощью метода item(), в который передается идентификатор элемента:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('for k in treeview.get_children(""): \n    print(treeview.item(k))'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "в данном случае treeview.item(k) возвратит набор значений элемента в Treeview (например, всю строку).",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Если нам надо получить не весь набор значений, а только одно значение (отдельную ячейку строки), то применяется метод set(), в который передается идентификатор элемента и номер столбца:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('for k in treeview.get_children(""): \n    print(treeview.set(k, 0))'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "В данном случае получаем значение первой ячейки строки (при табличном отображении).",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text("Изменение значений", size=16, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Если надо изменить один столбец, то применяется метод set()",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("set(item, column, value)"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "item: идентификатор элемента, который надо изменить.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=5),
                        
                        ft.Text(
                            "column: индекс элемента в кортеже (столбца в строке), который надо изменить.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=5),
                        
                        ft.Text(
                            "value: новое значение",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "например:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('treeview.set("I003", 0, "Admin")'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Здесь значение в первом столбце элемента с id=I003 меняется на строку \"Admin\"",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Если надо изменить вообще весь элемент со всеми его значениями, то применяется метод item()",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("item(item, values)"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "item: идентификатор элемента, который надо изменить.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=5),
                        
                        ft.Text(
                            "values: кортеж с новыми значениями",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "например:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('treeview.item("I003", values=("Tim", 34, "tim@email.com"))'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Здесь элемент с id=I003 в качестве значений принимает кортеж (\"Tim\", 34, \"tim@email.com\")",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В следующих статьях рассмотрим применение этих методов.",
                            size=14, color=colors["text_secondary"]
                        ),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_treeview_table_content(self):
        """Создание контента для темы 'Создание таблиц'"""
        image_path1 = self.get_library_image_path("t92.png")
        image_path2 = self.get_library_image_path("t93.png")
        image_path3 = self.get_library_image_path("t94.png")
        image_path4 = self.get_library_image_path("t95.png")
        colors = self.get_theme_colors()
        
        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            table_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            table_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение таблицы", size=12, color=colors["text_secondary"]),
                    ft.Text("t92.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            table_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            table_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение настройки столбцов", size=12, color=colors["text_secondary"]),
                    ft.Text("t93.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        # Проверяем существует ли изображение 3
        if os.path.exists(image_path3):
            table_image3 = ft.Image(
                src=image_path3,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            table_image3 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение картинки в заголовке", size=12, color=colors["text_secondary"]),
                    ft.Text("t94.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        # Проверяем существует ли изображение 4
        if os.path.exists(image_path4):
            table_image4 = ft.Image(
                src=image_path4,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            table_image4 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение прокрутки", size=12, color=colors["text_secondary"]),
                    ft.Text("t95.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Создание таблиц", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Для отображения данных в виде таблицы параметру show предпочтительно передать значение \"headings\" (если надо отображать заголовки), либо \" \" (для таблицы без заголовков). Определим небольшую таблицу с тремя столбцами:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200") \n \n# определяем данные для отображения\npeople = [("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com")]\n \n# определяем столбцы\ncolumns = ("name", "age", "email")\n \ntree = ttk.Treeview(columns=columns, show="headings")\ntree.pack(fill=BOTH, expand=1)\n \n# определяем заголовки\ntree.heading("name", text="Имя")\ntree.heading("age", text="Возраст")\ntree.heading("email", text="Email")\n \n# добавляем данные\nfor person in people:\n    tree.insert("", END, values=person)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь данные, которые будут отображаться в таблице, определены в виде списка people, который хранит набор кортежей. Каждый кортеж состоит из трех элементов. Условно будем считать, что первый элемент кортежа представляет имя пользователя, второй - возраст, а третий - электронный адрес. И эти данные нам надо отобразить в таблице:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('people = [("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com")]'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Для отображения этих данных определяем три столбца: name, age и email в виде кортежа и передаем их параметру columns:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''columns = ("name", "age", "email")\ntree = ttk.Treeview(columns=columns, show="headings")'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Далее нам надо настроить заголовки столбца с помощью метода heading() класса Treeview (по умолчанию столбцы не имеют никаких заголовков). Данный метод принимает ряд параметров:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('tree.heading("name", text="Имя")'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Первый параметр указывает на имя столбца. В примере выше определяем также параметр text, который определяет текст заголовка",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "И последний момент - добавляем сами данные в таблицу с помощью метода insert() класса Treeview",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('tree.insert("", END, values=person)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Первый параметр - пустая строка \"\" указывает, что элемент добавляется как элемент верхнего уровня (то есть у него нет родительского элемента). Значение END указывает, что элемент добавляется в конец набора. И параметр values в качестве добавляемых данных устанавливает кортеж person.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В итоге мы получим следующую таблицу:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 1
                        ft.Container(
                            content=table_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Создание таблицы с помощью Treeview в Tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Настройка столбца", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Вполне возможно, что изначальные настройки столбцов нас не устроят. Например, текст заголовка располагается по умолчанию по центру, а данные столбца выравниваются по левому краю. Кроме того, каждый столбец имеет некоторую начальную ширину, в следствие чего ширина виджета может оказаться больше ширины окна. Либо мы захотим как-то иначе настроить вид столбца.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Прежде всего мы можем настроить заголовки столбца с помощью метода heading():",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("heading(column, text, image, anchor, command)"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Параметры метода:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("column: имя настраиваемого столбца\n\ntext: текст заголовка\n\nimage: картинка для заголовка\n\nanchor: устанавливает выравнивание заголовка по определенному краю. Может принимать значения n, e, s, w, ne, nw, se, sw, c\n\ncommand: функция, выполняемая при нажатии на заголовок"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Для настройки столбца в целом применяется метод column():",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("column(column, width, minwidth, stretch, anchor)"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Параметры метода:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("column: индекс настраиваемого столбца в формате \"# номер_столбца\"\n\nwidth: ширина столбца\n\nminwidth: минимальная ширина\n\nanchor: устанавливает выравнивание заголовка по определенному краю. Может принимать значения n, e, s, w, ne, nw, se, sw, c\n\nstretch: указывает, будет ли столбец растягиваться при растяжении контейнера. Если будет, то значение True, иначе значение False"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Применим некоторые из этих параметров:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200") \n \n# определяем данные для отображения\npeople = [("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com")]\n \n# определяем столбцы\ncolumns = ("name", "age", "email")\n \ntree = ttk.Treeview(columns=columns, show="headings")\ntree.pack(fill=BOTH, expand=1)\n \n# определяем заголовки с выпавниваем по левому краю\ntree.heading("name", text="Имя", anchor=W)\ntree.heading("age", text="Возраст", anchor=W)\ntree.heading("email", text="Email", anchor=W)\n \n# настраиваем столбцы\ntree.column("#1", stretch=NO, width=70)\ntree.column("#2", stretch=NO, width=60)\ntree.column("#3", stretch=NO, width=100)\n \n# добавляем данные\nfor person in people:\n    tree.insert("", END, values=person)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае для заголовков устанавливаем выравнивание по левому краю. Для столбцов запрещаем растяжение и устанавливаем ширину.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 2
                        ft.Container(
                            content=table_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("настройка столбцов в таблице в виджете Treeview в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "При добавлении изображения оно помещается в правой части. Например, установка изображения для третьего столбца:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''# предполагается, что в папке приложения располагается файл email_icon_micro.png\nemail_icon = PhotoImage(file="./email_icon_micro.png")\ntree.heading("email", text="Email", anchor=W, image=email_icon)'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "картинка в заголовке столбца в таблице в виджете Treeview в Tkinter и Python",
                            size=14, color=colors["text_secondary"], italic=True
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 3
                        ft.Container(
                            content=table_image3,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Добавление к Treeview прокрутки", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200") \nroot.rowconfigure(index=0, weight=1)\nroot.columnconfigure(index=0, weight=1)\n \n# определяем данные для отображения\npeople = [\n    ("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com"),\n    ("Alice", 33, "alice@email.com"), ("Kate", 21, "kate@email.com"), ("Ann", 24, "ann@email.com"),\n    ("Mike", 34, "mike@email.com"), ("Alex", 52, "alex@email.com"), ("Jess", 28, "jess@email.com"),\n    ]\n \n# определяем столбцы\ncolumns = ("name", "age", "email")\n \ntree = ttk.Treeview(columns=columns, show="headings")\ntree.grid(row=0, column=0, sticky="nsew")\n \n# определяем заголовки\ntree.heading("name", text="Имя", anchor=W)\ntree.heading("age", text="Возраст", anchor=W)\ntree.heading("email", text="Email", anchor=W)\n \ntree.column("#1", stretch=NO, width=70)\ntree.column("#2", stretch=NO, width=60)\ntree.column("#3", stretch=NO, width=100)\n \n# добавляем данные\nfor person in people:\n    tree.insert("", END, values=person)\n \n# добавляем вертикальную прокрутку\nscrollbar = ttk.Scrollbar(orient=VERTICAL, command=tree.yview)\ntree.configure(yscroll=scrollbar.set)\nscrollbar.grid(row=0, column=1, sticky="ns")\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 4
                        ft.Container(
                            content=table_image4,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Прокрутка таблицы в Treeview в Tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_treeview_sorting_content(self):
        """Создание контента для темы 'Нажатие на заголовок столбца и сортировка'"""
        image_path1 = self.get_library_image_path("t96.png")
        colors = self.get_theme_colors()

        # Проверяем существует ли изображение
        if os.path.exists(image_path1):
            sorting_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            sorting_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение сортировки", size=12, color=colors["text_secondary"]),
                    ft.Text("t96.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Нажатие на заголовок столбца и сортировка", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "С помощью параметра command метода heading() можно привязать к заголовку некоторую функцию, которая будет вызываться по нажатию на заголовок.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("treeview.heading(имя_заголовка, command=функция)"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Рассмотрим на примере сортировки:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200") \n \n# определяем данные для отображения\npeople = [("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com")]\n \n# определяем столбцы\ncolumns = ("name", "age", "email")\n \ntree = ttk.Treeview(columns=columns, show="headings")\ntree.pack(expand=1, fill=BOTH)\n \ndef sort(col, reverse):\n    # получаем все значения столбцов в виде отдельного списка\n    l = [(tree.set(k, col), k) for k in tree.get_children("")]\n    # сортируем список\n    l.sort(reverse=reverse)\n    # переупорядочиваем значения в отсортированном порядке\n    for index,  (_, k) in enumerate(l):\n        tree.move(k, "", index)\n    # в следующий раз выполняем сортировку в обратном порядке\n    tree.heading(col, command=lambda: sort(col, not reverse))\n \n# определяем заголовки\ntree.heading("name", text="Имя", anchor=W, command=lambda: sort(0, False))\ntree.heading("age", text="Возраст", anchor=W, command=lambda: sort(1, False))\ntree.heading("email", text="Email", anchor=W, command=lambda: sort(2, False))\n \ntree.column("#1", stretch=NO, width=70)\ntree.column("#2", stretch=NO, width=60)\ntree.column("#3", stretch=NO, width=100)\n \n# добавляем данные\nfor person in people:\n    tree.insert("", END, values=person)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Как и в предыдущих примерах, виджет Treeview использует список кортежей people и представляет таблицу с тремя столбцами.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Для сортировки определена функция sort(), которая принимает два параметра: col(номер столбца, по которому идет сортировка) и reverse (направление сортировки - по возрастанию или убыванию)",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("def sort(col, reverse):"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Рассмотрим действие функции по этапно:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "При добавлениии элементов в Treeview каждому из них присваивается идентификатор. Используя идентификатор, можно получить все значения элемента в Treeview. Это необходимо, чтобы отсортировать элементы:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('l = [(tree.set(k, col), k) for k in tree.get_children("")]'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Здесь вначале пробегаемся по всем элементам в Treeview с помощью метода tree.get_children(\"\"). В метод передается пустая строка \"\", поскольку мы хотим получить элементы верхнего уровня (по сути строки таблицы). Соответственно переменная k здесь будет представлять идентификатор элемента",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для каждого элемента с помощью метода set получаем с помощью идентификатора значение столбца строки:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("tree.set(k, col)"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Например, если col=0 (то есть сортировка идет по имени, то вызов tree.set(k, col) возвращает имя (\"Tom\", \"Bob\", \"Sam\").",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Полученное значение помещаем в кортеж:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("(tree.set(k, col), k)"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Из кортежей формируется список:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('l = [(tree.set(k, col), k) for k in tree.get_children("")]'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "То есть если, к примеру, сортировка идет по имени, то на выходе переменная l будет представлять список кортежей типа [(\"Tom\", \"I001\"), (\"Bob\", \"I002\"), (\"Sam\", \"I003\")]",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Затем сортируем список с помощью встроенной метода sort():",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("l.sort(reverse=reverse)"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "В методе указываем направление сортировки с помощью параметра reverse",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Список отсортирован, но на отображение данных в таблице это пока никак не повлияло. Нам надо переупорядочить строки, привести их в соответствие с отсортированным списком l. Для этого переставляем их с помощью метода move():",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''for index,  (_, k) in enumerate(l):\n        tree.move(k, "", index)'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Сначала с помощью функции enumerate() из списка l получаем набор объектов, который состоит из индекса и собственно данных. При переборе этого набора индекс получаем в переменную index, а набор данных в кортеж (_, k) - первый элемент кортежа представляет имя, но здесь оно нам уже не нужно, оно использовалось на предыдущем шаге для сортировки. А второй элемент кортежа - идентификатор строки.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "В цикле с помощью вызова tree.move(k, \"\", index) перемещаем элемент с идентификатором k, который является элементов верхнего уровня (второй аргумент - \"\") на позицию с индексом index.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "На финальной стадии переустанавливаем определение заголовка:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("tree.heading(col, command=lambda: sort(col, not reverse))"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Параметр command в качестве выполняемой функции получает лямбда-выражение, которое вызывает функцию sort. При этом функции передается противоположное направление сортировки. Благодаря этому при следующем нажатии на заголовок сортировка будет идти в противоположном направлении.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Результат работы программы:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение
                        ft.Container(
                            content=sorting_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Сортировка и обработка нажатия на заголовок в Treeview в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_treeview_selection_content(self):
        """Создание контента для темы 'Выделение строк таблицы'"""
        image_path1 = self.get_library_image_path("t97.png")
        image_path2 = self.get_library_image_path("t98.png")
        colors = self.get_theme_colors()
        
        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            selection_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            selection_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение выделения строк", size=12, color=colors["text_secondary"]),
                    ft.Text("t97.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            selection_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            selection_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение режима выделения", size=12, color=colors["text_secondary"]),
                    ft.Text("t98.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Выделение строк таблицы", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Для работы с выделенными строками в Treeview определен ряд методов:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("selection(): возвращает идентификаторы выделенных строк в виде кортежа\n\nselection_add(items): выделяет строки с идентификаторами, которые передаются в качестве параметра\n\nselection_remove(items): снимает выделение строк с идентификаторами, которые передаются в качестве параметра\n\nselection_set(items): снимает выделение с ранее выделенных строк и выделяет строки с идентификаторами, которые передаются в качестве параметра"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Обработка события выделения", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для обработки выделения строк у Treeview применяется событие <<TreeviewSelect>>",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200") \n \n# определяем данные для отображения\npeople = [("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com")]\n \nlabel = ttk.Label()\nlabel.pack(anchor=N, fill=X)\n# определяем столбцы\ncolumns = ("name", "age", "email")\ntree = ttk.Treeview(columns=columns, show="headings")\ntree.pack(expand=1, fill=BOTH)\n \n# определяем заголовки\ntree.heading("name", text="Имя", anchor=W)\ntree.heading("age", text="Возраст", anchor=W)\ntree.heading("email", text="Email", anchor=W)\n \ntree.column("#1", stretch=NO, width=70)\ntree.column("#2", stretch=NO, width=60)\ntree.column("#3", stretch=NO, width=100)\n \n# добавляем данные\nfor person in people:\n    tree.insert("", END, values=person)\n \ndef item_selected(event):\n    selected_people = ""\n    for selected_item in tree.selection():\n        item = tree.item(selected_item)\n        person = item["values"]\n        selected_people = f"{selected_people}{person}\\\\n"\n    label["text"]=selected_people\n \ntree.bind("<<TreeviewSelect>>", item_selected)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь с помощью метода bind() устанавливаем для события <<TreeviewSelect>> функцию-обработчик item_selected. В этой функции получаем все идентификаторы выделенных строк с помощью метода tree.selection()",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("for selected_item in tree.selection()"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Используя полученный идентификатор, получаем выделенный элемент с помощью метода tree.item",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("item = tree.item(selected_item)"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для получения самих значений обращаемся к атрибуту values:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('person = item["values"]'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Склеиваем их в строку selected_people и отображаем ее в метке label.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 1
                        ft.Container(
                            content=selection_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("обработка выделения строк в Treeview в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Режим выделения", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "По умолчанию в Treeview можно выделить только один элемент (одну строку). За установку режима выделения в Treeview отвечает параметр selectionmode, который может принимать следующие значения:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("extended: позволяет выбрать несколько строк\n\nbrowse: позволяет выбрать только одну строку\n\nnone: выделение строк не доступно"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Например, изменим код Treeview, установив режим \"extended\":",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('tree = ttk.Treeview(columns=columns, show="headings", selectmode="extended")'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "И теперь можно выделять несколько строк:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 2
                        ft.Container(
                            content=selection_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("режим выделения строк в Treeview в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_treeview_tree_content(self):
        """Создание контента для темы 'Создание дерева'"""
        image_path1 = self.get_library_image_path("t99.png")
        image_path2 = self.get_library_image_path("t100.png")
        image_path3 = self.get_library_image_path("t101.png")
        colors = self.get_theme_colors()
        
        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            tree_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            tree_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение простого дерева", size=12, color=colors["text_secondary"]),
                    ft.Text("t99.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            tree_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            tree_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение иерархического дерева", size=12, color=colors["text_secondary"]),
                    ft.Text("t100.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        # Проверяем существует ли изображение 3
        if os.path.exists(image_path3):
            tree_image3 = ft.Image(
                src=image_path3,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            tree_image3 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение заголовка дерева", size=12, color=colors["text_secondary"]),
                    ft.Text("t101.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Создание дерева", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Для определения дерева параметру show виджета Treeview передается значение tree (дерево без заголовка) или tree headings (дерево с заголовком).",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Определим простейшее дерево:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200") \n \n# создаем дерево\ntree = ttk.Treeview(show="tree")\ntree.pack(expand=1, fill=BOTH)\n \n# добавляем данные\ntree.insert("", END, iid=1, text="Административный отдел")\ntree.insert("", END, iid=2, text="IT-отдел")\ntree.insert("", END, iid=3, text="Отдел продаж")\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь данные для отображения представлены условно представлены списком отделов некоторого предприятия. Каждый отдел добавляется как элемент верхнего уровня, поэтому в методе tree.insert в качестве первого аргумента указывается пустая строка \"\". Также устанавливаем для каждого добавляемого элемента параметр text - название отдела и его идентификатор - параметр iid. Конечно, мы могли бы положиться на tkinter, который установил бы идентификаторы автоматически. Однако ручная установка идентификаторов потом упростить добавление в них вложенныхи элементов.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В итоге получится следующее дерево:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 1
                        ft.Container(
                            content=tree_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Treeview в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Однако визуально пока никакого дерева по сути нет, а сами данные не являются иерархическими. Но теперь добавим в некоторые отделы сотрудников:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200") \n \ntree = ttk.Treeview(show="tree")\ntree.pack(expand=1, fill=BOTH)\n \n# добавляем отделы\ntree.insert("", END, iid=1, text="Административный отдел", open=True)\ntree.insert("", END, iid=2, text="IT-отдел")\ntree.insert("", END, iid=3, text="Отдел продаж")\n \n# добавим сотрудников отдела\ntree.insert(1, index=END, text="Tom")\ntree.insert(2, index=END, text="Bob")\ntree.insert(2, index=END, text="Sam")\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 2
                        ft.Container(
                            content=tree_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Отображение иерархических данных в дереве в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "При добавлении каждого сотрудника указываем в качестве первого параметра идентификатор элемента-отдела.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('tree.insert(2, index=END, text="Bob")'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Также устанавливаем текстовую метку элемента - параметр text - он представляет имя условного сотрудника.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "По умолчанию все элементы, которые содержат вложенные подэлементы, закрыты. Чтобы их отрыть по умолчанию, у элемента для параметра open передается значение True (по умолчанию равно False):",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('tree.insert("", END, iid=1, text="Административный отдел", open=True)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Установка заголовка", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Если в Treeview параметр show имеет значение \"tree headings\" (это значение по умолчанию), то мы можем также установить заголовок:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200") \n \ntree = ttk.Treeview()\n# установка заголовка\ntree.heading("#0", text="Отделы", anchor=NW)\ntree.pack(expand=1, fill=BOTH)\n \ntree.insert("", END, iid=1, text="Административный отдел", open=True)\ntree.insert("", END, iid=2, text="IT-отдел")\ntree.insert("", END, iid=3, text="Отдел продаж")\n \ntree.insert(1, index=END, text="Tom")\ntree.insert(2, index=END, text="Bob")\ntree.insert(2, index=END, text="Sam")\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 3
                        ft.Container(
                            content=tree_image3,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Заголовок дерева Treeview в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_windows_content(self):
        """Создание контента для темы 'Создание окон'"""
        image_path1 = self.get_library_image_path("t102.png")
        image_path2 = self.get_library_image_path("t103.png")
        colors = self.get_theme_colors()
        
        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            windows_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            windows_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение создания окна", size=12, color=colors["text_secondary"]),
                    ft.Text("t102.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            windows_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            windows_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение окна с виджетами", size=12, color=colors["text_secondary"]),
                    ft.Text("t103.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Создание окон", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "По умолчанию приложение Tkinter имеет одно главное окно, которое представляет класс tkinter.Tk. Запуск приложение приводит к запуску главного окно, в рамках которого помещаются все виджеты. Закрытие главного окна приводит к завершению работы приложения. Однако в рамках главного окна также можно запускать вторичные, неглавные окна. Например, октроем новое окно по нажатию на кнопку:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200") \n \ndef click():\n    window = Tk()\n    window.title("Новое окно")\n    window.geometry("250x200")\n \nbutton = ttk.Button(text="Создать окно", command=click)\nbutton.pack(anchor=CENTER, expand=1)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь по нажатию на кнопку создается новый объект window, у него устанавливается заголовок и размеры.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 1
                        ft.Container(
                            content=windows_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Создание окон в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Стоит отметить, что приложение завершит работу, когда будут закрыты все его окна.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Как и главное окно, вторичные окна могут иметь виджеты. Например, определим на новом окне метку:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200") \n \ndef click():\n    window = Tk()\n    window.title("Новое окно")\n    window.geometry("250x200")\n    label=ttk.Label(window, text="Принципиально новое окно")\n    label.pack(anchor=CENTER, expand=1)\n \nbutton = ttk.Button(text="Создать окно", command=click)\nbutton.pack(anchor=CENTER, expand=1)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Единственное не надо забывать у добавляемых виджетов устанавливать окно в качестве родительского контейнера",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 2
                        ft.Container(
                            content=windows_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Создание окон Tk в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Удаление окна", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для удаления окна применяется меnод destroy()",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n \ndef click():\n    window = Tk()\n    window.title("Новое окно")\n    window.geometry("250x200")\n    close_button = ttk.Button(window, text="Закрыть окно", command=lambda: window.destroy())\n    close_button.pack(anchor="center", expand=1)\n \nopen_button = ttk.Button(text="Создать окно", command=click)\nopen_button.pack(anchor="center", expand=1)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае в новом окне по нажатию на кнопку close_button срабатывает метод window.destroy(), который закрывает окно и по сути аналогичен нажатию на крестик в верхнем правом углу окна.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Определение окна в объектно-ориентированном стиле", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "В примере выше новое окно, его параметры и вложенные виджеты определялись внутри функции, однако это приводит к разбуханию кода функции. И гораздо проще вынести определение окна в отдельный класс:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nclass Window(Tk):\n    def __init__(self):\n        super().__init__()\n \n        # конфигурация окна\n        self.title("Новое окно")\n        self.geometry("250x200")\n \n        # определение кнопки\n        self.button = ttk.Button(self, text="закрыть")\n        self.button["command"] = self.button_clicked\n        self.button.pack(anchor="center", expand=1)\n \n    def button_clicked(self):\n        self.destroy()\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n \ndef click():\n    window = Window()\n \nopen_button = ttk.Button(text="Создать окно", command=click)\nopen_button.pack(anchor="center", expand=1)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь определение окна вынесено в отдельный класс Window, который наследуется от класса tkinter.Tk. Благодаря этому мы можем вынести весь код определения окна в отдельную структурную единицу - класс, что позволит упростить управление кодом.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Окно поверх других окон", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для создания диалогового окна, которое располагается поверх главного окна, применяется класс Toplevel:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n \ndef dismiss(window):\n    window.grab_release() \n    window.destroy()\n \ndef click():\n    window = Toplevel()\n    window.title("Новое окно")\n    window.geometry("250x200")\n    window.protocol("WM_DELETE_WINDOW", lambda: dismiss(window)) # перехватываем нажатие на крестик\n    close_button = ttk.Button(window, text="Закрыть окно", command=lambda: dismiss(window))\n    close_button.pack(anchor="center", expand=1)\n    window.grab_set()       # захватываем пользовательский ввод\n \nopen_button = ttk.Button(text="Создать окно", command=click)\nopen_button.pack(anchor="center", expand=1)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Toplevel по сути то же самое окно Tk, которое располагается поверх других окон. В примере выше оно также имеет кнопку. Но кроме того, чтобы пользователь не мог перейти обратно к главному окну пока не закроет это диалоговое окно, применяется ряд методов. Прежде всего захватываем весь пользовательский ввод с помощью метода grab_set():",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("window.grab_set()"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "В функции dismiss(), которая закрывает окно, освобождаем ввод с помощью метода grab_release()",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("window.grab_release()"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )
    
    def create_messagebox_content(self):
        """Создание контента для темы 'MessageBox'"""
        image_path1 = self.get_library_image_path("t104.png")
        image_path2 = self.get_library_image_path("t105.png")
        image_path3 = self.get_library_image_path("t106.png")
        image_path4 = self.get_library_image_path("t107.png")
        colors = self.get_theme_colors()
        
        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            messagebox_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            messagebox_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение окон сообщений", size=12, color=colors["text_secondary"]),
                    ft.Text("t104.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            messagebox_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            messagebox_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение диалогового окна", size=12, color=colors["text_secondary"]),
                    ft.Text("t105.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        # Проверяем существует ли изображение 3
        if os.path.exists(image_path3):
            messagebox_image3 = ft.Image(
                src=image_path3,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            messagebox_image3 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение окна подтверждения", size=12, color=colors["text_secondary"]),
                    ft.Text("t106.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        # Проверяем существует ли изображение 4
        if os.path.exists(image_path4):
            messagebox_image4 = ft.Image(
                src=image_path4,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            messagebox_image4 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение настроенного окна", size=12, color=colors["text_secondary"]),
                    ft.Text("t107.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("MessageBox", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text("Окна сообщений", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Tkinter имеет ряд встроенных окон для разных ситуаций, в частности, окна сообщений, функционал которых заключен в модуле tkinter.messagebox. Для отображения сообщений этот модуль предоставляет следующие функции:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("showinfo(): предназначена для отображения некоторой информации\n\nshowerror(): предназначена для отображения ошибок\n\nshowwarrning(): предназначена для отображения предупреждений"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Все эти функции принимают три параметра:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''showinfo(title, message, **options)\nshowerror(title, message, **options)\nshowwarrning(title, message, **options)'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "title: заголовок окна",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=5),
                        
                        ft.Text(
                            "message: отображаемое сообщение",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=5),
                        
                        ft.Text(
                            "options: настройки окна",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В реальности различие между этими типами сообщений заключается лишь в изображении, которое отображается рядом с текстом сообщения:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\nfrom tkinter.messagebox import showerror, showwarning, showinfo\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n \ndef open_info(): \n    showinfo(title="Информация", message="Информационное сообщение")\n \ndef open_warning(): \n    showwarning(title="Предупреждение", message="Сообщение о предупреждении")\n \ndef open_error(): \n    showerror(title="Ошибка", message="Сообщение об ошибке")\n \ninfo_button = ttk.Button(text="Информация", command=open_info)\ninfo_button.pack(anchor="center", expand=1)\n \nwarning_button = ttk.Button(text="Предупреждение", command=open_warning)\nwarning_button.pack(anchor="center", expand=1)\n \nerror_button = ttk.Button(text="Ошибка", command=open_error)\nerror_button.pack(anchor="center", expand=1)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь по нажатию на каждую из трех кнопок отображается соответствующее сообщение:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 1
                        ft.Container(
                            content=messagebox_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Окна с сообщениями messagebox в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Окна подтверждения операции", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Модуль tkinter.messagebox также предоставляет ряд функций для подтверждения операции, где пользователю предлагается нажать на одну из двух кнопок:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("askyesno()\n\naskokcancel()\n\naskretrycancel()"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Все эти функции принимают те же три параметра title, message и options. Отличие между ними только в том, что кнопки имеют разный текст. В случае нажатия на кнопку подтверждения, функция возвращает значение True, иначе возвращается False",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\nfrom tkinter.messagebox import showinfo, askyesno\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n \ndef click(): \n    result = askyesno(title="Подтвержение операции", message="Подтвердить операцию?")\n    if result: showinfo("Результат", "Операция подтверждена")\n    else: showinfo("Результат", "Операция отменена")\n \nttk.Button(text="Click", command=click).pack(anchor="center", expand=1)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае по нажатию на кнопку вызывается функция askyesno(), которая отображает диалоговое окно с двумя кнопками \"Да\" и \"Нет\". В зависимости от того, на какую кнопку нажмет пользователь, функция возвратит True или False. Получив результат функции, мы можем проверить его и выполнить те или иные действия.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 2
                        ft.Container(
                            content=messagebox_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Диалоговые окна в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Особняком стоит функция askquestion - она также отображает две кнопки для подтверждения или отмены действия (кнопки \"Yes\"(Да) и \"No\"(Нет)), но в зависимости от нажатой кнопки возвращает строку: \"yes\" или \"no\".",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Также отдельно стоит функция askyesnocancel() - она отображает три кнопки: Yes (возвращает True), No (возвращает False) и Cancel (возвращает None):",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\nfrom tkinter.messagebox import showinfo, askyesnocancel\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n \ndef click(): \n    result =  askyesnocancel(title="Подтвержение операции", message="Подтвердить операцию?")\n    if result==None: showinfo("Результат", "Операция приостановлена")\n    elif result: showinfo("Результат", "Операция подтверждена")\n    else : showinfo("Результат", "Операция отменена")\n \nttk.Button(text="Click", command=click).pack(anchor="center", expand=1)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В этом случае диалоговое окно предоставит выбор из трех альтернатив",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 3
                        ft.Container(
                            content=messagebox_image3,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Диалоговые окна подтверждения операции в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Настройка окон", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Дополнительно все вышерассмотренные функции принимают ряд параметров, которые могут применяться для настройки окон. Некоторые из них:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("detail: дополнительный текст, который отображается под основным сообщением\n\nicon: иконка, которая отображается рядом с сообщением. Должна представлять одно из втроенных изображений: info, error, question или warning\n\ndefault: кнопка по умолчанию. Должна представлять одно из встроенных значений: abort, retry, ignore, ok, cancel, no, yes"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\nfrom tkinter.messagebox import OK, INFO, showinfo \n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n \ndef click(): \n    showinfo(title="METANIT.COM", message="Добро пожаловать на сайт METANIT.COM", \n            detail="Hello World!", icon=INFO, default=OK)\n \nttk.Button(text="Click", command=click).pack(anchor="center", expand=1)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "При нажатии на кнопку отобразится следующее окно:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 4
                        ft.Container(
                            content=messagebox_image4,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("конфигурация окна сообщения в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_dialogs_content(self):
        """Создание контента для темы 'Диалоговые окна'"""
        image_path1 = self.get_library_image_path("t108.png")
        image_path2 = self.get_library_image_path("t109.png")
        image_path3 = self.get_library_image_path("t110.png")
        colors = self.get_theme_colors()

        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            dialogs_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            dialogs_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение файлового диалога", size=12, color=colors["text_secondary"]),
                    ft.Text("t108.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            dialogs_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            dialogs_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение выбора шрифта", size=12, color=colors["text_secondary"]),
                    ft.Text("t109.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        # Проверяем существует ли изображение 3
        if os.path.exists(image_path3):
            dialogs_image3 = ft.Image(
                src=image_path3,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            dialogs_image3 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение выбора цвета", size=12, color=colors["text_secondary"]),
                    ft.Text("t110.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Диалоговые окна", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Tkinter обладает рядом встроенных диалоговых окон для различных задач. Рассмотрим некоторые из них.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("filedialog", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Модуль filedialog предоставляет функциональность файловых диалоговых окон, которые позволяют выбрать файл или каталог для различных задач. В частности в модуле для работы с файлами определены следующие функции:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("askopenfilename(): открывает диалоговое окно для выбора файла и возвращает путь к выбранному файлу. Если файл не выбран, возвращается пустая строка \"\"\n\naskopenfilenames(): открывает диалоговое окно для выбора файлов и возвращает список путей к выбранным файлам. Если файл не выбран, возвращается пустая строка \"\"\n\nasksaveasfilename(): открывает диалоговое окно для сохранения файла и возвращает путь к сохраненному файлу. Если файл не выбран, возвращается пустая строка \"\"\n\nasksaveasfile(): открывает диалоговое окно для сохранения файла и возвращает сохраненный файл. Если файл не выбран, возвращается None\n\naskdirectory(): открывает диалоговое окно для выбора каталога и возвращает путь к выбранному каталогу. Если файл не выбран, возвращается пустая строка \"\"\n\naskopenfile(): открывает диалоговое окно для выбора файла и возвращает выбранный файл. Если файл не выбран, возвращается None\n\naskopenfiles(): открывает диалоговое окно для выбора файлов и возвращает список выбранных файлов"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Рассмотрим открытие и сохранение файла на примере:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\nfrom tkinter import filedialog\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n \nroot.grid_rowconfigure(index=0, weight=1)\nroot.grid_columnconfigure(index=0, weight=1)\nroot.grid_columnconfigure(index=1, weight=1)\n \ntext_editor = Text()\ntext_editor.grid(column=0, columnspan=2, row=0)\n \n# открываем файл в текстовое поле\ndef open_file():\n    filepath = filedialog.askopenfilename()\n    if filepath != "":\n        with open(filepath, "r") as file:\n            text =file.read()\n            text_editor.delete("1.0", END)\n            text_editor.insert("1.0", text)\n \n# сохраняем текст из текстового поля в файл\ndef save_file():\n    filepath = filedialog.asksaveasfilename()\n    if filepath != "":\n        text = text_editor.get("1.0", END)\n        with open(filepath, "w") as file:\n            file.write(text)\n \nopen_button = ttk.Button(text="Открыть файл", command=open_file)\nopen_button.grid(column=0, row=1, sticky=NSEW, padx=10)\n \nsave_button = ttk.Button(text="Сохранить файл", command=save_file)\nsave_button.grid(column=1, row=1, sticky=NSEW, padx=10)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 1
                        ft.Container(
                            content=dialogs_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Открытие и сохранение файлов в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь определены две кнопки. По нажатию по на кнопку open_button вызывается функция filedialog.askopenfilename(). Она возвращает путь к выбранному файлу. И если в диалоговом окне не нажата кнопка отмены (то есть путь к файлу не равен пустой строке), то считываем содержимое текстового файла и добавляем его в виджет Text",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''def open_file():\n    filepath = filedialog.askopenfilename()\n    if filepath != "":\n        with open(filepath, "r") as file:\n            text =file.read()\n            text_editor.delete("1.0", END)\n            text_editor.insert("1.0", text)'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "По нажатию на кнопку save_button срабатывает функция filedialog.asksaveasfilename(), которая возвращает путь к файлу для сохранения текста из виджета Text. И если файл выбран, то открываем его и сохраняем в него текст:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''def save_file():\n    filepath = filedialog.asksaveasfilename()\n    if filepath != "":\n        text = text_editor.get("1.0", END)\n        with open(filepath, "w") as file:\n            file.write(text)'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Эти функции могут принимать ряд параметров:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("confirmoverwrite: нужно ли подтверждение для перезаписи файла (для диалогового окна сохранения файла)\n\ndefaultextension: расширение по умолчанию\n\nfiletypes: шаблоны типов файлов\n\ninitialdir: стартовый каталог, который открывается в окне\n\ninitialfile: файл по умолчанию\n\ntitle: заголовок диалогового окна\n\ntypevariable: переменная, к которой привязан выбранный файл"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Применение параметров:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('filedialog.askopenfiles(title="Выбор файла", initialdir="D://tkinter", defaultextension="txt", initialfile="hello.txt")'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Выбор шрифта", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n \nlabel = ttk.Label(text="Hello World")\nlabel.pack(anchor=NW, padx=10, pady=10)\n \ndef font_changed(font):\n    label["font"] = font\n \ndef select_font():\n    root.tk.call("tk", "fontchooser", "configure", "-font", label["font"], "-command", root.register(font_changed))\n    root.tk.call("tk", "fontchooser", "show")\n         \n \nopen_button = ttk.Button(text="Выбрать шрифт", command=select_font)\nopen_button.pack(anchor=NW, padx=10, pady=10)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "По нажатию на кнопку вызывается функция select_font, в которой вначале производится настройка диалогового окна установки шрифта",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('root.tk.call("tk", "fontchooser", "configure", "-font", label["font"], "-command", root.register(font_changed))'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "В частности, значение \"configure\" указывает, что в данном случае производится настройка диалогового окна. Аргумент \"-font\" указывает, что следующее значение представляет настройка шрифта, который будет выбран в диалоговом окне по умолчанию. В качестве такового здесь используется шрифт метки label.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Аргумент \"-command\" указывает, что дальше идет определение функции, которая будет срабатывать при выборе шрифта. Здесь такой функцией является функция font_changed. Функция выбора шрифта должна принимать один параметр - через него будет передаваться выбранный шрифт. В данном случае просто переустанавливаем шрифт метки.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для отображения окна выбора шрифта выполняется вызов",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('root.tk.call("tk", "fontchooser", "show")'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Таким образом, при нажатии на кнопку откроется окно выбора шрифта, а после его выбора он будет применен к метке:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 2
                        ft.Container(
                            content=dialogs_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("выбор шрифта в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Выбор цвета", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для выбора цвета применяется функции из модуля colorchooser.askcolor():",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\nfrom tkinter import colorchooser\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n \nlabel = ttk.Label(text="Hello World")\nlabel.pack(anchor=NW, padx=10, pady=10)\n \ndef select_color():\n    result = colorchooser.askcolor(initialcolor="black")\n    label["foreground"] = result[1]\n \nopen_button = ttk.Button(text="Выбрать цвет", command=select_color)\nopen_button.pack(anchor=NW, padx=10, pady=10)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь по нажатию на кнопку вызывается функция select_color. В этой функции вызывается функция colorchooser.askcolor. С помощью параметра initialcolor устанавливаем цвет, который выбран по умолчанию в диалоговом окне. В данном случае это черный цвет (\"black\")",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Результатом функции является кортеж с определениями выбранного цвета. Например, для красного цвета кортеж будет выглядеть следующим образом: ((255, 0, 0), \"#ff0000\"). То есть, обратившись к второму элементу кортежа, можно получить шестнадцатиричное значение цвета. Здесь выбранный цвет применяется для установки цвета шрифта метки:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('label["foreground"] = result[1]'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 3
                        ft.Container(
                            content=dialogs_image3,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Выбор цвета в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_fonts_content(self):
        """Создание контента для темы 'Шрифты'"""
        image_path1 = self.get_library_image_path("t111.png")
        colors = self.get_theme_colors()

        # Проверяем существует ли изображение
        if os.path.exists(image_path1):
            fonts_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            fonts_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение шрифтов", size=12, color=colors["text_secondary"]),
                    ft.Text("t111.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Шрифты", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text("Имена шрифтов", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Ряд виджетов, например, Label или Text, поддерживают установку шрифта через параметр font. Каждая платформа может определять свои специфические шрифты. Но также библиотека Tk по умолчанию включает ряд именнованных шрифтов, которые могут использоваться на различных компонентах графического интерфейса и которые доступны на всех платформах:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("TkDefaultFont: шрифт по умолчанию, который применяется, если для виджета явным образом не определен шрифт\n\nTkTextFont: шрифт по умолчанию, который применяется для виджетов Entry, Listbox и ряда других\n\nTkFixedFont: шрифт с фиксированной шириной\n\nTkMenuFont: шрифт для пунктов меню\n\nTkHeadingFont: шрифт для заголовков в Listbox и в таблицах\n\nTkCaptionFont: шрифт для строки статуса в окнах\n\nTkSmallCaptionFont: шрифт малого размера для диалоговых окон\n\nTkIconFont: шрифт для подписей к иконкам\n\nTkTooltipFont: шрифт для высплывающих окон"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В принципе мы можем использовать эти шрифты не только в любых виджетах:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('ttk.Label(text="Hello World", font="TkTextFont")'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Tk также предоставляет дополнительный набор именнованных шрифтов, которые определены только на определенных платформах. Для их получения можно использовать функцию names() из пакета tkinter.font:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import font\n\nfor font_name in font.names():\n    print(font_name)'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Например, на Windows мы получим следующий набор:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''fixed\noemfixed\nTkDefaultFont\nTkMenuFont\nansifixed\nsystemfixed\nTkHeadingFont\ndevice\nTkTooltipFont\ndefaultgui\nTkTextFont\nansi\nTkCaptionFont\nsystem\nTkSmallCaptionFont\nTkFixedFont\nTkIconFont'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае выводятся и платформа-независимые, и платформо-специфичные шрифты, например, \"system\".",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('ttk.Label(text="Hello World", font="system")'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Определение шрифта", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "За определение шрифта в Tkinter отвечает класс Font из модуля tkinter.font. Он принимет следующие параметры:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("name: имя шрифта\n\nfamily: семейство шрифтов\n\nsize: высота шрифта (в точках при положительном значении или в пикселях при негативном значении)\n\nweight: вес шрифта. Принимает значения normal (обычный) или bold (жирный)\n\nslant: наклон. Принимает значения roman (обычный) или italic (наклонный)\n\nunderline: подчеркивание. Принимает значения True (с подчеркиванием) или False (без подчеркивания)\n\noverstrike: зачеркивание. Принимает значения True (с зачеркиванием) или False (без зачеркивания)"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Для получения всех доступных семейств шрифтов на текущей платформе можно использовать функцию families() из модуля tkinter.font",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import font\n\nfor family in font.families():\n    print(family)'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Пример применения шрифтов:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\nfrom tkinter import font\n \n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n \nfont1 = font.Font(family= "Arial", size=11, weight="normal", slant="roman", underline=True, overstrike=True)\nlabel1 = ttk.Label(text="Hello World", font=font1)\nlabel1.pack(anchor=NW)\n \nfont2 = font.Font(family= "Verdana", size=11, weight="normal", slant="roman")\nlabel2 = ttk.Label(text="Hello World", font=font2)\nlabel2.pack(anchor=NW)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение
                        ft.Container(
                            content=fonts_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Шрифты в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Также можно использовать определение шрифта в виде строки:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n \nlabel1 = ttk.Label(text="Hello World", font="Arial 11 normal roman")\nlabel1.pack(anchor=NW)\n \nlabel2 = ttk.Label(text="Hello World", font="Verdana 11 normal roman")\nlabel2.pack(anchor=NW)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Например, в определении \"Arial 11 normal roman\", применяется семейство шрифта Arial, высота 11 единиц, нежирный шрифт без наклона.",
                            size=14, color=colors["text_secondary"]
                        ),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_colors_content(self):
        """Создание контента для темы 'Установка цвета'"""
        image_path1 = self.get_library_image_path("t112.png")
        image_path2 = self.get_library_image_path("t113.png")
        colors = self.get_theme_colors()

        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            colors_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            colors_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение установки цвета", size=12, color=colors["text_secondary"]),
                    ft.Text("t112.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            colors_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            colors_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение RGB цвета", size=12, color=colors["text_secondary"]),
                    ft.Text("t113.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Установка цвета", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Ряд виджетов в Tkinter поддерживают установку цвета для различных аспектов. Например, у виджета Label можно установить параметры foreground и background, которые отвечают за цвет текста и фона соответственно. У некоторых виджетов настройки цвета спрятаны в параметре style.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Цвет можно установить разными способами:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Именнованные цвета, например, \"red\", который соответствует красному цвету. В зависимости от платформы набор доступных именнованных цветов может отличаться. Все доступные именнованные цвета можно посмотреть в документации. Например:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('ttk.Label(text="Hello World", foreground="red")'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Можно использовать шестнадцатеричный код RGB в формате #RRGGBB:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n \nlabel = ttk.Label(text="Hello World", \n                    padding=8,\n                    foreground="#01579B", \n                    background="#B3E5FC")\nlabel.pack(anchor=CENTER, expand=1)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 1
                        ft.Container(
                            content=colors_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Установка цвета в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Если нам даны отдельные коды RGB-составляющих, то их можно сконвертировать в шестнадцатеричный код цвета:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n \ndef get_rgb(rgb):\n    return "#%02x%02x%02x" % rgb  \n \nlabel = ttk.Label(text="Hello World", \n                    padding=8,\n                    foreground=get_rgb((0, 77, 64)), \n                    background=get_rgb((128, 203, 196)))\nlabel.pack(anchor=CENTER, expand=1)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь функция get_rgb в качестве параметра получает кортеж из трех составляющих цвет RGB и с помощью форматирования строки переводит значения кортежа в шестнадцатеричный код",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 2
                        ft.Container(
                            content=colors_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("RGB to hex в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_cursors_content(self):
        colors = self.get_theme_colors()
        """Создание контента для темы 'Курсоры'"""
        return ft.Container(
            content=ft.Column([
                ft.Text("Курсоры", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Tkinter позволяет настроить форму курсора для виджетов. Для этог у виджетов применяется параметр cursor.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Виджеты могут использовать следующие курсоры:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''arrow\nbased_arrow_down\nbased_arrow_up\nboat\nbogosity\nbottom_left_corner\nbottom_right_corner\nbottom_side\nbottom_tee\nbox_spiral\ncenter_ptr\ncircle\nclock\ncoffee_mug\ncross\ncross_reverse\ncrosshair\ndiamond_cross\ndot\ndotbox\ndouble_arrow\ndraft_large\ndraft_small\ndraped_box\nexchange\nfleur\ngobbler\ngumby\nhand1\nhand2\nheart\nicon\niron_cross\nleft_ptr\nleft_side\nleft_tee\nleftbutton\nll_angle\nlr_angle\nman\nmiddlebutton\nmouse\npencil\npirate\nplus\nquestion_arrow\nright_ptr\nright_side\nright_tee\nrightbutton\nrtl_logo\nsailboat\nsb_down_arrow\nsb_h_double_arrow\nsb_left_arrow\nsb_right_arrow\nsb_up_arrow\nsb_v_double_arrow\nshuttle\nsizing\nspider\nspraycan\nstar\ntarget\ntcross\ntop_left_arrow\ntop_left_corner\ntop_right_corner\ntop_side\ntop_tee\ntrek\nul_angle\numbrella\nur_angle\nwatch\nxterm\nX_cursor'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Пример использования:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n \nttk.Label(text="Hello World!", cursor="pencil").pack(anchor=CENTER, expand=1)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Для настройки курсора окна можно установить параметр cursor через метод config():",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\nroot.config(cursor="watch")     # установка курсора\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_styles_content(self):
        colors = self.get_theme_colors()
        """Создание контента для темы 'Установка стилей'"""
        image_path1 = self.get_library_image_path("t114.png")
        image_path2 = self.get_library_image_path("t115.png")
        image_path3 = self.get_library_image_path("t116.png")
        colors = self.get_theme_colors()
        
        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            styles_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            styles_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение стилей виджетов", size=12, color=colors["text_secondary"]),
                    ft.Text("t114.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            styles_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            styles_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение встроенных стилей", size=12, color=colors["text_secondary"]),
                    ft.Text("t115.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        # Проверяем существует ли изображение 3
        if os.path.exists(image_path3):
            styles_image3 = ft.Image(
                src=image_path3,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            styles_image3 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение общих стилей", size=12, color=colors["text_secondary"]),
                    ft.Text("t116.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Установка стилей", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Стиль описывает внешний вид виджета. За установку стиля в виджетах отвечает параметр style. Встроенные виджеты по умолчанию применяют некоторые встроенные стили. В частности, все кнопки применяют стиль TButton, который описывает, как выглядят кнопки. Каждый стиль имеет имя. При создании, изменении или применении стиля к виджетам, необходимо знать его имя.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Чтобы узнать стиль определенного виджета, можно обратиться к его параметру style:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''label = ttk.Label(text="Hello World")\nlabel.pack(anchor=CENTER, expand=1)\nprint(label["style"])'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Если возвращается пустая строка, то значит, что к виджету применяется стиль по умолчанию. В этом случае название стиля можно получить с помощью метода winfo_class():",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''label = ttk.Label(text="Hello World") \n \nprint(label.winfo_class())      # TLabel'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Как правило, встроенные стили называются по имени класса виджета и предваряются буквой T. Например, для виджета Label - стиль TLabel, для Button - TButton.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Определение и применение стилей", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Стиль в Tkinter представляет объект Style. У данного объект есть метод configure(), который позволяет настроить стиль",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n \nlabel_style = ttk.Style()\nlabel_style.configure("My.TLabel",          # имя стиля\n                    font="helvetica 14",    # шрифт\n                    foreground="#004D40",   # цвет текста\n                    padding=10,             # отступы\n                    background="#B2DFDB")   # фоновый цвет\n \nlabel = ttk.Label(text="Hello World", style="My.TLabel")\nlabel.pack(anchor=CENTER, expand=1)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 1
                        ft.Container(
                            content=styles_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("стили в виджетах в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь создается стиль в виде объекта label_style. В методе configure() первым параметром передается имя стиля - в даннои случае \"My.TLabel\". Все остальные параметры настраивают различные аспекты стиля, так здесь устанавливаются шрифт, цвет фона и текста и отступы.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''label_style.configure("My.TLabel",          # имя стиля\n                    font="helvetica 14",    # шрифт\n                    foreground="#004D40",   # цвет текста\n                    padding=10,             # отступы\n                    background="#B2DFDB")   # фоновый цвет'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Затем применяем этот стиль, передавая его параметру style:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('label = ttk.Label(text="Hello World", style="My.TLabel")'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Имена стилей", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Имя создаваемых стилей имеют следующий формат:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("новый_стиль.встроенный_стиль"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Например, в примере выше название стиля \"My.TLabel\" указывает, что фактически он называется \"My\" и наследуется от \"TLabel\". И те параметры, которые не будут явным образом определены, будут унаследованы от родительского стиля \"TLabel\"",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Расширение встроенных стилей", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Вместо создания новых стилей можно просто изменить отдельные характеристики уже существующих:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n \n \nttk.Style().configure("TLabel",  font="helvetica 13", foreground="#004D40", padding=8, background="#B2DFDB") \n \nttk.Label(text="Hello World!").pack(anchor=NW, padx=6, pady=6)\nttk.Label(text="Bye World..").pack(anchor=NW, padx=6, pady=6)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 2
                        ft.Container(
                            content=styles_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("изменение встроенных стилей в виджетах в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае изменяется встроенный стиль TLabel. Он применяется к меткам по умолчанию, поэтому данный стиль не надо явным образом устанавливать для меток.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Применение стиля ко всем виджетам", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Выше стиль применялся к меткам Label, к другим же типам виджетов он не применялся. Если же мы хотим, чтобы у нас был бы общий стиль для всех типов виджетов, то в метод configure() в качестве имени стиля передается \".\"",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n \nttk.Style().configure(".",  font="helvetica 13", foreground="#004D40", padding=8, background="#B2DFDB") \n \nttk.Label(text="Hello World!").pack(anchor=NW, padx=6, pady=6)\nttk.Button(text="Click").pack(anchor=NW, padx=6, pady=6)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Подобный стиль также не надо явно применять, он применяется автоматически ко всем виджетам",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 3
                        ft.Container(
                            content=styles_image3,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("применение стилей ко всем виджетам в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_themes_content(self):
        """Создание контента для темы 'Темы'"""
        image_path1 = self.get_library_image_path("t117.png")
        image_path2 = self.get_library_image_path("t118.png")
        colors = self.get_theme_colors()
        
        # Проверяем существует ли изображение 1
        if os.path.exists(image_path1):
            themes_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            themes_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение применения темы", size=12, color=colors["text_secondary"]),
                    ft.Text("t117.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )
            
        # Проверяем существует ли изображение 2
        if os.path.exists(image_path2):
            themes_image2 = ft.Image(
                src=image_path2,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            themes_image2 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение изменения темы", size=12, color=colors["text_secondary"]),
                    ft.Text("t118.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Темы", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Тема представляет коллекцию стилей. Все стили одно темы проектируются таким образом, чтобы визуально сочетаться друг с другом. Применение определенной темы означает, что к виджетам будут применяться стили из данной темы.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "По умолчанию Tkinter уже предоставляет ряд тем. Чтобы их получить, можно использовать метод theme_names() класса ttk.Style",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import ttk\n\nfor theme in ttk.Style().theme_names():\n    print(theme)'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Стоит учитывать, что на разных операционных системах свои встроенные темы.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Для получения текущей темы можно использовать метод theme_use()",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''current_theme = ttk.Style().theme_use()\nprint(current_theme)'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Для установки другой темы в этот метод в качестве параметра передается название темы:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n \n# устанавливаем тему "classic"\nttk.Style().theme_use("classic")\n \nttk.Button(text="Click").pack(anchor=CENTER, expand=1)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 1
                        ft.Container(
                            content=themes_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Применение тем и метод theme_use в Tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text(
                            "Подобным образом мы можем определить небольшое приложение для выбора из текущих тем:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n \n# выбранная тема\nselected_theme = StringVar()\nstyle = ttk.Style()\n \n# изменение текущей темы\ndef change_theme():\n    style.theme_use(selected_theme.get())\n \nttk.Label(textvariable=selected_theme, font="Helvetica 13").pack(anchor=NW)\n \nfor theme in style.theme_names():\n    ttk.Radiobutton(text=theme, \n                value=theme,\n                variable=selected_theme,\n                command=change_theme).pack(anchor=NW)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае каждый элемент Radiobutton представляет определенную тему. При выборе определенной кнопки Radiobutton будет срабатывать функция change_theme(), в которой будет изменены текущая тема:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 2
                        ft.Container(
                            content=themes_image2,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Изменение темы и метод theme_use в Tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_canvas_elements_content(self):
        """Создание контента для темы 'Добавление элементов на Canvas'"""
        image_path1 = self.get_library_image_path("t119.png")
        image_path2 = self.get_library_image_path("t120.png")
        image_path3 = self.get_library_image_path("t121.png")
        image_path4 = self.get_library_image_path("t122.png")
        image_path5 = self.get_library_image_path("t123.png")
        image_path6 = self.get_library_image_path("t124.png")
        image_path7 = self.get_library_image_path("t125.png")
        image_path8 = self.get_library_image_path("t126.png")
        image_path9 = self.get_library_image_path("t127.png")
        image_path10 = self.get_library_image_path("t128.png")
        colors = self.get_theme_colors()
        
        # Функция для создания изображений
        def create_image(path, description, filename):
            if os.path.exists(path):
                return ft.Image(
                    src=path,
                    width=400,
                    height=300,
                    fit=ft.ImageFit.CONTAIN,
                    border_radius=10
                )
            else:
                return ft.Container(
                    content=ft.Column([
                        ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                        ft.Text(description, size=12, color=colors["text_secondary"]),
                        ft.Text(filename, size=10, color=colors["text_secondary"]),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                    width=400,
                    height=300,
                    bgcolor=colors["bg_container"],
                    border_radius=10,
                    alignment=ft.alignment.center
                )

        return ft.Container(
            content=ft.Column([
                ft.Text("Добавление элементов на Canvas", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Виджет Canvas предоставляет возможности рисования двухмерных фигур. Стоит отметить, что Canvas есть только в пакете tkinter, а в пакете tkinter.ttk аналог отсутствует.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Некоторые основные параметры Canvas:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("bg / background: фоновый цвет\n\nbd / border: граница\n\nborderwidth: толщина границы\n\ncursor: курсор\n\nheight: высота виджета\n\nwidth: ширина виджета"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "По умолчанию Canvas представляет прямоугольную область:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("300x300")\n \ncanvas = Canvas(bg="white", width=250, height=250)\ncanvas.pack(anchor=CENTER, expand=1)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 1
                        ft.Container(
                            content=create_image(image_path1, "Canvas в Tkinter", "t119.png"),
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Canvas в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text(
                            "Для двухмерного рисования Canvas предоставляет ряд методов:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("create_line(): рисует линию\n\ncreate_rectangle(): рисует прямоугольник\n\ncreate_oval(): рисует овал\n\ncreate_arc(): рисует дугу\n\ncreate_polygon(): рисует многоугольник\n\ncreate_text(): добавляет текст\n\ncreate_image(): добавляет изображение\n\ncreate_window(): добавляет виджет"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В качестве результата все эти методы возвращают идентифтикатор добавленного элемента. Этот идентификатор в дальнейшем может использоваться для управления элементом. Рассмотрим применение этих методов.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Создание линии", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для рисования линии применяется метод create_line(). Для вывода линии необходимо как минимум задать координаты точек, например:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("create_line(__x0: float, __y0: float, __x1: float, __y1: float)"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Параметры __x0 и __y0 представляют координаты начальной точки линии, а __x1 и __y1 - конечной.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Началом координат в Canvas считается верхней левый угол виджета - это точка с координатами (0,0). Таким образом, ось X направлена вправо, а ось Y - вниз.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Нарисуем простейшую линию:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("300x300")\n \ncanvas = Canvas(bg="white", width=250, height=250)\ncanvas.pack(anchor=CENTER, expand=1)\n \ncanvas.create_line(10, 10, 200, 50)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 2
                        ft.Container(
                            content=create_image(image_path2, "Создание линии", "t120.png"),
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Создание линии на Canvas в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Кроме того у данного метода можно выделить ряд дополнительных параметров:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("arrow: помещает стрелку в начале линии (значение first), в конце (last) или на обоих концах (both)\n\narrowshape: позволяет изменить форму стрелки\n\ncapstyle: если линия не имеет стрелки, то устанавливает, как завершается линия. Принимает значения: butt (по умолчанию), projecting и round\n\njoinstyle: управляет соединением сегметов линии. Принимает значения: round (по умолчанию), bevel и miter\n\nsmooth: если значение \"true\" или \"bezier\", сглаживает сегменты линии\n\nsplinesteps: управляет сглаживанием изогнутых линий"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Параметры отрисовки", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Методы отрисовки имеют ряд параметров, которые позволяют настроить стилизацию фигур. Некоторые из этих параметров:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("fill: цвет заполнения фигуры\n\nwidth: ширина линий\n\noutline: для заполненных фигур цвет контура\n\ndash: устанавливает пунктирную линию\n\nstipple: устанавливает шаблон для заполнения фигуры (например, gray75, gray50, gray25, gray12)\n\nactivefill: цвет заполнения фигуры при наведении курсора\n\nactivewidth: ширина линий при наведении курсора\n\nactivestipple: шаблон заполнения фигуры при наведении курсора"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Применим некоторые параметры:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("300x250")\n \ncanvas = Canvas(bg="white", width=250, height=200)\ncanvas.pack(anchor=CENTER, expand=1)\n \ncanvas.create_line(10, 10, 200, 50, activefill="red", fill="blue", dash=2)\ncanvas.create_line(10, 50, 200, 90, activefill="red", fill="blue", dash=2)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае нарисованы две параллельные линии пунктиром синим цветом. При наведении на них указателя мыши, они окрашиваются в красный цвет.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 3
                        ft.Container(
                            content=create_image(image_path3, "Окраска фигур", "t121.png"),
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("окраска фигур и линий в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Создание прямоугольника", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для отрисовки прямоугольника применяется метод create_rectangle(), которому обязательно передаются координаты верхнего левого и правого нижнего угла:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("create_rectangle(__x0: float, __y0: float, __x1: float, __y1: float)"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Применение метода:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("300x250")\n \ncanvas = Canvas(bg="white", width=250, height=200)\ncanvas.pack(anchor=CENTER, expand=1)\n \ncanvas.create_rectangle(10, 20, 200, 60, fill="#80CBC4", outline="#004D40")\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 4
                        ft.Container(
                            content=create_image(image_path4, "Отрисовка прямоугольника", "t122.png"),
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("отрисовка прямоугольника на Canvas в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Отрисовка овала", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для отрисовки овала применяется метод create_oval(). В качестве обязательных параметров он принимает координаты прямоугольника, в который будет вписан овал. :",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("create_oval(__x0: float, __y0: float, __x1: float, __y1: float)"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Пример использования метода:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("300x250")\n \ncanvas = Canvas(bg="white", width=250, height=200)\ncanvas.pack(anchor=CENTER, expand=1)\n \ncanvas.create_oval(10, 10, 200, 50, fill="#80CBC4", outline="#004D40")\ncanvas.create_rectangle(10, 10, 200, 50)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Для наглядности здесь также отрисован прямоугольник, чтобы было видно как вписывается овал:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 5
                        ft.Container(
                            content=create_image(image_path5, "Отрисовка овала", "t123.png"),
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("отрисовка овала на Canvas в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Отрисовка многоугольника", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для создания многоугольника применяется метод create_polygon(). Он принимает в качестве обязательных параметров набор координатов точек:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("300x250")\n \ncanvas = Canvas(bg="white", width=250, height=200)\ncanvas.pack(anchor=CENTER, expand=1)\n \ncanvas.create_polygon(10, 30, 200, 200, 200, 30, fill="#80CBC4", outline="#004D40")\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае передаются координаты трех точек, которые в итоге станут вершинами треугольника",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 6
                        ft.Container(
                            content=create_image(image_path6, "Отрисовка многоугольника", "t124.png"),
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("отрисовка многоугольника на Canvas в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Для упрощения также можно передавать набор кортежей, где каждый кортеж представляет отдельную точку:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''points = (\n    (10, 30),\n    (200, 200),\n    (200, 30),\n)\ncanvas.create_polygon(*points, fill="#80CBC4", outline="#004D40")'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Отрисовка дуги", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для отрисовки дуги применяется метод create_arc(), который принимает набор точек:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("300x250")\n \ncanvas = Canvas(bg="white", width=250, height=200)\ncanvas.pack(anchor=CENTER, expand=1)\n \ncanvas.create_arc((10, 10), (200, 200), fill="#80CBC4", outline="#004D40")\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 7
                        ft.Container(
                            content=create_image(image_path7, "Отрисовка дуги", "t125.png"),
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("отрисовка дуги на Canvas в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Отображение текста", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для вывода текста применяется метод create_text(). Ключевыми его параметрами являются координаты точки вывода текста, а также параметр text - сам выводимый текст:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "При выводе текста стоит учитывать, что по умолчанию указанные координаты представляют центральную точку вывода текста. Но это поведение можно изменить с помощью опции anchor.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("300x250")\n \ncanvas = Canvas(bg="white", width=250, height=200)\ncanvas.pack(anchor=CENTER, expand=1)\n \ncanvas.create_text(50, 50, text="Hello METANIT.COM", fill="#004D40")\n \ncanvas.create_text(50, 100, anchor=NW, text="Hello METANIT.COM", fill="#004D40")\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь два раза выводится один и тот же текст. И в обоих случаях совпадает X-координата. Но во втором случае установлен параметр anchor: его значение \"NW\" указывает, что координаты будут представлять верхний левый угол прямогольной области, в которой выводится текст",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 8
                        ft.Container(
                            content=create_image(image_path8, "Вывод текста", "t126.png"),
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("вывод текста на Canvas в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "С помощью параметра font можно задать шрифт, в том числе его высоту:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('canvas.create_text(10, 10, font="Arial 14", anchor=NW, text="Hello METANIT.COM", fill="#004D40")'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Вывод изображения", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для вывода изображения применяется метод create_image(), который в качестве обязательно параметра принимает координаты изображения. Для установки самого изображения в метод через параметр image передается ссылка на изображение:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("300x250")\n \ncanvas = Canvas(bg="white", width=250, height=200)\ncanvas.pack(anchor=CENTER, expand=1)\n \npython_image = PhotoImage(file="python.png")\n \ncanvas.create_image(10, 10, anchor=NW, image=python_image)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае координаты представлены точкой с x=10 и y=10, а изображение представляет объект PhotoImage (здесь предполагается, что в одной папке с файлом программы находится файл \"python.png\"). Но как и в случае с выводом текста, следует учитывать, что по умолчанию координаты представляют центр изображения. Чтобы настроить положение изображения относительно координат, применяется параметр anchor. Так, в данном случае значение \"NW\" означает, что координата представляет верхний левый угол изображения.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 9
                        ft.Container(
                            content=create_image(image_path9, "Вывод изображения", "t127.png"),
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("вывод изображения на Canvas в tkinter и python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Добавление виджетов", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Одной из замечательных особенностей Canvas является то, что он позволяет добавлять другие виджеты и таким образом создавать сложные по композиции интерфейсы. Для этого применяется метод create_window().",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''create_window(__x: float, __y: float, *, anchor: _Anchor = ..., height: _ScreenUnits = ..., state: Literal['normal', 'active', 'disabled'] = ..., tags: str | list[str] | tuple[str, ...] = ..., width: _ScreenUnits = ..., window: Widget = ...) -> _CanvasItemId\ncreate_window(__coords: tuple[float, float] | list[int] | list[float], *, anchor: _Anchor = ..., height: _ScreenUnits = ..., state: Literal['normal', 'active', 'disabled'] = ..., tags: str | list[str] | tuple[str, ...] = ..., width: _ScreenUnits = ..., window: Widget = ...) -> _CanvasItemId'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Параметры",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("_x и _y или __coords: координаты точки размещения виджета. По умолчанию представляет центр виджета\n\n_anchor: устанавливает положение виджета относительно координат\n\nheight: высота виджета\n\nwidth: ширина виджета\n\nstate: состояние виджета\n\ntags: набор тегов, связанных с виджетом"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "В качестве результата этот метод возвращает идентификатор добавленного метода.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Например, добавим кнопку:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("300x250")\n \ncanvas = Canvas(bg="white", width=250, height=200)\ncanvas.pack(anchor=CENTER, expand=1)\n \nbtn = ttk.Button(text="Click")\ncanvas.create_window(10, 20, anchor=NW, window=btn, width=100, height=50)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае верхний левый угол кнопки будет иметь координаты (x=10, y=20), а сама кнопка имеет ширину 100 и высоту 50 единиц. Если ширина и высота явным образом не указаны, то они имеют значения по умолчанию.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение 10
                        ft.Container(
                            content=create_image(image_path10, "Добавление виджетов", "t128.png"),
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Добавление виджетов в Canvas в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        ft.Container(height=20),
                        
                        ft.Text("Создание прокрутки", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для создания прокрутки виджет Canvas предоставляет параметр , который позволяет установить прокручиваемую область:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n \nh = ttk.Scrollbar(orient=HORIZONTAL)\nv = ttk.Scrollbar(orient=VERTICAL)\ncanvas = Canvas(scrollregion=(0, 0, 1000, 1000), bg="white", yscrollcommand=v.set, xscrollcommand=h.set)\nh["command"] = canvas.xview\nv["command"] = canvas.yview\n \ncanvas.grid(column=0, row=0, sticky=(N,W,E,S))\nh.grid(column=0, row=1, sticky=(W,E))\nv.grid(column=1, row=0, sticky=(N,S))\nroot.grid_columnconfigure(0, weight=1)\nroot.grid_rowconfigure(0, weight=1)\n \ncanvas.create_rectangle(10,10, 300, 300, fill="red")\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае устанавливается прокручиваемая область 1000х1000:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('canvas = Canvas(scrollregion=(0, 0, 1000, 1000), ....'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_canvas_management_content(self):
        """Создание контента для темы 'Управление элементами в Canvas'"""
        image_path1 = self.get_library_image_path("t129.png")
        colors = self.get_theme_colors()
        
        # Проверяем существует ли изображение
        if os.path.exists(image_path1):
            canvas_management_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            canvas_management_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение управления элементами", size=12, color=colors["text_secondary"]),
                    ft.Text("t129.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Управление элементами в Canvas", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text("Удаление элемента", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для удаления применяется метод delete(), который в качестве параметра принимает идентификатор удаляемого элемента.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("300x250")\n \ncanvas = Canvas(bg="white", width=250, height=200)\ncanvas.pack(anchor=CENTER, expand=1)\n \n \ndef remove_button():\n    canvas.delete(btnId)\n \nbtn = ttk.Button(text="Click", command=remove_button)\nbtnId = canvas.create_window(10, 20, anchor=NW, window=btn, width=100, height=50)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь по нажатию на кнопку удаляется сама кнопка. В качестве аргумента в метод delete() передается идентификатор, который мы получаем при добавлении кнопки.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Управление координатами", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для получения/изменения координат элеимента применяется метод coords():",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''# получение координат\ncoords(__tagOrId: str | _CanvasItemId, /) -> list[float]     \n \n# изменение координат\ncoords(__tagOrId: str | _CanvasItemId, __args: list[int] | list[float] | tuple[float, ...], /) -> None\ncoords(__tagOrId: str | _CanvasItemId, __x1: float, __y1: float, *args: float) -> None'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Первая версия возвращает координаты в виде списка значений для элемента с определенным идентификатором.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Вторая и третья версии изменяют позицию, получая в качестве второго/третьего параметра(ов) новые координаты.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Например, динамически изменим координаты:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("300x250")\n \ny = 0\ndirection = -10\nbtn_height = 40\ncanvas_height = 200\n \ncanvas = Canvas(bg="white", width=250, height=canvas_height)\ncanvas.pack(anchor=CENTER, expand=1)\n \ndef cliked_button():\n    global y, direction\n    if y >= canvas_height - btn_height or y <=0: direction = direction * -1\n    y = y + direction\n    canvas.coords(btnId, 10, y)\n \nbtn = ttk.Button(text="Click", command=cliked_button)\nbtnId = canvas.create_window(10, y, anchor=NW, window=btn, width=100, height=btn_height)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь по нажатию на кнопку к координате y добавляется +-10. Когда кнопка достигает границ Canvas, то изменяем знак приращения на противоположный, и таким образом, кнопка изменяет направление движения.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Изменение параметров элемента", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для изменения параметров элемента на Canvas применяется метод itemconfigure(). В качестве обязательного параметра он принимает идентифкатор изменяемого элемента, а второй параметр - набор устанавливаемых параметров:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("itemconfigure: (tagOrId: str | _CanvasItemId, cnf: dict[str, Any] | None = ..., **kw: Any)"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Например, изменим цвет линии:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("300x250")\n \nred = "red"\nblue= "blue"\n \nselected_color = StringVar(value=red)\n \ncanvas = Canvas(bg="white", width=250, height=150)\ncanvas.pack(anchor=CENTER, expand=1)\n \ndef select():\n    canvas.itemconfigure(line, fill=selected_color.get())\n \nred_btn = ttk.Radiobutton(text=red, value=red, variable=selected_color, command=select, padding=6)\nred_btn.pack(anchor=NW)\nblue_btn = ttk.Radiobutton(text=blue, value=blue, variable=selected_color, command=select, padding=6)\nblue_btn.pack(anchor=NW)\n \nline = canvas.create_line(10, 10, 200, 100, fill=selected_color.get())\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае в окне определены два переключателя Radiobutton. Они привязаны к переменной selected_color, которая хранит выбранный цвет - \"red\" или \"blue\".",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "На canvas нарисована линия. При нажатии на один из переключателей изменяем цвет линии:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение
                        ft.Container(
                            content=canvas_management_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("itemconfigure и изменение параметров элементов в Canvas в Tkinter и Python", size=14, color=colors["text_secondary"], italic=True),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_canvas_tags_content(self):
        """Создание контента для темы 'Установка тегов'"""
        image_path1 = self.get_library_image_path("t130.png")
        colors = self.get_theme_colors()
        
        # Проверяем существует ли изображение
        if os.path.exists(image_path1):
            canvas_tags_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            canvas_tags_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение тегов Canvas", size=12, color=colors["text_secondary"]),
                    ft.Text("t130.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Установка тегов", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "При добавлении элемента в Canvas этому элементу автоматически присваивается числовой идентификатор. С помощью этого идентификатора затем мы можем ссылаться на данный элемент. Однако Canvas также поддерживает добавление тегов, через которые также можно ссылаться на элементы внутри Canvas. Более того каждому элементу можно назначить несколько тегов. Также нескольким элементам можно назначить один и тот же тег, благодаря чему можно ссылать не только на один элеимент, но и на группу элементов.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Установка тегов", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для установки тега элементу при его добавлении можно использовать параметр tags, который получает список тегов:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('canvas.create_line(10, 10, 200, 100, fill="red", tags=["line"])'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "В данном случае линии добавляется тег \"line\".",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Добавление тега", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для добавления тега можно использовать метод addtag():",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("addtag(название_тега, команда, идентификатор_элемента)"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Первый параметр - добавляемый тег, второй параметр - команда, обычно \"withtag\". Третий параметр - идентификатор элемента, для которого добавляется тег:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''line_id = canvas.create_line(10, 10, 200, 100, fill="red", tags=["line"])\ncanvas.addtag("figure", "withtag", line_id)'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Здесь для элемента line_id добавляется тег \"figure\"",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Получение тегов", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для получения списка тегов для определенного элемента применяется метод gettags(), в который передается идентификатор элеимента:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''line_id = canvas.create_line(10, 10, 200, 100, fill="red", tags=["line", "figure"])\n# получаем все теги для элемента line_id\nfor tag in canvas.gettags(line_id):\n    print(tag)'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Также можно получить идентификаторы элементов по определенному тегу с помощью метода find_withtag(), в который передается имя тега.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''canvas.create_line(10, 10, 200, 10, fill="red", tags=["line", "figure"])\ncanvas.create_line(10, 50, 200, 50, fill="blue", tags="line")\n# получаем все элементы с тегом line\nfor element_id in canvas.find_withtag("line"):\n    print(element_id)'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Удаление тега", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Для удаления тега применяется метод dtags()",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''line_id = canvas.create_line(10, 10, 200, 10, fill="red", tags=["line", "figure"])\n# удаляем у элемента line_id тег "figure"\ncanvas.dtag(line_id, "figure")'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "В метод dtag() передается идентификатор элемента и удаляемый тег.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Конфигурация через тег", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "С помощью метода itemconfigure() для элементов с определенным тегом можно установить различные опции",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("itemconfigure: (tagOrId: str | _CanvasItemId, cnf: dict[str, Any] | None = ..., **kw: Any)"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Первый параметр - тег или идентификатор элемента, а второй - набор устанавливаемых опций. Например:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''canvas.create_line(10, 50, 200, 50, fill="blue", tags="line")\n# устанавливаем для элементов с тегом "line" зеленый цвет\ncanvas.itemconfigure("line", fill="green")'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=20),
                        
                        ft.Text("Практическое использование тегов", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Одний из ключевых возможностей тегов состоит в том, что они позволяют управлять группой элементов:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x250")\n \nred = "red"\nblue= "blue"\ngreen = "green"\nselected_color = StringVar(value=red)\n \ncanvas = Canvas(bg="white", width=250, height=150)\ncanvas.pack(anchor=NW)\n \ncanvas.create_rectangle((10, 80, 130, 130), fill=selected_color.get(), outline="black", tags="house")\ncanvas.create_polygon((10, 80), (70, 30), (130, 80), fill=selected_color.get(), outline="black", tags="house")\n \ndef select():\n    canvas.itemconfigure("house", fill=selected_color.get())\n \nttk.Radiobutton(text=red, value=red, variable=selected_color, command=select, padding=6).pack(anchor=NW)\nttk.Radiobutton(text=blue, value=blue, variable=selected_color, command=select, padding=6).pack(anchor=NW)\nttk.Radiobutton(text=green, value=green, variable=selected_color, command=select, padding=6).pack(anchor=NW)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "В данном случае на Canvas отрисованы две фигуры - прямоугольник и многоугольник. Оба этих элемента имеют тег \"house\".",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "На окне также определены три переключателя Radiobutton, которые привязаны к переменной selected_color и позволяют выбрать цвет. При выборе одного из переключателей срабатывает функция select, в которой для элементов с тегом \"house\" устанавливается определенный цвет.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение
                        ft.Container(
                            content=canvas_tags_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def create_canvas_events_content(self):
        """Создание контента для темы 'Привязка событий'"""
        image_path1 = self.get_library_image_path("131.png")
        colors = self.get_theme_colors()
        
        # Проверяем существует ли изображение
        if os.path.exists(image_path1):
            canvas_events_image1 = ft.Image(
                src=image_path1,
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        else:
            canvas_events_image1 = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.IMAGE, size=60, color=colors["text_secondary"]),
                    ft.Text("Изображение привязки событий", size=12, color=colors["text_secondary"]),
                    ft.Text("131.png", size=10, color=colors["text_secondary"]),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER),
                width=400,
                height=300,
                bgcolor=colors["bg_container"],
                border_radius=10,
                alignment=ft.alignment.center
            )

        return ft.Container(
            content=ft.Column([
                ft.Text("Привязка событий", size=24, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=20),
                
                # Кнопка назад
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["text_secondary"]),
                        ft.Text("Назад к оглавлению", color=colors["text_secondary"]),
                    ]),
                    on_click=lambda e: self.show_library_page(),
                ),
                ft.Container(height=30),
                
                # Основной контент с прокруткой
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "С помощью метода tag_bind() можно привязать к определенному элементу в Canvas (например, к линии) событие:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax("tag_bind(тег_или_идентификатор_элемента, событие, функция)"),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Первый параметр представляет тег или идентификатор элеиментов, для которых добавляется событие.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=5),
                        
                        ft.Text(
                            "Второй параметр - обрабатываемое событие.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=5),
                        
                        ft.Text(
                            "Третий параметр - функция, которая выполняется при возникновении события",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Рассмотрим небольшой пример:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('''from tkinter import *\nfrom tkinter import ttk\n \nroot = Tk()\nroot.title("METANIT.COM")\nroot.geometry("250x200")\n \ncanvas = Canvas(bg="white", width=250, height=150)\ncanvas.pack(fill=BOTH, expand=1)\n \n# размеры прямоугольника\nbig_size = (60, 60, 150, 150)\nsmall_size = (60, 60, 100, 100)\n \n# обработчики событий\ndef make_big(event): canvas.coords(id, big_size)\ndef make_small(event): canvas.coords(id, small_size)\n \nid = canvas.create_rectangle(small_size, fill="red")\n# привязка событий к элементу с идентификатором id\ncanvas.tag_bind(id, "<Enter>", make_big)\ncanvas.tag_bind(id, "<Leave>", make_small)\n \nroot.mainloop()'''),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=15),
                        
                        ft.Text(
                            "Здесь на Canvas добавляется прямоугольник, идентификатор которого хранится в переменной id.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Сначала привязываем к прямоугольнику с идентификатором id событие \"<Enter>\", то есть событие вхождения курсора в пределы прямогольника:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('canvas.tag_bind(id, "<Enter>", make_big)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Когда указатель мыши окажется в пределах прямогольника, сработает функция make_big, которая с помощью метода canvas.coords изменит координаты и размеры прямоугольника:",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=10),
                        
                        ft.Container(
                            content=self.highlight_syntax('def make_big(event): canvas.coords(id, big_size)'),
                            padding=15,
                            bgcolor=colors["bg_container"],
                            border_radius=10,
                        ),
                        ft.Container(height=10),
                        
                        ft.Text(
                            "Аналогичным образом привязывается событие \"<Leave>\", которое срабатывает, когда указатель мыши выходит за пределы прямоугольника. В этом случае срабатывает функция make_small, которая уменьшит размер прямоугольника.",
                            size=14, color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                        
                        # Изображение
                        ft.Container(
                            content=canvas_events_image1,
                            alignment=ft.alignment.center,
                            margin=ft.margin.symmetric(vertical=10)
                        ),
                        
                        ft.Text("Привязка событий в Canvas в приложении на tkinter в Python", size=14, color=colors["text_secondary"], italic=True),
                        
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    expand=True,
                )
            ]),
            bgcolor=colors["bg_container"],
            border_radius=15,
            padding=30,
            expand=True
        )

    def show_videos_page(self):
        """Страница видео уроков"""
        colors = self.get_theme_colors()
        video_cards = []
        for i, video in enumerate(self.videos):
            video_cards.append(self.create_video_lesson_card(video, i))
            # Добавляем разделитель между карточками (кроме последней)
            if i < len(self.videos) - 1:
                video_cards.append(ft.Divider(color=colors["divider"], height=1, thickness=1))

        content = ft.Container(
            content=ft.Column([
                self.create_page_header("Видео уроки", "Интерактивное обучение Tkinter"),
                ft.Container(height=20),
                
                # Список видео уроков в одном контейнере с разделителями и скроллом
                ft.Container(
                    content=ft.Column(video_cards, scroll=ft.ScrollMode.ADAPTIVE),
                    bgcolor=colors["bg_container"],
                    border_radius=15,
                    padding=0,
                    expand=True,
                )
            ]),
            expand=True
        )
        self.update_content(content, "videos")

    def show_functions_page(self):
        """Страница функций"""
        colors = self.get_theme_colors()
        content = ft.Container(
            content=ft.Column([
                self.create_page_header("Функции Tkinter", "20 самых полезных функций для работы с GUI"),
                ft.Container(height=20),
                
                ft.Container(
                    content=ft.Column([
                        # 20 функций Tkinter
                        self.create_function_card(
                            "1. Функция выхода из приложения",
                            "Безопасное закрытие приложения с подтверждением",
                            '''def quit_app():\n    if messagebox.askokcancel("Выход", "Вы уверены, что хотите выйти?"):\n        root.destroy()\n        # или root.quit() для закрытия всего приложения'''
                        ),
                        
                        self.create_function_card(
                            "2. Добавление задачи в Listbox",
                            "Добавление новой задачи с валидацией пустого ввода",
                            '''def add_task():\n    task = entry.get().strip()\n    if task == "":\n        messagebox.showwarning("Ошибка", "Поле не может быть пустым")\n        return\n    tasks.append(task)\n    listbox.insert(tk.END, task)\n    entry.delete(0, tk.END)'''
                        ),
                        
                        self.create_function_card(
                            "3. Удаление выбранной задачи",
                            "Удаление задачи с обработкой ошибок выбора",
                            '''def delete_task():\n    try:\n        selected_index = listbox.curselection()[0]\n        listbox.delete(selected_index)\n        tasks.pop(selected_index)\n    except IndexError:\n        messagebox.showwarning("Ошибка", "Выберите задачу для удаления")'''
                        ),
                        
                                            self.create_function_card(
                        "1. Функция выхода из приложения",
                        "Безопасное закрытие приложения с подтверждением",
                        '''def quit_app():\n    if messagebox.askokcancel("Выход", "Вы уверены, что хотите выйти?"):\n        root.destroy()\n        # или root.quit() для закрытия всего приложения'''
                    ),
                    
                    self.create_function_card(
                        "2. Добавление задачи в Listbox",
                        "Добавление новой задачи с валидацией пустого ввода",
                        '''def add_task():\n    task = entry.get().strip()\n    if task == "":\n        messagebox.showwarning("Ошибка", "Поле не может быть пустым")\n        return\n    tasks.append(task)\n    listbox.insert(tk.END, task)\n    entry.delete(0, tk.END)'''
                    ),
                    
                    self.create_function_card(
                        "3. Удаление выбранной задачи",
                        "Удаление задачи с обработкой ошибок выбора",
                        '''def delete_task():\n    try:\n        selected_index = listbox.curselection()[0]\n        listbox.delete(selected_index)\n        tasks.pop(selected_index)\n    except IndexError:\n        messagebox.showwarning("Ошибка", "Выберите задачу для удаления")'''
                    ),
                    
                    self.create_function_card(
                        "4. Очистка всех записей",
                        "Полная очистка списка с подтверждением",
                        '''def clear_all():\n    if messagebox.askyesno("Подтверждение", "Удалить все записи?"):\n        listbox.delete(0, tk.END)\n        tasks.clear()'''
                    ),
                    
                    self.create_function_card(
                        "5. Редактирование выбранной записи",
                        "Открытие окна редактирования для выбранной задачи",
                        '''def edit_task():\n    try:\n        selected_index = listbox.curselection()[0]\n        current_text = listbox.get(selected_index)\n        \n        edit_window = tk.Toplevel(root)\n        edit_window.title("Редактирование")\n        \n        edit_entry = tk.Entry(edit_window, width=30)\n        edit_entry.insert(0, current_text)\n        edit_entry.pack(padx=10, pady=10)\n        \n        def save_edit():\n            new_text = edit_entry.get().strip()\n            if new_text:\n                listbox.delete(selected_index)\n                listbox.insert(selected_index, new_text)\n                tasks[selected_index] = new_text\n                edit_window.destroy()\n        \n        tk.Button(edit_window, text="Сохранить", command=save_edit).pack(pady=5)\n        \n    except IndexError:\n        messagebox.showwarning("Ошибка", "Выберите задачу для редактирования")'''
                    ),
                    
                    self.create_function_card(
                        "6. Сохранение данных в файл",
                        "Сохранение списка задач в текстовый файл",
                        '''def save_to_file():\n    filename = filedialog.asksaveasfilename(\n        defaultextension=".txt",\n        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]\n    )\n    if filename:\n        with open(filename, 'w', encoding='utf-8') as file:\n            for task in tasks:\n                file.write(task + '\\n')\n        messagebox.showinfo("Успех", "Данные сохранены")'''
                    ),
                    
                    self.create_function_card(
                        "7. Загрузка данных из файла",
                        "Загрузка списка задач из текстового файла",
                        '''def load_from_file():\n    filename = filedialog.askopenfilename(\n        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]\n    )\n    if filename:\n        clear_all()\n        with open(filename, 'r', encoding='utf-8') as file:\n            for line in file:\n                task = line.strip()\n                if task:\n                    tasks.append(task)\n                    listbox.insert(tk.END, task)'''
                    ),
                    
                    self.create_function_card(
                        "8. Поиск по списку",
                        "Фильтрация задач по поисковому запросу",
                        '''def search_tasks():\n    search_term = search_entry.get().strip().lower()\n    if not search_term:\n        return\n    \n    listbox.delete(0, tk.END)\n    for task in tasks:\n        if search_term in task.lower():\n            listbox.insert(tk.END, task)'''
                    ),
                    
                    self.create_function_card(
                        "9. Сброс поиска",
                        "Восстановление полного списка после поиска",
                        '''def reset_search():\n    search_entry.delete(0, tk.END)\n    listbox.delete(0, tk.END)\n    for task in tasks:\n        listbox.insert(tk.END, task)'''
                    ),
                    
                    self.create_function_card(
                        "10. Сортировка списка",
                        "Алфавитная сортировка всех задач",
                        '''def sort_tasks():\n    tasks.sort()\n    listbox.delete(0, tk.END)\n    for task in tasks:\n        listbox.insert(tk.END, task)'''
                    ),
                    
                    self.create_function_card(
                        "11. Перемещение задачи вверх",
                        "Изменение порядка задач - перемещение вверх",
                        '''def move_up():\n    try:\n        selected_index = listbox.curselection()[0]\n        if selected_index > 0:\n            tasks[selected_index], tasks[selected_index-1] = tasks[selected_index-1], tasks[selected_index]\n            refresh_listbox()\n            listbox.select_set(selected_index-1)\n    except IndexError:\n        messagebox.showwarning("Ошибка", "Выберите задачу")'''
                    ),
                    
                    self.create_function_card(
                        "12. Перемещение задачи вниз",
                        "Изменение порядка задач - перемещение вниз",
                        '''def move_down():\n    try:\n        selected_index = listbox.curselection()[0]\n        if selected_index < len(tasks) - 1:\n            tasks[selected_index], tasks[selected_index+1] = tasks[selected_index+1], tasks[selected_index]\n            refresh_listbox()\n            listbox.select_set(selected_index+1)\n    except IndexError:\n        messagebox.showwarning("Ошибка", "Выберите задачу")'''
                    ),
                    
                    self.create_function_card(
                        "13. Обновление Listbox",
                        "Перерисовка списка задач",
                        '''def refresh_listbox():\n    listbox.delete(0, tk.END)\n    for task in tasks:\n        listbox.insert(tk.END, task)'''
                    ),
                    
                    self.create_function_card(
                        "14. Подсчет элементов",
                        "Отображение статистики по задачам",
                        '''def count_tasks():\n    count = len(tasks)\n    messagebox.showinfo("Статистика", f"Всего задач: {count}")'''
                    ),
                    
                    self.create_function_card(
                        "15. Отметка выполнения",
                        "Пометка задачи как выполненной",
                        '''def mark_completed():\n    try:\n        selected_index = listbox.curselection()[0]\n        current_text = listbox.get(selected_index)\n        if not current_text.startswith("✓ "):\n            listbox.delete(selected_index)\n            listbox.insert(selected_index, "✓ " + current_text)\n            tasks[selected_index] = "✓ " + current_text\n    except IndexError:\n        messagebox.showwarning("Ошибка", "Выберите задачу")'''
                    ),
                    
                    self.create_function_card(
                        "16. Смена темы",
                        "Переключение между светлой и темной темами",
                        '''def toggle_theme():\n    current_bg = root.cget('bg')\n    if current_bg == 'white':\n        root.configure(bg='lightgray')\n        listbox.configure(bg='lightyellow')\n    else:\n        root.configure(bg='white')\n        listbox.configure(bg='white')'''
                    ),
                    
                    self.create_function_card(
                        "17. Валидация ввода",
                        "Ограничение длины вводимого текста",
                        '''def validate_entry(text):\n    return len(text) <= 50  # Ограничение длины\n\n# Использование:\nvcmd = root.register(validate_entry)\nentry = tk.Entry(root, validate="key", validatecommand=(vcmd, '%P'))'''
                    ),
                    
                    self.create_function_card(
                        "18. Обновление статусной строки",
                        "Отображение статистики в реальном времени",
                        '''def update_status(event=None):\n    count = len(tasks)\n    completed = sum(1 for task in tasks if task.startswith("✓ "))\n    status_label.config(text=f"Всего: {count} | Выполнено: {completed}")'''
                    ),
                    
                    self.create_function_card(
                        "19. Копирование в буфер обмена",
                        "Копирование текста задачи в буфер обмена",
                        '''def copy_to_clipboard():\n    try:\n        selected_index = listbox.curselection()[0]\n        task_text = listbox.get(selected_index)\n        root.clipboard_clear()\n        root.clipboard_append(task_text)\n        messagebox.showinfo("Успех", "Текст скопирован в буфер обмена")\n    except IndexError:\n        messagebox.showwarning("Ошибка", "Выберите задачу для копирования")'''
                    ),
                    
                    self.create_function_card(
                        "20. Импорт/экспорт JSON",
                        "Работа с данными в формате JSON",
                        '''def export_json():\n    filename = filedialog.asksaveasfilename(defaultextension=".json")\n    if filename:\n        import json\n        with open(filename, 'w', encoding='utf-8') as file:\n            json.dump(tasks, file, ensure_ascii=False, indent=2)\n\ndef import_json():\n    filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])\n    if filename:\n        import json\n        with open(filename, 'r', encoding='utf-8') as file:\n            global tasks\n            tasks = json.load(file)\n        refresh_listbox()'''
                    ),
                    
                    # Пример использования
                    ft.Container(
                        content=ft.Column([
                            ft.Text("Пример использования:", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                            ft.Container(height=10),
                            ft.Container(
                                content=ft.Text(
                                    '''import tkinter as tk \n from tkinter import messagebox, filedialog\n \n # Глобальные переменные\n tasks = []\n \n # Создание основного окна\n root = tk.Tk()\n root.title("Менеджер задач")\n # Создание элементов интерфейса\n entry = tk.Entry(root, width=30)\n listbox = tk.Listbox(root, width=50, height=15)\n \n # Кнопки с привязкой функций\n tk.Button(root, text="Добавить", command=add_task).pack()\n tk.Button(root, text="Удалить", command=delete_task).pack()\n tk.Button(root, text="Выход", command=quit_app).pack()\n \n root.mainloop()''',
                                    size=12, 
                                    color=colors["text_secondary"], 
                                    font_family="Courier New"
                                ),
                                padding=15,
                                bgcolor=colors["bg_container"],
                                border_radius=10,
                            )
                        ]),
                        padding=20,
                        bgcolor=colors["bg_container"],
                        border_radius=15,
                        margin=ft.margin.only(top=20)
                    )
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    bgcolor=colors["bg_primary"],
                    expand=True,
                )
            ]),
            expand=True
        )
        self.update_content(content, "functions")

    def open_file(self, file_path):
        """Открытие файла в системном приложении"""
        try:
            # Проверяем существование файла
            if os.path.exists(file_path):
                if sys.platform == "win32":
                    os.startfile(file_path)
                elif sys.platform == "darwin":  # macOS
                    os.system(f'open "{file_path}"')
                else:  # linux
                    os.system(f'xdg-open "{file_path}"')
            else:
                print(f"Файл не найден: {file_path}")
        except Exception as e:
            print(f"Ошибка при открытии файла: {e}")

    def create_task_card(self, num, title, goal, requirements, functions, level):
        """Создание карточки задания"""
        colors = self.get_theme_colors()
        
        # Цвета для уровней
        level_colors = {
            "beginner": "#4CAF50",  # Зеленый
            "intermediate": "#FF9800",  # Оранжевый
            "advanced": "#F44336"  # Красный
        }
        
        level_icons = {
            "beginner": ft.Icons.STAR_OUTLINE,
            "intermediate": ft.Icons.STAR_HALF,
            "advanced": ft.Icons.STAR
        }
        
        level_names = {
            "beginner": "Начальный",
            "intermediate": "Промежуточный",
            "advanced": "Продвинутый"
        }
        
        return ft.Container(
            content=ft.Column([
                # Заголовок с номером
                ft.Container(
                    content=ft.Text(
                        f"Задание {num}",
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        color=colors["text_primary"]
                    ),
                    bgcolor=level_colors[level],
                    padding=ft.padding.symmetric(horizontal=12, vertical=6),
                    border_radius=8,
                ),
                ft.Container(height=10),
                
                # Название задания
                ft.Text(title, size=20, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=8),
                
                # Цель
                ft.Row([
                    ft.Icon(ft.Icons.GPS_FIXED, size=18, color=colors["text_secondary"]),
                    ft.Text("Цель:", size=14, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ]),
                ft.Text(goal, size=14, color=colors["text_secondary"]),
                ft.Container(height=12),
                
                # Требования
                ft.Row([
                    ft.Icon(ft.Icons.CHECKLIST, size=18, color=colors["text_secondary"]),
                    ft.Text("Требования:", size=14, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ]),
                ft.Container(height=5),
                ft.Column([
                    ft.Text(f"• {req}", size=13, color=colors["text_secondary"]) for req in requirements
                ], spacing=4),
                ft.Container(height=12),
                
                # Функции
                ft.Row([
                    ft.Icon(ft.Icons.CODE, size=18, color=colors["text_secondary"]),
                    ft.Text("Функции:", size=14, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ]),
                ft.Container(height=5),
                ft.Container(
                    content=ft.Text(functions, size=12, color=colors["text_secondary"], font_family="Courier New"),
                    padding=10,
                    bgcolor=colors["bg_tertiary"],
                    border_radius=8,
                ),
                ft.Container(height=15),
                
                # Кнопка просмотра готового кода
                ft.ElevatedButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.VISIBILITY, size=18),
                        ft.Text("Просмотреть готовый код", size=14, weight=ft.FontWeight.BOLD),
                    ], tight=True),
                    on_click=lambda e, task_num=num: self.preview_task_code(task_num),
                    bgcolor=level_colors[level],
                    color=colors["text_primary"],
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                    ),
                ),
            ], spacing=0),
            padding=20,
            bgcolor=colors["bg_container"],
            border_radius=12,
            border=ft.border.all(1, level_colors[level]),
            margin=ft.margin.only(bottom=15),
        )

    def show_trainer_page(self):
        """Страница тренажера"""
        colors = self.get_theme_colors()
        
        # Задания начального уровня
        beginner_tasks = [
            {
                "num": 1,
                "title": "Кнопка-счетчик",
                "goal": "Освоить базовые виджеты и обработку событий.",
                "requirements": [
                    "Создать окно размером 300x200 пикселей",
                    "Добавить метку Label с текстом 'Счетчик: 0'",
                    "Добавить кнопку Button с текстом 'Нажать'",
                    "При каждом нажатии на кнопку счетчик должен увеличиваться на 1",
                    "Текст метки должен обновляться в реальном времени"
                ],
                "functions": "Button, Label, config(), IntVar"
            },
            {
                "num": 2,
                "title": "Конвертер температур",
                "goal": "Работа с полями ввода и преобразование данных.",
                "requirements": [
                    "Создать два поля ввода Entry для Цельсия и Фаренгейта",
                    "Добавить кнопку 'Конвертировать'",
                    "При вводе в поле Цельсия и нажатии кнопки - вычислять Фаренгейты по формуле: F = C × 9/5 + 32",
                    "При вводе в поле Фаренгейта - вычислять Цельсии по формуле: C = (F - 32) × 5/9",
                    "Реализовать автоматическую конвертацию при изменении текста (без кнопки)"
                ],
                "functions": "Entry, StringVar, trace(), get()"
            },
            {
                "num": 3,
                "title": "Простой список дел",
                "goal": "Освоить Listbox и управление элементами.",
                "requirements": [
                    "Поле ввода Entry для новой задачи",
                    "Кнопка 'Добавить' для помещения задачи в список",
                    "Listbox для отображения всех задач",
                    "Кнопка 'Удалить' для удаления выбранной задачи",
                    "Двойной клик по задаче должен удалять ее",
                    "При пустом поле ввода - кнопка 'Добавить' должна быть неактивной"
                ],
                "functions": "Listbox, insert(), delete(), bind()"
            },
            {
                "num": 4,
                "title": "Цветовой микшер",
                "goal": "Работа с шкалами (Scale) и динамическое обновление.",
                "requirements": [
                    "Три шкалы Scale от 0 до 255 для RGB цветов",
                    "Метка Label которая показывает текущие значения RGB",
                    "Холст Canvas размером 200x200 пикселей для предпросмотра цвета",
                    "При перемещении любого ползунка цвет холста должен мгновенно меняться",
                    "В метке должен отображаться hex-код цвета (например, #FF0034)"
                ],
                "functions": "Scale, Canvas, configure()"
            },
            {
                "num": 5,
                "title": "Простой текстовый редактор",
                "goal": "Освоить многострочный ввод и меню.",
                "requirements": [
                    "Текстовое поле Text с размерами 40x20 символов",
                    "Меню Menu с пунктами 'Файл' → 'Новый', 'Открыть', 'Сохранить', 'Выход'",
                    "При выборе 'Новый' - очищать текстовое поле",
                    "При выборе 'Выход' - закрывать приложение",
                    "Добавить статусную строку с количеством символов в тексте"
                ],
                "functions": "Text, Menu, filedialog"
            },
            {
                "num": 6,
                "title": "Калькулятор ИМТ",
                "goal": "Создание формы с валидацией данных.",
                "requirements": [
                    "Поле для ввода роста (в см) с валидацией - только числа",
                    "Поле для ввода веса (в кг) с валидацией - только числа",
                    "Кнопка 'Рассчитать'",
                    "Метка для вывода результата и категории (недостаток, норма, избыток)",
                    "Формула: ИМТ = вес / (рост/100)²",
                    "Категории: <18.5 - недостаток, 18.5-25 - норма, >25 - избыток"
                ],
                "functions": "validatecommand, register()"
            },
            {
                "num": 7,
                "title": "Игра 'Угадай число'",
                "goal": "Работа со случайными числами и логикой игры.",
                "requirements": [
                    "Программа загадывает случайное число от 1 до 100",
                    "Поле для ввода предположения",
                    "Кнопка 'Проверить'",
                    "Метка с подсказками ('больше', 'меньше', 'угадал!')",
                    "Счетчик попыток",
                    "Кнопка 'Новая игра' для перезапуска"
                ],
                "functions": "random.randint(), messagebox"
            },
            {
                "num": 8,
                "title": "Секундомер",
                "goal": "Работа со временем и обновлением интерфейса.",
                "requirements": [
                    "Большой дисплей с временем в формате MM:SS:MS",
                    "Кнопки 'Старт', 'Стоп', 'Сброс'",
                    "Список для сохранения промежуточных времен",
                    "Кнопка 'Круг' для фиксации текущего времени",
                    "Точность до десятых долей секунды"
                ],
                "functions": "after(), time"
            },
            {
                "num": 9,
                "title": "Переводчик цветов",
                "goal": "Работа с различными типами виджетов ввода.",
                "requirements": [
                    "Поле ввода для hex-кода цвета",
                    "Три поля для RGB значений",
                    "Холст для предпросмотра цвета",
                    "При изменении любого значения остальные должны автоматически обновляться",
                    "Валидация hex-кода (только 0-9, A-F, # в начале)"
                ],
                "functions": "FocusIn, FocusOut, StringVar.trace()"
            },
            {
                "num": 10,
                "title": "Система голосования",
                "goal": "Работа с радиокнопками и статистикой.",
                "requirements": [
                    "Три варианта ответа с Radiobutton",
                    "Кнопка 'Голосовать'",
                    "Прогресс-бары для каждого варианта",
                    "Метка с общим количеством голосов",
                    "Кнопка 'Сброс' для обнуления статистики",
                    "Проценты должны обновляться после каждого голоса"
                ],
                "functions": "Radiobutton, Progressbar, IntVar"
            }
        ]
        
        # Задания промежуточного уровня
        intermediate_tasks = [
            {
                "num": 11,
                "title": "Рисовалка с инструментами",
                "goal": "Создание интерактивного холста с меню инструментов.",
                "requirements": [
                    "Холст Canvas 500x400 пикселей",
                    "Панель инструментов: кисть, ластик, линия, прямоугольник, овал",
                    "Выбор цвета из палитры",
                    "Выбор толщины линии (1px, 3px, 5px, 10px)",
                    "Кнопка 'Очистить холст'",
                    "Сохранение рисунка в PNG файл"
                ],
                "functions": "Canvas.bind(), create_line(), create_rectangle(), filedialog.asksaveasfilename()"
            },
            {
                "num": 12,
                "title": "Менеджер паролей",
                "goal": "Создание CRUD приложения с шифрованием.",
                "requirements": [
                    "Таблица Treeview для отображения: сервис, логин, пароль",
                    "Кнопки: 'Добавить', 'Редактировать', 'Удалить', 'Копировать пароль'",
                    "Диалоговое окно для добавления/редактирования записей",
                    "Пароль должен отображаться как звездочки, с кнопкой 'Показать'",
                    "Простое шифрование паролей (base64)",
                    "Поиск по названию сервиса"
                ],
                "functions": "Treeview, Toplevel, base64, Entry(show='*')"
            },
            {
                "num": 13,
                "title": "Погодное приложение",
                "goal": "Интеграция с внешним API и работа с JSON.",
                "requirements": [
                    "Поле ввода города",
                    "Кнопка 'Получить погоду'",
                    "Отображение: температура, влажность, давление, описание",
                    "Иконка погоды (можно использовать emoji или простые картинки)",
                    "Сохранение последнего запрошенного города",
                    "Обработка ошибок (город не найден, нет интернета)"
                ],
                "functions": "requests.get(), json.loads(), Label.config()"
            },
            {
                "num": 14,
                "title": "Калькулятор с историей",
                "goal": "Создание полнофункционального калькулятора.",
                "requirements": [
                    "Поле ввода/вывода выражений",
                    "Кнопки для цифр 0-9 и операций +, -, *, /, =",
                    "Кнопки: очистка (C), backspace (⌫)",
                    "Память: M+, M-, MR, MC",
                    "История вычислений в отдельном виджете Listbox",
                    "Возможность использовать предыдущий результат"
                ],
                "functions": "eval() (с осторожностью), Listbox, lambda функции"
            },
            {
                "num": 15,
                "title": "Аудио-плеер",
                "goal": "Работа с мультимедиа и прогресс-баром.",
                "requirements": [
                    "Кнопки: 'Открыть', 'Воспроизвести', 'Пауза', 'Стоп'",
                    "Отображение названия текущего файла",
                    "Прогресс-бар воспроизведения",
                    "Регулятор громкости",
                    "Список плейлиста",
                    "Поддержка форматов: MP3, WAV"
                ],
                "functions": "pygame.mixer, Progressbar, Scale"
            },
            {
                "num": 16,
                "title": "Генератор QR-кодов",
                "goal": "Интеграция со сторонними библиотеками.",
                "requirements": [
                    "Поле ввода текста/ссылки для кодирования",
                    "Выбор размера QR-кода (S, M, L)",
                    "Превью QR-кода на холсте",
                    "Кнопки: 'Сгенерировать', 'Сохранить'",
                    "Отображение информации о размере данных"
                ],
                "functions": "qrcode, PIL.ImageTk, Canvas.create_image()"
            },
            {
                "num": 17,
                "title": "Система заметок с тегами",
                "goal": "Создание сложной системы управления данными.",
                "requirements": [
                    "Список заметок в Treeview с колонками: название, дата, теги",
                    "Редактор заметки с полем заголовка и текстовым полем",
                    "Система тегов с возможностью добавления/удаления",
                    "Поиск по заголовку и тегам",
                    "Сортировка по дате/названию",
                    "Автосохранение каждые 30 секунд"
                ],
                "functions": "sqlite3, Treeview.sort(), after()"
            },
            {
                "num": 18,
                "title": "Визуализатор сортировок",
                "goal": "Анимация алгоритмов на Canvas.",
                "requirements": [
                    "Генерация случайного массива чисел",
                    "Выбор алгоритма: пузырьковая, быстрая, выбором",
                    "Визуализация на Canvas столбцами разной высоты",
                    "Кнопки: 'Сгенерировать', 'Сортировать', 'Пауза'",
                    "Отображение количества сравнений и времени",
                    "Регулятор скорости анимации"
                ],
                "functions": "Canvas.create_rectangle(), timeit, yield для анимации"
            },
            {
                "num": 19,
                "title": "Файловый менеджер",
                "goal": "Работа с файловой системой.",
                "requirements": [
                    "Древовидное отображение папок Treeview",
                    "Список файлов текущей папки Listbox",
                    "Информация о выбранном файле: размер, дата изменения",
                    "Кнопки: 'Вверх', 'Удалить', 'Переименовать'",
                    "Контекстное меню для файлов",
                    "Поиск по имени файла"
                ],
                "functions": "os.listdir(), os.path.getsize(), os.remove()"
            },
            {
                "num": 20,
                "title": "Чат-приложение",
                "goal": "Создание клиент-серверного приложения.",
                "requirements": [
                    "Область сообщений с прокруткой",
                    "Поле ввода сообщения",
                    "Кнопка 'Отправить'",
                    "Список онлайн-пользователей",
                    "Поле для ввода IP и порта сервера",
                    "Timestamp для каждого сообщения"
                ],
                "functions": "socket, Thread, ScrolledText"
            }
        ]
        
        # Задания продвинутого уровня
        advanced_tasks = [
            {
                "num": 21,
                "title": "Арканоид",
                "goal": "Создание полноценной игры с физикой.",
                "requirements": [
                    "Игровое поле на Canvas",
                    "Передвижение платформы клавишами ← →",
                    "Шарик с отскоком от стен, платформы и блоков",
                    "Система уровней с разным расположением блоков",
                    "Счетчик очков и жизней",
                    "Меню паузы и начала игры"
                ],
                "functions": "Canvas.move(), bind(), after() для игрового цикла"
            },
            {
                "num": 22,
                "title": "Электронная таблица",
                "goal": "Создание подобия Excel с формулами.",
                "requirements": [
                    "Сетка ячеек 26x100 (A-Z колонки, 100 строк)",
                    "Редактирование ячеек с формулами (поддержка =SUM(A1:A5))",
                    "Панель формул как в Excel",
                    "Вычисление простых формул: SUM, AVG, MAX, MIN",
                    "Сохранение/загрузка в CSV",
                    "Выделение диапазонов"
                ],
                "functions": "Entry, eval() с безопасным контекстом, csv"
            },
            {
                "num": 23,
                "title": "Векторный редактор",
                "goal": "Создание инструмента для векторной графики.",
                "requirements": [
                    "Холст с поддержкой примитивов: линии, прямоугольники, эллипсы, кривые",
                    "Редактирование точек кривых Безье",
                    "Панель свойств: заливка, обводка, толщина",
                    "Слои с возможностью переупорядочивания",
                    "Инструменты: выделение, трансформация",
                    "Экспорт в SVG"
                ],
                "functions": "Canvas, xml.etree.ElementTree для SVG"
            },
            {
                "num": 24,
                "title": "Система контроля версий",
                "goal": "Создание простого GUI для Git-like операций.",
                "requirements": [
                    "Отображение измененных файлов в рабочей директории",
                    "Поле для комментария к коммиту",
                    "Кнопки: 'Добавить', 'Зафиксировать', 'История'",
                    "График коммитов (дерево)",
                    "Дифф между версиями",
                    "Восстановление файлов из истории"
                ],
                "functions": "subprocess, difflib, graphviz для визуализации"
            },
            {
                "num": 25,
                "title": "Монитор системы",
                "goal": "Создание системного монитора в реальном времени.",
                "requirements": [
                    "Графики загрузки CPU, памяти, диска",
                    "Список процессов с возможностью завершения",
                    "Сетевая статистика",
                    "Температуры компонентов (если доступно)",
                    "Настраиваемые интервалы обновления",
                    "Предупреждения при высокой нагрузке"
                ],
                "functions": "psutil, matplotlib, threading"
            },
            {
                "num": 26,
                "title": "Распознавание образов",
                "goal": "Интеграция с машинным обучением.",
                "requirements": [
                    "Загрузка изображения",
                    "Выбор модели распознавания: лица, объекты, текст",
                    "Отображение результатов с bounding boxes",
                    "Статистика точности распознавания",
                    "Сохранение размеченных изображений"
                ],
                "functions": "opencv-python, tensorflow/pytorch, Canvas"
            },
            {
                "num": 27,
                "title": "3D вьюер",
                "goal": "Отображение и манипуляция 3D объектами.",
                "requirements": [
                    "Загрузка 3D моделей в формате OBJ",
                    "Вращение, масштабирование, перемещение камеры",
                    "Простой рейкастинг для отображения",
                    "Настройки освещения",
                    "Экспорт скриншотов"
                ],
                "functions": "math для матриц, Canvas для отрисовки"
            },
            {
                "num": 28,
                "title": "Автоматизация тестирования GUI",
                "goal": "Создание системы для тестирования других приложений.",
                "requirements": [
                    "Запись действий мыши и клавиатуры",
                    "Воспроизведение записанных сценариев",
                    "Система проверок (assertions)",
                    "Генерация отчетов о тестировании",
                    "Поддержка параметризованных тестов"
                ],
                "functions": "pyautogui, unittest, logging"
            },
            {
                "num": 29,
                "title": "Удаленный рабочий стол",
                "goal": "Создание VNC-like клиента.",
                "requirements": [
                    "Клиентская часть: просмотр и управление удаленным рабочим столом",
                    "Серверная часть: трансляция экрана и ввода",
                    "Настройки качества и сжатия",
                    "Файловый менеджер между клиентом и сервером",
                    "Безопасное соединение"
                ],
                "functions": "socket, PIL.ImageGrab, zlib для сжатия"
            },
            {
                "num": 30,
                "title": "Интегрированная среда разработки",
                "goal": "Создание простого Python IDE.",
                "requirements": [
                    "Редактор кода с подсветкой синтаксиса",
                    "Файловый браузер",
                    "Терминал для выполнения команд",
                    "Отладчик с точками останова",
                    "Система плагинов",
                    "Интеграция с Git"
                ],
                "functions": "tkinter.scrolledtext, subprocess, syntax highlighting"
            }
        ]
        
        # Создание карточек заданий
        beginner_cards = [self.create_task_card(**task, level="beginner") for task in beginner_tasks]
        intermediate_cards = [self.create_task_card(**task, level="intermediate") for task in intermediate_tasks]
        advanced_cards = [self.create_task_card(**task, level="advanced") for task in advanced_tasks]
        
        content = ft.Container(
            content=ft.Column([
                self.create_page_header("Тренажер", "Практические задания для изучения Tkinter"),
                ft.Container(height=20),
                
                # Уровень 1: Начальный
                ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Icon(ft.Icons.STAR_OUTLINE, size=24, color="#4CAF50"),
                            ft.Text("УРОВЕНЬ 1: НАЧАЛЬНЫЙ", size=22, weight=ft.FontWeight.BOLD, color="#4CAF50"),
                        ]),
                        ft.Container(height=15),
                        ft.Text(
                            "10 заданий для освоения базовых концепций Tkinter: виджеты, события, простые приложения.",
                            size=14,
                            color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                    ] + beginner_cards),
                    padding=20,
                    bgcolor=colors["bg_container"],
                    border_radius=15,
                    margin=ft.margin.only(bottom=20),
                ),
                
                # Уровень 2: Промежуточный
                ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Icon(ft.Icons.STAR_HALF, size=24, color="#FF9800"),
                            ft.Text("УРОВЕНЬ 2: ПРОМЕЖУТОЧНЫЙ", size=22, weight=ft.FontWeight.BOLD, color="#FF9800"),
                        ]),
                        ft.Container(height=15),
                        ft.Text(
                            "10 заданий для создания более сложных приложений: работа с файлами, API, мультимедиа.",
                            size=14,
                            color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                    ] + intermediate_cards),
                    padding=20,
                    bgcolor=colors["bg_container"],
                    border_radius=15,
                    margin=ft.margin.only(bottom=20),
                ),
                
                # Уровень 3: Продвинутый
                ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Icon(ft.Icons.STAR, size=24, color="#F44336"),
                            ft.Text("УРОВЕНЬ 3: ПРОДВИНУТЫЙ", size=22, weight=ft.FontWeight.BOLD, color="#F44336"),
                        ]),
                        ft.Container(height=15),
                        ft.Text(
                            "10 заданий для создания профессиональных приложений: игры, IDE, системные утилиты.",
                            size=14,
                            color=colors["text_secondary"]
                        ),
                        ft.Container(height=15),
                    ] + advanced_cards),
                    padding=20,
                    bgcolor=colors["bg_container"],
                    border_radius=15,
                ),
            ], scroll=ft.ScrollMode.ADAPTIVE, spacing=0),
            expand=True
        )
        self.update_content(content, "trainer")

    def open_file(self, file_path):
        """Открытие файла в системном приложении"""
        try:
            if os.path.exists(file_path):
                if sys.platform == "win32":
                    os.startfile(file_path)
                elif sys.platform == "darwin":  # macOS
                    os.system(f'open "{file_path}"')
                else:  # linux
                    os.system(f'xdg-open "{file_path}"')
            else:
                print(f"Файл не найден: {file_path}")
        except Exception as e:
            print(f"Ошибка при открытии файла: {e}")

    def preview_task_code(self, task_num):
        """Открытие готового кода задания"""
        file_path = f"Ready_Tasks\Task_{task_num}.txt"
        # Проверяем существование файла
        if os.path.exists(file_path):
            self.open_file(file_path)
        else:
            # Показываем сообщение об ошибке
            colors = self.get_theme_colors()
            error_dialog = ft.AlertDialog(
                title=ft.Text("Файл не найден", color=colors["text_primary"]),
                content=ft.Text(
                    f"Файл Task_{task_num}.txt не найден в папке Ready_Tasks.",
                    color=colors["text_secondary"]
                ),
                actions=[
                    ft.TextButton("Закрыть", on_click=lambda e: self.close_dialog(error_dialog)),
                ],
            )
            self.page.dialog = error_dialog
            error_dialog.open = True
            self.page.update()

    def preview_text_file(self, file_path):
        """Предпросмотр текстового файла"""
        colors = self.get_theme_colors()
        try:
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                preview_dialog = ft.AlertDialog(
                    title=ft.Text(f"Предпросмотр: {os.path.basename(file_path)}", color=colors["text_primary"]),
                    content=ft.Container(
                        content=ft.Column([
                            ft.Container(
                                content=ft.Text(
                                    content,
                                    size=12,
                                    color=colors["text_secondary"],
                                    font_family="Courier New",
                                    selectable=True
                                ),
                                padding=15,
                                bgcolor=colors["bg_container"],
                                border_radius=10,
                                height=400,
                                width=600,
                            ),
                        ], scroll=ft.ScrollMode.ADAPTIVE),
                    ),
                    actions=[
                        ft.TextButton("Закрыть", on_click=lambda e: self.close_dialog(preview_dialog)),
                        ft.TextButton("Открыть файл", on_click=lambda e: self.open_file(file_path)),
                    ],
                    actions_alignment=ft.MainAxisAlignment.END,
                )
                
                self.page.dialog = preview_dialog
                preview_dialog.open = True
                self.page.update()
            else:
                # Показываем сообщение об ошибке
                error_dialog = ft.AlertDialog(
                    title=ft.Text("Файл не найден", color=colors["text_primary"]),
                    content=ft.Text(
                        f"Файл {os.path.basename(file_path)} не найден в папке Ready_Tasks.",
                        color=colors["text_secondary"]
                    ),
                    actions=[
                        ft.TextButton("Закрыть", on_click=lambda e: self.close_dialog(error_dialog)),
                    ],
                )
                self.page.dialog = error_dialog
                error_dialog.open = True
                self.page.update()
        except Exception as e:
            print(f"Ошибка при предпросмотре файла: {e}")

    def close_dialog(self, dialog):
        """Закрытие диалогового окна"""
        dialog.open = False
        self.page.update()

    def show_about_page(self):
        """Страница 'О программе'"""
        colors = self.get_theme_colors()
        # Основной контейнер с информацией о программе (слева)
        main_info_container = ft.Container(
            content=ft.Column([
                ft.Text("Tkinter Учебное Пособие", size=22, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=10),
                
                ft.Text(
                    "Это приложение представляет собой комплексное учебное пособие по библиотеке Tkinter для создания графических интерфейсов на Python.",
                    size=16, color=colors["text_secondary"]
                ),
                ft.Container(height=20),
                
                ft.Text("Основные возможности:", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=10),
                
                ft.Column([
                    ft.Row([
                        ft.Icon(ft.Icons.CHECK_CIRCLE, size=20, color=ft.Colors.GREEN),
                        ft.Text("Подробная библиотека с теорией", size=14, color=colors["text_secondary"], expand=True),
                    ]),
                    ft.Container(height=5),
                    ft.Row([
                        ft.Icon(ft.Icons.CHECK_CIRCLE, size=20, color=ft.Colors.GREEN),
                        ft.Text("Видео уроки для наглядного обучения", size=14, color=colors["text_secondary"], expand=True),
                    ]),
                    ft.Container(height=5),
                    ft.Row([
                        ft.Icon(ft.Icons.CHECK_CIRCLE, size=20, color=ft.Colors.GREEN),
                        ft.Text("Полезные функции с примерами кода", size=14, color=colors["text_secondary"], expand=True),
                    ]),
                    ft.Container(height=5),
                    ft.Row([
                        ft.Icon(ft.Icons.CHECK_CIRCLE, size=20, color=ft.Colors.GREEN),
                        ft.Text("Интерактивный тренажер для практики", size=14, color=colors["text_secondary"], expand=True),
                    ]),
                ]),
                ft.Container(height=30),
                
                ft.Text("Преимущества приложения:", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=10),
                
                ft.Column([
                    
                    ft.Row([
                        ft.Icon(ft.Icons.WIFI_OFF, size=20, color=ft.Colors.GREEN_200),
                        ft.Text("Работа без интернета", size=14, color=colors["text_secondary"], expand=True),
                    ]),
                    ft.Text("Все материалы доступны офлайн после установки приложения", 
                        size=12, color=colors["text_secondary"]),
                    ft.Container(height=8),
                    
                    ft.Row([
                        ft.Icon(ft.Icons.CODE, size=20, color=ft.Colors.ORANGE_200),
                        ft.Text("Открытый исходный код", size=14, color=colors["text_secondary"], expand=True),
                    ]),
                    ft.Text("Возможность модификации и улучшения приложения сообществом", 
                        size=12, color=colors["text_secondary"]),
                    ft.Container(height=8),
                    
                    ft.Row([
                        ft.Icon(ft.Icons.SPEED, size=20, color=ft.Colors.PURPLE_200),
                        ft.Text("Высокая производительность", size=14, color=colors["text_secondary"], expand=True),
                    ]),
                    ft.Text("Оптимизированное использование ресурсов и быстрое время отклика", 
                        size=12, color=colors["text_secondary"]),
                    ft.Container(height=8),
                    
                    ft.Row([
                        ft.Icon(ft.Icons.SECURITY, size=20, color=ft.Colors.TEAL_200),
                        ft.Text("Безопасность", size=14, color=colors["text_secondary"], expand=True),
                    ]),
                    ft.Text("Локальное хранение данных, отсутствие сбора личной информации", 
                        size=12, color=colors["text_secondary"]),
                    ft.Container(height=8),
                    
                    ft.Row([
                        ft.Icon(ft.Icons.UPDATE, size=20, color=ft.Colors.YELLOW_200),
                        ft.Text("Регулярные обновления", size=14, color=colors["text_secondary"], expand=True),
                    ]),
                    ft.Text("Постоянное улучшение функционала и добавление новых материалов", 
                        size=12, color=colors["text_secondary"]),
                ]),
                ft.Container(height=30),
                
                ft.Text("Техническая информация:", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                ft.Container(height=10),
                
                ft.Column([
                    ft.Row([
                        ft.Text("Версия:", size=14, color=colors["text_secondary"], width=120),
                        ft.Text("1.0.0", size=14, color=colors["text_primary"]),
                    ]),
                    ft.Row([
                        ft.Text("Платформа:", size=14, color=colors["text_secondary"], width=120),
                        ft.Text("Windows 10/11", size=14, color=colors["text_primary"]),
                    ]),
                    ft.Row([
                        ft.Text("Язык программирования:", size=14, color=colors["text_secondary"], width=120),
                        ft.Text("Python 3.8+", size=14, color=colors["text_primary"]),
                    ]),
                    ft.Row([
                        ft.Text("GUI фреймворк:", size=14, color=colors["text_secondary"], width=120),
                        ft.Text("Flet", size=14, color=colors["text_primary"]),
                    ]),
                    ft.Row([
                        ft.Text("Лицензия:", size=14, color=colors["text_secondary"], width=120),
                        ft.Text("MIT Open Source", size=14, color=colors["text_primary"]),
                    ]),
                ]),
                ft.Container(height=20),
                
                ft.Text(
                    "Приложение разработано для облегчения изучения библиотеки Tkinter и предоставляет "
                    "структурированные материалы для начинающих и опытных разработчиков.",
                    size=14, color=colors["text_secondary"], italic=True
                ),
            ], scroll=ft.ScrollMode.ADAPTIVE),
            padding=30,
            bgcolor=colors["bg_container"],
            border_radius=15,
            expand=True,
        )

        # Правый контейнер с документацией и автором
        right_container = ft.Container(
            content=ft.Column([
                # Раздел "Автор"
                ft.Container(
                    content=ft.Column([
                        ft.Text("Автор", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        ft.Container(
                            content=ft.Image(
                                src="About_Page/about_card.png",
                                width=700,
                                fit=ft.ImageFit.COVER,
                            ),
                            bgcolor=colors["bg_container"],
                            border_radius=5,
                        ),
                    ]),
                    padding=20,
                    bgcolor=colors["bg_container"],
                    border_radius=5,
                ),
                ft.Container(height=20),
                
                # Раздел "Документация"
                ft.Container(
                    content=ft.Column([
                        ft.Text("Документация", size=18, weight=ft.FontWeight.BOLD, color=colors["text_primary"]),
                        ft.Container(height=10),
                        
                        # Список файлов для скачивания
                        ft.Container(
                            content=ft.Column([
                                # Файл 1 - MANUAL.pdf
                                ft.Container(
                                    content=ft.Row([
                                        ft.Icon(ft.Icons.DESCRIPTION, size=24, color=ft.Colors.BLUE_200),
                                        ft.Column([
                                            ft.Text("Руководство пользователя", size=14, color=colors["text_primary"], weight=ft.FontWeight.BOLD),
                                            ft.Text("MANUAL.pdf", size=12, color=colors["text_secondary"]),
                                        ], expand=True),
                                        ft.Row([
                                            ft.IconButton(
                                                icon=ft.Icons.VISIBILITY,
                                                icon_color=ft.Colors.BLUE_200,
                                                tooltip="Предпросмотр",
                                                on_click=lambda e: self.open_file("About_Page\MANUAL.pdf")
                                            ),
                                        ]),
                                    ]),
                                    padding=10,
                                    bgcolor=colors["bg_container"],
                                    border_radius=8,
                                ),
                                ft.Container(height=5),
                                
                                # Файл 2 - README.txt
                                ft.Container(
                                    content=ft.Row([
                                        ft.Icon(ft.Icons.BOOK, size=24, color=ft.Colors.ORANGE_200),
                                        ft.Column([
                                            ft.Text("README", size=14, color=colors["text_primary"], weight=ft.FontWeight.BOLD),
                                            ft.Text("README.txt", size=12, color=colors["text_secondary"]),
                                        ], expand=True),
                                        ft.Row([
                                            ft.IconButton(
                                                icon=ft.Icons.VISIBILITY,
                                                icon_color=ft.Colors.BLUE_200,
                                                tooltip="Предпросмотр",
                                                on_click=lambda e: self.open_file("About_Page\README.txt")
                                            ),
                                        ]),
                                    ]),
                                    padding=10,
                                    bgcolor=colors["bg_container"],
                                    border_radius=8,
                                ),
                                ft.Container(height=1),
                                
                                # Файл 3 - Лицензия MIT
                                ft.Container(
                                    content=ft.Row([
                                        ft.Icon(ft.Icons.SECURITY, size=24, color=ft.Colors.PURPLE_200),
                                        ft.Column([
                                            ft.Text("Лицензия MIT", size=14, color=colors["text_primary"], weight=ft.FontWeight.BOLD),
                                            ft.Text("LICENSE.txt", size=12, color=colors["text_secondary"]),
                                        ], expand=True),
                                        ft.Row([
                                            ft.IconButton(
                                                icon=ft.Icons.VISIBILITY,
                                                icon_color=ft.Colors.BLUE_200,
                                                tooltip="Предпросмотр",
                                                on_click=lambda e: self.open_file("About_Page\LICENSE.txt")
                                            ),
                                        ]),
                                    ]),
                                    padding=10,
                                    bgcolor=colors["bg_container"],
                                    border_radius=8,
                                ),
                            ]),
                        ),
                    ], scroll=ft.ScrollMode.ADAPTIVE),
                    padding=20,
                    bgcolor=colors["bg_container"],
                    border_radius=15,
                    expand=True,
                ),
            ]),
            width=350,
            expand=True,
        )

        content = ft.Container(
            content=ft.Column([
                self.create_page_header("О программе", "Информация о приложении"),
                ft.Container(height=20),
                
                # Основной контент с двумя колонками
                ft.Container(
                    content=ft.Row([
                        # Левый контейнер - основная информация
                        main_info_container,
                        
                        # Правый контейнер - автор и документация
                        right_container,
                    ], spacing=20, expand=True),
                    expand=True,
                )
            ]),
            expand=True
        )
        self.update_content(content, "about")

def main(page: ft.Page):
    """Главная функция приложения"""
    app = TkinterGuideApp(page)

if __name__ == "__main__":
    ft.app(target=main)