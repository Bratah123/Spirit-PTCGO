from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4dd644ed-17be-52d4-b5da-66d3922e2fd7",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tranquill.Name",
    display_name="Tranquill",
    searchable_by=["Tranquill", "Stage 1", "Tranquill"],
    subtypes=["Stage 1"],
    collector_number=62,
    set_code="PGO",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pidove.Name",
    family_id=519,
    abilities=[
        Attack(
            title="Aerial Ace",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Flap",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)