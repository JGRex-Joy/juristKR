from rag_service.llm.layers.base import BaseLLMLayer

class LLMQuery(BaseLLMLayer):
    def __init__(self, llm):
        super().__init__(llm)
        
    def answer(self, user_query: str, contexts: list[str]) -> str:
        context_text = "\n\n---\n\n".join(contexts)
        
        prompt = f"""
            Ты — юридический ассистент. Используй только следующие контексты:

            {context_text}

            Вопрос пользователя:
            {user_query}

            Ответь строго по контекстам. Не придумывай лишнего.
            Дай чёткий юридический вывод и укажи статьи, если они есть в контексте.
        """
        
        result = self.llm.generate(prompt)
        
        print(f"[INFO] Context: {result}")
        
        return result