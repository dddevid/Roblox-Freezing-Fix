#include <windows.h>
#include <shlobj.h> // Per SHGetFolderPath
#include <filesystem>
#include <fstream>
#include <nlohmann/json.hpp>

// Usa il namespace per json per semplicità
using json = nlohmann::json;
namespace fs = std::filesystem;

// Funzione per creare e scrivere il file JSON
void createJsonFile(const std::wstring& path) {
    json jsonContent = {
        {"FFlagHandleAltEnterFullscreenManually", "False"},
        {"DFIntTaskSchedulerTargetFps", 9999},
        {"FFlagDebugGraphicsPreferD3D11", "True"}
    };

    std::ofstream jsonFile(path);
    if (jsonFile.is_open()) {
        jsonFile << std::setw(4) << jsonContent << std::endl;
    }
    else {
        MessageBox(nullptr, L"Errore nella scrittura del file JSON.", L"Errore", MB_OK | MB_ICONERROR);
        return;
    }

    MessageBox(nullptr, L"Fix completato con successo", L"Successo", MB_OK | MB_ICONINFORMATION);
}

int WINAPI wWinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPWSTR lpCmdLine, int nCmdShow) {
    WCHAR userPath[MAX_PATH];
    if (SHGetFolderPathW(nullptr, CSIDL_PROFILE, nullptr, 0, userPath) != S_OK) {
        MessageBox(nullptr, L"Errore nel recupero del percorso utente.", L"Errore", MB_OK | MB_ICONERROR);
        return 1;
    }

    fs::path robloxPath = fs::path(userPath) / L"AppData/Local/Roblox/Versions/version-3243b6d003cf4642/ClientSettings";

    if (!fs::exists(robloxPath)) {
        fs::create_directories(robloxPath);
    }

    fs::path jsonFilePath = robloxPath / "ClientAppSettings.json";

    createJsonFile(jsonFilePath.wstring());

    return 0;
}
