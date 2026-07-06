from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="50d2a992-b8bf-568a-82a8-59d812e82fb8",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luxray.Name",
    display_name="Luxray",
    searchable_by=["Luxray", "Stage 2", "Luxray"],
    subtypes=["Stage 2"],
    collector_number=51,
    set_code="SWSH9",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name",
    family_id=403,
    abilities=[
        Attack(
            title="Energy Crush",
            game_text="This attack does 50 damage for each Energy attached to all of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Flash Impact",
            game_text="This attack also does 30 damage to 1 of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=110,
            effect=unimplemented,
        ),
    ],
)