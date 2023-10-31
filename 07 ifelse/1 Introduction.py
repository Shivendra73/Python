#Flow-Control stmts:

-Every Python stmt executes only once from top to bottom.

-To execute or not to execute set of stmts, we go for flow-control stmts
#or
-To execute set of stmts for repeated no of times or for multiple times we go for loops or
 control structures.

Flow-Control stmts are divided into 2 parts
1.Condition: An Expresson which returns a boolean value
2.Block/clause:set of Stmts following the same space indentation

Various flow-control stmts/loops:
    1.if
    2.if-else
    3.elif
    4.for
    5.while
    6.while-else
    7.break
    8.continue
    9.pass
#Syntax for defining if-else:

if(condition):
    stmt1
    stmt2---------->Block1
    stmt3
    stmt4
else:
    stmt5
    stmt6---------->Block2
    stmt7
    stmt8
If the condition is True then the stmts within the if-block(Block1) will be executed
IF the condition is False then the stmts within the else-block(Block2) will be executed.

#Nested Blocks: Blocks within a block

if(condition):
    stmt1
    stmt2
    stmt3
    if(condition):
        stmt4
        stmt5
        stmt6
        stmt7
    else:
        stmt8
        stmt9
        stmt10
        stmt11
    stmt12
    stmt13
    stmt14
else:
    stmt15
    stmt16
    stmt17
















