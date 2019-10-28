from redbot.brains import language


class RedBot:

    @staticmethod
    def input(sentence: str) -> str:
        """
        Answers with proper answer
        :param sentence:
        :return:
        """

        processor = language.LanguageProcessor(sentence, None)
        processor.process()

        return processor.result
