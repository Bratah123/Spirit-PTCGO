from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


card = PokemonCardDef(
    guid="af251b08-899e-5870-a3df-c1a384ba90c1",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ImakunisDoduo.Name",
    display_name="Imakuni?'s Doduo",
    searchable_by=["Imakuni?'s Doduo", "Basic", "ImakunisDoduo"],
    subtypes=["Basic"],
    collector_number=112,
    set_code="XY12",
    rarity=Rarities.RareSecret,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=84,
    abilities=[
        Ability(
            title="Frenzied Escape",
            game_text="When this Doduo retreats, hold this card and throw it as hard as you can because Doduo is running away. Throw the card horizontally with a snap to get the farthest distance!",
            passive=None  # no in-game effect (joke card),
        ),
        Attack(
            title="Harmonize",
            game_text="From the moment you use this attack, you must begin to sing a song. (While the song is being sung, the game continues.) When the song is finished, this attack does 30 damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=None  # the song is not modeled; plain 30 damage,
        ),
    ],
)