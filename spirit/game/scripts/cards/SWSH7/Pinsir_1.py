from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f2928e4f-4662-5c5a-aca8-905e7ea6e7bd",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pinsir.Name",
    display_name="Pinsir",
    searchable_by=["Pinsir", "Basic", "Single Strike", "Pinsir"],
    subtypes=["Basic", "Single Strike"],
    collector_number=1,
    set_code="SWSH7",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=127,
    abilities=[
        Ability(
            title="Vise Coach",
            game_text="Damage from your Single Strike Pok\u00e9mon's attacks isn't affected by your opponent's Active Pok\u00e9mon's Resistance.",
            effect=unimplemented,
        ),
        Attack(
            title="Seismic Toss",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)