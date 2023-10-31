

#Transaction Management
ex:
    if query1
         &
       query2 ,both r executed successfully then commit
               if any one or both doesn't executes then rollback.
Set of queries,which are grouped logically is called a transaction.
If all the queries of a transaction,executed successfully,then only
we have to commit the transaction.
we can commit the transaction by calling commit()method of connection object.
If any one of the query of transaction execution is failed,then we need to
rollback the transaction.
we can rollback the transaction by calling rollback()method of connection object.
