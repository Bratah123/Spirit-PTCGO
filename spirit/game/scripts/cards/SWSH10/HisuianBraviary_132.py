from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1db0cd12-3529-52fe-998e-eb88e1bcf668",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianBraviary.Name",
    display_name="Hisuian Braviary",
    searchable_by=["Hisuian Braviary", "Stage 1", "HisuianBraviary"],
    subtypes=["Stage 1"],
    collector_number=132,
    set_code="SWSH10",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rufflet.Name",
    family_id=627,
    abilities=[
        Attack(
            title="Psywave",
            game_text="This attack does 30 damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Slashing Strike",
            game_text="During your next turn, this Pok\u00e9mon can't use Slashing Strike.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=unimplemented,
        ),
    ],
)