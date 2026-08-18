import json
import os
import re

from dotenv import load_dotenv
from openai import OpenAI


# .env dosyasını yükle
load_dotenv()


# OpenRouter üzerinden OpenAI SDK kullanıyoruz
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    timeout=30.0,
    max_retries=1,
)


def _extract_json(content: str) -> dict:
    """
    AI cevabından JSON objesini çıkarır.

    Desteklenen cevap tipleri:

    1. Direkt JSON
    2. ```json ... ``` code block
    3. JSON etrafında açıklama bulunan cevap
    """

    content = content.strip()

    # =========================
    # 1. Direkt JSON
    # =========================

    try:
        result = json.loads(content)

        if isinstance(result, dict):
            return result

    except json.JSONDecodeError:
        pass

    # =========================
    # 2. Markdown JSON
    # =========================

    code_block_match = re.search(
        r"```(?:json)?\s*(\{.*?\})\s*```",
        content,
        re.DOTALL,
    )

    if code_block_match:
        json_content = code_block_match.group(1)

        try:
            result = json.loads(json_content)

            if isinstance(result, dict):
                return result

        except json.JSONDecodeError:
            pass

    # =========================
    # 3. Metin içerisindeki JSON
    # =========================

    first_brace = content.find("{")
    last_brace = content.rfind("}")

    if first_brace != -1 and last_brace != -1:
        json_content = content[first_brace:last_brace + 1]

        try:
            result = json.loads(json_content)

            if isinstance(result, dict):
                return result

        except json.JSONDecodeError:
            pass

    # =========================
    # JSON bulunamadı
    # =========================

    raise RuntimeError(
        f"AI geçerli JSON döndürmedi: {content}"
    )


def generate_test(prompt: str) -> dict:
    """
    Kullanıcının doğal dilde verdiği açıklamadan
    otomatik test case üretir.
    """

    system_prompt = """
Sen TestPilot AI isimli bir yazılım test otomasyon platformunun
AI test üretim motorusun.

Görevin, kullanıcının verdiği yazılım gereksinimine göre
otomatik bir test case ve pytest kodu oluşturmaktır.

ÇOK ÖNEMLİ:

Cevabını SADECE geçerli bir JSON objesi olarak döndür.

Markdown kullanma.
```json kullanma.
Açıklama yazma.
JSON'un öncesinde veya sonrasında hiçbir metin yazma.

JSON formatı:

{
  "title": "Test başlığı",
  "description": "Test açıklaması",
  "test_type": "API",
  "framework": "pytest",
  "generated_code": "Python pytest kodu",
  "status": "generated"
}

Kurallar:

- title kısa ve açıklayıcı olmalı.
- description kullanıcının istediği senaryoyu açıklamalı.
- test_type API, UI veya UNIT olabilir.
- framework uygun test framework'ü olmalı.
- generated_code pytest ile yazılmış Python test kodu olmalı.
- status her zaman "generated" olmalı.
- Gerçek endpoint bilgisi verilmemişse örnek URL kullanılabilir.
- generated_code JSON string içerisinde düzgün escape edilmelidir.
- JSON dışında hiçbir şey döndürme.
"""


    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b:free",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )

    except Exception as e:
        raise RuntimeError(
            f"OpenRouter API hatası: {str(e)}"
        )

    if not response.choices:
        raise RuntimeError(
            "AI herhangi bir cevap döndürmedi."
        )

    content = response.choices[0].message.content

    if not content:
        raise RuntimeError(
            "AI boş cevap döndürdü."
        )

    return _extract_json(content)