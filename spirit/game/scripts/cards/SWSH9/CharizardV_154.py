from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e4f997d7-d063-5261-8e6c-f8da0003b100",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardV.Name",
    display_name="Charizard V",
    searchable_by=["Charizard V", "Basic", "V", "CharizardV"],
    subtypes=["Basic", "V"],
    collector_number=154,
    set_code="SWSH9",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=6,
    abilities=[
        Attack(
            title="Incinerate",
            game_text="Before doing damage, discard all Pok\u00e9mon Tools from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=unimplemented,
        ),
        Attack(
            title="Heat Blast",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
        ),
    ],
)