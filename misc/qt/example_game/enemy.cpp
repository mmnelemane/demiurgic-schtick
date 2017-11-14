#include "enemy.h"
#include <QTimer>
#include <QGraphicsScene>
#include <QDebug>
#include <stdlib.h>

Enemy::Enemy(): QObject(), QGraphicsRectItem()
{
    // set random position
    int random_number = rand() % 700;
    setPos(random_number,0);

    // create a rect
    setRect(0,0,100,100);

    // connect
    QTimer * timer = new QTimer();
    connect(timer, SIGNAL(timeout()), this, SLOT(move()));

    timer->start(50);

}

void Enemy::move()
{
    // move bullet up
    setPos(x(),y()+5);
    if (pos().y() + rect().height() < 0) {
        scene()->removeItem(this);
        delete this;
        qDebug() << "Bullet Deleted";
    }
}
