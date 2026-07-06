from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="012b670a-095d-5b21-ac8a-ed579ea71446",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Corvisquire.Name",
    display_name="Corvisquire",
    searchable_by=["Corvisquire", "Stage 1", "Corvisquire"],
    subtypes=["Stage 1"],
    collector_number=220,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rookidee.Name",
    family_id=821,
    abilities=[
        Attack(
            title="Fury Attack",
            game_text="Flip 3 coins. This attack does 30 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)