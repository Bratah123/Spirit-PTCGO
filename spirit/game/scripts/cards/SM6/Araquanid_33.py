from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.sm6 import bubble_trap

card = PokemonCardDef(
    guid="59ee9eb6-6bfc-5a27-8d0b-afee84e97ca6",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Araquanid.Name",
    display_name="Araquanid",
    searchable_by=["Araquanid", "Stage 1", "Araquanid"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dewpider.Name",
    family_id=751,
    abilities=[
        Attack(
            title="Bubble",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Bubble Trap",
            game_text="If 1 of your Pok\u00e9mon used Bubble during your last turn, this attack does 80 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=bubble_trap,
        ),
    ],
)
