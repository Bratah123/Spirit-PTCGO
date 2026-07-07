from enum import Enum, IntEnum

class AttrID(IntEnum):
    IS_PROMO = 200560
    IS_VALID_FOR_TRADE = 10640
    IS_SPECIAL_ENERGY = 200970
    SET_ID = 201410

    # Core Attributes
    ARCHETYPE_ID = 10000
    EXPANSION = 10020
    SET_KEY = 10020
    DISPLAY_NAME = 10140
    NAME = 10140
    CURRENCY_TYPE = 10200
    PRODUCT_TYPE = 10540
    # Booster pack rarity odds (a.g[]): the "i" info popup builds new List<a.g>(ValueFor)
    # and NREs if this is absent. Array of {rarityIcon, rarityName, count}.
    PACK_RARITY_DATA = 202250
    # Product contents / preview cards (ArchetypeID[]): the pack "i" popup marquee reads this
    # via the cache-safe GetArchetype filter; the unfiltered set-featured fallback crashes instead.
    PACK_PREVIEW_CARDS = 201505
    RARITY = 200550
    CARD_TYPE = 200300
    COLLECTION_ID = 200000
    COLLECTOR_NUMBER = 200780
    SET_CACHE_KEY = 200580

    # Pokemon Specific
    HP = 200490
    STAGE = 200540
    POKEMON_TYPES = 200570
    WEAKNESS_TYPES = 200590
    WEAKNESS_OPERATOR = 200660
    WEAKNESS_AMOUNT = 200820
    RESISTANCE_TYPES = 200600
    RESISTANCE_OPERATOR = 200650
    RESISTANCE_AMOUNT = 200830
    RETREAT_COST = 200800
    ABILITIES = 200720
    PIE_ABILITIES = 200740
    # Playmat attr: EntityID[] of the acting attack/ability source; the client's
    # Attack executor reads element [0] and the orb FX shoots from it.
    ATTACK_SOURCES = 201870

    # Trainer Specific
    TRAINER_TYPE = 200270

    # SpecialConditions[] on the (Active) Pokemon entity; the client's
    # Add/RemoveSpecialCondition executors diff this array against their set.
    SPECIAL_CONDITIONS = 200340

    # SpecialVisualizations (P.G[]) on a Pokemon entity: the stat-modifier PiP
    # arrows (green up / red down). displayType must be non-null (s.F derefs
    # .Value unguarded); arrow "Positive"/"Negative" drives the arrow.
    SPECIAL_VISUALIZATIONS = 200370

    # Play area (pile/zone) attributes -- read by the playmat layouts via
    # k.P.configurePile (U.E facet). BenchLayout divides by AREA_SLOTS
    # (201920 int) when spacing cards: a missing/zero value produces
    # NaN transforms and invisible cards, so slotted areas MUST carry it.
    # AREA_EMPTY_SLOTS (201860 int[]) marks gaps; null reads as "no gaps".
    AREA_SLOTS = 201920
    AREA_EMPTY_SLOTS = 201860

    # Energy Specific
    ENERGY_INFO = 201040 # Type: global::P.f (PokemonTypes[][] A)

    # Scenario Specific
    SCENARIO_LEAGUE_ID = 201420
    SCENARIO_DESCRIPTION = 201430
    SCENARIO_IMAGE = 10060

    # Wallet / UI
    TRAINER_TOKENS = -1784319558
    EVENT_TICKETS = -992199324
    GEMS = 2012906479
    REAL_CURRENCY = 2012906479

    # Avatar Specific
    AVATAR_GENDER = 10220
    AVATAR_GROUP = 200890
    AVATAR_BUNDLE_NAME = 200930
    AVATAR_RARITY = 200900
    AVATAR_IS_FREE = 200950
    AVATAR_STYLE_LINK_ID = 200215
    AVATAR_STYLE_COLLECTION_NAME = 200880
    AVATAR_IS_DEFAULT = 200940

    # Deck Cosmetics (Verified from CakeDeckExtensions.cs)
    SELECTED_COIN = 200670
    SELECTED_SLEEVE = 200680
    SELECTED_DECK_BOX = 200690
    VALID_FORMATS = 10860

    # Other
    HIDDEN_ON_CLIENT = 201740 # Guessing from b in g.4.cs

    # Evolution & Family (Verified from client source)
    FAMILY_ID = 200260
    EVOLVES_FROM = 200280
    EVOLUTION_LOGIC_NAME = 200630 # P.F.C (string) - Internal name for evolution chain basic
    EVOLUTION_LOGIC_FROM = 200640 # P.F.F (string) - Internal name this evolves from
    RELATED_ARCHETYPE = 200670 # Note: Also used for SelectedCoin in Decks

    # Foil / Holo Attributes
    FOIL_EFFECT = 200610
    FOIL_EFFECTS = 200611
    FOIL_MASK = 200620
    FOIL_INTENSITY = 202080

    # From g.4.cs analysis
    # global::P.F.d (10140)
    # global::P.F.h (10510) -> Image
    # global::P.F.b (10020) -> Image fallback / Set
    # global::P.F.e (10480) -> Image fallback
    # global::P.F.m (200580) -> Set/Cache Key?
    IMAGE_URL = 10510
    IMAGE_NAME = 10520
    IMAGE_FALLBACK_1 = 10020
    IMAGE_FALLBACK_2 = 10480
    CATALOG_ID = 10570
    SET_NUMBER = 10190
    SHOP_PRICE_MAP = 77381929

    # Social Permissions (UserFlags)
    FRIEND_CHAT_MODE = 201510
    FRIEND_MODE = 201520
    FRIEND_TRADE_MODE = 201530
    GAME_CHAT_MODE = 201540
    PUBLIC_CHAT_MODE = 201550
    SHOPPING_MODE = 201560
    TRADE_MODE = 201570
    PRIVATE_MESSAGING_MODE = 201580

    # Deck Creation
    DECK_SHARE_MODE = 201850

    # Versus ladder (account attributes read by the client versus screen)
    SEASON_POINTS = 201810
    ALL_TIME_SEASON_POINTS = 201840

    # Server-persisted client settings dict (Dictionary<int,int>; K.L.GetSetting(n))
    ACCOUNT_SETTINGS = 10230

    # Account screen name (string; H.J.UserScreenName falls back to this outside a match)
    SCREEN_NAME = 10360

class Rarities(IntEnum):
    Common = 0
    Uncommon = 1
    Rare = 2
    RareHolo = 3
    RareHoloEX = 4
    RareHoloGX = 5
    RareHoloV = 6
    RareHoloVMAX = 7
    RareHoloVSTAR = 8
    ChrRareHolo = 9
    ChrRareHoloV = 10
    ChrRareSecret = 11
    ChrRareUltra = 12
    RarePrime = 13
    Legendary = 14
    Ace = 15
    RareUltra = 16
    RareSecret = 17
    RareRainbow = 18
    DisplayNone = 19
    medium = 20
    PromoExclusive = 21
    RarePromo = 22
    Token = 23
    ExtraRare = 24
    VeryRare = 25
    Unassigned = 26
    BreakRare = 27
    Shining = 28
    Prism = 29
    Amazing = 30
    RareRadiant = 31
    RareDitto = 32
    UNSET = -1

class CardType(IntEnum):
    POKEMON = 0
    LEGEND_HALF = 1
    TRAINER = 2
    ENERGY = 3
    UNSET = -1

class PokemonTypes(IntEnum):
    NO_COLOR = 0
    COLORLESS = 1
    DARKNESS = 2
    DRAGON = 3
    FAIRY = 4
    FIGHTING = 5
    FIRE = 6
    GRASS = 7
    LIGHTNING = 8
    METAL = 9
    PSYCHIC = 10
    WATER = 11
    STRONG = 12
    HERBAL = 13
    UNSET = -1


# Client Cake.enums.PokemonTypes member names. JSON dictionary KEYS typed as
# PokemonTypes (e.g. attack cost) coerce by NAME only -- "11" crashes; JSON
# numbers elsewhere coerce by value.
CLIENT_POKEMON_TYPE_NAMES = {
    PokemonTypes.NO_COLOR: "NoColor",
    PokemonTypes.COLORLESS: "Colorless",
    PokemonTypes.DARKNESS: "Darkness",
    PokemonTypes.DRAGON: "Dragon",
    PokemonTypes.FAIRY: "Fairy",
    PokemonTypes.FIGHTING: "Fighting",
    PokemonTypes.FIRE: "Fire",
    PokemonTypes.GRASS: "Grass",
    PokemonTypes.LIGHTNING: "Lightning",
    PokemonTypes.METAL: "Metal",
    PokemonTypes.PSYCHIC: "Psychic",
    PokemonTypes.WATER: "Water",
    PokemonTypes.STRONG: "Strong",
    PokemonTypes.HERBAL: "Herbal",
}
POKEMON_TYPES_BY_CLIENT_NAME = {v: k for k, v in CLIENT_POKEMON_TYPE_NAMES.items()}

class SpecialConditions(IntEnum):
    ASLEEP = 0
    BURNED = 1
    CONFUSED = 2
    PARALYZED = 3
    POISONED = 4
    UNSET = -1


# Attr 200340 arrays coerce by NAME on the client (enum-typed JSON strings).
CLIENT_SPECIAL_CONDITION_NAMES = {
    SpecialConditions.ASLEEP: "Asleep",
    SpecialConditions.BURNED: "Burned",
    SpecialConditions.CONFUSED: "Confused",
    SpecialConditions.PARALYZED: "Paralyzed",
    SpecialConditions.POISONED: "Poisoned",
}


class PokemonStage(IntEnum):
    BASIC = 0
    STAGE1 = 1
    STAGE2 = 2
    RESTORED = 3
    LEVELUP = 4
    LEGEND = 5
    BREAK = 6
    VMAX = 7
    VUNION = 8
    VSTAR = 9
    UNSET = -1

class TrainerType(IntEnum):
    ITEM = 0
    STADIUM = 1
    SUPPORTER = 2
    TECHNICAL_MACHINE = 3
    POKEMON_TOOL = 4
    POKEMON_TOOL_F = 5
    TRAINER = 6
    UNSET = -1

class AbilityTypes(IntEnum):
    ATTACK = 0
    NON_DAMAGING_ATTACK = 1
    POKE_ABILITY = 2
    POKE_POWER = 3
    POKE_BODY = 4
    TECHNICAL_MACHINE = 5
    ANCIENT_TRAIT = 8
    UNSET = -1

class ProductType(IntEnum):
    AVATARS = 0
    AVATAR_ITEMS = 1
    AVATAR_PRODUCTS = 2
    BUNDLES = 3
    CAMPAIGNS = 4
    COINS = 5
    CURRENCY = 6
    CURRENCY_TRANSFER = 8
    DECK_BOX = 11
    DECKS = 12
    DRAFT_ENTRY = 13
    EXTRAS = 15
    FACTION_PACKS = 16
    GIFTS = 17
    INVESTMENT = 18
    ITEM = 19
    MISCELLANEOUS = 20
    PACKS = 21
    PLAYMAT = 22
    POWERUPS = 23
    PROOFSET = 24
    RESOURCES = 25
    SINGLES = 26
    SLEEVE = 27
    TOURNAMENT_ENTRY = 28
    WORKSHOP_RECIPE = 30
    EXTERNAL_PRODUCT = 14
    CUSTOM_PRODUCT = 7
    COLLECTIBLES = 9
    COLLECTIBLE_BASES = 10
    UNSET = -1

class CurrencyType(IntEnum):
    EVENT_TICKETS = -605044899
    VIRTUAL_CURRENCY = -706482148
    REAL_CURRENCY = 2012906479

class FoilMasks(IntEnum):
    NONE = 0
    HOLO = 1
    REVERSE = 2
    THATCH = 3
    ETCHED = 4
    UNSET = -1

class FoilEffects(IntEnum):
    NONE = 0
    COSMOS = 1
    GALAXY = 2
    RAINBOW = 3
    CRACKED_ICE = 4
    LITHOGRAPH = 5
    TINSEL = 6
    FLATSILVER = 7
    ETCHED = 8
    ETCHEDSUNPILLAR = 9
    ANGLEDPILLARS = 10
    SQUARES = 11
    SUNLAVA = 12
    SUNPILLAR = 13
    SUNBEAM = 14
    SOLGALEOETCH = 15
    LUNALAETCH = 16
    XYETCH = 17
    BWETCH = 18
    TAPUFINIETCH = 19
    TAPUBULUETCH = 20
    TAPUKOKOETCH = 21
    TAPULELEETCH = 22
    SOLGALEOHFETCH = 23
    LUNALAHFETCH = 24
    SWHOLO = 25
    SWSECRET = 26
    ANN25THCONFETTI = 27
    RADIANTHOLO = 28
    SVHOLO = 29
    UNSET = -1

class FeatureToken(str):
    """
    Feature flags for AllFeatureStatuses_v2 — names decoded from the client's
    W.GetFeatureCommand registry (XOR string blob); made-up names match nothing.
    """
    # TournamentFeature -> TournamentStateModel: enables the Events nav button
    TOURNAMENT_FEATURE = "TournamentFeature"
    # Leaderboards -> TournamentLeaderboardsEnabledModel (weekly rewards request)
    LEADERBOARDS = "Leaderboards"
    CHAT_ENABLED = "ChatEnabled"
    CODES_ENABLED = "CodesEnabled"
    EXCHANGE_FEATURE = "ExchangeFeature"  # -> "trade" model
    COMMERCE_FEATURE = "CommerceFeature"
    # Recognized by the registry but wired to no command in this build
    GENERIC_FEATURE = "GenericFeature"
    SOCIAL_FEATURE = "SocialFeature"
    DECK_BUILDER_FEATURE = "DeckBuilderFeature"
    STORE_GENERIC_FEATURE = "StoreGenericFeature"
    PROGRESSION_FEATURE = "ProgressionFeature"
    MATCH_FEATURE = "MatchFeature"
    DRAFT_FEATURE = "DraftFeature"
    PROFILE_FEATURE = "ProfileFeature"

class DeckFormat(str, Enum):
    STANDARD = "6402e830-7fed-4cd1-b172-2a320047c2bb"
    EXPANDED = "98c83df9-ec82-4193-84a8-104115ce4e25"
    UNLIMITED = "6a1dec5a-34db-4cee-a503-4ee759304135"
    LEGACY = "6b33d420-73cc-40d4-ada5-88a7d68063a9"
    THEME = "1414fd67-a632-4e38-ae04-0adf0074ac16"
    TRAINER_CHALLENGE = "6a1dec5a-34db-4cee-a503-4ee759304136"

class PlayerAttrID(IntEnum):
    """
    Attributes specifically set on PlayerEntity (CakePlayerEntity).
    """
    HAS_GX_TOKEN = 202130       # F.m - Enables physical GX Token on the playmat
    HAS_VSTAR_TOKEN = 203300    # F.N - Enables physical VSTAR Token on the playmat


class GameSequence(str, Enum):
    """
    All valid GameSequence names matched by sequence command constructors 
    in the PTCGO client source code.
    """
    RECURSIVE_RETURN_TO_OWNERS_HAND = "RecursiveReturnToOwnersHand" # Found in: client_source\pie\pie-src\B\S.cs
    REVEAL_MULLIGANS = "RevealMulligans" # Found in: client_source\pie\pie-src\B\T.2.cs
    ALWAYS_REVEAL = "AlwaysReveal" # Found in: client_source\pie\pie-src\B\Y.3.cs
    REPLACE_ACTIVE = "ReplaceActive" # Found in: client_source\pie\pie-src\B\Z.2.cs
    SIMULTANEOUS_FLIP_THEN_ACTION = "SimultaneousFlipThenAction" # Found in: client_source\pie\pie-src\C\A.cs
    TRANSFORM_ENTITY = "TransformEntity" # Found in: client_source\pie\pie-src\C\b.cs
    WONDER_LOCK = "WonderLock" # Found in: client_source\pie\pie-src\C\D.cs
    DEAL_INITIAL_HANDS = "DealInitialHands" # Found in: client_source\pie\pie-src\D\n.3.cs
    DEVOLVE = "Devolve" # Found in: client_source\pie\pie-src\D\o.2.cs
    DISCARD_RETREAT_COST = "DiscardRetreatCost" # Found in: client_source\pie\pie-src\D\Q.cs
    ROBO_SUBSTITUTE = "RoboSubstitute" # Found in: client_source\pie\pie-src\D\R.cs
    FLIP_TO_WAKE_UP = "FlipToWakeUp" # Found in: client_source\pie\pie-src\D\s.cs
    WITH_OPEN_PRIZE_CARDS = "WithOpenPrizeCards" # Found in: client_source\pie\pie-src\D\t.cs
    ACTIVE_PLAYER_SET = "ActivePlayerSet" # Found in: client_source\pie\pie-src\L\Z.2.cs
    BURN_DAMAGE = "BurnDamage" # Found in: client_source\pie\pie-src\M\a.2.cs
    BENCH_SIZE_MODIFIED = "BenchSizeModified" # Found in: client_source\pie\pie-src\M\A.cs
    CREATE_LEGEND = "CreateLegend" # Found in: client_source\pie\pie-src\M\B.cs
    DRAW = "Draw" # Found in: client_source\pie\pie-src\M\c.2.cs
    FLIP_FOR_BURN = "FlipForBurn" # Found in: client_source\pie\pie-src\M\C.cs
    FLIP_FOR_CONFUSION = "FlipForConfusion" # Found in: client_source\pie\pie-src\M\D.cs
    USE_STADIUM_ABILITY = "UseStadiumAbility" # Found in: client_source\pie\pie-src\M\E.cs
    PLAY_CARD = "PlayCard" # Found in: client_source\pie\pie-src\M\F.cs
    HURT_FROM_CONFUSION = "HurtFromConfusion" # Found in: client_source\pie\pie-src\M\g.cs
    INITIAL_COIN_FLIP = "InitialCoinFlip" # Found in: client_source\pie\pie-src\M\h.cs
    INTRODUCE_INITIAL_POKEMON = "IntroduceInitialPokemon" # Found in: client_source\pie\pie-src\M\i.cs
    GROUPED_MOVE = "GroupedMove" # Found in: client_source\pie\pie-src\M\j.cs
    ATTACK = "Attack" # Found in: client_source\pie\pie-src\M\N.cs
    OPPONENT_CHOOSING_TO_GO_FIRST = "OpponentChoosingToGoFirst" # Found in: client_source\pie\pie-src\M\o.cs
    OPPONENT_PICKING_HEADS_OR_TAILS = "OpponentPickingHeadsOrTails" # Found in: client_source\pie\pie-src\M\Q.cs
    TRAINER_CARD = "TrainerCard" # Found in: client_source\pie\pie-src\M\r.cs
    POKE_ABILITY = "PokeAbility" # Found in: client_source\pie\pie-src\M\s.cs
    REMOVE_SPECIAL_CONDITION = "RemoveSpecialCondition" # Found in: client_source\pie\pie-src\M\t.cs
    ADD_SPECIAL_CONDITION = "AddSpecialCondition" # Found in: client_source\pie\pie-src\M\u.cs
    MULLIGAN = "Mulligan" # Found in: client_source\pie\pie-src\M\v.cs
    DRAW_PRIZE_CARD = "DrawPrizeCard" # Found in: client_source\pie\pie-src\M\w.cs
    POISON_DAMAGE = "PoisonDamage" # Found in: client_source\pie\pie-src\M\y.cs
    DEAL_INITIAL_PRIZE_CARDS = "DealInitialPrizeCards" # Found in: client_source\pie\pie-src\M\z.cs
    INITIAL_PICK = "InitialPick" # Found in: client_source\pie\pie-src\N\j.cs
    KNOCKOUT = "Knockout" # Found in: client_source\pie\pie-src\N\k.cs
    PLAY_ACTIVE = "PlayActive" # Found in: client_source\pie\pie-src\N\M.cs
    PLAY_ENERGY = "PlayEnergy" # Found in: client_source\pie\pie-src\N\N.cs
    PLAY_TOOL = "PlayTool" # Found in: client_source\pie\pie-src\N\O.cs
    RETREAT = "Retreat" # Found in: client_source\pie\pie-src\N\P.cs
    STADIUM_PRESENT = "StadiumPresent" # Found in: client_source\pie\pie-src\N\Q.cs
    TRAINER_PRESENT = "TrainerPresent" # Found in: client_source\pie\pie-src\N\R.cs
    MOVE_FROM_BOTTOM_OF_DECK = "MoveFromBottomOfDeck" # Found in: client_source\pie\pie-src\R\g.cs
    MOVE_FROM_MIDDLE_OF_DECK = "MoveFromMiddleOfDeck" # Found in: client_source\pie\pie-src\R\H.2.cs
    MOVE_FROM_TOP_OF_DECK = "MoveFromTopOfDeck" # Found in: client_source\pie\pie-src\R\i.2.cs
    ATTACH_TO_VUNION = "AttachToVUnion" # Found in: client_source\pie\pie-src\R\J.cs
    CLOSE_PRIZE_PILE = "ClosePrizePile" # Found in: client_source\pie\pie-src\R\K.2.cs
    DISMISS_ABILITY_SELECT = "DismissAbilitySelect" # Found in: client_source\pie\pie-src\R\L.cs
    PARALLEL_SEQUENCE = "ParallelSequence" # BROKEN client-side: r.M's command list is never assigned (IL-verified), executor NREs
    REVEAL_AND_SKIP_MOVE = "RevealAndSkipMove" # Found in: client_source\pie\pie-src\R\N.2.cs
    SERIAL_SEQUENCE = "SerialSequence" # Found in: client_source\pie\pie-src\R\O.2.cs
    VUNION_BREAK_SEQUENCE = "VUnionBreakSequence" # Found in: client_source\pie\pie-src\R\P.cs
    CREATE_VUNION = "CreateVUnion" # Found in: client_source\pie\pie-src\R\Q.cs
    ACTIVE_CARD_AND_ATTACHMENTS_SHUFFLED = "ActiveCardAndAttachmentsShuffled" # Found in: client_source\pie\pie-src\V\r.3.cs
    HAND_SHUFFLED_AND_MOVED_TO_DECK = "HandShuffledAndMovedToDeck" # Found in: client_source\pie\pie-src\V\s.3.cs
    TRANSFORM_SWAP = "TransformSwap" # Found in: client_source\pie\pie-src\V\U.2.cs
    # Real executor M.k (its decompile fails, hence missing above): requires
    # EntityIDDataEffect entries "From" (pre-evolution) and "Into" (evolution)
    # or its ctor crashes; it plays the spin FX itself and applies moves raw.
    EVOLVE = "Evolve" # Found in: pie-src.dll M\k (IL only)

