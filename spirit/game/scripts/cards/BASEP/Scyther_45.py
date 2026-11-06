from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


card = PokemonCardDef(
    guid="144d3502-6e44-5f31-9aaa-991b7e1b628b",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name",
    display_name="Scyther",
    searchable_by=["Scyther", "Basic", "Scyther"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=123,
    abilities=[
        Attack(
            title="Slashing Strike",
            game_text="Scyther can't use this attack during your next turn. (Benching or evolving Scyther ends this effect.)",
            cost={PokemonTypes.GRASS: 2},
            damage=40,
            locks_next_turn=True,
        ),
    ],
)
