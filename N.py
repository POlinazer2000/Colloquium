class N:
	def __init__( self, digit ):
		self.digits = []
		if isinstance( digit, ( list, tuple ) ):
			try:
				self.digits = [ int( i ) for i in digit ]
			except:
				raise RuntimeError( "Digit cannot be presented as integer > 0." )
		elif isinstance( digit, int ):
			try:
				self.digits = [ int( i ) for i in str( digit ) ]
			except:
				raise RuntimeError( "Digit cannot be presented as integer > 0." )
		#print( self.digits )

	def __str__( self ):
		return str( ''.join( map( str, self.digits ) ) )
