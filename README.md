# BroncoCTF-2023-Internal

This is the internal repo for BroncoCTF 2023. *Every file that makes BroncoCTF run should be stored here.*

## Directory Structure

`
BroncoCTF-2023-Internal/
├── README.md
└── Challenges/
    └── README.md
    └── <Challenge Category>/
        └── <Challenge Name>/
            ├── Infra/
            ├── Files/
            ├── README.md
            └── Solution.md (or PDF)
`
The orginization for this repo should be easy to understand. The only files in the root directory should be system files (such as .gitignore, etc.), and files that explain where everything is (this README). Everything else is in a subfolder who's name should succintly describe it's purpouse (Challenges/ holds challenges). It's also a smart idea for subfolders to have README that explains the folder's specific purpouse, just so people have a good idea of what's going on.

The reason we do all of this is to make it easy for current board members to contribute to BroncoCTF, and make it easy for future board members to understand pervious BroncoCTF infrastructure.

## Contributing to this repo

Please don't push directly to the main branch. It can make it hard to roll back changes if anything goes wrong, and it makes it harder for people to work on multiple things at a time. Instead, create a new branch named after your challenge/change, make your changes there, then open a pull request to have your challenge/change merged into main.

Main should serve as a collection of our "completed work".
