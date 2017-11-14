#include <QApplication>
#include <QGraphicsScene>
#include "myrect.h"
#include <QGraphicsView>
#include <QTimer>

/*
 * Using classes:
 * QGraphicsScene
 * QGraphicsItem (QGraphicsRectItem)
 * QGraphicsView - used to visualize a scene
 * QKeyEvent - keyPressEvent
 * QDebug
 * QGraphicView/QGraphicScene/QGraphicItem coordinates
 */

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    // create a scene
    QGraphicsScene * scene = new QGraphicsScene();

    // create an item to put into the scene
    MyRect * rect = new MyRect();
    rect->setRect(0,0,100,100);

    // add item tot he scene
    scene->addItem(rect);

    // make item focusable
    rect->setFlag(QGraphicsItem::ItemIsFocusable);
    rect->setFocus();

    // add a view
    QGraphicsView * view = new QGraphicsView(scene);
    view->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
    view->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);

    view->show();
    view->setFixedSize(800,600);
    scene->setSceneRect(0,0,800,600);
    rect->setPos(view->width()/2, view->height() - rect->rect().height());

    // spawn enemies
    QTimer * timer = new QTimer();
    QObject::connect(timer, SIGNAL(timeout()), rect, SLOT(spawn()));
    timer->start(2000);

    return a.exec();
}
