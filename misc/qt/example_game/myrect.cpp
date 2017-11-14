#include "myrect.h"
#include <QGraphicsScene>
#include <QDebug>
#include <QKeyEvent>
#include "bullet.h"
#include "enemy.h"

void MyRect::keyPressEvent(QKeyEvent *event)
{
    qDebug() << "MyRect knows that you pressed a key";

    if (event->key() == Qt::Key_Left) {
        if (pos().x() > 0)
            setPos(x()-10,y());
    }
    else if (event->key() == Qt::Key_Right) {
        if (pos().x() + 100 < 800)
            setPos(x()+10,y());
    }
    else if (event->key() == Qt::Key_Up) {
        setPos(x(),y()-10);
    }
    else if (event->key() == Qt::Key_Down) {
        setPos(x(),y()+10);
    }
    else if (event->key() == Qt::Key_Space) {
        // create a bullet
        Bullet * bullet = new Bullet();
        qDebug() << "bullet created";
        bullet->setPos(x(),y());
        scene()->addItem(bullet);

    }
}

void MyRect::spawn()
{
    //create an enemy
    Enemy *enemy = new Enemy();
    scene()->addItem(enemy);
}