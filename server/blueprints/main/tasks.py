from server.app import create_celery_app

celery = create_celery_app()


# @celery.task()
# def predeploy_coin_async(id_arg):
#     # time.sleep(2)

#     print("CELERY: Begin predeploy...")
#     coin = Coin.query.filter(Coin.id == id_arg).first()
#     deployer = ChialispDeployer(coin.puzzlejson,coin.filename)
#     deployer.preDeployCoin()

#     puzhash = deployer.getPuzHash()
#     print("CELERY: PUZ: ",puzhash)
#     coin.puzzlehash = puzhash
#     coin.save()
#     print("CELERY: Async finished")

#     return None
