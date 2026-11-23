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
- [ ] Чек-лист и тест-кейсы
- [ ] Баг-репорты по найденным проблемам
- [ ] Postman-коллекция
- [ ] UI-тесты на Playwright
- [ ] CI на GitHub Actions
