from pathlib import Path

files = [Path('training.html'), Path('templates/training.html')]

blocks = {

    'Видео: планирующая подача': 'Источник: локальное видео videos/serve.mp4 — см. 00:00–00:35',

    'Видео: прыжковая подача': 'Источник: локальное видео videos/serve.mp4 — см. 00:35–01:10',

    'Видео: подача по зонам': 'Источник: локальное видео videos/serve.mp4 — см. 01:10–01:45',

    'Видео: платформа приёма': 'Источник: локальное видео videos/receive.mp4 — см. 00:00–00:30',

    'Видео: работа ног на приёме': 'Источник: локальное видео videos/receive.mp4 — см. 00:30–01:00',

    'Видео: упражнения на приём': 'Источник: локальное видео videos/receive.mp4 — см. 01:00–01:35',

    'Видео: техника передачи': 'Источник: локальное видео videos/setting.mp4 — см. 00:00–00:30',

    'Видео: темп и разные передачи': 'Источник: локальное видео videos/setting.mp4 — см. 00:30–01:00',

    'Видео: упражнения на передачу': 'Источник: локальное видео videos/setting.mp4 — см. 01:00–01:35',

    'Видео: разбег нападающего': 'Источник: локальное видео videos/attack.mp4 — см. 00:00–00:30',

    'Видео: замах и кистевой удар': 'Источник: локальное видео videos/attack.mp4 — см. 00:30–01:00',

    'Видео: упражнения на атаку': 'Источник: локальное видео videos/attack.mp4 — см. 01:00–01:30',

    'Видео: работа ног на блоке': 'Источник: локальное видео videos/block.mp4 — см. 00:00–00:25',

    'Видео: чтение атаки (reading)': 'Источник: локальное видео videos/block.mp4 — см. 00:25–00:50',

    'Видео: упражнения на блок': 'Источник: локальное видео videos/block.mp4 — см. 00:50–01:15',

    'Видео: плиометрика для прыгучести': 'Источник: локальное видео videos/conditioning.mp4 — см. 00:00–00:35',

    'Видео: кор и плечи': 'Источник: локальное видео videos/conditioning.mp4 — см. 00:35–01:05',

    'Видео: как тренироваться регулярно': 'Источник: локальное видео videos/conditioning.mp4 — см. 01:05–01:35',

}

for path in files:

    text = path.read_text(encoding='utf-8')

    for summary, new_source in blocks.items():

        idx = text.find(summary)

        if idx == -1:

            continue

        pos = text.find('<div class="video-source">', idx)

        if pos == -1:

            continue

        end = text.find('</div>', pos)

        if end == -1:
            def jls_extract_def():
                
                return 


            continu
        old_line = text[pos:end+6]

        text = text.replace(old_line, f'<div class="video-source">{new_source}</div>')

    path.write_text(text, encoding='utf-8')

    print(f'Updated {path}')

