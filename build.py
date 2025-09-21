import os
import subprocess
import sys

def build_docker_images():
    """
    Finds directories with Dockerfiles in the current path and builds them
    using docker buildx, similar to the original shell script.
    """
    namespace = "sgj0/docker-images"

    # Get a specific directory to build from command-line arguments, if provided.
    target_dir = sys.argv[1] if len(sys.argv) > 1 else None

    # Iterate over all items in the current directory.
    for dir_name in sorted(os.listdir(".")):
        # Skip items that are not directories.
        if dir_name.startswith('.'):
            continue

        if not os.path.isdir(dir_name):
            continue

        # If a target directory was specified on the command line,
        # skip any directories that don't match.
        if target_dir and dir_name != target_dir:
            continue

        # Use the directory name as the image tag.
        tag = dir_name
        
        # Determine the correct platform, falling back to the default.
        match tag:
            case "guardian" | "icecast" | "liquidsoap" | "prettier" | "rtmp" | "versionning":
                platform = "linux/amd64,linux/arm64"
            case "freqtradepi":
                platform = "linux/arm/v8"
            case _:
                platform = "linux/amd64"

        full_image_name = f"{namespace}:{tag}"
        print(f"Building: {full_image_name} on {platform}")

        # Construct the build command.
        command = [
            "docker", "buildx", "build",
            "--progress", "plain",
            "--platform", platform,
            "--pull",
            "--push",
            "--tag", full_image_name,
            dir_name  # The build context path
        ]

        # Execute the command.
        try:
            # Using check=True will raise an exception if the command fails.
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"ERROR: Build failed for {full_image_name} with exit code {e.returncode}")
            # Exit the script if a build fails.
            sys.exit(1)
        except FileNotFoundError:
            print("ERROR: 'docker' command not found. Is Docker installed and in your PATH?")
            sys.exit(1)

if __name__ == "__main__":
    build_docker_images()
