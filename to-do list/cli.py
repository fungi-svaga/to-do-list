import sys
import argparse
from .task_list import TaskList
from .priority import PriorityManager


def print_tasks(tasks, title="Задачи"):
    if not tasks:
        print(f"{title}: нет задач")
        return

    print(f"\n{title}:")
    for i, task in enumerate(tasks, 1):
        print(f"  {i}. {task}")


def main():
    parser = argparse.ArgumentParser(description="Менеджер задач")
    parser.add_argument('--add', '-a', type=str, help='Добавить задачу')
    parser.add_argument('--priority', '-p', type=str, default='medium',
                        choices=['low', 'medium', 'high', 'critical'],
                        help='Приоритет задачи')
    parser.add_argument('--due', '-d', type=str, help='Дата выполнения (ГГГГ-ММ-ДД)')
    parser.add_argument('--complete', '-c', type=int, help='Отметить задачу как выполненную (номер)')
    parser.add_argument('--remove', '-r', type=int, help='Удалить задачу (номер)')
    parser.add_argument('--list', '-l', action='store_true', help='Показать все задачи')
    parser.add_argument('--filter-priority', type=str,
                        choices=['low', 'medium', 'high', 'critical'],
                        help='Фильтр по приоритету')
    parser.add_argument('--filter-date', type=str, help='Фильтр по дате (ГГГГ-ММ-ДД)')
    parser.add_argument('--sort', '-s', type=str,
                        choices=['priority', 'date', 'created'],
                        help='Сортировать задачи')
    parser.add_argument('--suggest', action='store_true', help='Предложить следующую задачу')

    args = parser.parse_args()

    task_list = TaskList()

    if not any(vars(args).values()):
        parser.print_help()
        return

    try:
        if args.add:
            task_list.add_task(args.add, args.priority, args.due)
            print(f"Задача добавлена: {args.add}")

        if args.complete is not None:
            task_list.mark_completed(args.complete - 1)
            print(f"Задача {args.complete} отмечена как выполненная")

        if args.remove is not None:
            task_list.remove_task(args.remove - 1)
            print(f"Задача {args.remove} удалена")

        if args.filter_priority:
            tasks = task_list.filter_by_priority(args.filter_priority)
            print_tasks(tasks, f"Задачи с приоритетом '{args.filter_priority}'")

        if args.filter_date:
            tasks = task_list.filter_by_date(args.filter_date)
            print_tasks(tasks, f"Задачи на {args.filter_date}")

        if args.sort:
            if args.sort == 'priority':
                task_list.sort_by_priority()
                print("Задачи отсортированы по приоритету")
            elif args.sort == 'date':
                task_list.sort_by_date()
                print("Задачи отсортированы по дате")
            elif args.sort == 'created':
                task_list.sort_by_created()
                print("Задачи отсортированы по дате создания")

        if args.suggest:
            manager = PriorityManager(task_list)
            next_task = manager.suggest_next_task()
            if next_task:
                print(f"Рекомендуемая задача: {next_task}")
            else:
                print("Нет задач для выполнения")

        if args.list:
            if len(task_list) == 0:
                print("Список задач пуст")
            else:
                print(task_list)

    except IndexError:
        print("Ошибка: задачи с таким номером не существует", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
