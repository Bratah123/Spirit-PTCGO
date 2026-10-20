from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing

card = PokemonCardDef(
    guid="25a75911-5dd9-5270-b221-aaa501743ed7",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tranquill.Name",
    display_name="Tranquill",
    searchable_by=["Tranquill", "Stage 1", "Tranquill"],
    subtypes=["Stage 1"],
    collector_number=81,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pidove.Name",
    family_id=519,
    abilities=[
        Attack(
            title="Claw",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=flip_or_nothing(),
        ),
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)