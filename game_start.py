import asyncio
import pygame

async def main():
    pygame.init()
    # 設定一個很小的視窗，避免解析度問題
    screen = pygame.display.set_mode((640, 360))
    print("🚨 [測試成功] 紅色畫面已啟動！") 
    
    while True:
        # 填滿紅色背景
        screen.fill((255, 0, 0)) 
        pygame.display.update()
        # 這是網頁版最重要的一行，交出控制權給瀏覽器
        await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())
