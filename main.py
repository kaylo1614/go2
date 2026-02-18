import asyncio
import pygame

async def main():
    pygame.init()
    # 建立一個測試視窗
    screen = pygame.display.set_mode((640, 360))
    print("🚨 [main.py] 成功接管！紅色畫面已啟動！")
    
    while True:
        # 畫紅色背景，確認繪圖引擎正常
        screen.fill((255, 0, 0)) 
        pygame.display.update()
        await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())
