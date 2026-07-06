from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="aeee1e90-e43b-596c-b65a-3612e05de81b",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EspeonV.Name",
    display_name="Espeon V",
    searchable_by=["Espeon V", "Basic", "V", "EspeonV"],
    subtypes=["Basic", "V"],
    collector_number=180,
    set_code="SWSH7",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=196,
    abilities=[
        Attack(
            title="Zen Shot",
            game_text="This attack does 60 damage to 1 of your opponent's Pok\u00e9mon V. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Super Psy Bolt",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)