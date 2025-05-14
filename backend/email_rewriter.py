import openai
from typing import Optional, Dict, Any
from dataclasses import dataclass

@dataclass
class EmailConfig:
    tone: str
    model: str = "gpt-3.5-turbo"
    temperature: float = 0.7
    max_tokens: int = 1000

class EmailRewriter:
    def __init__(self, api_key: str):
        """Initialize the EmailRewriter with OpenAI API key."""
        self.api_key = api_key
        openai.api_key = api_key

    def _construct_prompt(self, email: str, tone: str) -> str:
        """Construct the prompt for the OpenAI API."""
        return f"""Rewrite the following email in a {tone.lower()} tone. 
        Improve clarity, professionalism, and politeness while maintaining the original message.
        Make sure the rewritten version is well-structured and effectively communicates the message.
        
        Original email: {email}"""

    def rewrite_email(self, email: str, config: EmailConfig) -> Dict[str, Any]:
        """
        Rewrite the email using OpenAI's API with the specified configuration.
        
        Args:
            email: The original email text
            config: EmailConfig object containing tone, model, and other parameters
            
        Returns:
            Dict containing status, rewritten email or error message
        """
        try:
            prompt = self._construct_prompt(email, config.tone)
            
            response = openai.ChatCompletion.create(
                model=config.model,
                messages=[
                    {"role": "system", "content": "You are a professional email writing assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=config.max_tokens,
                temperature=config.temperature,
            )
            
            rewritten_email = response.choices[0].message.content.strip()
            
            return {
                "status": "success",
                "rewritten_email": rewritten_email
            }
            
        except Exception as e:
            return {
                "status": "error",
                "error": str(e)
            }

    def validate_api_key(self) -> bool:
        """Validate the OpenAI API key by making a test request."""
        try:
            openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": "test"}],
                max_tokens=5
            )
            return True
        except:
            return False
