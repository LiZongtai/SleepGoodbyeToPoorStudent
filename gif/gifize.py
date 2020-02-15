
import imageio
def create_gif(image_list, gif_name, duration = 1.0):
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))

    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return

def main():
    #这里放上自己所需要合成的图片
    image_list = []
    for i in range(50):
        image_list.append("img/" + str(i) + '.jpg')
    gif_name = 'new.gif'
    duration = 0.1
    create_gif(image_list, gif_name, duration)

if __name__ == '__main__':
    main()