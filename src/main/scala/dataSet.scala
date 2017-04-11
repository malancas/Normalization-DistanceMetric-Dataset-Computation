import scala.math

sealed trait DataSet {
  val data
  val minAtt
  val maxAtt

  def addDataFromFile(filename: String): Unit = {
    /*
     with open(dataFile, 'r') as f:
       for line in f:
         line = map(str.strip, line.split(','))
         for i in range(0, len(line)-1):
           line[i] = float(line[i])
           dataList.append(line)
           self.datSet = dataList
    */

    io.Source.fromFile(filename).map(str => str.strip, line => line.split(',')).map(i => float(i))
  }

  // Update the new extreme minimum and maximum attributes. Used with scala.math.min and scala.math.max
  def getExtremesRecursive(i: Int, dataSet: List[List[Double]], minAtts: List[Double], maxAtts: List[Double]): List[List[Double]] = {
    if (i < dataSet.length - 1) {
      getExtremesRecursive(i+1, dataSet, for ((a,b) <- (dataSet(i) zip minAtts)) yield math.min(a,b), for ((a,b) <- (dataSet(i) zip minAtts)) yield math.min(a,b))
    }
    List(for ((a,b) <- (dataSet(i) zip minAtts)) yield math.min(a,b), for ((a,b) <- (dataSet(i) zip maxAtts)) yield math.max(a,b))
}

  def getExtremes(dataSet: List[List[Double]], minAtts: List[Double], maxAtts: List[Double]): List[List[Double]] = {
    for ( i <- 0 until dataSet.length){
      val newMaxes = for ((a,b) <- (dataSet(i) zip maxAtts)) yield math.max(a,b)

      val newMins = for ((a,b) <- (dataSet(i) zip minAtts)) yield math.min(a,b)
    }

    List(newMaxes, newMins)
  }

  def goDoMath(i: Int, k: Int, minAtts: List[Double], maxAtts: List[Double], data: List[List[Double]], newData: List[List[Double]]): List[List[Double]] = {
    if (i < data.length){
      if (k < numAttributes) {
        goDoMath(i+1, k+1, minAtts, maxAtts, data, newData(i) :+ doMath(i, k, minAtts, maxAtts, data))
      }
    }
  }

  def doMath(i: Int, k: Int, minAtts: List[Double], maxAtts: List[Double], data: List[List[Double]]): List[Double] = {
    (data(i)(k) - minAtts(k)) / (maxAtts(k) - minAtts(k))
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

object DataSet {
  case object NilDataSet extends DataSet[Nothing]

  case class Data(data: List[Double]) extends DataSet {
    this.data = data
  }
}
