from __future__ import annotations

import re



class ReportValidator:


    def validate(
        self,
        summary: str,
    ) -> str:


        if not summary:

            return summary



        result = summary



        replacements = {

            r"high risk of clipping":
            "possible clipping risk",

            r"critical clipping risk":
            "possible clipping risk",

            r"immediate action is required":
            "review is recommended",

            r"professional standard":
            "technical measurement",

        }



        for pattern, replacement in replacements.items():

            result = re.sub(
                pattern,
                replacement,
                result,
                flags=re.IGNORECASE,
            )



        remove_patterns = [

            r"without being overly wide or narrow",

            r"sounds good across all playback systems",

            r"often features dense transients",

            r"listener fatigue",

            r"across all playback systems",

        ]



        for pattern in remove_patterns:

            result = re.sub(
                pattern,
                "",
                result,
                flags=re.IGNORECASE,
            )



        sentences = re.split(
            r"(?<=[.!?])\s+",
            result,
        )


        clean_sentences = []


        for sentence in sentences:

            sentence = sentence.strip()


            if not sentence:

                continue


            if sentence.lower() in (

                "the mix .",

                "the mix.",

                ".",

            ):

                continue


            if len(sentence) < 5:

                continue


            # Capitalize every sentence

            sentence = (
                sentence[0].upper()
                +
                sentence[1:]
            )


            clean_sentences.append(
                sentence
            )



        result = " ".join(
            clean_sentences
        )



        result = re.sub(
            r"\s+",
            " ",
            result,
        )


        result = re.sub(
            r"\s+([.,!?])",
            r"\1",
            result,
        )


        return result.strip()