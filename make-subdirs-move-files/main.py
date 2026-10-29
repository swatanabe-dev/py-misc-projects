
import sys
import shutil

from file_utils import (
    prompt_for_directory,
    validate_directories,
    get_source_files,
    get_files_per_folder,
    create_subdirectories,
    move_files,
)


def main() -> int:
    '''
    Run the interactive program.
    '''
    try:
       
        source_directory = prompt_for_directory(
            "Enter the source folder path: "
        )

        destination_directory = prompt_for_directory(
            "Enter the destination folder path: "
        )

        validate_directories(
            source_directory,
            destination_directory,
        )

        source_files = get_source_files(source_directory)

        if not source_files:
            raise ValueError("No eligible files were found.")

        files_per_folder = get_files_per_folder()

        number_of_folders = (
            len(source_files) + files_per_folder - 1
        ) // files_per_folder

        print(f"Files to move: {len(source_files)}")
        print(f"Subfolders to create: {number_of_folders}")

        confirmation = input(
            "Type 'yes' to proceed: "
        ).strip().lower()

        if confirmation != "yes":
            print("Operation cancelled.")
            return 0

        destination_subdirectories = create_subdirectories(
            destination_directory,
            number_of_folders,
        )

        moved_count = move_files(
            source_files,
            destination_subdirectories,
            files_per_folder,
        )

        print(f"Successfully moved {moved_count} files.")
        return 0

    except KeyboardInterrupt:
        print("\nOperation interrupted.", file=sys.stderr)
        return 130

    except (ValueError, OSError, RuntimeError, shutil.Error) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())