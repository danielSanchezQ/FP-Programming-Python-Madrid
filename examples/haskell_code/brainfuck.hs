import System.Environment
import Data.Char

type Cells      = [Int]
type Ptr        =  Int
type OutBuffer  =  String
type Stack      = (Ptr, Cells, OutBuffer)

defValue :: Int
defValue = 0

maxSize :: Int
maxSize = 256

cells   :: Cells
cells   = [defValue]

ptr     :: Ptr
ptr     =  0    :: Ptr

outbfr  :: OutBuffer
outbfr  = ""

modPtr :: (Int -> Int) -> Stack -> Stack
modPtr f (p, c, o) = (newp, newc, o)
  where
    newp = f p
    newc = if newp > length c then c ++ replicate newp defValue else c

next :: Stack -> Stack
next = modPtr (+1)

prev :: Stack -> Stack
prev = modPtr (+ (-1))

applyIntFunc :: (Int -> Int) -> Stack -> Stack
applyIntFunc  f (p, c, o) = (p, res, o)
    where
        (h, t) = (take p c, drop p c)
        v = f $ head t
        res = h ++ [v] ++ tail t

inc :: Stack -> Stack
inc = applyIntFunc (\x-> mod (x+1) maxSize)

dec :: Stack -> Stack
dec = applyIntFunc (\x-> mod (x-1) maxSize)

toBuff :: Stack -> Stack
toBuff (p, c, o) =  (p, c, o ++ [chr v])
    where
        v = head $ drop p c

outVal :: Stack -> IO ()
outVal (p, c, o) = putChar $ chr v
    where
        v = head $ drop p c

printStack :: Stack -> IO ()
printStack (_, _, b) = putStrLn b

inVal :: Stack -> IO Stack
inVal (p, c, o) = do
    iv <- getLine
    let (h, t)  = (take p c, drop p c)
    let v       = read iv :: Int
    let res     = h ++ [v] ++ tail t
    return (p, res, o)

evalOne :: Char -> Stack -> Stack
evalOne '>' = next
evalOne '<' = prev
evalOne '+' = inc
evalOne '-' = dec
evalOne '.' = toBuff
evalOne  _  = id
-- evalOne ',' = inVal

snippetLoop :: String -> (String, String)
snippetLoop []         = ([], [])
snippetLoop ('[':xs)  = fst $ foldr reducef (("",""), 1) $ reverse xs
  where
    reducef ::  Char -> ((String, String), Int) -> ((String, String), Int)
    reducef c ((l, r), n)= ((newl, newr), num)
      where
        num = if n == 0 then 0 else case c of
          '['       -> n+1
          ']'       -> n-1
          otherwise -> n
        newl = if num == 0 then l       else l++[c]
        newr = if num == 0 then r++[c]  else r

--Recursive version, too slow , better with foldr
-- fuckloop :: Stack -> String -> Stack
-- fuckloop s [] = s
-- fuckloop s@(p, c, o) str = if v == 0 then s else fuckloop news str
--   where
--     v     = head $ drop p c
--     news  = fuckeval s str

fuckloop :: Stack -> String -> Stack
fuckloop s [] = s
fuckloop s@(p, c, o) str = head $ dropWhile (\(pp, cc, _)-> (head (drop pp cc) /= 0 )) $ scanl fuckeval s $ repeat str

fuckeval :: Stack -> String -> Stack
fuckeval s            []                = s
fuckeval s@(p, c, o) (x:xs) | x == '['  = fuckeval (fuckloop s l) r
                            | x == ']'  = fuckeval s xs
                            | otherwise = fuckeval (evalOne x s) xs
    where
      (l, r)              = snippetLoop (x:xs)


main = do
  [args] <- getArgs
  ff <- readFile args
  let l = [x | x<-lines ff, x /= ""]
  mapM_ ( printStack . fuckeval (127, replicate 256 0, "")) l