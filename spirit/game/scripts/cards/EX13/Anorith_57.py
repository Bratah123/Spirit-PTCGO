from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import one_two_punch


card = PokemonCardDef(
    guid="b66d23d3-152e-504a-8328-f5b5635042b5",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Anorith.Name",
    display_name="Anorith δ",
    searchable_by=["Anorith \u03b4", "Stage 1", "Anorith"],
    subtypes=["Stage 1"],
    collector_number=57,
    set_code="EX13",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ClawFossil.Name",
    family_id=347,
    abilities=[
        Attack(
            title="Metal Claw",
            cost={PokemonTypes.METAL: 1},
            damage=20,
        ),
        Attack(
            title="Rising Lunge",
            game_text="Flip a coin. If heads, this attack does 30 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=one_two_punch(30, 20),
        ),
    ],
)