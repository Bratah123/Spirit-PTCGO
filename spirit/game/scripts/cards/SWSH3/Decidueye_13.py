from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7024b910-8cfd-5096-bee9-77c505f96e64",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Decidueye.Name",
    display_name="Decidueye",
    searchable_by=["Decidueye", "Stage 2", "Decidueye"],
    subtypes=["Stage 2"],
    collector_number=13,
    set_code="SWSH3",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dartrix.Name",
    family_id=722,
    abilities=[
        Ability(
            title="Deep Forest Camo",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon V and Pok\u00e9mon-GX.",
            effect=unimplemented,
        ),
        Attack(
            title="Splitting Arrow",
            game_text="This attack also does 20 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=unimplemented,
        ),
    ],
)