class AssertArguments:
    def __init__(self) -> None:
        pass

    def AssertArguments(self, args: dict = dict(), required: list = list(), valid: list = list(), oneoff: list = list(),
                        oneplus: list = list()) -> None:
        '''
            AssertArguments:

            Description:
                Asserts when either all required Argumentss are not present or a parameter is not a valid one.\n
                In addition when oneoff parameter is passed, only one of the required Arguments should be present.\n
                In addition when oneplus parameter is passed, atleast one of required Arguments should be present.

            Arguments:
                Required:
                    args     : dict - Key, value pair of args.
                    required : list - List of required Arguments.
                    valid    : list - List of valid Arguments.
                Optional:
                    oneoff   : list - List of one off Arguments.
                    oneplus  : list - List of one plus Arguments.

            Return:
                None.
        '''

        self.AssertRequiredArguments(args, required, oneoff, oneplus)
        valid = oneoff + oneplus + required + valid
        self.AssertValidArguments(args, valid)

        return

    def AssertRequiredArguments(self, args: dict = dict(), required: list = list(), oneoff: list = list(),
                                oneplus: list = list()) -> None:
        '''
            AssertRequiredArguments:

            Description:
                Asserts when all required Argumentss are not present.\n
                In addition when oneoff parameter is passed, only one of the required Arguments should be present.\n
                In addition when oneplus parameter is passed, atleast one of required Arguments should be present.

            Arguments:
                Required:
                    args     : dict - Key, value pair of args.
                    required : list - List of required Arguments.
                Optional:
                    oneoff   : list - List of one off Arguments.
                    oneplus  : list - List of one plus Arguments.

            Return:
                None.
        '''

        if oneoff:
            self.AssertOneOffArguments(args, oneoff)

        if oneplus:
            self.AssertOnePlusArguments(args, oneplus)

        for field in required:
            assert args.get(field), 'Missing Required Param ' + field + '.'

        return

    def AssertValidArguments(self, args: dict = dict(), valid: list = list()) -> None:
        '''
            AssertValidArguments:

            Description:
                Asserts when a parameter is not valid.

            Arguments:
                Required:
                    args     : dict - Key, value pair of args.
                    valid    : list - List of valid Arguments.
                Optional:
                    None.

            Return:
                None.
        '''

        valid_dict = dict.fromkeys(valid, True)
        for arg in args.keys():
            assert arg in valid_dict, arg + ' is Not a Valid Argument.'

        return

    def AssertOneOffArguments(self, args: dict = dict(), oneoff: list = list()) -> None:
        '''
            AssertOneOffArguments:

            Description:
                Asserts when either multple Arguments are present or none of the Arguments were present.

            Arguments:
                Required:
                    args  : dict - Key, value pair of args.
                    oneoff : list - List of valid Arguments.
                Optional:
                    None.

            Return:
                None.
        '''

        count = len(list(filter(lambda x: args.get(x), oneoff)))

        if count == 0:
            assert False, 'Required one of these Arguments ' + ', '.join(oneoff) + '.'
        elif count > 1:
            assert False, 'Only one of these Arguments are required ' + ', '.join(oneoff) + '.'
        return

    def AssertOnePlusArguments(self, args: dict = dict(), oneplus: list = list()) -> None:
        '''
            AssertOnePlusArguments:

            Description:
                Asserts none of the Arguments were present.

            Arguments:
                Required:
                    args    : dict - Key, value pair of args.
                    oneplus : list - List of valid Arguments.
                Optional:
                    None.

            Return:
                None.
        '''

        if not any(filter(lambda x: args.get(x), oneplus)):
            assert False, 'Atleast one of these Arguments were required ' + ', '.join(oneplus) + '.'

        return