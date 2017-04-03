import scala.math

sealed trait DataSet {
  val data
  def addDataFromFile(filename: String): Unit

  def recordExtremes(i: Int, k: Int): List[Double] = {
    if (data(i)(k) < minAtt(k)) min(k) = data(i)(k)
    if (data(i)(k) < maxAtt(k)) maxAtt(k) = data(i)(k)
  }

  def doMath(i: Int, k: Int): List[Double] = {
    data(i)(k) = (data(i)(k) - minAtt(k)) / (maxAtt(k) - minAtt(k))
  }

  def go(i: Int, k: Int, f: Int, Int => List[Double]): Double = {
    if (i < data.length) {
      if (k < numAttributes) {
        f(i, k)
      }
    }
    go(i+1, k+1, f)
  }

  def normalize(): Double = {
    val numOfAttributes = (data.length - 1)
    val maxAtt = (math.NEG_INF_DOUBLE * numOfAttributes)
    val minAtt = (math.POS_INF_DOUBLE * numOfAttributes)

    go(0, 0, recordExtremes)
    go(0, 0, doMath)
  }
}

case object Nil extends DataSet[Nothing]

case class Data(data: List[Double]) extends DataSet {
  val data //get data
}
