PseudoCode

3 Page Application:

First Page: Sampling Phase, Represented by class App
Second Page : Decision Phase, Represented by class Page_1
Third Page: Results Page, Represented by Class Page_2

Main Function
    Creates and Calls Object of Class App


Class App:
    CONSTRUCTOR:
        INPUT AmountBetted
        DISPLAY Start Game Button
        DISPLAY Go To Decision Phase Button
        CREATE LABEL for AmountWon
        CREATE LABEL for HeadCount
        Create LABEL for FlipCount
        IF User Clicks Start Game Button THEN
            CALL Validate() function:
                IF AmountBetted is Integer and greater than 0 THEN
                    CALL startGame() function:
                        INITIALIZE CountOfHead to 0
                        INITIALIZE CountOfFlips to 0
                        INITIALIZE AmountWon to 0
                        WHILE True
                            INCREMENT CountOfFlips by 1
                            INITIALIZE OUTCOME to 0 or 1 randomly
                            IF OUTCOME is 0 THEN
                                LOAD image of Heads
                                INCREMENT CountOFHeads
                                SET AmountWon to 2 raise to power of CountOfFlips
                                DISPLAY CountOfHead
                                DISPLAY AmountWon
                        
                            ELSE IF OUTCOME is 1 THEN
                                LOAD image of Tails
                                SET AmountWon to 2 raise to power of CountOfFlips
                                DISPLAY CountOfHead
                                DISPLAY AmountWon
                                Break out of While LOOP
                            ENDIF
                        ENDWHILE
                    END startGame() function
                ELSE throw exception
                ENDIF
            END Validate() Function
        EndIF

        IF User Clicks Go To Decision Phase Button THEN
            CALL make_page_1() function
        ENDIF

        //LOOP This whole frame 

    DEFINTION of make_page_1() function:
        Reset AmountWon Label to '0'
        Reset HeadCount Label to '0'
        Reset FlipCount Label to '0'
        CALL Object of Class Page_1
    END make_page_1() function

END Class App Definiton


Class Page_1:

    CONSTRUCTOR:
        INPUT AmountBetted
        DISPLAY Start Game Button
        CREATE LABEL for AmountWon
        CREATE LABEL for HeadCount
        Create LABEL for FlipCount
        IF User Clicks Start Game Button THEN
            CALL Validate() function:
                IF AmountBetted is Integer and greater than 0 THEN
                    CALL startGame() function:
                        INITIALIZE CountOfHead to 0
                        INITIALIZE CountOfFlips to 0
                        INITIALIZE AmountWon to 0
                        WHILE True
                            INCREMENT CountOfFlips by 1
                            INITIALIZE OUTCOME to 0 or 1 randomly
                            IF OUTCOME is 0 THEN
                                LOAD image of Heads
                                INCREMENT CountOFHeads
                                SET AmountWon to 2 raise to power of CountOfFlips
                                DISPLAY CountOfHead
                                DISPLAY AmountWon
                        
                            ELSE IF OUTCOME is 1 THEN
                                LOAD image of Tails
                                SET AmountWon to 2 raise to power of CountOfFlips
                                DISPLAY CountOfHead
                                DISPLAY AmountWon
                                Break out of While LOOP
                            ENDIF
                        ENDWHILE
                        LOAD AmountBetted and AmountWon to Object of Class Page_2
                        CALL make_page_2() function
                    END startGame() function
                ELSE throw exception
                ENDIF
            END Validate() Function
        EndIF
    
    DEFINTION of make_page_2() function:
        CALLS Object of Class Page_2;
    END make_page_2() function;

END class Page_2 Definiton

Class Page_2:

    CONSTRUCTOR:
        Create AmountWonLabel
        Create AmountBettedLabel
        Display AmountWon
        Display AmountBetted
        Loads Button to go back to sampling phase
        IF User clicks the Button:
            LOAD go_back() function
        ENDIF

    Definiton of go_back() function
        Calls Object of Class App
    END go_back() function
    
END class Page_2 Definiton
