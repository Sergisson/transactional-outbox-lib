from app.repositories.databases.sqlalchemy.handler import SqlAldchemyHandler
from app.repositories.queue.kafka.handler import KafkaHandler

databases = {
    "sqlalchemy": SqlAldchemyHandler,
}
queues = {
    "kafka": KafkaHandler,
}


class TransactionalOutbox:
    # TODO подумать куда положить, тут не место и над именем
    def __init__(
        self,
        database_name: str,
        queue_name: str,
    ):
        self.database_handler = databases.get(database_name)
        if not self.database_handler:
            raise ValueError("Your database didn't support")

        self.queues_handler = queues.get(queue_name)
        if not self.queues_handler:
            raise ValueError("Your queue didn't support")

    def execute_transaction(
        self,
        database_table: str,
        queue_name: str,
        message: str,
    ):
        self.database_handler.save_changes(
            database_table=database_table,
        )
        self.queues_handler.send_message(
            queue_name=queue_name,
            message=message,
        )


if __name__ == "__main__":
    # Для тестов, потом надо вынести в реальные тесты и написать интрфейс запуска
    # Так же нужно подумать над тем, чтобы не устанавливались лишние зависимости
    transactional_outbox = TransactionalOutbox(
        database_name="sqlalchemy",
        queue_name="kafka",
    )
    transactional_outbox.execute_transaction(
        database_table="user",
        queue_name="change_user",
        # TODO посмотреть мб dict лучше
        message="{user:\"name:\"Ivan\"\"}",
    )
