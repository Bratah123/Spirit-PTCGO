from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b71b318e-92a8-5a2c-8293-46f7899ca5bd",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hattrem.Name",
    display_name="Hattrem",
    searchable_by=["Hattrem", "Stage 1", "Hattrem"],
    subtypes=["Stage 1"],
    collector_number=84,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hatenna.Name",
    family_id=856,
    abilities=[
        Attack(
            title="Calm Mind",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Brutal Swing",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)