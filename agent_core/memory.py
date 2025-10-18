class Memory:
    def __init__(self):
        self.history = []

    def add_entry(self, round_num, executor_output, evaluator_feedback, improver_output):
        self.history.append({
            "round": round_num,
            "executor_output": executor_output,
            "evaluator_feedback": evaluator_feedback,
            "improver_output": improver_output
        })

    def get_history(self):
        return self.history
