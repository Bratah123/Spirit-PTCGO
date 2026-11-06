from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.passives_common import flip_protection


card = PokemonCardDef(
    guid="d134cf1a-a6e9-5523-9f1f-bd9a0bd8b2af",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic", "Pikachu"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="NEO1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 20 more damage; if tails, this attack does 10 damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
        Attack(
            title="Agility",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all effects of attacks, including damage, done to Pikachu.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=flip_protection(prevent=True, effects_too=True),
        ),
    ],
)
