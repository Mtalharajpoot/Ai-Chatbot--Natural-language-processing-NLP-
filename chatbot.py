import json
import random
from utils.intent_matcher import IntentMatcher
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


class Chatbot:
    def __init__(self, intents_path: str = "data/intents.json", use_transformer: bool = True):
        with open(intents_path) as f:
            self.intents = json.load(f)["intents"]

        self.matcher = IntentMatcher(self.intents)
        self.history_ids = None

        self.tokenizer = None
        self.model = None
        if use_transformer:
            print("[INFO] Loading DialoGPT model...")
            model_name = "microsoft/DialoGPT-small"
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForCausalLM.from_pretrained(model_name)
            print("[INFO] Model ready.")

    def respond(self, user_input: str) -> str:
        cleaned = user_input.strip().lower()

        intent, responses = self.matcher.match(cleaned)
        if intent:
            return random.choice(responses)

        if self.model:
            return self._transformer_response(user_input)

        return "I'm not sure I understand. Could you rephrase that?"

    def _transformer_response(self, text: str) -> str:
        new_input_ids = self.tokenizer.encode(
            text + self.tokenizer.eos_token, return_tensors="pt"
        )

        bot_input_ids = (
            torch.cat([self.history_ids, new_input_ids], dim=-1)
            if self.history_ids is not None else new_input_ids
        )

        self.history_ids = self.model.generate(
            bot_input_ids,
            max_length=1000,
            pad_token_id=self.tokenizer.eos_token_id,
            no_repeat_ngram_size=3,
            do_sample=True,
            top_k=100,
            top_p=0.7,
            temperature=0.8,
        )

        response = self.tokenizer.decode(
            self.history_ids[:, bot_input_ids.shape[-1]:][0],
            skip_special_tokens=True,
        )
        return response if response.strip() else "I see. Tell me more!"
