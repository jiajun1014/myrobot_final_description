本系統是在Ubuntu Linux 20.04 ros1 noetic執行

💡wsl 安裝教學
step1：在空的硬碟磁區直接安裝Ubuntu Linux 20.04
安裝步驟：https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview
step2：安裝ros1 noetic https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/

優點：
-安裝簡單，可直接從 Microsoft Store 安裝 Ubuntu 等發行版
-啟動快、效能佳，適合日常開發與命令列工具使用
-和 Windows 整合性高，可以直接存取 Windows 檔案、用 VS Code 開啟專案
-支援 Windows 11 的 GUI 應用（WSLg），可以直接跑 Linux 的圖形介面程式
-不需要事先分配 RAM 或硬碟空間，使用彈性高

缺點：
-不是完整虛擬機，系統隔離性較差
-相容性有限，某些需要完整 Linux 環境或模擬硬體的工具（如 Gazebo、RViz）可能不穩定或無法使用
-圖形顯示或硬體模擬支援度較低，容易出現驅動或畫面問題
-WSL1 網路功能較有限，WSL2 雖改善但有時仍需手動設定

💡VirtualBox 安裝教學
step1：下載VirtualBox
https://www.virtualbox.org/wiki/Downloads
step2：下載官方映像檔(Desktop image) 
https://releases.ubuntu.com/20.04/?source=post_page-----5a998c7c037d---------------------------------------
step3：安裝ros1 noetic https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/

優點：
-提供完整的 Linux 系統環境，與實體機幾乎無異
-適合需要圖形介面、模擬硬體、ROS + Gazebo 等複雜任務
-系統完全隔離，適合測試、部署或模擬不同系統環境
-高度可自定，支援多種虛擬網路設定、快照、共享資料夾等功能

缺點：
-安裝與設定相對繁瑣，需要手動載入 ISO、分配資源
-效能比 WSL 低，因為要模擬整個作業系統
-每次使用需開啟虛擬機，啟動速度慢、耗用記憶體與 CPU
-與 Windows 的整合性差，例如不能直接用 Windows 編輯器開啟虛擬機內的檔案

本文介紹：
  機器人作業系統（Robot Operating System, ROS）是一套開源的機器人應用開發框架，提供建構複雜機器人系統所需的通訊機制、函式庫與工具。透過主題（topic）、服務（service）與動作（action）等方式，實現分散式系統下的數據交換與協同作業。其附帶的工具如 RViz（視覺化）、Gazebo（模擬環境）大幅簡化了開發流程。 隨著技術演進，ROS 進入 ROS 2 階段，基於 DDS 架構，強化即時性、多機協作與資安機制，使其更適用於無人載具、自主機器人與智慧工廠等現代應用。 本專題以 ROS 為主架構，進行機器人行為控制與模擬。ROS 的模組化設計與元件間高度相容性，使得系統整合與快速原型開發更為便利。
  本專題旨在利用 ROS（Robot Operating System）與 Gazebo 模擬環境，建立一套具備基本移動功能的虛擬四輪車系統。專案從零開始建構機器人模型，包含底盤、輪子，並結合 URDF（Unified Robot Description Format）與控制插件，實現模型 Gazebo 中的物理行為與感測模。
  透過此模擬系統，使用者可以在不依賴實體硬體的情況下進行功能測試與控制開發，如鍵盤遙控與視覺輸出等，進一步了解 ROS 架構整合的流程與模組功能。本系統可作為四輪汽車實作前的測試平台，具有良好的延展性與學習價值。

