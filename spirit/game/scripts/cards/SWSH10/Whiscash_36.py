from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fc00cf30-d33d-56fd-ab61-082fc03570dc",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whiscash.Name",
    display_name="Whiscash",
    searchable_by=["Whiscash", "Stage 1", "Whiscash"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Barboach.Name",
    family_id=339,
    abilities=[
        Attack(
            title="Mud Shot",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
        Attack(
            title="Thrash",
            game_text="Flip a coin. If tails, this Pok\u00e9mon also does 60 damage to itself. If heads, this attack does 60 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)