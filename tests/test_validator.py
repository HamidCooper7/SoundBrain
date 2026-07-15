from brain.report import ReportValidator



def main():


    test_summary = """

The stereo image is acceptable.

However, there is a high risk of clipping.

This is a professional standard result.

The mix often features dense transients.

Immediate action is required.

"""



    validator = ReportValidator()



    result = validator.validate(
        test_summary
    )



    print()

    print(
        "========== VALIDATED SUMMARY =========="
    )


    print(
        result
    )



if __name__ == "__main__":

    main()