# restful-booker-qa

Учебный QA-проект: тестирование публичного API [Restful-Booker](https://restful-booker.herokuapp.com/apidoc/index.html).

## Что внутри
- `tests/` — автотесты на Python (pytest + requests)
- `docs/` — чек-лист, тест-кейсы, баг-репорты
- `postman/` — Postman-коллекция с проверками

## Запуск
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest
pytest -m smoke      # только быстрые проверки
pytest -m negative   # только негативные
```

## План
- [x] API-автотесты: CRUD, авторизация, негативные сценарии
- [x] Postman-коллекция с проверками
- [x] Первый баг-репорт
- [ ] Чек-лист и тест-кейсы
- [ ] UI-тесты на Playwright
- [ ] CI на GitHub Actions

## Найденные баги
- [BUG-001: POST /auth с неверным паролем возвращает 200 OK](docs/bug-001-auth-returns-200.md)
