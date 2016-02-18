import System.Environment
import Data.List
import Data.Char


convert :: (Char, Char) -> Char
convert (f, s) 	| s == '1' 	= toUpper $ f
				| otherwise	= f

doIt :: [String] -> String
doIt l =  foldr (:) [] $ map convert $ zip (head l) (last l)


main = do
	[args] <- getArgs
	ff <- readFile args
	let l = [words x | x<-lines ff, x /= ""]
	mapM_ putStrLn [doIt x  | x <- l]