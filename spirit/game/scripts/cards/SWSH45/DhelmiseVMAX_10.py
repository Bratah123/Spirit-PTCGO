from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="64878312-a93f-5b53-ab2d-255fd5bf5529",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DhelmiseVMAX.Name",
    display_name="Dhelmise VMAX",
    searchable_by=["Dhelmise VMAX", "VMAX", "DhelmiseVMAX"],
    subtypes=["VMAX"],
    collector_number=10,
    set_code="SWSH45",
    rarity=Rarities.RareHoloVMAX,
    hp=330,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DhelmiseV.Name",
    family_id=781,
    abilities=[
        Attack(
            title="Swinging Chain",
            game_text="This attack does 30 damage to 1 of your opponent's Pok\u00e9mon for each Grass Energy attached to this Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Max Anchor",
            game_text="During your next turn, this Pok\u00e9mon can't use Max Anchor.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=240,
            effect=unimplemented,
        ),
    ],
)