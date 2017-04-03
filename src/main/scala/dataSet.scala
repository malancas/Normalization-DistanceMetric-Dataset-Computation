import math

sealed trait DataSet {
  val data
  def addDataFromFile(filename: String): Unit

  def normalize(): Double = {
    val numOfAttributes = (data.length - 1)
    val maxAtt = (math.NEG_INF_DOUBLE * numOfAttributes)
    val minAtt = (math.POS_INF_DOUBLE * numOfAttributes)
  }
}

case object Nil extends DataSet {
  val data = List()
}

case class Data extends DataSet {
  val data = //get data
}
