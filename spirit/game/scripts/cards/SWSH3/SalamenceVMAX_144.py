from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bb349d05-047e-562a-b8cf-80b19c7d35b8",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SalamenceVMAX.Name",
    display_name="Salamence VMAX",
    searchable_by=["Salamence VMAX", "VMAX", "SalamenceVMAX"],
    subtypes=["VMAX"],
    collector_number=144,
    set_code="SWSH3",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SalamenceV.Name",
    family_id=373,
    abilities=[
        Attack(
            title="Sonic Double",
            game_text="This attack does 40 damage to 2 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Max Wings",
            game_text="During your next turn, this Pok\u00e9mon can't use Max Wings.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=240,
            effect=unimplemented,
        ),
    ],
)