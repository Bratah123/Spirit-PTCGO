from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import spiral_rush


card = PokemonCardDef(
    guid="c317f038-81ba-5027-bc11-ac2aad5ccca8",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lairon.Name",
    display_name="Lairon",
    searchable_by=["Lairon", "Stage 1", "Lairon"],
    subtypes=["Stage 1"],
    collector_number=45,
    set_code="EX13",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Aron.Name",
    family_id=304,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Iron Head",
            game_text="Flip a coin until you get tails. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="x",
            effect=spiral_rush(),
        ),
    ],
)