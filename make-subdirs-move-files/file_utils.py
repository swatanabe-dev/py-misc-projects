import shutil
from typing import List
from pathlib import Path

def prompt_for_directory(prompt: str) -> Path:
    '''
    Ask the user for an existing directory and validate the path.
    '''
    entered_path = input(prompt).strip()

    if not entered_path:
        raise ValueError("The directory path cannot be empty.")

    try:
        directory = Path(entered_path).expanduser().resolve(strict=True)
    except (OSError, RuntimeError) as error:
        raise ValueError(
            f"Could not find or access the directory: {entered_path}"
        ) from error

    if not directory.is_dir():
        raise ValueError(f"The path is not a directory")

    return directory


def validate_directories(source_directory:Path, destination_directory: Path)->None:
    '''
    Validate the directories relationship between the source and destination.
    '''
    # Keep these two directories on separate/parallel branches like Documents/Source and Documents/Destination
    if(source_directory == destination_directory or source_directory in destination_directory.parents or destination_directory in source_directory.parents):
        raise ValueError(
            "The source and destination must be separate directories."
            "Neither directory can be inside the other."
        )

    existing_items = []
    for item in destination_directory.iterdir():
        if not (item.name == ".DS_Store" and item.is_file()):
            existing_items.append(item)

    if existing_items:
        raise ValueError(
            "The destination directory must be empty before starting"
            "the program. Please check its contents and try again."
        )

def get_source_files(source_directory: Path) -> List[Path]:
    '''
    Return eligible source files in ascending file name order. 
    '''
    source_files =[]
    for item in source_directory.iterdir():
        if (item.name != ".DS_Store" and item.is_file() and not item.is_symlink()):\
        source_files.append(item)

    return sorted(
        source_files,
        key=lambda item: (item.name.casefold(), item.name),
    )


def get_files_per_folder() -> int:
    '''
    Ask how many files each subfolder should contain. 
    '''
    try:
        files_per_folder = int(input("\nHOw many files should each subfolder store?\n"
                                     "Files per subfolder: ").strip())
    except ValueError as error:
        raise ValueError(
            "Please enter a whole number greater than zero. "
        ) from error

    if files_per_folder <= 0:
        raise ValueError(
            "The number of files per subfolder must be greater than zero."
        )

    return files_per_folder




def create_subdirectories(
    destination_directory: Path,
    number_of_folders: int,
) -> List[Path]:
    """
    Create numbered subfolders and return their paths.
    """

    subdirectories = []
    try:
        for folder_number in range(1, number_of_folders + 1):
            folder_name = f"{folder_number:02d}"
            folder_path = destination_directory / folder_name
            folder_path.mkdir()

            subdirectories.append(folder_path)

    except OSError as error:
        raise RuntimeError(
            "Could not create all subfolders. Some folders may already "
            "have been created. Inspect the destination before trying again. "
            f"Details: {error}"
        ) from error

    return subdirectories


def move_files(
    source_files: List[Path],
    destination_subdirectories: List[Path],
    files_per_folder: int,
) -> int:
    """
    Move files into the supplied subfolders in their sorted order.
    """

    moved_count = 0
    try:
        for index, source_file in enumerate(source_files):
            destination_index = index // files_per_folder
            destination_folder = destination_subdirectories[destination_index]

            destination_file = destination_folder / source_file.name

            # Never overwrite an existing file or link.
            if destination_file.exists() or destination_file.is_symlink():
                raise FileExistsError(
                    f"A destination item already exists: {destination_file}"
                )

            shutil.move(str(source_file), str(destination_file))
            moved_count += 1

    except (OSError, shutil.Error) as error:
        # Tell that some files may already have been moved.
        raise RuntimeError(
            f"File moving stopped after {moved_count} file(s). "
            "Some files may already have been moved. Check both directories "
            "before trying again. "
            f"Details: {error}"
        ) from error

    return moved_count

