
#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

int main()
{
    HWND hWnd = GetConsoleWindow();
    ShowWindow(hWnd, SW_MINIMIZE); //won't hide the window without SW_MINIMIZE
    ShowWindow(hWnd, SW_HIDE);
    system("cd $(dirname $0)/..");
    system("python src/main.py");
    return 0;
}